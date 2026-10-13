"""Animações da aula 07 - robô de cadastro."""

from base import *  # noqa: F401,F403

CAMPOS = ["Fábrica", "Código do Material", "Nome do Material", "Lote", "Data de Produção",
          "Data de Validade", "Quantidade", "Unidade de Medida", "Observação"]


def formulario(ax, x, y, valores, foco=None, salvar_foco=False, alpha=1.0, largura_campo=3.6, tamanho=9.5, passo_y=0.52):
    """Formulário de cadastro do site. (x, y) = canto superior esquerdo do primeiro campo."""
    for i, campo in enumerate(CAMPOS):
        yy = y - i * passo_y
        texto(ax, x, yy, campo, tamanho=tamanho, alpha=alpha)
        focado = foco == i
        retangulo(ax, x + 2.7, yy - 0.2, largura_campo, 0.4, fc="white", ec=CORES["int"] if focado else "#9CA3AF",
                  lw=2.5 if focado else 1, alpha=alpha, raio=0.04)
        if valores and i < len(valores) and valores[i]:
            texto(ax, x + 2.8, yy, valores[i], tamanho=tamanho, alpha=alpha, mono=False)
    yb = y - len(CAMPOS) * passo_y - 0.1
    retangulo(ax, x + 2.7, yb - 0.25, 1.6, 0.5, fc=DESTAQUE if salvar_foco else "#DCFCE7",
              ec=LARANJA if salvar_foco else VERDE, lw=2.5 if salvar_foco else 1.5, alpha=alpha, raio=0.06)
    texto(ax, x + 3.5, yb, "Salvar", tamanho=10, ha="center", alpha=alpha, negrito=True)


