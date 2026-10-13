"""Animações da aula 03 - login e token."""

from api_comum import *  # noqa: F401,F403


# -----------------------------------------------------------------------------
# POST de login e extração do token
# -----------------------------------------------------------------------------
def login_post_token(ax, q):
    titulo(ax, "Login: enviando usuário e senha e pegando o token")

    linhas = ['dados = {"usuario": "treinamento", "senha": "12345678"}',
              "resposta = requests.post(url, json=dados)",
              'token = resposta.json()["access_token"]',
              'headers = {"Authorization": "Bearer " + token}']
    tempos = [(0, 2, 10), (1, 10, 50), (2, 50, 72), (3, 72, 999)]
    destaque_codigo(ax, 0.9, [7.2, 6.65, 6.1, 5.55], linhas, q, tempos, tamanho=11.5)

    cliente(ax, 2.2, 3.4)
    servidor(ax, 13.8, 3.4, destaque=janela(q, 26, 34, 2, 2))

    ida = viagem(q, 12, 14)
    if 10 <= q and ida < 1:
        pacote(ax, mix(4.8, 11.2, ida), 3.6, "POST /api/auth/login", ['{"usuario": "treinamento",', ' "senha": "12345678"}'],
               cor=CORES_VERBO["POST"], w=5.0, alpha=progresso(q, 10, 13))
    volta = viagem(q, 34, 14)
    if q >= 34:
        x = mix(11.2, 8.0, volta)
        pacote(ax, x, 3.3, "200 OK", ['{"access_token": "eyJhbGciOi...",', ' "token_type": "bearer",',
                                       ' "expira_em": "2026-10-12T21:10"}'], cor=COR_RESP, w=5.6)
        # destaque da chave access_token
        if q >= 52:
            retangulo(ax, x - 2.75, 3.3 + 0.12, 2.4, 0.36, fc="none", ec=LARANJA, lw=2, raio=0.05, alpha=janela(q, 52, 999, 2, 1))

    voa = progresso(q, 58, 70)
    if 0 < voa < 1:
        valor_solto(ax, mix(8.2, 4.5, voa), mix(3.6, 1.2, voa), '"eyJhbGciOi..."', cor=CORES["str"], tamanho=12)
    caixa(ax, 4.5, 1.2, "token", '"eyJhbGciOi..."' if voa >= 1 else None, cor=CORES["str"], w=3.6, h=0.8,
          tamanho_valor=12, alpha=progresso(q, 52, 56))
    caixa(ax, 11.3, 1.2, "headers", '{"Authorization": "Bearer eyJ..."}' if q >= 80 else None, cor=CORES["dict"], w=7.6,
          h=0.8, tamanho_valor=11, alpha=progresso(q, 74, 78))
    if q >= 76:
        seta(ax, 6.4, 1.2, 7.4, 1.2, cor=SUAVE, alpha=progresso(q, 76, 80))


ANIMACOES = {
    "login_post_token": (login_post_token, 110),
}
