"""Animações da aula 01 - descobrir a posição do mouse."""

from base import *  # noqa: F401,F403


def caminho(q, pontos, inicio, movimento, pausa):
    """Posição (px, py) do mouse percorrendo 'pontos', parando um pouco em cada um."""
    t = q - inicio
    for k in range(len(pontos) - 1):
        trecho = movimento + pausa
        if t < (k + 1) * trecho:
            p = progresso(t - k * trecho, 0, movimento)
            (x0, y0), (x1, y1) = pontos[k], pontos[k + 1]
            return mix(x0, x1, p), mix(y0, y1, p), k
    return pontos[-1][0], pontos[-1][1], len(pontos) - 2


# -----------------------------------------------------------------------------
# A tela como um plano de coordenadas
# -----------------------------------------------------------------------------
def coordenadas_tela(ax, q):
    titulo(ax, "A tela é um plano de coordenadas (x, y) em pixels")

    tela = Tela(0.9, 1.5, 9.6, 5.4)
    tela.desenhar(ax)

    # eixos
    seta(ax, tela.x + 0.2, tela.y + tela.h + 0.35, tela.x + 3.2, tela.y + tela.h + 0.35, cor=CORES["int"], lw=2)
    texto(ax, tela.x + 3.4, tela.y + tela.h + 0.35, "x aumenta", tamanho=10.5, cor=CORES["int"])
    seta(ax, tela.x - 0.45, tela.y + tela.h - 0.2, tela.x - 0.45, tela.y + tela.h - 2.6, cor=VERMELHO, lw=2)
    ax.text(tela.x - 0.75, tela.y + tela.h - 1.4, "y aumenta", rotation=90, fontsize=10.5, color=VERMELHO,
            va="center", ha="center", family=FONTE)
    texto(ax, tela.x + 0.1, tela.y + tela.h - 0.25, "(0, 0)", tamanho=10, mono=True, negrito=True)
    texto(ax, tela.x + tela.w - 0.1, tela.y + 0.25, "(1919, 1079)", tamanho=10, mono=True, negrito=True, ha="right")

    pontos = [(200, 150), (960, 540), (1700, 880), (350, 950), (1500, 200)]
    px, py, _ = caminho(q, pontos, 6, 16, 12)
    x, y = tela.ponto(px, py)

    # linhas-guia até as bordas
    ax.plot([x, x], [y, tela.y + tela.h], color=CORES["int"], lw=1.3, ls="--", alpha=0.8)
    ax.plot([tela.x, x], [y, y], color=VERMELHO, lw=1.3, ls="--", alpha=0.8)
    cursor(ax, x, y, escala=1.1)

    # leitura da posição
    painel(ax, 11.2, 3.6, 4.3, 2.2, "pyautogui.position()", escuro=True)
    saida_terminal(ax, 11.5, 4.7, f"x={int(px):5d}", tamanho=15)
    saida_terminal(ax, 11.5, 4.1, f"y={int(py):5d}", tamanho=15)
    texto(ax, 11.2, 2.9, "tela de 1920 x 1080", tamanho=11, cor=SUAVE)
    texto(ax, 11.2, 2.4, "pyautogui.size()", tamanho=11, cor=SUAVE, mono=True)

    legenda(ax, "O canto SUPERIOR esquerdo é o (0, 0) e o y cresce para BAIXO", progresso(q, 30, 36))


ANIMACOES = {
    "coordenadas_tela": (coordenadas_tela, 130),
}
