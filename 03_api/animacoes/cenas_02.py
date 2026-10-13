"""Animações da aula 02 - requisições HTTP."""

from api_comum import *  # noqa: F401,F403

X_CLIENTE, X_SERVIDOR, Y_LINHA = 2.2, 13.8, 4.2


# -----------------------------------------------------------------------------
# Requisição e resposta
# -----------------------------------------------------------------------------
def request_response(ax, q):
    titulo(ax, "API: seu programa PEDE e recebe uma RESPOSTA")

    cliente(ax, X_CLIENTE, Y_LINHA)
    servidor(ax, X_SERVIDOR, Y_LINHA, destaque=janela(q, 30, 44, 2, 2))

    ida = viagem(q, 10, 18)
    if q >= 6 and ida < 1:
        pacote(ax, mix(X_CLIENTE + 2.6, X_SERVIDOR - 2.6, ida), 6.3, "GET /api/produtos",
               ["Host: 127.0.0.1:8000", "Authorization: Bearer eyJ..."], cor=COR_REQ, alpha=progresso(q, 6, 10), w=4.8)
    texto(ax, 8.0, 7.4, "requisição (request)", tamanho=12, cor=COR_REQ, ha="center", negrito=True,
          alpha=janela(q, 6, 30, 3, 3))

    texto(ax, X_SERVIDOR, 2.3, "processando...", tamanho=10.5, cor=SUAVE, ha="center", alpha=janela(q, 30, 44, 2, 2))

    volta = viagem(q, 46, 18)
    if q >= 44:
        pacote(ax, mix(X_SERVIDOR - 2.6, X_CLIENTE + 2.6, volta), 2.0, "200 OK",
               ['[{"id": 1, "nome": "Açúcar"},', ' {"id": 2, "nome": "Óleo"}]'],
               cor=COR_RESP, alpha=progresso(q, 44, 48), w=5.0)
        texto(ax, 8.0, 0.65, "resposta (response)", tamanho=12, cor=COR_RESP, ha="center", negrito=True,
              alpha=progresso(q, 44, 48))

    texto(ax, 8.0, 4.3, "como num restaurante: pedido → cozinha → prato", tamanho=11, cor=SUAVE, ha="center",
          alpha=progresso(q, 70, 76))


