"""Animações da aula 04 - listando e consultando (GET)."""

from api_comum import *  # noqa: F401,F403

PRODUTOS = [[1, "MAT-0001", "Açúcar", 500], [2, "MAT-0002", "Óleo", 1200], [3, "MAT-0003", "Farinha", 8]]


# -----------------------------------------------------------------------------
# GET da lista e o for
# -----------------------------------------------------------------------------
def get_listar(ax, q):
    titulo(ax, "GET: a API devolve uma LISTA de produtos")

    codigo(ax, 0.6, 7.25, 'resposta = requests.get(url + "/api/produtos", headers=headers)', tamanho=11.5,
           destaque=janela(q, 2, 40, 2, 2))
    cliente(ax, 2.2, 4.8)
    servidor(ax, 13.8, 4.8, destaque=janela(q, 18, 26, 2, 2))
    banco(ax, 11.3, 2.6, PRODUTOS, destaques={r: (DESTAQUE, LARANJA) for r in range(3)} if 18 <= q < 30 else {},
          tamanho=9.5, larguras=(0.5, 1.4, 1.2, 0.8), titulo_banco="banco")

    ida = viagem(q, 6, 12)
    if 4 <= q and ida < 1:
        pacote(ax, mix(4.8, 11.2, ida), 6.3, "GET /api/produtos", ["Authorization: Bearer eyJ..."],
               cor=CORES_VERBO["GET"], w=4.8)
    volta = viagem(q, 28, 12)
    if q >= 28 and volta < 1:
        pacote(ax, mix(11.2, 6.5, volta), 5.0, "200 OK", ['[{"id": 1, ...}, {"id": 2, ...},', ' {"id": 3, ...}]'],
               cor=COR_RESP, w=5.0)

    # vira uma lista de dicionários
    if q >= 40:
        codigo(ax, 0.6, 3.1, "produtos = resposta.json()", tamanho=11.5, destaque=janela(q, 40, 54, 2, 2))
        for i, (id_, cod, nome, qtd) in enumerate(PRODUTOS):
            a = progresso(q, 44 + i * 3, 48 + i * 3)
            texto(ax, 0.8, 2.45 - i * 0.45, f'{{"id": {id_}, "nome_material": "{nome}"}}', tamanho=10, mono=True,
                  cor=CORES["dict"], alpha=a)
        texto(ax, 0.8, 0.85, "= uma lista de dicionários", tamanho=10.5, cor=SUAVE,
              alpha=progresso(q, 56, 62))

    if q >= 70:
        painel(ax, 7.4, 0.7, 3.6, 2.9, "for produto in produtos:", escuro=True)
        for i, (id_, cod, nome, qtd) in enumerate(PRODUTOS):
            saida_terminal(ax, 7.65, 2.75 - i * 0.55, f"{id_} - {nome} - {qtd}", tamanho=10.5,
                           alpha=progresso(q, 72 + i * 6, 75 + i * 6))


# -----------------------------------------------------------------------------
# GET por id e 404
# -----------------------------------------------------------------------------
def get_por_id(ax, q):
    titulo(ax, "GET /api/produtos/{id}: consultando UM produto")

    cliente(ax, 2.2, 4.2)
    servidor(ax, 13.8, 4.6)

    duracao = 56
    rodada = min(1, int(q // duracao))
    q0 = rodada * duracao
    t = q - q0
    id_busca = [2, 999999][rodada]

    codigo(ax, 0.6, 7.25, f'requests.get(url + "/api/produtos/{id_busca}", headers=headers)', tamanho=11.5)

    procurando = 14 <= t < 30
    destaques = {}
    if procurando:
        linha_atual = min(2, int((t - 14) // 4))
        destaques = {linha_atual: (DESTAQUE, LARANJA)}
    if rodada == 0 and t >= 22:
        destaques = {1: ("#DCFCE7", VERDE)}
    banco(ax, 11.2, 2.7, PRODUTOS, destaques=destaques, tamanho=9.5, larguras=(0.5, 1.4, 1.2, 0.8), titulo_banco="banco")
    if rodada == 1 and t >= 26:
        texto(ax, 11.2, 0.95, "nenhum produto com id 999999", tamanho=10, cor=VERMELHO)

    ida = viagem(t, 4, 10)
    if 2 <= t and ida < 1:
        pacote(ax, mix(4.6, 11.2, ida), 6.2, f"GET /api/produtos/{id_busca}", [], cor=CORES_VERBO["GET"], w=4.6)
    volta = viagem(t, 30, 12)
    if t >= 30:
        if rodada == 0:
            pacote(ax, mix(11.0, 6.4, volta), 5.6, "200 OK", ['{"id": 2, "codigo_material": "MAT-0002",', ' "nome_material": "Óleo", ...}'],
                   cor=COR_RESP, w=6.0)
        else:
            pacote(ax, mix(11.0, 6.4, volta), 5.6, "404 Not Found", ['{"detail": "Produto não encontrado"}'],
                   cor=LARANJA, w=5.4)
    texto(ax, 0.6, 1.4, "o ID vai no FINAL da rota", tamanho=11, cor=SUAVE, alpha=progresso(q, 10, 16))


ANIMACOES = {
    "get_listar": (get_listar, 100),
    "get_por_id": (get_por_id, 125),
}
