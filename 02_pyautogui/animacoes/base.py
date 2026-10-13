"""Funções de desenho compartilhadas por todas as animações.

Cada animação é uma função desenhar(ax, q) que redesenha a cena inteira no quadro q.
O "palco" vai de 0 a 16 na horizontal e de 0 a 9 na vertical.
"""

import math
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch, Polygon

PASTA = Path(__file__).parent
FPS = 12

# Paleta
FUNDO = "#FFFFFF"
TINTA = "#1F2937"
SUAVE = "#6B7280"
BORDA = "#D1D5DB"
CAIXA = "#F9FAFB"
DESTAQUE = "#FEF3C7"
LARANJA = "#D97706"
TERMINAL = "#111827"
TERMINAL_TEXTO = "#E5E7EB"
VERDE = "#16A34A"
VERMELHO = "#DC2626"
CORES = {"str": "#16A34A", "int": "#2563EB", "float": "#EA580C", "bool": "#9333EA",
         "list": "#0891B2", "dict": "#DB2777", "func": "#4F46E5", "none": "#6B7280"}

FONTE = "DejaVu Sans"
MONO = "DejaVu Sans Mono"
LARGURA_CHAR = 0.25   # largura aproximada de 1 caractere mono em fontsize 15 (unidades do palco)


# -----------------------------------------------------------------------------
# Tempo e movimento
# -----------------------------------------------------------------------------
def progresso(q, inicio, fim):
    """0 antes do início, 1 depois do fim, e suave entre os dois."""
    if q <= inicio:
        return 0.0
    if q >= fim:
        return 1.0
    x = (q - inicio) / (fim - inicio)
    return 0.5 - 0.5 * math.cos(math.pi * x)


def janela(q, inicio, fim, entrada=5, saida=5):
    """Sobe de 0 a 1 no início e desce de 1 a 0 no fim (para destaques temporários)."""
    return progresso(q, inicio, inicio + entrada) * (1 - progresso(q, fim, fim + saida))


def mix(a, b, x):
    return a + (b - a) * x


def digitado(texto, q, inicio, fim):
    """Parte do texto já "digitada" no quadro q."""
    return texto[: int(len(texto) * progresso(q, inicio, fim))]


# -----------------------------------------------------------------------------
# Elementos
# -----------------------------------------------------------------------------
def preparar(ax):
    ax.clear()
    ax.set_xlim(0, 16)
    ax.set_ylim(0, 9)
    ax.axis("off")


def titulo(ax, texto):
    ax.text(0.6, 8.25, texto, fontsize=18, weight="bold", color=TINTA, va="center", family=FONTE)


def legenda(ax, texto, alpha=1.0):
    if alpha > 0:
        ax.text(8, 0.55, texto, fontsize=13, color=SUAVE, ha="center", va="center", alpha=alpha, family=FONTE)


def texto(ax, x, y, conteudo, tamanho=13, cor=TINTA, alpha=1.0, ha="left", mono=False, negrito=False):
    if alpha > 0 and conteudo:
        ax.text(x, y, conteudo, fontsize=tamanho, color=cor, alpha=alpha, ha=ha, va="center",
                family=MONO if mono else FONTE, weight="bold" if negrito else "normal")


def codigo(ax, x, y, conteudo, destaque=0.0, alpha=1.0, tamanho=15, cor=TINTA, cor_destaque=DESTAQUE):
    """Uma linha de código; destaque (0 a 1) pinta o fundo."""
    if destaque > 0:
        largura = max(len(conteudo), 6) * LARGURA_CHAR * tamanho / 15 + 0.4
        ax.add_patch(FancyBboxPatch((x - 0.2, y - 0.3 * tamanho / 15), largura, 0.6 * tamanho / 15,
                                    boxstyle="round,pad=0,rounding_size=0.1",
                                    fc=cor_destaque, ec="none", alpha=destaque * alpha))
    if alpha > 0 and conteudo:
        ax.text(x, y, conteudo, fontsize=tamanho, family=MONO, color=cor, va="center", ha="left", alpha=alpha)


def x_char(x, indice, tamanho=15):
    """Posição x do início do caractere de número 'indice' numa linha de código."""
    return x + indice * LARGURA_CHAR * tamanho / 15


def x_do_trecho(x, linha, trecho, tamanho=15):
    """Posição x do centro de um trecho dentro de uma linha de código."""
    inicio = linha.index(trecho)
    return x + (inicio + len(trecho) / 2) * LARGURA_CHAR * tamanho / 15


