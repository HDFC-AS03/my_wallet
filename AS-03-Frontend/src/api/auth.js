// Change localhost to your AWS Public IP
const API_BASE = "http://18.214.226.2"; 

export function login() {
  window.location.href = `${API_BASE}/login`;
}

export function logout() {
  window.location.href = `${API_BASE}/logout`;
}

export async function getCurrentUser() {
  const response = await fetch(`${API_BASE}/me`, {
    credentials: "include", // Required for FastAPI session cookies
  });

  if (!response.ok) {
    throw new Error("Not authenticated");
  }

  const result = await response.json();
  return result.data;  
}