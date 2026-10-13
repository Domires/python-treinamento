"""Animações da aula 03 - mouse."""

from base import *  # noqa: F401,F403


def lista_comandos(ax, x, y0, comandos, atual, passo_y=0.62, tamanho=12):
    """Lista de linhas de código com a atual destacada."""
    for k, linha in enumerate(comandos):
        y = y0 - k * passo_y
        ativo = 1.0 if k == atual else 0.0
        codigo(ax, x, y, linha, destaque=ativo, tamanho=tamanho, alpha=1.0 if k <= atual else 0.35)
        ponteiro(ax, x - 0.3, y, alpha=ativo, tamanho=11)


# -----------------------------------------------------------------------------
# moveTo (absoluto) x move (relativo)
# -----------------------------------------------------------------------------
def moveto_vs_move(ax, q):
    titulo(ax, "moveTo vai ATÉ o ponto · move ANDA a partir dele")

    tela = Tela(0.7, 1.5, 9.0, 5.06)
    tela.desenhar(ax)
    # grade a cada 200 px
    for gx in range(200, 1920, 200):
        x, _ = tela.ponto(gx, 0)
        ax.plot([x, x], [tela.y, tela.y + tela.h], color="#DBEAFE", lw=0.8)
    for gy in range(200, 1080, 200):
        _, y = tela.ponto(0, gy)
        ax.plot([tela.x, tela.x + tela.w], [y, y], color="#DBEAFE", lw=0.8)

    comandos = ["pyautogui.moveTo(500, 300)", "pyautogui.move(300, 0)", "pyautogui.move(0, 200)",
                "pyautogui.move(-300, 0)", "pyautogui.move(0, -200)"]
    pontos = [(1500, 900), (500, 300), (800, 300), (800, 500), (500, 500), (500, 300)]
    passo = 22
    atual = max(0, min(len(comandos) - 1, int((q - 8) // passo)))
    p = progresso(q, 8 + atual * passo, 8 + atual * passo + 12)

    # trilha já percorrida
    for k in range(atual + (1 if p >= 1 else 0)):
        if k == 0:
            continue
        (x0, y0), (x1, y1) = tela.ponto(*pontos[k]), tela.ponto(*pontos[k + 1])
        seta(ax, x0, y0, x1, y1, cor=VERDE, lw=2.5)
    (x0, y0), (x1, y1) = pontos[atual], pontos[atual + 1]
    px, py = mix(x0, x1, p), mix(y0, y1, p)
    x, y = tela.ponto(px, py)
    if atual == 0:
        alvo = tela.ponto(500, 300)
        ax.scatter([alvo[0]], [alvo[1]], s=60, color=CORES["int"], zorder=5)
        texto(ax, alvo[0] + 0.15, alvo[1] + 0.3, "(500, 300)", tamanho=10, mono=True, cor=CORES["int"])
    cursor(ax, x, y, escala=1.0)

    lista_comandos(ax, 10.4, 6.6, comandos, atual, tamanho=11)
    nota = "absoluto: vai direto ao ponto" if atual == 0 else "relativo: anda a partir de onde está"
    texto(ax, 10.1, 3.1, nota, tamanho=11, cor=CORES["int"] if atual == 0 else VERDE)
    texto(ax, 10.1, 2.5, "duration=1  → o movimento leva 1 s", tamanho=10.5, cor=SUAVE)
    legenda(ax, "Com move() desenhamos um retângulo: direita, baixo, esquerda, cima", progresso(q, 120, 126))


# -----------------------------------------------------------------------------
# click, doubleClick e rightClick
# -----------------------------------------------------------------------------
def cliques(ax, q):
    titulo(ax, "Clicando: click, doubleClick e rightClick")

    tela = Tela(0.7, 1.5, 9.0, 5.06)
    tela.desenhar(ax, fundo="#E0F2FE")

    comandos = ["pyautogui.click(800, 480)", "pyautogui.doubleClick(300, 250)", "pyautogui.rightClick(1200, 700)"]
    passo = 38
    atual = max(0, min(2, int((q - 6) // passo)))
    q0 = 6 + atual * passo

    # ícone de pasta na área de trabalho (para o clique duplo)
    xi, yi = tela.ponto(300, 250)
    retangulo(ax, xi - 0.4, yi - 0.3, 0.8, 0.6, fc="#FDE68A", ec="#CA8A04", lw=1.5, raio=0.06)
    texto(ax, xi, yi - 0.55, "Relatórios", tamanho=9, ha="center")
    # botão para o clique simples
    xb, yb = tela.ponto(800, 480)
    retangulo(ax, xb - 0.8, yb - 0.25, 1.6, 0.5, fc=DESTAQUE if (atual == 0 and q > q0 + 18) else "white",
              ec="#6B7280", lw=1.5, raio=0.08)
    texto(ax, xb, yb, "Salvar", tamanho=10, ha="center")

    alvos = [(800, 480), (300, 250), (1200, 700)]
    origem = (1500, 900) if atual == 0 else alvos[atual - 1]
    p = progresso(q, q0 + 4, q0 + 14)
    px, py = mix(origem[0], alvos[atual][0], p), mix(origem[1], alvos[atual][1], p)
    x, y = tela.ponto(px, py)

    if atual == 0:
        onda_clique(ax, x, y, progresso(q, q0 + 15, q0 + 22))
    elif atual == 1:
        onda_clique(ax, x, y, progresso(q, q0 + 15, q0 + 20))
        onda_clique(ax, x, y, progresso(q, q0 + 19, q0 + 24))
        janela_programa(ax, tela.x + 3.3, tela.y + 0.4, 5.2, 2.8, "Relatórios", alpha=progresso(q, q0 + 24, q0 + 28))
    else:
        onda_clique(ax, x, y, progresso(q, q0 + 15, q0 + 22), cor=CORES["func"])
        menu = progresso(q, q0 + 18, q0 + 22)
        if menu > 0:
            retangulo(ax, x + 0.1, y - 1.9, 2.4, 1.85, fc="white", ec="#9CA3AF", lw=1.3, alpha=menu, raio=0.05)
            for i, item in enumerate(["Copiar", "Colar", "Excluir", "Propriedades"]):
                texto(ax, x + 0.3, y - 0.3 - i * 0.42, item, tamanho=10, alpha=menu)
    cursor(ax, x, y)

    lista_comandos(ax, 10.3, 6.6, comandos, atual, passo_y=0.8, tamanho=9.5)
    notas = ["clique simples (botão esquerdo)", "clique duplo: abre a pasta", "botão direito: abre o menu"]
    texto(ax, 10.1, 3.6, notas[atual], tamanho=11.5, cor=CORES["int"], alpha=progresso(q, q0 + 16, q0 + 20))
    texto(ax, 10.1, 2.6, "click(x, y, clicks=3)\n→ clique triplo", tamanho=10.5, cor=SUAVE, mono=False)


# -----------------------------------------------------------------------------
# scroll
# -----------------------------------------------------------------------------
def scroll(ax, q):
    titulo(ax, "scroll: rolando a tela")

    jx, jy, jw, jh = 1.0, 1.3, 8.0, 5.7
    janela_programa(ax, jx, jy, jw, jh, "Relatório.pdf")
    # deslocamento do conteúdo: desce de 0 até 4 e depois volta
    desloca = 4.0 * progresso(q, 14, 40) * (1 - progresso(q, 64, 90))

    ax.set_clip_on(True)
    from matplotlib.patches import Rectangle
    area = Rectangle((jx, jy), jw - 0.4, jh - 0.45, transform=ax.transData)
    for i in range(18):
        y = jy + jh - 0.9 - i * 0.55 + desloca
        if jy + 0.1 < y < jy + jh - 0.6:
            t = ax.text(jx + 0.4, y, f"Linha {i + 1:02d} do relatório de vendas", fontsize=11,
                        family=MONO, va="center", color=TINTA if i % 5 else CORES["int"])
            t.set_clip_path(area)
    # barra de rolagem
    retangulo(ax, jx + jw - 0.35, jy + 0.1, 0.25, jh - 0.6, fc="#F3F4F6", ec="none", raio=0.05)
    altura_barra = 2.0
    y_barra = jy + jh - 0.55 - altura_barra - desloca / 4.0 * (jh - 0.7 - altura_barra)
    retangulo(ax, jx + jw - 0.35, y_barra, 0.25, altura_barra, fc="#9CA3AF", ec="none", raio=0.05)

    cursor(ax, jx + jw / 2, jy + jh / 2)
    roda = "▼" if 14 <= q < 40 else ("▲" if 64 <= q < 90 else "")
    texto(ax, jx + jw / 2 + 0.6, jy + jh / 2 - 0.3, roda, tamanho=16, cor=LARANJA)

    codigo(ax, 9.8, 6.0, "pyautogui.scroll(-500)", tamanho=12.5, destaque=janela(q, 10, 44, 3, 3))
    texto(ax, 9.8, 5.4, "negativo: DESCE", tamanho=11, cor=SUAVE)
    codigo(ax, 9.8, 4.3, "pyautogui.scroll(500)", tamanho=12.5, destaque=janela(q, 60, 94, 3, 3))
    texto(ax, 9.8, 3.7, "positivo: SOBE", tamanho=11, cor=SUAVE)


# -----------------------------------------------------------------------------
# drag: desenhando no Paint
# -----------------------------------------------------------------------------
def drag_quadrado(ax, q):
    titulo(ax, "drag: segura o botão, move e solta")

    jx, jy, jw, jh = 0.7, 1.2, 9.2, 5.9
    janela_programa(ax, jx, jy, jw, jh, "Sem título - Paint")
    retangulo(ax, jx + 0.2, jy + 0.2, jw - 0.4, jh - 0.9, fc="white", ec=BORDA, raio=0.02)

    comandos = ["pyautogui.moveTo(inicio)", "pyautogui.drag(200, 0)", "pyautogui.drag(0, 200)",
                "pyautogui.drag(-200, 0)", "pyautogui.drag(0, -200)"]
    escala = 2.4 / 200
    origem = (2.2, 5.6)
    deltas = [(200, 0), (0, 200), (-200, 0), (0, -200)]
    pontos = [origem]
    for dx, dy in deltas:
        x, y = pontos[-1]
        pontos.append((x + dx * escala, y - dy * escala))

    passo = 18
    inicio = 14
    atual = max(0, min(len(deltas), int((q - inicio) // passo) + 1)) if q >= inicio else 0
    # traços já desenhados
    for k in range(len(deltas)):
        q0 = inicio + k * passo
        p = progresso(q, q0, q0 + 12)
        if p > 0:
            (x0, y0), (x1, y1) = pontos[k], pontos[k + 1]
            ax.plot([x0, mix(x0, x1, p)], [y0, mix(y0, y1, p)], color=TINTA, lw=3.5, solid_capstyle="round")
    # posição do mouse
    if q < inicio:
        p = progresso(q, 2, 10)
        x, y = mix(8.0, origem[0], p), mix(2.5, origem[1], p)
        segurando = False
    else:
        k = min(len(deltas) - 1, int((q - inicio) // passo))
        p = progresso(q, inicio + k * passo, inicio + k * passo + 12)
        (x0, y0), (x1, y1) = pontos[k], pontos[k + 1]
        x, y = mix(x0, x1, p), mix(y0, y1, p)
        segurando = q < inicio + len(deltas) * passo - 6 and p < 1
    cursor(ax, x, y)
    if segurando:
        texto(ax, x + 0.5, y - 0.9, "botão pressionado", tamanho=9.5, cor=LARANJA)

    # escada com for
    q_escada = inicio + len(deltas) * passo + 6
    xe, ye = 5.5, 5.6
    for degrau in range(5):
        q0 = q_escada + degrau * 6
        p1 = progresso(q, q0, q0 + 3)
        p2 = progresso(q, q0 + 3, q0 + 6)
        if p1 > 0:
            ax.plot([xe, xe + 0.5 * p1], [ye, ye], color=CORES["int"], lw=3)
        if p2 > 0:
            ax.plot([xe + 0.5, xe + 0.5], [ye, ye - 0.5 * p2], color=CORES["int"], lw=3)
        xe, ye = xe + 0.5, ye - 0.5

    lista_comandos(ax, 10.6, 6.6, comandos, min(atual, len(comandos) - 1), tamanho=11)
    codigo(ax, 10.4, 3.2, "for degrau in range(5):", tamanho=11, alpha=progresso(q, q_escada - 4, q_escada))
    codigo(ax, 10.4, 2.7, "    pyautogui.drag(40, 0)", tamanho=11, alpha=progresso(q, q_escada - 4, q_escada))
    codigo(ax, 10.4, 2.2, "    pyautogui.drag(0, 40)", tamanho=11, alpha=progresso(q, q_escada - 4, q_escada))


ANIMACOES = {
    "moveto_vs_move": (moveto_vs_move, 135),
    "cliques": (cliques, 125),
    "scroll": (scroll, 105),
    "drag_quadrado": (drag_quadrado, 135),
}
