import { create } from 'zustand'

const TOKEN_KEY = 'garden_token'

interface AuthState {
  token: string | null
  cryptoKey: CryptoKey | null
  setToken: (token: string | null) => void
  setCryptoKey: (key: CryptoKey | null) => void
  login: (token: string) => void
  logout: () => void
  isAuthenticated: () => boolean
}

export const useAuthStore = create<AuthState>((set, get) => ({
  token: localStorage.getItem(TOKEN_KEY),
  cryptoKey: null,
  setToken: (token) => {
    if (token) {
      localStorage.setItem(TOKEN_KEY, token)
    } else {
      localStorage.removeItem(TOKEN_KEY)
    }
    set({ token })
  },
  setCryptoKey: (cryptoKey) => set({ cryptoKey }),
  login: (token) => get().setToken(token),
  logout: () => {
    set({ cryptoKey: null })
    get().setToken(null)
  },
  isAuthenticated: () => !!get().token,
}))