def retangulo(ax, x, y, w, h, fc=CAIXA, ec=BORDA, lw=1.5, alpha=1.0, raio=0.2):
    """Retângulo arredondado com (x, y) no CANTO INFERIOR ESQUERDO."""
    if alpha > 0:
        ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle=f"round,pad=0,rounding_size={raio}",
                                    fc=fc, ec=ec, lw=lw, alpha=alpha))


def painel(ax, x, y, w, h, nome="", escuro=False, alpha=1.0):
    """Painel de código (claro) ou de terminal (escuro), com nome no topo."""
    retangulo(ax, x, y, w, h, fc=TERMINAL if escuro else CAIXA, ec="none" if escuro else BORDA, alpha=alpha)
    if nome:
        texto(ax, x + 0.3, y + h - 0.35, nome, tamanho=10.5, cor="#9CA3AF" if escuro else SUAVE, alpha=alpha)


def saida_terminal(ax, x, y, conteudo, alpha=1.0, tamanho=12):
    texto(ax, x, y, conteudo, tamanho=tamanho, cor=TERMINAL_TEXTO, alpha=alpha, mono=True)


def caixa(ax, x, y, nome, valor=None, cor=TINTA, alpha=1.0, w=3.2, h=1.5, tipo=None, tipo_alpha=1.0,
          tamanho_valor=19, destaque=0.0):
    """Uma variável: caixa com etiqueta (nome) em cima e o valor dentro. (x, y) é o CENTRO."""
    if alpha <= 0:
        return
    ax.add_patch(FancyBboxPatch((x - w / 2, y - h / 2), w, h,
                                boxstyle="round,pad=0,rounding_size=0.25",
                                fc=DESTAQUE if destaque > 0.5 else CAIXA, ec=cor, lw=2.5, alpha=alpha))
    if nome:
        ax.text(x, y + h / 2 + 0.38, nome, ha="center", va="center", fontsize=13, family=MONO,
                weight="bold", color=TINTA, alpha=alpha,
                bbox=dict(boxstyle="round,pad=0.3", fc=FUNDO, ec=BORDA, alpha=alpha))
    if valor is not None:
        ax.text(x, y, valor, ha="center", va="center", fontsize=tamanho_valor, family=MONO, color=cor, alpha=alpha)
    if tipo and tipo_alpha > 0:
        etiqueta(ax, x, y - h / 2 - 0.45, tipo, cor, alpha=alpha * tipo_alpha)


def etiqueta(ax, x, y, conteudo, cor, alpha=1.0, tamanho=12, ha="center"):
    """Texto branco em uma etiqueta colorida."""
    if alpha > 0:
        ax.text(x, y, conteudo, ha=ha, va="center", fontsize=tamanho, family=FONTE, color="white",
                weight="bold", alpha=alpha, bbox=dict(boxstyle="round,pad=0.35", fc=cor, ec="none", alpha=alpha))


def balao(ax, x, y, conteudo, alpha=1.0, tamanho=14, fc=DESTAQUE, cor=TINTA, mono=True):
    """Texto dentro de um balão (fundo colorido)."""
    if alpha > 0:
        ax.text(x, y, conteudo, ha="center", va="center", fontsize=tamanho, family=MONO if mono else FONTE,
                color=cor, alpha=alpha, bbox=dict(boxstyle="round,pad=0.4", fc=fc, ec="none", alpha=alpha))


def valor_solto(ax, x, y, conteudo, cor=TINTA, alpha=1.0, tamanho=19):
    """Um valor "voando" pela tela."""
    if alpha > 0:
        ax.text(x, y, conteudo, ha="center", va="center", fontsize=tamanho, family=MONO,
                color=cor, weight="bold", alpha=alpha)


def bloco(ax, x, y, conteudo, cor, alpha=1.0, w=1.6, h=1.1, tamanho=19, destaque=0.0):
    """Um valor dentro de um bloco colorido. (x, y) é o CENTRO."""
    if alpha <= 0:
        return
    ax.add_patch(FancyBboxPatch((x - w / 2, y - h / 2), w, h, boxstyle="round,pad=0,rounding_size=0.2",
                                fc=DESTAQUE if destaque > 0.5 else cor, ec="none",
                                alpha=(1.0 if destaque > 0.5 else 0.15) * alpha))
    ax.add_patch(FancyBboxPatch((x - w / 2, y - h / 2), w, h, boxstyle="round,pad=0,rounding_size=0.2",
                                fc="none", ec=cor, lw=2.5, alpha=alpha))
    if conteudo != "":
        ax.text(x, y, conteudo, ha="center", va="center", fontsize=tamanho, family=MONO, color=cor,
                weight="bold", alpha=alpha)


