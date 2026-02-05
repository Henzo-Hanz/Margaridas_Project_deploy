/**
 * Margarida's Garden - CRUD de Credenciais
 */

async function listCredentials(showPassword = false) {
  const res = await apiRequest(`/passwords?show_password=${showPassword}`);
  if (!res.ok) throw new Error('Erro ao listar credenciais');
  return res.json();
}

async function createCredential(data) {
  const res = await apiRequest('/passwords', {
    method: 'POST',
    body: JSON.stringify(data),
  });
  if (!res.ok) {
    const err = await res.json().catch(() => ({}));
    throw new Error(err.detail || 'Erro ao criar');
  }
  return res.json();
}

async function updateCredential(id, data) {
  const res = await apiRequest(`/passwords/${id}`, {
    method: 'PUT',
    body: JSON.stringify(data),
  });
  if (!res.ok) throw new Error('Erro ao atualizar');
  return res.json();
}

async function deleteCredential(id) {
  const res = await apiRequest(`/passwords/${id}`, { method: 'DELETE' });
  if (!res.ok) throw new Error('Erro ao excluir');
}
