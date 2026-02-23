import { useCallback, useEffect, useState } from 'react'
import { Link } from 'react-router-dom'
import { useAuthStore } from '../stores/useAuthStore'
import { apiRequest } from '../services/api'
import { encrypt, decrypt } from '../lib/crypto'

interface Credential {
  id: number
  service_name: string
  username?: string
  password: string
  client_encrypted?: boolean
  notes?: string
}

export function Garden() {
  const logout = useAuthStore((s) => s.logout)
  const cryptoKey = useAuthStore((s) => s.cryptoKey)
  const [creds, setCreds] = useState<Credential[]>([])
  const [loading, setLoading] = useState(true)
  const [showModal, setShowModal] = useState(false)
  const [form, setForm] = useState({ service_name: '', username: '', password: '', notes: '' })
  const [revealed, setRevealed] = useState<number | null>(null)
  const [decrypted, setDecrypted] = useState<Record<number, string>>({})

  const loadCreds = useCallback(async () => {
    const list = await apiRequest<Credential[]>('/passwords')
    setCreds(list)
  }, [])

  useEffect(() => {
    loadCreds().catch(console.error).finally(() => setLoading(false))
  }, [loadCreds])

  async function handleReveal(id: number, cred: Credential) {
    if (decrypted[id] !== undefined) {
      setRevealed(revealed === id ? null : id)
      return
    }
    if (cred.client_encrypted && cryptoKey) {
      try {
        const detail = await apiRequest<Credential>(`/passwords/${id}`)
        const plain = await decrypt(detail.password, cryptoKey)
        setDecrypted((d) => ({ ...d, [id]: plain }))
        setRevealed(id)
      } catch {
        setDecrypted((d) => ({ ...d, [id]: '(erro ao descriptografar)' }))
        setRevealed(id)
      }
    } else if (!cred.client_encrypted) {
      try {
        const detail = await apiRequest<Credential>(`/passwords/${id}`)
        setDecrypted((d) => ({ ...d, [id]: detail.password }))
        setRevealed(id)
      } catch {
        setDecrypted((d) => ({ ...d, [id]: '(erro)' }))
        setRevealed(id)
      }
    }
  }

  async function handleSubmit(e: React.FormEvent) {
    e.preventDefault()
    if (!cryptoKey) {
      alert('Faça login novamente para adicionar credenciais com Zero Knowledge.')
      return
    }
    try {
      const blob = await encrypt(form.password, cryptoKey)
      await apiRequest('/passwords', {
        method: 'POST',
        body: JSON.stringify({
          service_name: form.service_name,
          username: form.username || undefined,
          password_encrypted: blob,
          notes: form.notes || undefined,
        }),
      })
      setForm({ service_name: '', username: '', password: '', notes: '' })
      setShowModal(false)
      await loadCreds()
    } catch (err) {
      alert(err instanceof Error ? err.message : 'Erro ao salvar')
    }
  }

  return (
    <>
    <div className="min-h-screen p-8">
      <div className="flex justify-between items-center mb-8 flex-wrap gap-4">
        <h1 className="text-xl font-semibold text-grass-dark">Margarida's Garden</h1>
        <div className="flex gap-2">
          <button
            onClick={() => setShowModal(true)}
            className="px-4 py-2 bg-grass-green text-white rounded-lg hover:bg-grass-dark"
          >
            + Nova Senha
          </button>
          <Link to="/dashboard" className="px-4 py-2 bg-gray-200 rounded-lg hover:bg-gray-300">
            ← Voltar
          </Link>
          <button
            onClick={() => {
              logout()
              window.location.href = '/'
            }}
            className="px-4 py-2 border rounded-lg hover:bg-gray-100"
          >
            Sair
          </button>
        </div>
      </div>
      <div className="max-w-3xl space-y-4">
        {loading ? (
          <p>Carregando...</p>
        ) : creds.length === 0 ? (
          <p className="text-text-dark">Nenhuma senha cadastrada. Clique em Nova Senha para adicionar.</p>
        ) : (
          creds.map((c) => (
            <div
              key={c.id}
              className="p-5 rounded-xl bg-white/90 shadow border-l-4 border-flower-pink flex justify-between items-center"
            >
              <div>
                <h3 className="font-semibold text-grass-dark">{c.service_name}</h3>
                {c.username && <span className="text-sm text-gray-600">{c.username}</span>}
                <p className="font-mono text-sm mt-1">
                  {revealed === c.id ? decrypted[c.id] ?? c.password : '••••••••'}
                </p>
              </div>
              <div className="flex gap-2">
                <button
                    onClick={() => handleReveal(c.id, c)}
                    className="px-3 py-1 text-sm bg-grass-green text-white rounded hover:bg-grass-dark"
                  >
                    {revealed === c.id ? 'Ocultar' : 'Ver'}
                  </button>
              </div>
            </div>
          ))
        )}
      </div>
    </div>

    {showModal && (
      <div className="fixed inset-0 bg-black/40 flex items-center justify-center z-50 p-4" onClick={() => setShowModal(false)}>
        <div className="bg-white rounded-xl p-6 max-w-md w-full shadow-xl" onClick={(e) => e.stopPropagation()}>
          <h2 className="text-lg font-semibold mb-4">Nova Senha</h2>
          <form onSubmit={handleSubmit} className="space-y-3">
            <div>
              <label className="block text-sm font-medium mb-1">Serviço</label>
              <input
                value={form.service_name}
                onChange={(e) => setForm((f) => ({ ...f, service_name: e.target.value }))}
                className="w-full px-3 py-2 border rounded"
                required
              />
            </div>
            <div>
              <label className="block text-sm font-medium mb-1">Usuário/Email</label>
              <input
                value={form.username}
                onChange={(e) => setForm((f) => ({ ...f, username: e.target.value }))}
                className="w-full px-3 py-2 border rounded"
              />
            </div>
            <div>
              <label className="block text-sm font-medium mb-1">Senha</label>
              <input
                type="password"
                value={form.password}
                onChange={(e) => setForm((f) => ({ ...f, password: e.target.value }))}
                className="w-full px-3 py-2 border rounded"
                required
              />
            </div>
            <div>
              <label className="block text-sm font-medium mb-1">Notas</label>
              <input
                value={form.notes}
                onChange={(e) => setForm((f) => ({ ...f, notes: e.target.value }))}
                className="w-full px-3 py-2 border rounded"
              />
            </div>
            <div className="flex gap-2 pt-2">
              <button type="submit" className="px-4 py-2 bg-grass-green text-white rounded hover:bg-grass-dark">
                Salvar
              </button>
              <button type="button" onClick={() => setShowModal(false)} className="px-4 py-2 border rounded hover:bg-gray-100">
                Cancelar
              </button>
            </div>
          </form>
        </div>
      </div>
    )}
    </>
  )
}
