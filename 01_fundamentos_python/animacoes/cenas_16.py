"""Animações da aula 16 - módulos."""

from base import *  # noqa: F401,F403

COR_MODULO = "#0F766E"


# -----------------------------------------------------------------------------
# Importando funções de outro arquivo
# -----------------------------------------------------------------------------
def importar_modulo(ax, q):
    titulo(ax, "Módulo: usar funções de OUTRO arquivo .py")

    # arquivo do módulo
    painel(ax, 0.5, 1.3, 6.4, 5.9, "utilitarios.py")
    funcoes = ["def formatar_moeda(valor):", "def calcular_desconto(preco, pct):", "def saudacao(nome):"]
    for k, f in enumerate(funcoes):
        destaque = 0
        if k == 0:
            destaque = janela(q, 30, 58, 3, 3)
        if k == 2:
            destaque = janela(q, 72, 999, 3, 1)
        codigo(ax, 0.8, 6.3 - k * 1.25, f, tamanho=10.5, destaque=destaque)
        codigo(ax, 0.8, 5.8 - k * 1.25, "    ...", tamanho=10.5, cor=SUAVE)

    # script que importa
    painel(ax, 9.1, 1.3, 6.4, 5.9, "16_modulos.py")
    codigo(ax, 9.4, 6.3, digitado("import utilitarios", q, 6, 14), tamanho=12)
    seta(ax, 9.0, 6.3, 7.0, 6.3, cor=COR_MODULO, alpha=progresso(q, 14, 20), lw=2.5)
    texto(ax, 8.0, 6.75, "import", tamanho=10.5, cor=COR_MODULO, ha="center", alpha=progresso(q, 14, 20))

    codigo(ax, 9.4, 5.4, digitado("utilitarios.formatar_moeda(1234.5)", q, 24, 32), tamanho=10.3)
    vai = progresso(q, 34, 44)
    volta = progresso(q, 46, 56)
    if 0 < vai < 1:
        valor_solto(ax, mix(12.0, 3.5, vai), mix(5.0, 5.5, vai), "1234.5", cor=CORES["float"], tamanho=14)
    if 0 < volta < 1:
        valor_solto(ax, mix(3.5, 12.4, volta), mix(5.5, 4.7, volta), '"R$ 1.234,50"', cor=CORES["str"], tamanho=14)
    texto(ax, 9.4, 4.7, '→ "R$ 1.234,50"', tamanho=12, mono=True, cor=CORES["str"], alpha=progresso(q, 55, 58))

    codigo(ax, 9.4, 3.6, digitado("from utilitarios import saudacao", q, 66, 74), tamanho=11)
    codigo(ax, 9.4, 2.9, digitado('saudacao("Bruno")', q, 78, 84), tamanho=12)
    texto(ax, 9.4, 2.25, "→ só importou essa função", tamanho=11, cor=SUAVE, alpha=progresso(q, 84, 90))

    legenda(ax, "O nome do módulo é o nome do arquivo sem o .py (e na mesma pasta)", progresso(q, 96, 102))


# -----------------------------------------------------------------------------
# if __name__ == "__main__"
# -----------------------------------------------------------------------------
def name_main(ax, q):
    titulo(ax, 'if __name__ == "__main__":')

    linhas = ["def formatar_moeda(valor):", "    ...", "", 'if __name__ == "__main__":', '    print("Testando...")',
              "    print(formatar_moeda(1234.5))"]
    ys = [6.4 - k * 0.6 for k in range(len(linhas))]

    rodadas = [
        ("python utilitarios.py", '"__main__"', True, "executou o arquivo DIRETAMENTE"),
        ("import utilitarios", '"utilitarios"', False, "o arquivo foi IMPORTADO"),
    ]
    duracao = 60
    rodada = min(1, int(q // duracao))
    q0 = rodada * duracao
    comando, valor_name, roda, nota = rodadas[rodada]

    painel(ax, 0.5, 2.3, 8.2, 4.9, "utilitarios.py")
    bloco_alpha = 1.0 if (roda or q - q0 < 22) else 0.3
    for k, (y, linha) in enumerate(zip(ys, linhas)):
        alpha = bloco_alpha if k >= 4 else 1.0
        destaque = janela(q - q0, 14, 26, 2, 2) if k == 3 else (janela(q - q0, 26, 50, 2, 2) if (k >= 4 and roda) else 0)
        codigo(ax, 0.9, y, linha, tamanho=12.5, alpha=alpha, destaque=destaque)
    if not roda:
        texto(ax, 5.6, (ys[4] + ys[5]) / 2, "← ignorado", tamanho=12, cor=VERMELHO, alpha=progresso(q - q0, 24, 30))

    codigo(ax, 9.2, 6.6, comando, tamanho=13.5, alpha=progresso(q - q0, 0, 4))
    texto(ax, 9.2, 5.95, nota, tamanho=11, cor=SUAVE, alpha=progresso(q - q0, 4, 8))
    caixa(ax, 12.2, 4.2, "__name__", valor_name, cor=CORES["str"], w=4.4, h=1.0, tamanho_valor=14,
          alpha=progresso(q - q0, 6, 12))

    painel(ax, 9.2, 1.0, 6.3, 2.3, "Terminal", escuro=True)
    if roda:
        saida_terminal(ax, 9.5, 2.3, "Testando...", alpha=progresso(q - q0, 30, 34), tamanho=12)
        saida_terminal(ax, 9.5, 1.7, "R$ 1.234,50", alpha=progresso(q - q0, 38, 42), tamanho=12)
    else:
        saida_terminal(ax, 9.5, 2.3, "(nada aparece)", alpha=progresso(q - q0, 26, 30), tamanho=12)

    legenda(ax, "Use esse bloco para TESTAR o módulo sem atrapalhar quem o importa", progresso(q, duracao + 40, duracao + 46))


ANIMACOES = {
    "importar_modulo": (importar_modulo, 120),
    "name_main": (name_main, 130),
}
