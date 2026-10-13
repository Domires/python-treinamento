// Funções compartilhadas entre as páginas.
// O token JWT fica salvo no localStorage: assim, se o usuário já estiver
// logado, a tela de login redireciona direto para o cadastro.

const TOKEN_KEY = "token_treinamento";

function getToken() {
  return localStorage.getItem(TOKEN_KEY);
}

function setToken(token) {
  localStorage.setItem(TOKEN_KEY, token);
}

function logout() {
  localStorage.removeItem(TOKEN_KEY);
  window.location.href = "/login";
}

// Chamada à API já enviando o header Authorization: Bearer <token>
async function api(url, options = {}) {
  const headers = { "Content-Type": "application/json", ...(options.headers || {}) };
  const token = getToken();
  if (token) headers["Authorization"] = "Bearer " + token;

  const resp = await fetch(url, { ...options, headers });

  if (resp.status === 401 && !url.endsWith("/api/auth/login")) {
    logout();
    throw new Error("Sessão expirada");
  }
  return resp;
}

// Verifica se o token salvo ainda é válido
async function estaLogado() {
  if (!getToken()) return false;
  try {
    const resp = await fetch("/api/auth/me", {
      headers: { Authorization: "Bearer " + getToken() },
    });
    return resp.ok;
  } catch {
    return false;
  }
}

// Usado nas páginas protegidas
async function exigirLogin() {
  if (!(await estaLogado())) {
    localStorage.removeItem(TOKEN_KEY);
    window.location.href = "/login";
  }
}

// Extrai a mensagem de erro retornada pelo FastAPI
async function mensagemErro(resp) {
  try {
    const dados = await resp.json();
    if (typeof dados.detail === "string") return dados.detail;
    if (Array.isArray(dados.detail)) {
      return dados.detail.map((e) => e.msg.replace(/^Value error, /, "")).join(" | ");
    }
  } catch {}
  return "Erro " + resp.status;
}

function mostrarMensagem(el, texto, tipo) {
  el.textContent = texto;
  el.className = "mensagem " + tipo;
}

function limparMensagem(el) {
  el.textContent = "";
  el.className = "mensagem";
}

// ---------- Datas: tela usa dd/mm/aaaa, API usa aaaa-mm-dd ----------

// Máscara: aceita digitar "12102026" ou "12/10/2026"
function aplicarMascaraData(input) {
  input.addEventListener("input", () => {
    const d = input.value.replace(/\D/g, "").slice(0, 8);
    let v = d;
    if (d.length > 4) v = d.slice(0, 2) + "/" + d.slice(2, 4) + "/" + d.slice(4);
    else if (d.length > 2) v = d.slice(0, 2) + "/" + d.slice(2);
    input.value = v;
  });
}

function brParaIso(br) {
  const m = /^(\d{2})\/(\d{2})\/(\d{4})$/.exec(br);
  if (!m) return null;
  const [, dia, mes, ano] = m;
  const dt = new Date(Number(ano), Number(mes) - 1, Number(dia));
  if (dt.getFullYear() != ano || dt.getMonth() + 1 != mes || dt.getDate() != dia) return null;
  return `${ano}-${mes}-${dia}`;
}

function isoParaBr(iso) {
  const [ano, mes, dia] = iso.split("-");
  return `${dia}/${mes}/${ano}`;
}
