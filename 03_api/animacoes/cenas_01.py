"""Animações da aula 01 - JSON."""

from api_comum import *  # noqa: F401,F403


# -----------------------------------------------------------------------------
# JSON x dicionário Python
# -----------------------------------------------------------------------------
def json_vs_python(ax, q):
    titulo(ax, "JSON é quase igual a um dicionário Python")

    python = ['{', '    "codigo": "MAT-0001",', '    "quantidade": 500,', '    "ativo": True,',
              '    "observacao": None,', '    "lotes": ["L1", "L2"]', '}']
    json_ = ['{', '    "codigo": "MAT-0001",', '    "quantidade": 500,', '    "ativo": true,',
             '    "observacao": null,', '    "lotes": ["L1", "L2"]', '}']

    painel(ax, 0.5, 1.4, 6.9, 5.6, "Python (dicionário)")
    painel(ax, 8.6, 1.4, 6.9, 5.6, "JSON (texto)")
    diferencas = {3: ("True", "true", 40), 4: ("None", "null", 62)}
    for i, (lp, lj) in enumerate(zip(python, json_)):
        y = 6.3 - i * 0.62
        aparece = progresso(q, 2 + i * 3, 7 + i * 3)
        if i in diferencas:
            tp, tj, q0 = diferencas[i]
            d = janela(q, q0, q0 + 18, 3, 3) if q < 100 else 1
            marcar_trecho(ax, 0.9, y, lp, tp, alpha=d, tamanho=14)
            marcar_trecho(ax, 9.0, y, lj, tj, alpha=d, tamanho=14)
        codigo(ax, 0.9, y, lp, tamanho=14, alpha=aparece)
        codigo(ax, 9.0, y, lj, tamanho=14, alpha=aparece)

    for i, (_, _, q0) in diferencas.items():
        y = 6.3 - i * 0.62
        seta(ax, 5.0, y, 10.6, y, cor=LARANJA, alpha=janela(q, q0 + 3, q0 + 18, 3, 3), curva=-0.15)

    texto(ax, 8.0, 0.95, "True/False → true/false   ·   None → null   ·   texto SEMPRE com aspas duplas", tamanho=11.5,
          cor=SUAVE, ha="center", alpha=progresso(q, 86, 92))


# -----------------------------------------------------------------------------
# dumps e loads
# -----------------------------------------------------------------------------
def dumps_loads(ax, q):
    titulo(ax, "json.dumps() e json.loads(): ida e volta")

    # dicionário
    pares = [("usuario", '"treinamento"'), ("ativo", "True"), ("acessos", "[1, 2, 3]")]
    texto(ax, 0.6, 6.95, "dados  (dict)", tamanho=11, mono=True, negrito=True, cor=CORES["dict"])
    for i, (k, v) in enumerate(pares):
        y = 6.3 - i * 0.62
        retangulo(ax, 0.6, y - 0.25, 1.9, 0.5, fc=CORES["dict"], ec="none", raio=0.08, alpha=0.9)
        texto(ax, 1.55, y, k, tamanho=10.5, mono=True, cor="white", ha="center", negrito=True)
        texto(ax, 2.7, y, v, tamanho=11, mono=True)

    # texto JSON
    texto_json = '\'{"usuario": "treinamento", "ativo": true, "acessos": [1, 2, 3]}\''
    ida = progresso(q, 14, 30)
    codigo(ax, 6.2, 6.6, "texto = json.dumps(dados)", tamanho=12.5, destaque=janela(q, 8, 40, 3, 3))
    seta(ax, 5.2, 5.6, 7.0, 4.4, cor=COR_REQ, alpha=progresso(q, 10, 16), lw=2.5)
    if ida > 0:
        retangulo(ax, 2.1, 3.75, 11.8, 0.7, fc="#F0FDF4", ec=CORES["str"], lw=2, alpha=ida, raio=0.08)
        texto(ax, 2.3, 4.1, texto_json[: int(len(texto_json) * ida)], tamanho=10, mono=True, cor=CORES["str"])
        etiqueta(ax, 14.6, 4.1, "str", CORES["str"], alpha=progresso(q, 30, 34))
    texto(ax, 8.0, 3.3, "um único TEXTO: é assim que os dados viajam pela internet", tamanho=10.5, cor=SUAVE,
          ha="center", alpha=progresso(q, 32, 38))

    # volta
    volta = progresso(q, 56, 72)
    codigo(ax, 6.2, 2.3, "dados = json.loads(texto)", tamanho=12.5, alpha=progresso(q, 48, 52), destaque=janela(q, 50, 90, 3, 3))
    if volta > 0:
        for i, (k, v) in enumerate(pares):
            x = 0.6 + i * 4.6
            retangulo(ax, x, 1.0, 1.6, 0.5, fc=CORES["dict"], ec="none", alpha=volta, raio=0.08)
            texto(ax, x + 0.8, 1.25, k, tamanho=10, mono=True, cor="white", ha="center", negrito=True, alpha=volta)
            texto(ax, x + 1.75, 1.25, v, tamanho=10.5, mono=True, alpha=volta)
        etiqueta(ax, 14.6, 1.25, "dict", CORES["dict"], alpha=progresso(q, 72, 76))
    texto(ax, 0.6, 0.45, 'agora dá para acessar: dados["usuario"]', tamanho=11, mono=True, alpha=progresso(q, 78, 84))


ANIMACOES = {
    "json_vs_python": (json_vs_python, 120),
    "dumps_loads": (dumps_loads, 110),
}
