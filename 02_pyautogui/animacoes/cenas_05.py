"""Animações da aula 05 - prints e localização de imagens."""

from base import *  # noqa: F401,F403


def area_de_trabalho(ax, tela, mostrar_botao=True):
    """Conteúdo simples dentro da tela: uma janela com alguns botões."""
    x0, y0 = tela.ponto(250, 150)
    x1, y1 = tela.ponto(1650, 950)
    janela_programa(ax, x0, y1, x1 - x0, y0 - y1, "Sistema de Cadastro", tamanho=9)
    for i, campo in enumerate(["Código", "Produto", "Quantidade"]):
        cx, cy = tela.ponto(350, 330 + i * 140)
        texto(ax, cx, cy, campo, tamanho=9)
        retangulo(ax, cx + 1.5, cy - 0.17, 3.2, 0.34, fc="white", ec="#9CA3AF", lw=1, raio=0.03)
    if mostrar_botao:
        for rotulo, px in [("Cancelar", 1050), ("Salvar", 1400)]:
            bx, by = tela.ponto(px, 830)
            cor = VERDE if rotulo == "Salvar" else "#9CA3AF"
            retangulo(ax, bx - 0.6, by - 0.22, 1.2, 0.44, fc="#DCFCE7" if rotulo == "Salvar" else "#F3F4F6", ec=cor,
                      lw=1.5, raio=0.06)
            texto(ax, bx, by, rotulo, tamanho=9, ha="center")


def miniatura(ax, x, y, w, h, nome, alpha=1.0, conteudo=None):
    """Arquivo de imagem salvo (x, y = canto inferior esquerdo)."""
    if alpha <= 0:
        return
    retangulo(ax, x, y, w, h, fc="#EFF6FF", ec=CORES["int"], lw=2, alpha=alpha, raio=0.05)
    if conteudo:
        conteudo(alpha)
    texto(ax, x + w / 2, y - 0.3, nome, tamanho=10, mono=True, ha="center", alpha=alpha)


# -----------------------------------------------------------------------------
# screenshot: tela inteira e região
# -----------------------------------------------------------------------------
def screenshot_regiao(ax, q):
    titulo(ax, "screenshot: print da tela inteira ou de uma região")

    tela = Tela(0.7, 1.6, 8.6, 4.84)
    tela.desenhar(ax)
    area_de_trabalho(ax, tela)

    # 1) tela inteira
    codigo(ax, 9.9, 6.9, "pyautogui.screenshot()", tamanho=11.5, destaque=janela(q, 4, 40, 2, 2))
    flash = janela(q, 10, 13, 1, 4)
    if flash > 0:
        retangulo(ax, tela.x, tela.y, tela.w, tela.h, fc="white", ec="none", alpha=flash, raio=0.05)
    voa = progresso(q, 16, 30)
    if voa > 0:
        w, h = mix(tela.w, 2.4, voa), mix(tela.h, 1.35, voa)
        x, y = mix(tela.x, 10.0, voa), mix(tela.y, 4.4, voa)
        retangulo(ax, x, y, w, h, fc="#DBEAFE", ec=CORES["int"], lw=2, raio=0.05)
        if voa >= 1:
            texto(ax, x + w / 2, y - 0.3, "tela_inteira.png", tamanho=10, mono=True, ha="center")

    # 2) região
    b = 48
    codigo(ax, 9.9, 3.3, "pyautogui.screenshot(", tamanho=11.5, alpha=progresso(q, b - 4, b),
           destaque=janela(q, b, 999, 2, 1))
    codigo(ax, 9.9, 2.8, "    region=(0, 0, 400, 300))", tamanho=11.5, alpha=progresso(q, b - 4, b))
    regiao = progresso(q, b + 4, b + 14)
    x0, y0 = tela.ponto(0, 0)
    x1, y1 = tela.ponto(400 * regiao, 300 * regiao)
    if regiao > 0:
        ax.plot([x0, x1, x1, x0, x0], [y0, y0, y1, y1, y0], color=LARANJA, lw=2.5, ls="--")
        texto(ax, x1 + 0.1, y1 - 0.25, "400 x 300", tamanho=9.5, cor=LARANJA, alpha=regiao)
    flash = janela(q, b + 16, b + 19, 1, 4)
    if flash > 0:
        retangulo(ax, x0, y1, x1 - x0, y0 - y1, fc="white", ec="none", alpha=flash, raio=0)
    voa = progresso(q, b + 20, b + 32)
    if voa > 0:
        w, h = mix(x1 - x0, 1.6, voa), mix(y0 - y1, 1.2, voa)
        x, y = mix(x0, 13.3, voa), mix(y1, 4.55, voa)
        retangulo(ax, x, y, w, h, fc="#FFEDD5", ec=LARANJA, lw=2, raio=0.05)
        if voa >= 1:
            texto(ax, x + w / 2, y - 0.3, "canto_superior.png", tamanho=10, mono=True, ha="center")

    legenda(ax, "region = (x, y, largura, altura) · ótimo como EVIDÊNCIA de que o robô executou", progresso(q, b + 34, b + 40))


