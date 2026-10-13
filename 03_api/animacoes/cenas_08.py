"""Animações da aula 08 - cadastro automático pela API."""

from api_comum import *  # noqa: F401,F403

REGISTROS = [("MAT-0001", "Açúcar Cristal"), ("MAT-0002", "Óleo de Soja"), ("MAT-0003", "Farinha de Trigo"),
             ("MAT-0004", "Leite Integral"), ("MAT-0005", "Sal Refinado"), ("MAT-0006", "Arroz Branco")]


# -----------------------------------------------------------------------------
# Cada linha do CSV vira um POST
# -----------------------------------------------------------------------------
def csv_para_api(ax, q):
    titulo(ax, "Cadastro automático: cada linha vira um POST")

    texto(ax, 0.6, 7.2, "produtos.csv", tamanho=11, mono=True, negrito=True)
    passo = 9
    inicio = 8
    servidor(ax, 8.0, 5.7, destaque=1.0 if inicio <= q < inicio + len(REGISTROS) * passo + 6 else 0)

    linhas_banco = []
    for i, (cod, nome) in enumerate(REGISTROS):
        y = 6.6 - i * 0.5
        q0 = inicio + i * passo
        enviado = q >= q0 + 6
        ativo = q0 <= q < q0 + 6
        retangulo(ax, 0.5, y - 0.21, 4.6, 0.42, fc=DESTAQUE if ativo else ("#DCFCE7" if enviado else CAIXA),
                  ec=LARANJA if ativo else BORDA, lw=1.3, raio=0.04)
        texto(ax, 0.65, y, f"{cod};{nome}", tamanho=9.5, mono=True)
        # o "pacote" voando até a API
        ida = progresso(q, q0, q0 + 5)
        if 0 < ida < 1:
            etiqueta(ax, mix(5.4, 7.0, ida), mix(y, 5.7, ida), "POST", CORES_VERBO["POST"], tamanho=9)
        if enviado:
            texto(ax, 5.35, y, "201 ✓", tamanho=10, cor=VERDE, negrito=True)
            linhas_banco.append([i + 1, cod, nome[:12]])

    banco(ax, 10.2, 6.6, linhas_banco, colunas=("id", "codigo", "nome"), larguras=(0.6, 1.6, 3.0), titulo_banco="banco",
          tamanho=9.5)

    fim = inicio + len(REGISTROS) * passo + 6
    # comparação de tempo
    texto(ax, 0.6, 2.4, "Tempo para cadastrar 10 produtos:", tamanho=12, negrito=True, alpha=progresso(q, fim, fim + 5))
    barra_api = progresso(q, fim + 4, fim + 8)
    barra_robo = progresso(q, fim + 8, fim + 40)
    retangulo(ax, 4.4, 1.45, 0.15 * barra_api + 0.01, 0.4, fc=VERDE, ec="none", alpha=progresso(q, fim, fim + 5), raio=0.04)
    texto(ax, 0.6, 1.65, "API (requests)", tamanho=11, alpha=progresso(q, fim, fim + 5))
    texto(ax, 4.8, 1.65, "≈ 0,1 segundo", tamanho=11, cor=VERDE, negrito=True, alpha=barra_api)
    retangulo(ax, 4.4, 0.65, 10.5 * barra_robo + 0.01, 0.4, fc=CORES["func"], ec="none", alpha=progresso(q, fim, fim + 5), raio=0.04)
    texto(ax, 0.6, 0.85, "robô pyautogui", tamanho=11, alpha=progresso(q, fim, fim + 5))
    texto(ax, 14.8, 1.25, "≈ 1 minuto", tamanho=11, cor=CORES["func"], negrito=True, ha="right", alpha=progresso(q, fim + 38, fim + 42))


ANIMACOES = {
    "csv_para_api": (csv_para_api, 130),
}
