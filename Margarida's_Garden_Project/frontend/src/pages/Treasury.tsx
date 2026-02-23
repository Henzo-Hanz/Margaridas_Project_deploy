import { useEffect, useState } from 'react'
import { Link } from 'react-router-dom'
import { useAuthStore } from '../stores/useAuthStore'
import { apiRequest } from '../services/api'

interface Summary {
  expenses_total: number
  incomes_total: number
  balance: number
}

export function Treasury() {
  const logout = useAuthStore((s) => s.logout)
  const [summary, setSummary] = useState<Summary | null>(null)

  useEffect(() => {
    apiRequest<Summary>('/treasury/analytics/summary?period=6m')
      .then(setSummary)
      .catch(console.error)
  }, [])

  const fmt = (n: number) => n.toLocaleString('pt-BR', { minimumFractionDigits: 2 })

  return (
    <div className="min-h-screen p-8">
      <div className="flex justify-between items-center mb-8">
        <h1 className="text-xl font-semibold text-grass-dark">Margarida's Treasury</h1>
        <div className="flex gap-2">
          <Link to="/dashboard" className="px-4 py-2 bg-grass-green text-white rounded-lg hover:bg-grass-dark">
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
      {summary && (
        <div className="grid grid-cols-3 gap-4 mb-8">
          <div className="bg-white/80 rounded-lg p-4 shadow">
            <span className="text-sm text-text-dark">Despesas</span>
            <p className="text-lg font-semibold">R$ {fmt(summary.expenses_total)}</p>
          </div>
          <div className="bg-white/80 rounded-lg p-4 shadow">
            <span className="text-sm text-text-dark">Receitas</span>
            <p className="text-lg font-semibold">R$ {fmt(summary.incomes_total)}</p>
          </div>
          <div className="bg-white/80 rounded-lg p-4 shadow">
            <span className="text-sm text-text-dark">Balanço</span>
            <p className={`text-lg font-semibold ${summary.balance < 0 ? 'text-red-600' : 'text-grass-dark'}`}>
              R$ {fmt(summary.balance)}
            </p>
          </div>
        </div>
      )}
      <p className="text-text-dark">Use o app legado para gerenciar despesas e receitas em detalhe.</p>
    </div>
  )
}