def seta(ax, x0, y0, x1, y1, cor=SUAVE, alpha=1.0, lw=2.0, curva=0.0, estilo="-|>"):
    if alpha > 0:
        ax.add_patch(FancyArrowPatch((x0, y0), (x1, y1), arrowstyle=estilo, mutation_scale=18,
                                     color=cor, lw=lw, alpha=alpha,
                                     connectionstyle=f"arc3,rad={curva}"))


def losango(ax, x, y, w, h, conteudo, cor=TINTA, alpha=1.0, fc=CAIXA, tamanho=13):
    """Losango de decisão (fluxograma). (x, y) é o CENTRO."""
    if alpha <= 0:
        return
    ax.add_patch(Polygon([(x - w / 2, y), (x, y + h / 2), (x + w / 2, y), (x, y - h / 2)],
                         closed=True, fc=fc, ec=cor, lw=2.5, alpha=alpha))
    ax.text(x, y, conteudo, ha="center", va="center", fontsize=tamanho, family=MONO, color=TINTA, alpha=alpha)


def ponteiro(ax, x, y, alpha=1.0, cor=LARANJA, tamanho=14):
    """Triângulo ▶ indicando a linha em execução."""
    if alpha > 0:
        ax.text(x, y, "▶", fontsize=tamanho, color=cor, va="center", ha="center", alpha=alpha)


def destaque_codigo(ax, x, ys, linhas, q, tempos, tamanho=13, fim=None):
    """Desenha várias linhas de código e destaca a linha ativa conforme 'tempos'.

    tempos: lista de (indice_da_linha, quadro_inicio, quadro_fim).
    """
    ativo = {}
    for indice, inicio, termino in tempos:
        ativo[indice] = max(ativo.get(indice, 0), janela(q, inicio, termino, 3, 3))
    for i, (y, linha) in enumerate(zip(ys, linhas)):
        a = ativo.get(i, 0)
        codigo(ax, x, y, linha, destaque=a, tamanho=tamanho)
        ponteiro(ax, x - 0.35, y, alpha=a, tamanho=tamanho - 1)


def marcar_trecho(ax, x, y, linha, trecho, alpha=1.0, tamanho=15, cor=DESTAQUE):
    """Pinta o fundo de um trecho dentro de uma linha de código (desenhe antes do texto)."""
    if alpha <= 0 or trecho not in linha:
        return
    largura_char = LARGURA_CHAR * tamanho / 15
    inicio = linha.index(trecho)
    ax.add_patch(FancyBboxPatch((x + inicio * largura_char - 0.06, y - 0.32 * tamanho / 15),
                                len(trecho) * largura_char + 0.12, 0.64 * tamanho / 15,
                                boxstyle="round,pad=0,rounding_size=0.1", fc=cor, ec="none", alpha=alpha))


