/**
 * Margarida's Garden - Autenticação e API
 */

const API_BASE = '/api';

function getToken() {
  return localStorage.getItem('garden_token');
}

function setToken(token) {
  localStorage.setItem('garden_token', token);
}

function clearToken() {
  localStorage.removeItem('garden_token');
}

function isAuthenticated() {
  return !!getToken();
}

async function login(email, password) {
  const formData = new URLSearchParams();
  formData.append('username', email);
  formData.append('password', password);

  const res = await fetch(`${API_BASE}/auth/login`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
    body: formData,
  });

  if (!res.ok) {
    const err = await res.json().catch(() => ({}));
    throw new Error(err.detail || 'Login falhou');
  }
  const data = await res.json();
  setToken(data.access_token);
  return data;
}

async function apiRequest(path, options = {}) {
  const token = getToken();
  const headers = {
    'Content-Type': 'application/json',
    ...(token && { Authorization: `Bearer ${token}` }),
    ...options.headers,
  };

  const res = await fetch(`${API_BASE}${path}`, { ...options, headers });

  if (res.status === 401) {
    clearToken();
    window.location.href = '/login';
    throw new Error('Sessão expirada');
  }

  if (!res.ok) {
    const err = await res.json().catch(() => ({}));
    throw new Error(err.detail || `Erro ${res.status}`);
  }

  return {
    status: res.status,
    ok: true,
    json: () => res.json(),
  };
}