# -----------------------------------------------------------------------------
# O "mapa" do robô: a ordem do Tab
# -----------------------------------------------------------------------------
def mapa_tab(ax, q):
    titulo(ax, "O \"mapa\" do robô: a ordem dos campos com Tab")

    janela_programa(ax, 0.6, 0.9, 8.3, 6.6, "Cadastro - Cadastro de Produtos")
    passo = 9
    indice = min(len(CAMPOS), max(0, int((q - 6) // passo)))
    formulario(ax, 0.9, 6.55, None, foco=indice if indice < len(CAMPOS) else None,
               salvar_foco=indice >= len(CAMPOS))

    tecla(ax, 10.6, 6.3, "Tab", pressionada=1.0 if (q >= 6 and (q - 6) % passo < 3 and 0 < indice <= len(CAMPOS)) else 0, w=1.6, h=0.9)
    texto(ax, 11.8, 6.3, f"Tab nº {indice}", tamanho=12, alpha=1 if indice > 0 else 0)

    texto(ax, 9.6, 5.0, "• o cursor começa em Fábrica", tamanho=11)
    texto(ax, 9.6, 4.4, "• cada Tab vai para o próximo campo", tamanho=11)
    texto(ax, 9.6, 3.8, "• Unidade: basta digitar KG, T ou L", tamanho=11)
    texto(ax, 9.6, 3.2, "• Observação: Enter quebra a linha,", tamanho=11)
    texto(ax, 9.6, 2.75, "   então use Tab até o Salvar", tamanho=11)
    balao(ax, 12.5, 1.6, "Tab + Enter no Salvar = salva!", alpha=progresso(q, 6 + len(CAMPOS) * passo, 6 + len(CAMPOS) * passo + 6),
          tamanho=11.5, mono=False)


# -----------------------------------------------------------------------------
# Login: decidindo pelo título da janela
# -----------------------------------------------------------------------------
def login_titulo(ax, q):
    titulo(ax, "Já está logado? O robô olha o TÍTULO da janela")

    linhas = ["titulo = pyautogui.getActiveWindowTitle()", 'if "Login" in titulo:', "    # digita usuário e senha",
              "else:", '    print("Já está logado!")']
    ys = [6.95 - k * 0.55 for k in range(len(linhas))]

    duracao = 64
    rodada = min(1, int(q // duracao))
    q0 = rodada * duracao
    t = q - q0
    na_tela_login = rodada == 0 and t < 44
    titulo_janela = "Login - Cadastro de Produtos" if na_tela_login else "Cadastro - Cadastro de Produtos"

    tempos = [(0, 2, 12), (1, 12, 22)]
    tempos.append((2, 22, 44) if rodada == 0 else (3, 22, 30))
    if rodada == 1:
        tempos.append((4, 30, 60))
    destaque_codigo(ax, 0.9, ys, linhas, t, tempos, tamanho=11.5)

    # janela do navegador
    jx, jy, jw, jh = 8.0, 1.0, 7.6, 5.3
    janela_programa(ax, jx, jy, jw, jh, titulo_janela, tamanho=10.5)
    retangulo(ax, jx + 0.05, jy + jh - 0.47, 4.7, 0.43, fc="none", ec=LARANJA, lw=2.5, alpha=janela(t, 2, 14, 2, 2), raio=0.05)
    if na_tela_login:
        texto(ax, jx + 0.6, 5.1, "Usuário", tamanho=10.5)
        retangulo(ax, jx + 2.0, 4.9, 3.6, 0.42, fc="white", ec=CORES["int"], lw=1.5, raio=0.04)
        texto(ax, jx + 2.1, 5.1, digitado("treinamento", t, 24, 30), tamanho=10.5, mono=True)
        texto(ax, jx + 0.6, 4.3, "Senha", tamanho=10.5)
        retangulo(ax, jx + 2.0, 4.1, 3.6, 0.42, fc="white", ec=CORES["int"], lw=1.5, raio=0.04)
        texto(ax, jx + 2.1, 4.3, "•" * len(digitado("12345678", t, 32, 38)), tamanho=10.5, mono=True)
        tecla(ax, jx + 6.5, 4.3, "Enter", pressionada=janela(t, 39, 43, 1, 1), w=1.3, h=0.6, tamanho=10)
    else:
        formulario(ax, jx + 0.25, 5.5, None, foco=0, largura_campo=3.3, tamanho=8.5, passo_y=0.44)

    if rodada == 0:
        texto(ax, 0.9, 3.6, '"Login" está no título → faz o login', tamanho=11.5, cor=VERDE, negrito=True,
              alpha=janela(t, 14, 60, 2, 3))
    else:
        texto(ax, 0.9, 3.6, '"Login" NÃO está no título → já logado', tamanho=11.5, cor=CORES["int"], negrito=True,
              alpha=progresso(t, 14, 18))
    legenda(ax, "O site lembra o login por 8 horas: o robô precisa funcionar nos dois casos",
            progresso(q, duracao + 40, duracao + 46))


# -----------------------------------------------------------------------------
# O robô cadastrando linha por linha
# -----------------------------------------------------------------------------
def robo_formulario(ax, q):
    titulo(ax, "Robô: cada linha do CSV vira um cadastro")

    registros = [
        ["Fábrica São Paulo", "MAT-0001", "Açúcar Cristal", "L2026-001", "01/10/2026", "01/10/2027", "500", "KG", "Local seco"],
        ["Fábrica Campinas", "MAT-0002", "Óleo de Soja", "L2026-002", "15/09/2026", "15/03/2027", "1200", "L", ""],
        ["Fábrica Curitiba", "MAT-0003", "Farinha de Trigo", "L2026-003", "20/09/2026", "20/03/2027", "8", "T", "Exportação"],
    ]

    # "CSV" à esquerda
    texto(ax, 0.6, 7.2, "produtos.csv", tamanho=11, mono=True, negrito=True)
    passo_campo = 4
    duracao_registro = len(CAMPOS) * passo_campo + 14
    inicio = 6
    atual = max(0, min(len(registros) - 1, int((q - inicio) // duracao_registro)))
    q0 = inicio + atual * duracao_registro
    for r, registro in enumerate(registros):
        y = 6.55 - r * 0.6
        feito = q >= inicio + (r + 1) * duracao_registro - 4
        ativo = r == atual and not feito
        retangulo(ax, 0.5, y - 0.26, 6.3, 0.52, fc=DESTAQUE if ativo else ("#DCFCE7" if feito else CAIXA),
                  ec=LARANJA if ativo else BORDA, lw=1.5, raio=0.05)
        texto(ax, 0.65, y, f"{registro[1]}  {registro[2]}", tamanho=10, mono=True)
        if feito:
            texto(ax, 6.5, y, "✓", tamanho=13, cor=VERDE, ha="center")

    # formulário à direita
    janela_programa(ax, 7.3, 0.9, 8.3, 6.6, "Cadastro - Cadastro de Produtos")
    preenchidos = max(0, min(len(CAMPOS), int((q - q0) // passo_campo)))
    salvo = q >= q0 + len(CAMPOS) * passo_campo + 6
    valores = registros[atual][:preenchidos] if not salvo else []
    foco = preenchidos if preenchidos < len(CAMPOS) and not salvo else None
    formulario(ax, 7.6, 6.55, valores, foco=foco if not salvo else 0,
               salvar_foco=(preenchidos >= len(CAMPOS) and not salvo))

    # valor "voando" do CSV para o campo
    if not salvo and preenchidos < len(CAMPOS):
        p = progresso(q, q0 + preenchidos * passo_campo, q0 + preenchidos * passo_campo + 3)
        if 0 < p < 1:
            valor = registros[atual][preenchidos]
            if valor:
                valor_solto(ax, mix(3.5, 11.6, p), mix(6.55 - atual * 0.6, 6.55 - preenchidos * 0.52, p), valor,
                            cor=CORES["str"], tamanho=10)
    if preenchidos >= len(CAMPOS):
        onda_clique(ax, 11.1, 6.55 - len(CAMPOS) * 0.52 - 0.1, progresso(q, q0 + len(CAMPOS) * passo_campo + 2,
                                                                      q0 + len(CAMPOS) * passo_campo + 8))

    cadastrados = sum(1 for r in range(len(registros)) if q >= inicio + (r + 1) * duracao_registro - 4)
    caixa(ax, 3.6, 3.0, "cadastrados", str(cadastrados), cor=VERDE, w=2.8, h=1.0, tamanho_valor=17)
    texto(ax, 0.6, 1.6, "digitar(valor) + Tab, para cada campo", tamanho=10.5, cor=SUAVE)
    texto(ax, 0.6, 1.15, "Tab + Enter no Salvar · próximo registro", tamanho=10.5, cor=SUAVE)


ANIMACOES = {
    "mapa_tab": (mapa_tab, 110),
    "login_titulo": (login_titulo, 140),
    "robo_formulario": (robo_formulario, 165),
}
