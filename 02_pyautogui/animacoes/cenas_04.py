"""Animações da aula 04 - teclado."""

from base import *  # noqa: F401,F403


def bloco_de_notas(ax, x, y, w, h, linhas, selecionado=0.0, titulo_janela="Sem título - Bloco de Notas", cursor_texto=True,
                   q=0, cores=None):
    """Bloco de Notas com as linhas de texto informadas (x, y = canto inferior esquerdo)."""
    janela_programa(ax, x, y, w, h, titulo_janela)
    for i, linha in enumerate(linhas):
        yy = y + h - 0.85 - i * 0.5
        if selecionado > 0 and linha:
            retangulo(ax, x + 0.25, yy - 0.2, len(linha) * 0.2 + 0.1, 0.4, fc="#BFDBFE", ec="none",
                      alpha=selecionado, raio=0.02)
        cor = cores[i] if cores and i < len(cores) else TINTA
        texto(ax, x + 0.3, yy, linha, tamanho=12, mono=True, cor=cor)
    if cursor_texto and (q // 5) % 2 == 0:
        ultima = linhas[-1] if linhas else ""
        yy = y + h - 0.85 - (len(linhas) - 1 if linhas else 0) * 0.5
        retangulo(ax, x + 0.3 + len(ultima) * 0.2 + 0.03, yy - 0.2, 0.05, 0.4, fc=TINTA, ec="none", raio=0)


# -----------------------------------------------------------------------------
# write, press e hotkey
# -----------------------------------------------------------------------------
def write_press_hotkey(ax, q):
    titulo(ax, "Teclado: write, press e hotkey")

    passos = [
        ('pyautogui.write("Ola, mundo!")', "digita o texto letra por letra"),
        ('pyautogui.press("enter")', "aperta UMA tecla"),
        ('pyautogui.hotkey("ctrl", "a")', "atalho: Ctrl + A (seleciona tudo)"),
    ]
    inicios = [6, 40, 62]
    atual = 0
    for k, inicio in enumerate(inicios):
        if q >= inicio:
            atual = k

    for k, (comando, nota) in enumerate(passos):
        codigo(ax, 9.9, 6.6 - k * 1.1, comando, tamanho=11, destaque=1.0 if k == atual else 0,
               alpha=1.0 if q >= inicios[k] - 4 else 0.3)
        texto(ax, 9.9, 6.15 - k * 1.1, nota, tamanho=9.5, cor=SUAVE, alpha=1.0 if q >= inicios[k] else 0)

    frase = "Ola, mundo!"
    digitadas = int(len(frase) * progresso(q, inicios[0] + 2, inicios[0] + 28)) if q >= inicios[0] else 0
    linhas = [frase[:digitadas]]
    if q >= inicios[1] + 6:
        linhas.append("")
    selecao = progresso(q, inicios[2] + 10, inicios[2] + 14)
    bloco_de_notas(ax, 0.6, 2.9, 8.8, 4.2, linhas, selecionado=selecao, q=q, cursor_texto=selecao < 0.5)

    # teclado
    letra_atual = frase[digitadas - 1].upper() if 0 < digitadas and q < inicios[0] + 30 else ""
    pisca_letra = 1.0 if letra_atual and (q % 3) != 2 else 0.0
    enter = janela(q, inicios[1] + 3, inicios[1] + 9, 1, 2)
    ctrl = janela(q, inicios[2] + 4, inicios[2] + 16, 1, 2)
    tecla_a = janela(q, inicios[2] + 8, inicios[2] + 14, 1, 2)
    y = 1.6
    tecla(ax, 1.4, y, "Tab", w=1.3)
    tecla(ax, 3.0, y, "Ctrl", pressionada=ctrl, w=1.4)
    tecla(ax, 4.6, y, "Shift", w=1.4)
    tecla(ax, 6.1, y, letra_atual if letra_atual not in ("", " ") else "·", pressionada=pisca_letra, w=1.0)
    tecla(ax, 7.4, y, "A", pressionada=tecla_a, w=1.0)
    tecla(ax, 9.0, y, "Enter", pressionada=enter, w=1.6)
    texto(ax, 10.3, y, "teclas apertadas pelo robô", tamanho=10, cor=SUAVE)


# -----------------------------------------------------------------------------
# Acentos: write x pyperclip + Ctrl+V
# -----------------------------------------------------------------------------
def acentos_pyperclip(ax, q):
    titulo(ax, "Acentos: write() falha · copiar e colar resolve")

    texto_original = "Fábrica São Paulo"

    # lado esquerdo: write
    codigo(ax, 0.6, 7.1, 'pyautogui.write("Fábrica São Paulo")', tamanho=10.5)
    sem_acentos = "".join(c for c in texto_original if c not in "áã")
    n = int(len(sem_acentos) * progresso(q, 6, 26))
    bloco_de_notas(ax, 0.6, 3.6, 7.0, 2.9, [sem_acentos[:n]], q=q, titulo_janela="Bloco de Notas")
    erro = progresso(q, 28, 34)
    if erro > 0:
        balao(ax, 4.1, 3.0, "Fbrica So Paulo  ✗  os acentos sumiram!", alpha=erro, tamanho=11, fc="#FEE2E2", cor=VERMELHO,
              mono=False)

    # lado direito: pyperclip
    b = 44
    codigo(ax, 8.4, 7.1, 'pyperclip.copy("Fábrica São Paulo")', tamanho=10.5, alpha=progresso(q, b, b + 4),
           destaque=janela(q, b, b + 22, 2, 2))
    codigo(ax, 8.4, 6.55, 'pyautogui.hotkey("ctrl", "v")', tamanho=10.5, alpha=progresso(q, b + 18, b + 22),
           destaque=janela(q, b + 22, b + 40, 2, 2))

    # área de transferência
    copia = progresso(q, b + 4, b + 14)
    retangulo(ax, 9.0, 4.4, 5.8, 1.3, fc="#F0FDF4", ec=VERDE, lw=2, alpha=progresso(q, b, b + 4))
    texto(ax, 9.2, 5.45, "área de transferência", tamanho=9.5, cor=VERDE, alpha=progresso(q, b, b + 4))
    texto(ax, 9.3, 4.9, texto_original, tamanho=13, mono=True, alpha=copia)

    cola = progresso(q, b + 26, b + 34)
    if 0 < cola < 1:
        valor_solto(ax, 11.9, mix(4.9, 2.4, cola), texto_original, cor=VERDE, tamanho=12)
    bloco_de_notas(ax, 8.4, 0.9, 7.0, 2.6, [texto_original if cola >= 1 else ""], q=q, titulo_janela="Bloco de Notas")
    if cola >= 1:
        texto(ax, 14.9, 1.55, "✓", tamanho=20, cor=VERDE, ha="center")
    tecla(ax, 13.6, 6.0, "Ctrl", pressionada=janela(q, b + 24, b + 32, 1, 2), w=1.1, h=0.6, tamanho=10)
    tecla(ax, 14.9, 6.0, "V", pressionada=janela(q, b + 26, b + 32, 1, 2), w=0.8, h=0.6, tamanho=10)

    legenda(ax, "Por isso criamos a função digitar(): copia e cola qualquer texto", progresso(q, b + 40, b + 46))


ANIMACOES = {
    "write_press_hotkey": (write_press_hotkey, 110),
    "acentos_pyperclip": (acentos_pyperclip, 120),
}
