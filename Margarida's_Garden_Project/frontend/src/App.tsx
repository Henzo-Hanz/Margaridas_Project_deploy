import { Routes, Route, Navigate } from 'react-router-dom'
import { ProtectedRoute } from './components/ProtectedRoute'
import { Landing } from './pages/Landing'
import { Login } from './pages/Login'
import { Dashboard } from './pages/Dashboard'
import { Garden } from './pages/Garden'
import { Treasury } from './pages/Treasury'

export default function App() {
  return (
    <Routes>
      <Route path="/" element={<Landing />} />
      <Route path="/login" element={<Login />} />
      <Route
        path="/dashboard"
        element={
          <ProtectedRoute>
            <Dashboard />
          </ProtectedRoute>
        }
      />
      <Route
        path="/garden"
        element={
          <ProtectedRoute>
            <Garden />
          </ProtectedRoute>
        }
      />
      <Route
        path="/treasury"
        element={
          <ProtectedRoute>
            <Treasury />
          </ProtectedRoute>
        }
      />
      <Route path="*" element={<Navigate to="/" replace />} />
    </Routes>
  )
}
