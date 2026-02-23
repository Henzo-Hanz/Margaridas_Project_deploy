import { useState } from 'react'
import { useNavigate, useLocation } from 'react-router-dom'
import { useAuthStore } from '../stores/useAuthStore'
import { login, fetchMe } from '../services/api'
import { deriveKey } from '../lib/crypto'

export function Login() {
  const [email, setEmail] = useState('')
  const [password, setPassword] = useState('')
  const [error, setError] = useState('')
  const [loading, setLoading] = useState(false)
  const navigate = useNavigate()
  const location = useLocation()
  const setToken = useAuthStore((s) => s.setToken)
  const setCryptoKey = useAuthStore((s) => s.setCryptoKey)

  const from = (location.state as { from?: { pathname: string } })?.from?.pathname || '/dashboard'

  async function handleSubmit(e: React.FormEvent) {
    e.preventDefault()
    setError('')
    setLoading(true)
    try {
      const token = await login(email, password)
      setToken(token)
      const me = await fetchMe()
      if (me.encryption_salt) {
        const key = await deriveKey(password, me.encryption_salt)
        setCryptoKey(key)
      }
      navigate(from, { replace: true })
    } catch (err) {
      setError(err instanceof Error ? err.message : 'Login falhou')
    } finally {
      setLoading(false)
    }
  }

  return (
    <div className="min-h-screen flex items-center justify-center p-8">
      <div className="bg-white p-10 rounded-2xl shadow-xl w-full max-w-md border-2 border-pink-200/30">
        <h1 className="text-grass-dark text-xl font-semibold mb-6 text-center">Margarida's Garden</h1>
        <form onSubmit={handleSubmit} className="space-y-5">
          <div>
            <label htmlFor="email" className="block text-text-dark font-medium mb-2">
              Email
            </label>
            <input
              id="email"
              type="email"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
              className="w-full px-3 py-3 border border-gray-300 rounded-lg"
              required
            />
          </div>
          <div>
            <label htmlFor="password" className="block text-text-dark font-medium mb-2">
              Senha
            </label>
            <input
              id="password"
              type="password"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              className="w-full px-3 py-3 border border-gray-300 rounded-lg"
              required
            />
          </div>
          {error && (
            <p className="text-red-600 text-sm" role="alert">
              {error}
            </p>
          )}
          <button
            type="submit"
            disabled={loading}
            className="w-full py-3 bg-grass-green text-white rounded-lg font-semibold hover:bg-grass-dark transition disabled:opacity-50"
          >
            {loading ? 'Entrando...' : 'Entrar'}
          </button>
        </form>
      </div>
    </div>
  )
}