def reducao(ax, x, y, etapas, q, q0, duracao=22, tamanho=22, x_nota=None, cor_final=VERDE):
    """Mostra uma expressão sendo resolvida passo a passo.

    etapas: lista de (texto, trecho_destacado_ou_None, nota). A última etapa é o resultado.
    """
    if q < q0:
        return
    indice = min(int((q - q0) // duracao), len(etapas) - 1)
    inicio_etapa = q0 + indice * duracao
    conteudo, trecho, nota = etapas[indice]
    aparece = progresso(q, inicio_etapa, inicio_etapa + 5)
    ultima = indice == len(etapas) - 1
    if trecho:
        marcar_trecho(ax, x, y, conteudo, trecho, alpha=progresso(q, inicio_etapa + 6, inicio_etapa + 11),
                      tamanho=tamanho)
    codigo(ax, x, y, conteudo, alpha=aparece, tamanho=tamanho, cor=cor_final if ultima else TINTA)
    if nota:
        texto(ax, x_nota if x_nota is not None else x + len(conteudo) * LARGURA_CHAR * tamanho / 15 + 0.6,
              y, nota, tamanho=12, cor=SUAVE, alpha=progresso(q, inicio_etapa + 6, inicio_etapa + 11))


# -----------------------------------------------------------------------------
# Elementos de "tela" (usados nas animações de automação)
# -----------------------------------------------------------------------------
class Tela:
    """Um monitor desenhado no palco, com conversão de pixels (pyautogui) para o palco.

    No pyautogui o (0, 0) fica no canto SUPERIOR esquerdo e o y cresce para BAIXO.
    """

    def __init__(self, x, y, w, h, largura_px=1920, altura_px=1080):
        self.x, self.y, self.w, self.h = x, y, w, h
        self.largura_px, self.altura_px = largura_px, altura_px

    def ponto(self, px, py):
        """Converte (px, py) do pyautogui para coordenadas do palco."""
        return (self.x + px / self.largura_px * self.w, self.y + self.h - py / self.altura_px * self.h)

    def desenhar(self, ax, fundo="#EFF6FF", alpha=1.0, base=True):
        retangulo(ax, self.x - 0.15, self.y - 0.15, self.w + 0.3, self.h + 0.3, fc=TINTA, ec="none", alpha=alpha, raio=0.15)
        retangulo(ax, self.x, self.y, self.w, self.h, fc=fundo, ec="none", alpha=alpha, raio=0.05)
        if base:
            retangulo(ax, self.x + self.w / 2 - 0.5, self.y - 0.55, 1.0, 0.4, fc=TINTA, ec="none", alpha=alpha, raio=0.02)
            retangulo(ax, self.x + self.w / 2 - 1.2, self.y - 0.7, 2.4, 0.18, fc=TINTA, ec="none", alpha=alpha, raio=0.05)


def cursor(ax, x, y, alpha=1.0, escala=1.0, cor="white"):
    """Seta do mouse com a PONTA em (x, y)."""
    if alpha <= 0:
        return
    pontos = [(0, 0), (0, -0.62), (0.15, -0.48), (0.27, -0.74), (0.37, -0.69), (0.25, -0.44), (0.45, -0.44)]
    ax.add_patch(Polygon([(x + px * escala, y + py * escala) for px, py in pontos], closed=True,
                         fc=cor, ec=TINTA, lw=1.4, alpha=alpha, zorder=10))


def onda_clique(ax, x, y, p, cor=LARANJA, raio_max=0.6):
    """Círculo que se expande e some (efeito de clique). p vai de 0 a 1."""
    if 0 < p < 1:
        from matplotlib.patches import Circle
        ax.add_patch(Circle((x, y), raio_max * p, fc="none", ec=cor, lw=2.5, alpha=1 - p, zorder=9))


def janela_programa(ax, x, y, w, h, titulo_janela="", alpha=1.0, fundo="white", cor_barra="#E5E7EB", tamanho=10):
    """Janela de programa (x, y = canto inferior esquerdo) com barra de título."""
    if alpha <= 0:
        return
    retangulo(ax, x, y, w, h, fc=fundo, ec="#9CA3AF", lw=1.3, alpha=alpha, raio=0.08)
    retangulo(ax, x, y + h - 0.45, w, 0.45, fc=cor_barra, ec="#9CA3AF", lw=1.3, alpha=alpha, raio=0.08)
    texto(ax, x + 0.2, y + h - 0.225, titulo_janela, tamanho=tamanho, alpha=alpha)
    texto(ax, x + w - 0.3, y + h - 0.225, "✕", tamanho=tamanho, alpha=alpha, ha="center", cor=SUAVE)


def tecla(ax, x, y, rotulo, pressionada=0.0, w=1.1, h=0.8, tamanho=12, alpha=1.0):
    """Uma tecla do teclado (x, y = CENTRO). pressionada de 0 a 1."""
    if alpha <= 0:
        return
    afunda = 0.08 * pressionada
    retangulo(ax, x - w / 2, y - h / 2 - 0.1, w, h, fc="#9CA3AF", ec="none", alpha=alpha, raio=0.12)
    retangulo(ax, x - w / 2, y - h / 2 - afunda, w, h, fc=DESTAQUE if pressionada > 0.5 else "#F9FAFB",
              ec=LARANJA if pressionada > 0.5 else "#9CA3AF", lw=1.5, alpha=alpha, raio=0.12)
    texto(ax, x, y - afunda, rotulo, tamanho=tamanho, ha="center", alpha=alpha, negrito=True)


# -----------------------------------------------------------------------------
# Gravação
# -----------------------------------------------------------------------------
def salvar(nome, desenhar, total):
    fig = plt.figure(figsize=(8, 4.5), dpi=100, facecolor=FUNDO)
    ax = fig.add_axes([0, 0, 1, 1])

    def quadro(i):
        preparar(ax)
        desenhar(ax, i)

    animacao = FuncAnimation(fig, quadro, frames=total)
    animacao.save(PASTA / f"{nome}.gif", writer=PillowWriter(fps=FPS))
    plt.close(fig)
    print(f"ok  {nome}.gif")
