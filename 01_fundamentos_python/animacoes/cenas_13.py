"""Animações da aula 13 - bibliotecas e datas."""

from base import *  # noqa: F401,F403

COR_LIB = "#0F766E"


def caixa_ferramentas(ax, x, y, nome, ferramentas, alpha=1.0, destaque=None, w=3.6):
    """Uma biblioteca desenhada como caixa de ferramentas. (x, y) = canto inferior esquerdo."""
    h = 0.75 + len(ferramentas) * 0.6
    retangulo(ax, x, y, w, h, fc="#F0FDFA", ec=COR_LIB, lw=2.5, alpha=alpha)
    texto(ax, x + w / 2, y + h - 0.35, nome, tamanho=13, mono=True, negrito=True, cor=COR_LIB, ha="center", alpha=alpha)
    for i, ferramenta in enumerate(ferramentas):
        yy = y + h - 0.95 - i * 0.6
        if destaque == ferramenta:
            retangulo(ax, x + 0.2, yy - 0.24, w - 0.4, 0.48, fc=DESTAQUE, ec=LARANJA, alpha=alpha, raio=0.08)
        texto(ax, x + w / 2, yy, ferramenta, tamanho=11, mono=True, ha="center", alpha=alpha)


# -----------------------------------------------------------------------------
# Formas de importar
# -----------------------------------------------------------------------------
def importar(ax, q):
    titulo(ax, "Bibliotecas: caixas de ferramentas prontas")

    passos = [
        ("import math", "traz a caixa INTEIRA → use math.ceil(10.1)"),
        ("from datetime import date", "traz só UMA ferramenta → use date.today()"),
        ("import random as rd", "traz a caixa com APELIDO → use rd.randint(1, 100)"),
    ]
    passo = 36
    atual = max(0, min(2, int((q - 6) // passo)))
    q0 = 6 + atual * passo

    # "prateleira" com as bibliotecas
    texto(ax, 0.8, 7.2, "bibliotecas disponíveis", tamanho=11, cor=SUAVE)
    libs = [("math", ["floor()", "ceil()", "sqrt()"]), ("datetime", ["date", "datetime", "timedelta"]),
            ("random", ["randint()", "choice()"])]
    x_libs = [0.8, 4.8, 8.8]
    for k, (nome, ferramentas) in enumerate(libs):
        usado = q >= 6 + k * passo + 10
        caixa_ferramentas(ax, x_libs[k], 3.9, nome, ferramentas, alpha=0.35 if usado and k != 1 else (0.35 if usado else 1))

    # o script recebendo
    painel(ax, 12.6, 1.0, 3.0, 6.3, "meu_script.py")
    for k in range(atual + 1):
        qk = 6 + k * passo
        chega = progresso(q, qk + 6, qk + 16)
        y_destino = 5.7 - k * 1.65
        if k == 0:
            nome_box, ferramentas = "math", ["floor()", "ceil()", "sqrt()"]
            caixa_ferramentas(ax, mix(x_libs[0], 12.8, chega), mix(3.9, y_destino - 1.3, chega), nome_box,
                              ferramentas if chega < 1 else ["ceil()"], w=mix(3.6, 2.6, chega),
                              destaque="ceil()" if chega >= 1 and atual == 0 else None)
        elif k == 1:
            x0 = x_libs[1] + 0.5
            bloco(ax, mix(x0 + 1.3, 14.1, chega), mix(4.65, y_destino - 0.7, chega), "date", COR_LIB, w=2.4, h=0.7,
                  tamanho=12)
        else:
            nome_box = "random" if chega < 0.6 else "rd"
            caixa_ferramentas(ax, mix(x_libs[2], 12.8, chega), mix(3.9, y_destino - 1.0, chega), nome_box,
                              ["randint()", "choice()"] if chega < 1 else ["randint()"], w=mix(3.6, 2.6, chega))

    comando, explicacao = passos[atual]
    codigo(ax, 0.8, 2.6, digitado(comando, q, q0, q0 + 7), tamanho=17)
    texto(ax, 0.8, 1.7, explicacao, tamanho=12, cor=SUAVE, alpha=progresso(q, q0 + 14, q0 + 20))
    legenda(ax, "Algumas já vêm com o Python; outras instalamos com  pip install", progresso(q, 112, 118))


# -----------------------------------------------------------------------------
# Contas com datas (timedelta)
# -----------------------------------------------------------------------------
def datas_timedelta(ax, q):
    titulo(ax, "Contas com datas: timedelta")

    from datetime import date, timedelta

    hoje = date(2026, 10, 12)
    x_hoje, escala, y = 4.0, 0.3, 4.2
    # linha do tempo de -3 a +35 dias
    ax.plot([0.8, 15.2], [y, y], color=BORDA, lw=3)
    for d in range(-10, 38):
        x = x_hoje + d * escala
        if 0.8 <= x <= 15.2:
            ax.plot([x, x], [y - 0.08, y + 0.08], color=BORDA, lw=1)

    def marcador(dias, rotulo, cor, alpha, acima=True):
        if alpha <= 0:
            return
        x = x_hoje + dias * escala
        ax.plot([x, x], [y - 0.35, y + 0.35], color=cor, lw=3, alpha=alpha)
        data = hoje + timedelta(days=dias)
        yy = y + 1.0 if acima else y - 1.0
        texto(ax, x, yy, data.strftime("%d/%m/%Y"), tamanho=13, mono=True, negrito=True, cor=cor, ha="center", alpha=alpha)
        texto(ax, x, yy + (0.55 if acima else -0.55), rotulo, tamanho=11, cor=cor, ha="center", alpha=alpha)

    marcador(0, "hoje", CORES["int"], progresso(q, 2, 8))

    # + 30 dias
    codigo(ax, 0.8, 7.2, "prazo = hoje + timedelta(days=30)", tamanho=14, alpha=progresso(q, 12, 16))
    pulo = progresso(q, 18, 40)
    if pulo > 0:
        seta(ax, x_hoje, y + 0.4, x_hoje + 30 * escala * pulo + 0.001, y + 0.4, curva=-0.35, cor=VERDE, lw=2.5)
    marcador(30, "prazo (+30 dias)", VERDE, progresso(q, 38, 44))

    # - 1 dia
    codigo(ax, 0.8, 6.6, "ontem = hoje - timedelta(days=1)", tamanho=14, alpha=progresso(q, 52, 56))
    marcador(-1, "ontem", LARANJA, progresso(q, 58, 64), acima=False)

    # diferença
    codigo(ax, 0.8, 1.6, "(prazo - hoje).days", tamanho=14, alpha=progresso(q, 74, 78))
    texto(ax, 6.0, 1.6, "→  30", tamanho=15, mono=True, cor=VERDE, negrito=True, alpha=progresso(q, 80, 84))
    legenda(ax, "Subtraindo duas datas temos a diferença em dias", progresso(q, 84, 90))


# -----------------------------------------------------------------------------
# strftime: transformando data em texto
# -----------------------------------------------------------------------------
def strftime_codigos(ax, q):
    titulo(ax, "strftime: data → texto no formato que você quiser")

    partes = [("dia", "12", "%d"), ("mês", "10", "%m"), ("ano", "2026", "%Y"), ("hora", "14", "%H"), ("minuto", "30", "%M")]
    x_partes = [2.0, 4.6, 7.4, 10.4, 13.2]
    texto(ax, 0.8, 7.2, "agora = datetime(2026, 10, 12, 14, 30)", tamanho=14, mono=True)

    for k, ((nome, valor, cod), x) in enumerate(zip(partes, x_partes)):
        aparece = progresso(q, 4 + k * 5, 10 + k * 5)
        bloco(ax, x, 5.6, valor, CORES["int"], w=1.9, h=0.9, tamanho=16, alpha=aparece)
        texto(ax, x, 6.35, nome, tamanho=11, cor=SUAVE, ha="center", alpha=aparece)
        etiqueta(ax, x, 4.55, cod, LARANJA, tamanho=13, alpha=progresso(q, 34 + k * 5, 40 + k * 5))

    formatos = [('agora.strftime("%d/%m/%Y %H:%M")', "12/10/2026 14:30"),
                ('agora.strftime("relatorio_%Y%m%d")', "relatorio_20261012")]
    for k, (chamada, resultado) in enumerate(formatos):
        q0 = 66 + k * 24
        codigo(ax, 0.8, 3.0 - k * 1.1, digitado(chamada, q, q0, q0 + 8), tamanho=13)
        texto(ax, 9.6, 3.0 - k * 1.1, "→", tamanho=15, cor=SUAVE, alpha=progresso(q, q0 + 9, q0 + 12))
        codigo(ax, 10.3, 3.0 - k * 1.1, f'"{resultado}"', tamanho=14, cor=CORES["str"], alpha=progresso(q, q0 + 10, q0 + 15))

    legenda(ax, "strptime faz o caminho inverso: texto → data", progresso(q, 118, 124))


ANIMACOES = {
    "importar": (importar, 135),
    "datas_timedelta": (datas_timedelta, 115),
    "strftime_codigos": (strftime_codigos, 140),
}