# -----------------------------------------------------------------------------
# locateCenterOnScreen: procurando a imagem na tela
# -----------------------------------------------------------------------------
def localizar_imagem(ax, q):
    titulo(ax, "Localizando uma imagem na tela")

    tela = Tela(0.7, 1.6, 8.6, 4.84)
    tela.desenhar(ax)
    area_de_trabalho(ax, tela)

    # a "foto" do botão
    texto(ax, 10.0, 6.95, "imagens/botao_salvar.png", tamanho=10.5, mono=True)
    retangulo(ax, 10.6, 5.95, 1.6, 0.6, fc="#DCFCE7", ec=VERDE, lw=1.5, raio=0.06)
    texto(ax, 11.4, 6.25, "Salvar", tamanho=11, ha="center")

    # janela de busca varrendo a tela
    alvo_px = (1400, 830)
    passos = [(px, py) for py in (200, 500, 830) for px in (300, 700, 1100, 1400)]
    indice_alvo = passos.index(alvo_px)
    t = (q - 10) / 4
    atual = max(0, min(indice_alvo, int(t))) if q >= 10 else -1
    achou = q >= 10 + indice_alvo * 4 + 4
    if atual >= 0:
        px, py = passos[atual]
        x, y = tela.ponto(px, py)
        cor = VERDE if achou else LARANJA
        retangulo(ax, x - 0.65, y - 0.28, 1.3, 0.56, fc="none", ec=cor, lw=2.5, raio=0.04)
    texto(ax, 10.0, 4.9, "procurando..." if not achou else "encontrou!", tamanho=12,
          cor=LARANJA if not achou else VERDE, negrito=True, alpha=1 if q >= 10 else 0)

    codigo(ax, 10.0, 4.1, "posicao = pyautogui.", tamanho=11)
    codigo(ax, 10.0, 3.6, '  locateCenterOnScreen("...png")', tamanho=11)
    q_achou = 10 + indice_alvo * 4 + 4
    if achou:
        cx, cy = tela.ponto(*alvo_px)
        ax.scatter([cx], [cy], s=50, color=VERMELHO, zorder=6)
        texto(ax, 10.0, 2.9, "posicao = Point(x=1400, y=830)", tamanho=11, mono=True, cor=VERDE,
              alpha=progresso(q, q_achou, q_achou + 4))
        codigo(ax, 10.0, 2.2, "pyautogui.click(posicao)", tamanho=11, alpha=progresso(q, q_achou + 8, q_achou + 12))
        p = progresso(q, q_achou + 12, q_achou + 22)
        cursor(ax, mix(tela.x + 1.0, cx, p), mix(tela.y + 0.8, cy, p))
        onda_clique(ax, cx, cy, progresso(q, q_achou + 23, q_achou + 30))
    else:
        cursor(ax, tela.x + 1.0, tela.y + 0.8)

    legenda(ax, "Se a janela mudar de lugar, o robô continua achando o botão", progresso(q, q_achou + 30, q_achou + 36))


# -----------------------------------------------------------------------------
# Esperando algo aparecer na tela
# -----------------------------------------------------------------------------
def esperar_imagem(ax, q):
    titulo(ax, "Esperando o botão aparecer na tela")

    tela = Tela(0.7, 1.6, 8.6, 4.84)
    tela.desenhar(ax)

    aparece = 60
    if q < aparece:
        cx, cy = tela.x + tela.w / 2, tela.y + tela.h / 2
        texto(ax, cx, cy + 0.5, "Carregando...", tamanho=14, ha="center", cor=SUAVE)
        angulo = q * 30
        import math as _m
        for i in range(8):
            a = _m.radians(angulo + i * 45)
            ax.scatter([cx + 0.45 * _m.cos(a)], [cy - 0.4 + 0.45 * _m.sin(a)], s=30,
                       color=CORES["int"], alpha=0.15 + 0.1 * i)
    else:
        area_de_trabalho(ax, tela)

    codigo(ax, 9.9, 7.0, "for segundo in range(30):", tamanho=11)
    codigo(ax, 9.9, 6.5, "    pos = locateCenterOnScreen(img)", tamanho=9.5)
    codigo(ax, 9.9, 6.0, "    if pos is not None:", tamanho=11)
    codigo(ax, 9.9, 5.5, "        return pos", tamanho=11)
    codigo(ax, 9.9, 5.0, "    time.sleep(1)", tamanho=11)

    tentativas = min(6, int(q // 12) + 1)
    for k in range(tentativas):
        y = 4.2 - k * 0.45
        ok = 12 * k >= aparece
        texto(ax, 10.0, y, f"{k + 1}º segundo:", tamanho=10.5, cor=SUAVE)
        texto(ax, 11.9, y, "encontrou → clica!" if ok else "None (ainda não)", tamanho=10.5,
              cor=VERDE if ok else VERMELHO, negrito=ok)
        if ok:
            break

    if q >= aparece + 14:
        bx, by = tela.ponto(1400, 830)
        p = progresso(q, aparece + 14, aparece + 24)
        cursor(ax, mix(tela.x + 1.5, bx, p), mix(tela.y + 0.8, by, p))
        onda_clique(ax, bx, by, progresso(q, aparece + 25, aparece + 32))
    legenda(ax, "Melhor que um time.sleep \"chutado\": espera só o necessário", progresso(q, aparece + 30, aparece + 36))


ANIMACOES = {
    "screenshot_regiao": (screenshot_regiao, 110),
    "localizar_imagem": (localizar_imagem, 120),
    "esperar_imagem": (esperar_imagem, 120),
}
