"""Animações da aula 06 - alterando (PATCH e PUT)."""

from api_comum import *  # noqa: F401,F403

COLUNAS = ("id", "codigo", "nome", "lote", "qtd", "un")
LARG = (0.6, 1.7, 2.6, 1.9, 0.9, 0.7)


# -----------------------------------------------------------------------------
# PATCH (alguns campos) x PUT (todos os campos)
# -----------------------------------------------------------------------------
def patch_vs_put(ax, q):
    titulo(ax, "PATCH altera ALGUNS campos · PUT reescreve TUDO")

    passos = [
        ("PATCH", 'requests.patch(url + "/api/produtos/11", json={"quantidade": 999})',
         ['{"quantidade": 999}'], [11, "MAT-9999", "Teste", "L-TESTE", 999, "KG"], {4}, 200),
        ("PUT", 'requests.put(url + "/api/produtos/11", json=produto_completo)',
         ['{"fabrica": ..., "codigo_material": ...,', ' "nome_material": ..., (TODOS os campos)}'],
         [11, "MAT-9999", "Teste v2", "L-TESTE-03", 250, "L"], {2, 3, 4, 5}, 200),
        ("PUT", 'requests.put(url + "/api/produtos/11", json={"quantidade": 1})',
         ['{"quantidade": 1}'], None, set(), 422),
    ]
    inicial = [11, "MAT-9999", "Teste", "L-TESTE", 100, "KG"]
    passo = 40
    atual = max(0, min(2, int((q - 4) // passo)))
    q0 = 4 + atual * passo
    t = q - q0
    verbo, comando, corpo, depois, mudou, status = passos[atual]

    codigo(ax, 0.6, 7.25, comando, tamanho=10.8)
    servidor(ax, 13.8, 5.2, destaque=janela(t, 12, 20, 2, 2))

    ida = viagem(t, 4, 10)
    if 2 <= t and ida < 1:
        pacote(ax, mix(3.0, 10.6, ida), 5.6, f"{verbo} /api/produtos/11", corpo, cor=CORES_VERBO[verbo],
               w=6.2 if len(corpo[0]) > 25 else 4.6)

    # estado da linha no banco
    if atual == 0:
        linha = depois if t >= 16 else inicial
    elif atual == 1:
        linha = depois if t >= 16 else passos[0][3]
    else:
        linha = passos[1][3]
    destaques = {}
    if t >= 16 and atual < 2:
        destaques = {0: ("#FEF9C3", CORES_VERBO[verbo])}
    banco(ax, 0.8, 3.4, [linha], colunas=COLUNAS, larguras=LARG, destaques=destaques, tamanho=11, titulo_banco="banco: produto 11")
    if t >= 16 and atual < 2:
        xx = 0.8
        for c, w in enumerate(LARG):
            if c in mudou:
                retangulo(ax, xx - 0.02, 2.71, w - 0.04, 0.38, fc="none", ec=CORES_VERBO[verbo], lw=2.5, raio=0.04)
            xx += w

    volta = viagem(t, 20, 10)
    if t >= 20:
        if status == 200:
            pacote(ax, mix(10.6, 11.8, volta), 2.3, "200 OK", ["produto atualizado"], cor=COR_RESP, w=3.8)
        else:
            pacote(ax, mix(10.6, 11.8, volta), 2.3, "422", ["faltam campos obrigatórios"], cor=LARANJA, w=4.4)

    notas = ["PATCH: só a quantidade mudou", "PUT: precisa mandar o produto COMPLETO", "PUT incompleto: recusado, nada muda"]
    texto(ax, 0.8, 1.4, notas[atual], tamanho=12.5, negrito=True, cor=CORES_VERBO[verbo] if status == 200 else VERMELHO,
          alpha=progresso(t, 18, 24))


ANIMACOES = {
    "patch_vs_put": (patch_vs_put, 130),
}