# -----------------------------------------------------------------------------
# Verbos HTTP agindo sobre a tabela
# -----------------------------------------------------------------------------
def verbos_http(ax, q):
    titulo(ax, "Verbos HTTP: o que queremos fazer com os dados")

    verbos = [
        ("GET", "consultar / listar", "lê as linhas"),
        ("POST", "cadastrar", "insere uma linha nova"),
        ("PUT", "atualizar TUDO", "reescreve a linha inteira"),
        ("PATCH", "atualizar ALGUNS campos", "altera só uma célula"),
        ("DELETE", "excluir", "apaga a linha"),
    ]
    passo = 26
    atual = max(0, min(4, int((q - 6) // passo)))
    q0 = 6 + atual * passo
    efeito = progresso(q, q0 + 8, q0 + 16)

    for i, (verbo, acao, _) in enumerate(verbos):
        y = 6.6 - i * 0.95
        ativo = i == atual
        etiqueta(ax, 1.4, y, verbo, CORES_VERBO[verbo], alpha=1.0 if i <= atual else 0.35, tamanho=12)
        texto(ax, 2.6, y, acao, tamanho=11.5, negrito=ativo, alpha=1.0 if i <= atual else 0.35)
        if ativo:
            retangulo(ax, 0.5, y - 0.38, 6.8, 0.76, fc="none", ec=LARANJA, lw=2, raio=0.1)

    # estado da tabela
    base_linhas = [[1, "MAT-0001", "Açúcar", 500], [2, "MAT-0002", "Óleo", 1200], [3, "MAT-0003", "Farinha", 8]]
    linhas = [list(l) for l in base_linhas]
    destaques, alphas = {}, {}
    cor_v = CORES_VERBO[verbos[atual][0]]
    fundo = DESTAQUE
    if atual == 0:
        destaques = {r: (fundo, cor_v) for r in range(3)} if efeito > 0.5 else {}
    elif atual == 1:
        linhas.append([4, "MAT-0004", "Leite", 3000])
        alphas = {3: efeito}
        destaques = {3: ("#DCFCE7", cor_v)}
    elif atual == 2:
        if efeito > 0.5:
            linhas[1] = [2, "MAT-0020", "Óleo Extra", 900]
            destaques = {1: (fundo, cor_v)}
    elif atual == 3:
        if efeito > 0.5:
            linhas[1][3] = 999
        destaques = {1: (fundo, cor_v)} if efeito > 0.5 else {}
    else:
        alphas = {1: 1 - efeito}
        destaques = {1: ("#FEE2E2", cor_v)}
        if efeito >= 1:
            linhas.pop(1)
            destaques, alphas = {}, {}

    banco(ax, 8.6, 6.4, linhas, destaques=destaques, alphas=alphas, tamanho=11, larguras=(0.8, 1.9, 2.4, 1.1))
    texto(ax, 8.6, 3.6, verbos[atual][2], tamanho=13, cor=cor_v, negrito=True, alpha=progresso(q, q0 + 8, q0 + 12))
    if atual == 3 and efeito > 0.5:
        texto(ax, 14.9, 5.9 - 0.42, "←", tamanho=11, cor=cor_v, negrito=True)


# -----------------------------------------------------------------------------
# Códigos de status
# -----------------------------------------------------------------------------
def status_codes(ax, q):
    titulo(ax, "Códigos de status: a resposta diz se deu certo")

    grupos = [
        ("2xx  sucesso", VERDE, [(200, "OK: deu certo"), (201, "Created: cadastrado"), (204, "No Content: excluído")]),
        ("4xx  erro NOSSO", LARANJA, [(400, "Bad Request"), (401, "sem token / login errado"),
                                              (404, "Not Found: não existe"), (422, "dado enviado errado")]),
        ("5xx  erro do servidor", VERMELHO, [(500, "Internal Server Error")]),
    ]
    x_grupos = [0.6, 5.8, 11.0]
    k = 0
    for (nome, cor, codigos), x in zip(grupos, x_grupos):
        retangulo(ax, x, 6.6, 4.6, 0.65, fc=cor, ec="none", alpha=progresso(q, 2, 8), raio=0.1)
        texto(ax, x + 0.2, 6.92, nome, tamanho=12, cor="white", negrito=True, alpha=progresso(q, 2, 8))
        for i, (numero, significado) in enumerate(codigos):
            y = 5.8 - i * 1.0
            aparece = progresso(q, 10 + k * 8, 16 + k * 8)
            texto(ax, x + 0.2, y, str(numero), tamanho=18, mono=True, negrito=True, cor=cor, alpha=aparece)
            texto(ax, x + 1.5, y, significado, tamanho=10.5, alpha=aparece)
            k += 1

    codigo(ax, 0.6, 1.3, "resposta.status_code   →   201", tamanho=13, alpha=progresso(q, 80, 86))
    texto(ax, 8.0, 1.3, "o 1º dígito diz quem errou", tamanho=11, cor=SUAVE,
          alpha=progresso(q, 86, 92))


# -----------------------------------------------------------------------------
# Autenticação, token e autorização
# -----------------------------------------------------------------------------
def token_autenticacao(ax, q):
    titulo(ax, "Login → token (crachá) → acesso liberado")

    cliente(ax, X_CLIENTE, Y_LINHA)
    servidor(ax, X_SERVIDOR, Y_LINHA, destaque=janela(q, 18, 26, 2, 2) + janela(q, 60, 66, 2, 2))

    # 1) login
    ida = viagem(q, 6, 12)
    if q >= 4 and ida < 1:
        pacote(ax, mix(X_CLIENTE + 2.6, X_SERVIDOR - 2.6, ida), 6.4, "POST /api/auth/login",
               ['{"usuario": "treinamento",', ' "senha": "12345678"}'], cor=CORES_VERBO["POST"], alpha=progresso(q, 4, 7), w=5.0)
    volta = viagem(q, 24, 12)
    if 24 <= q and volta < 1:
        pacote(ax, mix(X_SERVIDOR - 2.6, X_CLIENTE + 2.6, volta), 6.4, "200 OK",
               ['{"access_token": "eyJhbGci..."}'], cor=COR_RESP, w=5.0)
    texto(ax, 8.0, 7.45, "1) AUTENTICAÇÃO: provar quem você é", tamanho=12, ha="center", negrito=True, cor=COR_REQ,
          alpha=janela(q, 4, 38, 3, 3))

    # crachá com o token
    if q >= 36:
        etiqueta(ax, X_CLIENTE, 6.3, "token: eyJhbGci...", LARANJA, tamanho=11)

    # 2) acesso com token
    ida2 = viagem(q, 44, 12)
    if 42 <= q and ida2 < 1:
        pacote(ax, mix(X_CLIENTE + 2.6, X_SERVIDOR - 2.6, ida2), 6.4, "GET /api/produtos",
               ["Authorization: Bearer eyJhbGci..."], cor=CORES_VERBO["GET"], w=5.4)
    volta2 = viagem(q, 62, 10)
    if 62 <= q < 80:
        x = mix(X_SERVIDOR - 2.0, X_CLIENTE + 2.4, volta2)
        etiqueta_status(ax, x, 5.2, 200, "OK", tamanho=12)
    texto(ax, 8.0, 7.45, "2) AUTORIZAÇÃO: com o token, o acesso é liberado", tamanho=12, ha="center", negrito=True,
          cor=VERDE, alpha=janela(q, 42, 80, 3, 3))

    # 3) sem token
    ida3 = viagem(q, 84, 12)
    if 82 <= q and ida3 < 1:
        pacote(ax, mix(X_CLIENTE + 2.6, X_SERVIDOR - 2.6, ida3), 6.4, "GET /api/produtos", ["(sem token)"],
               cor=CORES_VERBO["GET"], w=4.6)
    if q >= 96:
        etiqueta_status(ax, mix(X_SERVIDOR - 2.0, X_CLIENTE + 2.4, viagem(q, 98, 10)), 5.2, 401, "Unauthorized", tamanho=12)
    texto(ax, 8.0, 7.45, "3) sem token: acesso NEGADO", tamanho=12, ha="center", negrito=True, cor=VERMELHO,
          alpha=progresso(q, 82, 86))

    texto(ax, 8.0, 1.0, "O token vai no HEADER de cada requisição e expira (aqui, em 8 horas)", tamanho=11, cor=SUAVE,
          ha="center", alpha=progresso(q, 108, 114))


# -----------------------------------------------------------------------------
# Parâmetros na URL
# -----------------------------------------------------------------------------
def parametros_url(ax, q):
    titulo(ax, "Parâmetros: filtros que vão na URL")

    codigo(ax, 0.6, 7.1, 'requests.get(url, headers=headers,', tamanho=12.5)
    codigo(ax, 0.6, 6.55, '             params={"fabrica": "Recife", "lote": "L2026"})', tamanho=12.5)

    partes = [("http://127.0.0.1:8000", "servidor", CORES["int"]), ("/api/produtos", "rota", CORES["func"]),
              ("?", "", TINTA), ("fabrica=Recife", "parâmetro 1", VERDE), ("&", "", TINTA),
              ("lote=L2026", "parâmetro 2", VERDE)]
    tamanho = 14
    lc = LARGURA_CHAR * tamanho / 15
    x = 0.8
    y = 4.3
    for k, (trecho, rotulo, cor) in enumerate(partes):
        aparece = progresso(q, 10 + k * 8, 16 + k * 8)
        w = len(trecho) * lc
        if rotulo:
            retangulo(ax, x - 0.05, y - 0.32, w + 0.1, 0.64, fc=cor, ec="none", alpha=0.15 * aparece, raio=0.06)
            texto(ax, x + w / 2, y - 0.75, rotulo, tamanho=10, cor=cor, ha="center", alpha=aparece)
        codigo(ax, x, y, trecho, tamanho=tamanho, cor=cor, alpha=aparece)
        if k in (3, 5):
            origem_x = 6.0 if k == 3 else 10.0
            voo = progresso(q, 6 + k * 8, 12 + k * 8)
            if 0 < voo < 1:
                valor_solto(ax, mix(origem_x, x + w / 2, voo), mix(6.55, y, voo), trecho, cor=VERDE, tamanho=12)
        x += w

    texto(ax, 0.8, 2.7, "?  começa os parâmetros   ·   &  separa um do outro", tamanho=12, alpha=progresso(q, 64, 70))
    texto(ax, 0.8, 1.9, "O argumento params= monta essa URL para você (resposta.url mostra o resultado)", tamanho=11,
          cor=SUAVE, alpha=progresso(q, 72, 78))


ANIMACOES = {
    "request_response": (request_response, 100),
    "verbos_http": (verbos_http, 145),
    "status_codes": (status_codes, 115),
    "token_autenticacao": (token_autenticacao, 135),
    "parametros_url": (parametros_url, 100),
}
