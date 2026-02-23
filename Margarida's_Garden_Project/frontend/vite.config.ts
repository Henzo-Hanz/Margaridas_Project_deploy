import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

export default defineConfig({
  plugins: [react()],
  server: {
    port: 5173,
    proxy: {
      '/api': {
        target: 'http://127.0.0.1:8000',
        changeOrigin: true,
      },
      '/static': { target: 'http://127.0.0.1:8000' },
      '/login': { target: 'http://127.0.0.1:8000' },
      '/dashboard': { target: 'http://127.0.0.1:8000' },
      '/garden': { target: 'http://127.0.0.1:8000' },
      '/treasury': { target: 'http://127.0.0.1:8000' },
    },
  },
})
