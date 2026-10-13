"""Desenhos usados nas animações de API: cliente, servidor, requisição/resposta e banco de dados."""

from base import *  # noqa: F401,F403

COR_REQ = CORES["func"]       # requisição
COR_RESP = "#0F766E"          # resposta
CORES_VERBO = {"GET": "#2563EB", "POST": "#16A34A", "PUT": "#EA580C", "PATCH": "#CA8A04", "DELETE": "#DC2626"}


def cor_status(codigo):
    if codigo < 300:
        return VERDE
    if codigo < 500:
        return LARANJA if codigo != 401 else VERMELHO
    return VERMELHO


def cliente(ax, x, y, rotulo="seu script Python", alpha=1.0):
    """Notebook representando o seu programa (x, y = CENTRO da tela do notebook)."""
    retangulo(ax, x - 1.2, y - 0.6, 2.4, 1.5, fc=TERMINAL, ec=TINTA, lw=2, alpha=alpha, raio=0.08)
    texto(ax, x - 0.95, y + 0.55, ">>> import", tamanho=8.5, mono=True, cor="#9CA3AF", alpha=alpha)
    texto(ax, x - 0.95, y + 0.2, "requests", tamanho=8.5, mono=True, cor="#9CA3AF", alpha=alpha)
    retangulo(ax, x - 1.5, y - 0.8, 3.0, 0.2, fc="#9CA3AF", ec="none", alpha=alpha, raio=0.04)
    texto(ax, x, y - 1.2, rotulo, tamanho=10.5, ha="center", cor=SUAVE, alpha=alpha)


def servidor(ax, x, y, rotulo="API (servidor)", alpha=1.0, destaque=0.0):
    """Servidor (x, y = CENTRO)."""
    for i in range(3):
        yy = y + 0.55 - i * 0.6
        retangulo(ax, x - 1.0, yy - 0.25, 2.0, 0.5, fc=DESTAQUE if destaque > 0.5 else "#E5E7EB", ec=TINTA, lw=1.8,
                  alpha=alpha, raio=0.06)
        ax.scatter([x + 0.7], [yy], s=18, color=VERDE if destaque > 0.5 else "#9CA3AF", alpha=alpha, zorder=4)
        ax.plot([x - 0.8, x + 0.3], [yy, yy], color="#9CA3AF", lw=1.5, alpha=alpha)
    texto(ax, x, y - 1.2, rotulo, tamanho=10.5, ha="center", cor=SUAVE, alpha=alpha)


def pacote(ax, x, y, cabecalho, linhas=(), cor=COR_REQ, alpha=1.0, w=4.6, tamanho=9.5):
    """Cartão de requisição/resposta (x, y = CENTRO). cabecalho em destaque e linhas abaixo."""
    if alpha <= 0:
        return
    h = 0.55 + 0.38 * len(linhas) + 0.1
    retangulo(ax, x - w / 2, y - h / 2, w, h, fc="white", ec=cor, lw=2.2, alpha=alpha, raio=0.08)
    retangulo(ax, x - w / 2, y + h / 2 - 0.5, w, 0.5, fc=cor, ec="none", alpha=alpha, raio=0.08)
    texto(ax, x - w / 2 + 0.15, y + h / 2 - 0.25, cabecalho, tamanho=tamanho + 0.5, mono=True, cor="white", negrito=True,
          alpha=alpha)
    for i, linha in enumerate(linhas):
        texto(ax, x - w / 2 + 0.15, y + h / 2 - 0.75 - i * 0.38, linha, tamanho=tamanho, mono=True, alpha=alpha)


def etiqueta_status(ax, x, y, codigo, descricao="", alpha=1.0, tamanho=12):
    etiqueta(ax, x, y, f"{codigo} {descricao}".strip(), cor_status(codigo), alpha=alpha, tamanho=tamanho)


def banco(ax, x, y, linhas, colunas=("id", "codigo", "nome", "qtd"), larguras=(0.6, 1.4, 2.0, 0.9),
          destaques=None, alpha=1.0, titulo_banco="banco de dados (produtos)", alphas=None, tamanho=9.5):
    """Tabela do banco de dados (x, y = canto SUPERIOR esquerdo).

    destaques: {indice_linha: (cor_fundo, cor_borda)} | alphas: {indice_linha: alpha}
    """
    destaques = destaques or {}
    alphas = alphas or {}
    largura = sum(larguras)
    texto(ax, x, y + 0.35, titulo_banco, tamanho=9.5, cor=SUAVE, alpha=alpha)
    xx = x
    for nome, lw in zip(colunas, larguras):
        retangulo(ax, xx, y - 0.25, lw - 0.04, 0.45, fc="#E0F2FE", ec="none", alpha=alpha, raio=0.03)
        texto(ax, xx + 0.08, y, nome, tamanho=tamanho, mono=True, negrito=True, alpha=alpha)
        xx += lw
    for r, valores in enumerate(linhas):
        yy = y - 0.5 - r * 0.42
        a = alpha * alphas.get(r, 1.0)
        if a <= 0:
            continue
        if r in destaques:
            fc, ec = destaques[r]
            retangulo(ax, x - 0.05, yy - 0.19, largura, 0.38, fc=fc, ec=ec, lw=1.5, alpha=a, raio=0.04)
        xx = x
        for valor, lw in zip(valores, larguras):
            texto(ax, xx + 0.08, yy, str(valor), tamanho=tamanho, mono=True, alpha=a)
            xx += lw


def viagem(q, inicio, duracao=12):
    """Progresso (0 a 1) de um pacote viajando entre cliente e servidor."""
    return progresso(q, inicio, inicio + duracao)
