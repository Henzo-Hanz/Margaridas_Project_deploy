import { useAuthStore } from '../stores/useAuthStore'

const API_BASE = '/api'

async function apiRequest<T = unknown>(path: string, options: RequestInit = {}): Promise<T> {
  const token = useAuthStore.getState().token
  const headers: Record<string, string> = {
    'Content-Type': 'application/json',
    ...(options.headers as Record<string, string>),
  }
  if (token) {
    headers['Authorization'] = `Bearer ${token}`
  }

  const res = await fetch(`${API_BASE}${path}`, { ...options, headers })

  if (res.status === 401) {
    useAuthStore.getState().logout()
    window.location.href = '/login'
    throw new Error('Sessão expirada')
  }

  if (!res.ok) {
    const err = await res.json().catch(() => ({}))
    throw new Error((err as { detail?: string }).detail || `Erro ${res.status}`)
  }

  return res.json()
}

export interface UserMe {
  id: number
  name: string
  email: string
  encryption_salt: string | null
}

export async function fetchMe(): Promise<UserMe> {
  return apiRequest<UserMe>('/auth/me')
}

export async function login(email: string, password: string) {
  const formData = new URLSearchParams()
  formData.append('username', email)
  formData.append('password', password)
  const res = await fetch(`${API_BASE}/auth/login`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
    body: formData,
  })
  if (!res.ok) {
    const err = await res.json().catch(() => ({}))
    throw new Error((err as { detail?: string }).detail || 'Login falhou')
  }
  const data = (await res.json()) as { access_token: string }
  return data.access_token
}

export { apiRequest }
