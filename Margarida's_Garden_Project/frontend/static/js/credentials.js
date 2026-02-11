/**
 * Margarida's Garden - CRUD de Credenciais
 */

async function listCredentials(showPassword = false) {
  try {
    const res = await apiRequest(`/passwords?show_password=${showPassword}`);
    if (!res.ok) {
      const err = await res.json().catch(() => ({}));
      throw new Error(err.detail || 'Erro ao listar credenciais');
    }
    return await res.json();
  } catch (error) {
    throw new Error(error.message || 'Erro ao listar credenciais');
  }
}

async function createCredential(data) {
  try {
    const res = await apiRequest('/passwords', {
      method: 'POST',
      body: JSON.stringify(data),
    });
    if (!res.ok) {
      const err = await res.json().catch(() => ({}));
      throw new Error(err.detail || 'Erro ao criar credencial');
    }
    return await res.json();
  } catch (error) {
    throw new Error(error.message || 'Erro ao criar credencial');
  }
}

async function updateCredential(id, data) {
  try {
    const res = await apiRequest(`/passwords/${id}`, {
      method: 'PUT',
      body: JSON.stringify(data),
    });
    if (!res.ok) {
      const err = await res.json().catch(() => ({}));
      throw new Error(err.detail || 'Erro ao atualizar credencial');
    }
    return await res.json();
  } catch (error) {
    throw new Error(error.message || 'Erro ao atualizar credencial');
  }
}

async function deleteCredential(id) {
  try {
    const res = await apiRequest(`/passwords/${id}`, { method: 'DELETE' });
    if (!res.ok) {
      const err = await res.json().catch(() => ({}));
      throw new Error(err.detail || 'Erro ao excluir credencial');
    }
    // Para DELETE, pode retornar 204 No Content ou objeto vazio
    if (res.status === 204) {
      return null;
    }
    return await res.json();
  } catch (error) {
    throw new Error(error.message || 'Erro ao excluir credencial');
  }
}
