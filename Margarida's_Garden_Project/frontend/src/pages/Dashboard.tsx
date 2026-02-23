import { Link } from 'react-router-dom'
import { useAuthStore } from '../stores/useAuthStore'
import { apiRequest } from '../services/api'
import { useEffect, useState } from 'react'

export function Dashboard() {
  const logout = useAuthStore((s) => s.logout)
  const [stats, setStats] = useState<{ expenses_total: number; incomes_total: number; balance: number } | null>(null)

  useEffect(() => {
    apiRequest<{ expenses_total: number; incomes_total: number; balance: number }>(
      '/treasury/analytics/summary?period=3m'
    )
      .then(setStats)
      .catch(console.error)
  }, [])

  const fmt = (n: number) => n.toLocaleString('pt-BR', { minimumFractionDigits: 2 })

  return (
    <div className="min-h-screen flex flex-col p-8">
      <div className="flex-1">
        <h1 className="text-2xl font-semibold text-grass-dark mb-2">Bem-vindo, Margarida!</h1>
        <p className="text-text-dark mb-8">Escolha um dos nossos serviços</p>
        <div className="grid md:grid-cols-2 gap-6 max-w-4xl">
          <Link
            to="/garden"
            className="block p-6 rounded-xl bg-white/90 shadow-lg border border-gray-200 hover:shadow-xl transition"
          >
            <div className="text-4xl mb-3">🌷</div>
            <h2 className="text-xl font-semibold text-grass-dark">Margarida's Garden</h2>
            <p className="text-text-dark text-sm mt-1">Gerenciador de senhas seguro e intuitivo</p>
            <button className="mt-4 px-4 py-2 bg-grass-green text-white rounded-lg hover:bg-grass-dark transition">
              Acessar Jardim →
            </button>
          </Link>
          <Link
            to="/treasury"
            className="block p-6 rounded-xl bg-white/90 shadow-lg border border-gray-200 hover:shadow-xl transition"
          >
            <div className="text-4xl mb-3">💎</div>
            <h2 className="text-xl font-semibold text-grass-dark">Margarida's Treasury</h2>
            <p className="text-text-dark text-sm mt-1">Gestor de finanças pessoais completo</p>
            <button className="mt-4 px-4 py-2 bg-flower-purple text-white rounded-lg hover:opacity-90 transition">
              Acessar Tesouro →
            </button>
          </Link>
        </div>
        {stats && (
          <div className="mt-8 grid grid-cols-3 gap-4 max-w-2xl">
            <div className="bg-white/80 rounded-lg p-4 shadow">
              <span className="text-sm text-text-dark">Despesas (3m)</span>
              <p className="text-lg font-semibold">R$ {fmt(stats.expenses_total)}</p>
            </div>
            <div className="bg-white/80 rounded-lg p-4 shadow">
              <span className="text-sm text-text-dark">Receitas (3m)</span>
              <p className="text-lg font-semibold">R$ {fmt(stats.incomes_total)}</p>
            </div>
            <div className="bg-white/80 rounded-lg p-4 shadow">
              <span className="text-sm text-text-dark">Balanço (3m)</span>
              <p className={`text-lg font-semibold ${stats.balance < 0 ? 'text-red-600' : 'text-grass-dark'}`}>
                R$ {fmt(stats.balance)}
              </p>
            </div>
          </div>
        )}
      </div>
      <div className="pt-8">
        <button
          onClick={() => {
            logout()
            window.location.href = '/'
          }}
          className="px-4 py-2 border border-gray-300 rounded-lg hover:bg-gray-100"
        >
          Sair
        </button>
      </div>
    </div>
  )
}
