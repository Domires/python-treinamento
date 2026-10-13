"""Animações da aula 02 - introdução e segurança."""

from base import *  # noqa: F401,F403


def botao(ax, x, y, rotulo, w=1.4, h=0.55, destaque=False, alpha=1.0, tamanho=11):
    """Botão de janela (x, y = CENTRO)."""
    retangulo(ax, x - w / 2, y - h / 2, w, h, fc=DESTAQUE if destaque else "#F3F4F6",
              ec=LARANJA if destaque else "#9CA3AF", lw=1.5, alpha=alpha, raio=0.08)
    texto(ax, x, y, rotulo, tamanho=tamanho, ha="center", alpha=alpha)


# -----------------------------------------------------------------------------
# FAILSAFE: mouse no canto interrompe o robô
# -----------------------------------------------------------------------------
def failsafe(ax, q):
    titulo(ax, "FAILSAFE: o botão de emergência do robô")

    tela = Tela(0.9, 1.5, 9.0, 5.06)
    tela.desenhar(ax)

    # o robô trabalhando: o mouse vai e volta entre "campos"
    campos = [(500, 300), (1400, 300), (500, 600), (1400, 600), (500, 850)]
    for px, py in campos:
        x, y = tela.ponto(px, py)
        retangulo(ax, x - 0.9, y - 0.22, 1.8, 0.44, fc="white", ec="#9CA3AF", alpha=0.9, raio=0.05)

    parada = 64
    if q < parada - 14:
        k = int(q // 10) % len(campos)
        p = progresso(q % 10, 0, 7)
        (x0, y0), (x1, y1) = campos[k], campos[(k + 1) % len(campos)]
        px, py = mix(x0, x1, p), mix(y0, y1, p)
        if p >= 1:
            onda_clique(ax, *tela.ponto(px, py), progresso(q % 10, 7, 10))
    else:
        # a pessoa joga o mouse para o canto superior esquerdo
        k = int((parada - 14) // 10) % len(campos)
        x0, y0 = campos[k]
        p = progresso(q, parada - 14, parada - 4)
        px, py = mix(x0, 0, p), mix(y0, 0, p)
    x, y = tela.ponto(px, py)
    cursor(ax, x, y, escala=1.1)

    texto(ax, tela.x + tela.w / 2, tela.y + tela.h + 0.35, "robô trabalhando...", tamanho=11, cor=VERDE, ha="center",
          alpha=1 - progresso(q, parada - 4, parada))
    alerta = progresso(q, parada - 2, parada + 4)
    if alerta > 0:
        from matplotlib.patches import Circle
        ax.add_patch(Circle(tela.ponto(0, 0), 0.6 * alerta, fc=VERMELHO, ec="none", alpha=0.35))

    codigo(ax, 10.5, 6.6, "pyautogui.FAILSAFE = True", tamanho=12.5)
    texto(ax, 10.5, 5.9, "(já é o padrão)", tamanho=10.5, cor=SUAVE)
    balao(ax, 13.0, 4.3, "FailSafeException:\nrobô interrompido!", alpha=progresso(q, parada + 2, parada + 8),
          tamanho=12, fc="#FEE2E2", cor=VERMELHO, mono=True)
    legenda(ax, "Emergência: leve o mouse para um dos 4 CANTOS da tela", progresso(q, parada + 8, parada + 14))


# -----------------------------------------------------------------------------
# PAUSE: espera entre cada comando
# -----------------------------------------------------------------------------
def pause(ax, q):
    titulo(ax, "PAUSE: uma pausa automática entre os comandos")
    codigo(ax, 0.8, 7.2, "pyautogui.PAUSE = 0.5", tamanho=15)

    comandos = ["click()", "write()", "press()", "hotkey()"]
    largura_cmd, largura_pausa = 2.2, 1.4
    x = 0.9
    blocos = []
    for k, cmd in enumerate(comandos):
        blocos.append(("cmd", cmd, x, largura_cmd))
        x += largura_cmd
        if k < len(comandos) - 1:
            blocos.append(("pausa", "0.5 s", x, largura_pausa))
            x += largura_pausa
    fim_x = x

    y = 4.4
    # cabeça de leitura percorrendo a linha do tempo
    cabeca = mix(0.9, fim_x, progresso(q, 10, 100))
    for tipo, rotulo, x0, w in blocos:
        ativo = x0 <= cabeca < x0 + w
        if tipo == "cmd":
            retangulo(ax, x0 + 0.05, y - 0.5, w - 0.1, 1.0, fc=DESTAQUE if ativo else "#EEF2FF",
                      ec=LARANJA if ativo else CORES["func"], lw=2, raio=0.12)
            texto(ax, x0 + w / 2, y, rotulo, tamanho=13, mono=True, ha="center", negrito=True)
        else:
            ax.plot([x0 + 0.1, x0 + w - 0.1], [y, y], color=SUAVE if not ativo else LARANJA, lw=2, ls=(0, (3, 3)))
            texto(ax, x0 + w / 2, y + 0.45, rotulo, tamanho=11, ha="center", cor=LARANJA if ativo else SUAVE)
            texto(ax, x0 + w / 2, y - 0.45, "espera", tamanho=9.5, ha="center", cor=SUAVE)
    ax.plot([cabeca, cabeca], [y - 1.0, y + 1.0], color=VERMELHO, lw=2)
    texto(ax, cabeca, y - 1.3, "▲", tamanho=11, cor=VERMELHO, ha="center")

    texto(ax, 0.9, 2.3, "tempo  →", tamanho=11, cor=SUAVE)
    legenda(ax, "Dá tempo para o sistema responder. Teste devagar e depois diminua a pausa", progresso(q, 100, 106))


# -----------------------------------------------------------------------------
# Caixas de mensagem: alert, confirm e prompt
# -----------------------------------------------------------------------------
def caixas_mensagem(ax, q):
    titulo(ax, "Caixas de mensagem: alert, confirm e prompt")

    passos = [
        ('pyautogui.alert("O robô terminou!")', "alerta", '"OK"'),
        ('resposta = pyautogui.confirm("Deseja continuar?", buttons=["Sim", "Não"])', "resposta", '"Sim"'),
        ('nome = pyautogui.prompt("Digite seu nome:")', "nome", '"Ana"'),
    ]
    passo = 40
    atual = max(0, min(2, int((q - 4) // passo)))
    q0 = 4 + atual * passo
    comando, variavel, valor = passos[atual]
    codigo(ax, 0.6, 7.25, digitado(comando, q, q0, q0 + 8), tamanho=11)

    # janela da caixa de mensagem
    jx, jy, jw, jh = 3.0, 2.4, 6.2, 3.6
    aparece = progresso(q, q0 + 8, q0 + 12) * (1 - progresso(q, q0 + 30, q0 + 33))
    janela_programa(ax, jx, jy, jw, jh, ["Aviso", "Confirmação", "Entrada"][atual], alpha=aparece)
    mensagem = ["O robô terminou!", "Deseja continuar?", "Digite seu nome:"][atual]
    texto(ax, jx + 0.4, jy + 2.4, mensagem, tamanho=13, alpha=aparece)

    clique = q0 + 24
    if atual == 0:
        bx, by = jx + jw - 1.2, jy + 0.6
        botao(ax, bx, by, "OK", alpha=aparece, destaque=q >= clique)
    elif atual == 1:
        bx, by = jx + jw - 2.9, jy + 0.6
        botao(ax, bx, by, "Sim", alpha=aparece, destaque=q >= clique)
        botao(ax, jx + jw - 1.2, jy + 0.6, "Não", alpha=aparece)
    else:
        retangulo(ax, jx + 0.4, jy + 1.35, jw - 0.8, 0.6, fc="white", ec=CORES["int"], lw=1.5, alpha=aparece, raio=0.05)
        texto(ax, jx + 0.55, jy + 1.65, digitado("Ana", q, q0 + 13, q0 + 19), tamanho=13, mono=True, alpha=aparece)
        bx, by = jx + jw - 1.2, jy + 0.6
        botao(ax, bx, by, "OK", alpha=aparece, destaque=q >= clique)

    # mouse indo clicar no botão
    if aparece > 0:
        p = progresso(q, q0 + 14, q0 + 23)
        cursor(ax, mix(jx + 1.0, bx, p), mix(jy + 0.3, by - 0.05, p))
        onda_clique(ax, bx, by, progresso(q, clique, clique + 6))

    texto(ax, 12.6, 6.0, "o programa fica\nPARADO até a\npessoa responder", tamanho=11, cor=SUAVE, ha="center",
          alpha=aparece)
    caixa(ax, 12.6, 3.4, variavel, valor if q >= clique + 4 else None, cor=CORES["str"], w=3.0, h=1.0,
          tamanho_valor=15, alpha=progresso(q, q0 + 8, q0 + 12))
    texto(ax, 12.6, 2.2, "o valor devolvido", tamanho=10.5, cor=SUAVE, ha="center", alpha=progresso(q, clique + 4, clique + 8))


ANIMACOES = {
    "failsafe": (failsafe, 105),
    "pause": (pause, 125),
    "caixas_mensagem": (caixas_mensagem, 130),
}
