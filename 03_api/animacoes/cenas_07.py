"""Animações da aula 07 - excluindo (DELETE)."""

from api_comum import *  # noqa: F401,F403

LINHAS = [[9, "MAT-0009", "Feijão", 6], [10, "MAT-0010", "Vinagre", 450], [11, "MAT-9999", "Teste", 999]]
LARG = (0.7, 1.6, 1.5, 0.8)


# -----------------------------------------------------------------------------
# DELETE e conferência com GET
# -----------------------------------------------------------------------------
def delete_produto(ax, q):
    titulo(ax, "DELETE: excluindo um produto (não tem volta!)")

    cliente(ax, 2.2, 4.4)
    servidor(ax, 13.8, 5.8, destaque=janela(q, 18, 26, 2, 2) + janela(q, 66, 72, 2, 2))

    # 1) DELETE
    codigo(ax, 0.6, 7.25, 'requests.delete(url + "/api/produtos/11", headers=headers)', tamanho=11.5,
           destaque=janela(q, 2, 52, 2, 2))
    ida = viagem(q, 6, 12)
    if 4 <= q and ida < 1:
        pacote(ax, mix(4.6, 11.4, ida), 6.2, "DELETE /api/produtos/11", [], cor=CORES_VERBO["DELETE"], w=5.0)
    sai = progresso(q, 22, 34)
    banco(ax, 10.6, 3.6, LINHAS if sai < 1 else LINHAS[:2], larguras=LARG, titulo_banco="banco",
          alphas={2: 1 - sai} if sai < 1 else {}, destaques={2: ("#FEE2E2", VERMELHO)} if 18 <= q and sai < 1 else {})
    volta = viagem(q, 34, 12)
    if 34 <= q < 56:
        pacote(ax, mix(11.0, 6.4, volta), 4.9, "204 No Content", ["(resposta vazia: não use .json())"], cor=COR_RESP, w=5.4)

    # 2) GET para conferir
    if q >= 54:
        codigo(ax, 0.6, 2.4, 'requests.get(url + "/api/produtos/11", headers=headers)', tamanho=11.5,
               destaque=janela(q, 54, 999, 2, 1))
        ida2 = viagem(q, 56, 10)
        if ida2 < 1:
            pacote(ax, mix(4.6, 11.4, ida2), 6.2, "GET /api/produtos/11", [], cor=CORES_VERBO["GET"], w=4.6)
        volta2 = viagem(q, 72, 10)
        if q >= 72:
            pacote(ax, mix(11.0, 6.4, volta2), 4.9, "404 Not Found", ['{"detail": "Produto não encontrado"}'],
                   cor=LARANJA, w=5.4)
    texto(ax, 0.6, 1.3, "Confirmar que a exclusão funcionou é uma boa prática", tamanho=11, cor=SUAVE,
          alpha=progresso(q, 84, 90))


ANIMACOES = {
    "delete_produto": (delete_produto, 110),
}
