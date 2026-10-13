# GERAR AS BASES DE PRODUÇÃO (DADOS FICTÍCIOS)
# Ele cria a pasta "dados" com as bases usadas no módulo:
#   - producao.xlsx     -> ordens de produção de 2025 (a base principal)
#   - produtos.csv      -> cadastro de produtos (categoria e custo por kg)
#   - unidades.xlsx     -> cadastro de unidades (cidade, gerente e meta mensal)
#   - producao_mensal/  -> uma planilha por mês (aula de juntar arquivos)
# As bases já vêm prontas na pasta "dados". Rode este arquivo só se quiser
# recriá-las. Não é preciso entender este código agora: apenas execute.

import random
from datetime import date, timedelta
from pathlib import Path

import pandas as pd

random.seed(42)   # garante que todos gerem exatamente os mesmos dados

PASTA_DADOS = Path(__file__).parent / "dados"
PASTA_DADOS.mkdir(exist_ok=True)
(PASTA_DADOS / "producao_mensal").mkdir(exist_ok=True)

# Tabelas de apoio
produtos = {
    # produto: (categoria, custo em R$ por kg)
    "Produto_A": ("Granulado", 2.35),
    "Produto_B": ("Granulado", 2.80),
    "Produto_C": ("Pó", 4.10),
    "Produto_D": ("Pó", 3.65),
    "Produto_E": ("Líquido", 5.20),
    "Produto_F": ("Líquido", 6.75),
    "Produto_G": ("Granulado", 1.95),
    "Produto_H": ("Pó", 7.40),
}

unidades = {
    # unidade: (cidade, UF, gerente, capacidade por turno em kg, eficiência típica, produtos que fabrica)
    "Unidade_A": ("Jacareí", "SP", "Marcos Lima", 30000, 0.95, ["Produto_A", "Produto_B", "Produto_C", "Produto_G"]),
    "Unidade_B": ("Suzano", "SP", "Patrícia Rocha", 24000, 0.91, ["Produto_A", "Produto_D", "Produto_E", "Produto_H"]),
    "Unidade_C": ("Cruz Alta", "RS", "Ricardo Nunes", 18000, 0.86, ["Produto_B", "Produto_C", "Produto_F"]),
    "Unidade_D": ("Uberaba", "MG", "Fernanda Alves", 20000, 0.92, ["Produto_D", "Produto_E", "Produto_G", "Produto_H"]),
    "Unidade_E": ("Rio Verde", "GO", "Carlos Souza", 15000, 0.82, ["Produto_A", "Produto_F", "Produto_G"]),
    "Unidade_F": ("Cuiabá", "MT", "-", 9000, 0.88, ["Produto_A", "Produto_G"]),   # NÃO estará no cadastro (de propósito)
}
pesos_unidades = [0.24, 0.22, 0.17, 0.18, 0.15, 0.04]

turnos = ["A", "B", "C"]
motivos_parada = ["Manutenção corretiva", "Manutenção preventiva", "Setup", "Falta de matéria-prima", "Falta de energia"]

# 1. producao.xlsx (uma linha = uma ordem de produção)
linhas = []
for i in range(900):
    data = date(2025, 1, 1) + timedelta(days=random.randint(0, 364))
    unidade = random.choices(list(unidades), weights=pesos_unidades)[0]
    cidade, uf, gerente, capacidade, eficiencia_tipica, mix = unidades[unidade]
    turno = random.choice(turnos)
    produto = random.choice(mix)

    planejada = round(capacidade * random.uniform(0.6, 1.0), -2)

    eficiencia = eficiencia_tipica + random.gauss(0, 0.06)
    if turno == "C":
        eficiencia -= 0.05          # turno da noite rende um pouco menos
    horas_paradas = 0.0
    motivo = None
    if random.random() < 0.35:
        horas_paradas = random.choice([0.5, 1.0, 1.5, 2.0, 3.0, 4.0, 6.0])
        motivo = random.choice(motivos_parada)
        eficiencia -= horas_paradas / 8 * 0.6
    eficiencia = min(1.08, max(0.35, eficiencia))
    produzida = round(planejada * eficiencia)

    taxa_refugo = random.uniform(0.0, 0.05)
    if turno == "C":
        taxa_refugo += 0.015
    if produto in ("Produto_E", "Produto_H"):
        taxa_refugo += 0.02
    refugo = round(produzida * taxa_refugo)

    linhas.append({
        "data": pd.Timestamp(data),
        "unidade": unidade,
        "turno": turno,
        "produto": produto,
        "qtd_planejada_kg": int(planejada),
        "qtd_produzida_kg": int(produzida),
        "qtd_refugo_kg": int(refugo),
        "horas_paradas": horas_paradas,
        "motivo_parada": motivo,
    })

producao = pd.DataFrame(linhas).sort_values(["data", "unidade", "turno"]).reset_index(drop=True)
producao.insert(0, "id_ordem", [f"OP-{n:04d}" for n in range(1, len(producao) + 1)])
producao.to_excel(PASTA_DADOS / "producao.xlsx", index=False, sheet_name="Producao")

# 2. produtos.csv (cadastro, no padrão brasileiro: ; e vírgula decimal)
cadastro_produtos = pd.DataFrame([
    {"produto": nome, "categoria": categoria, "custo_kg": custo}
    for nome, (categoria, custo) in produtos.items()
])
cadastro_produtos.to_csv(PASTA_DADOS / "produtos.csv", index=False, sep=";", decimal=",", encoding="utf-8-sig")

# 3. unidades.xlsx (cadastro com a meta mensal; a Unidade_F fica de fora)
fator_meta = {"Unidade_A": 0.95, "Unidade_B": 1.03, "Unidade_C": 1.15, "Unidade_D": 1.00, "Unidade_E": 1.22}
media_mensal = producao.groupby("unidade")["qtd_produzida_kg"].sum() / 12
cadastro_unidades = pd.DataFrame([
    {"unidade": nome, "cidade": cidade, "uf": uf, "gerente": gerente,
     "meta_mensal_kg": int(round(media_mensal[nome] * fator_meta[nome], -3))}
    for nome, (cidade, uf, gerente, *_ ) in unidades.items()
    if nome != "Unidade_F"
])
cadastro_unidades.to_excel(PASTA_DADOS / "unidades.xlsx", index=False)

# 4. producao_mensal/ (uma planilha por mês)
for mes in range(1, 13):
    producao_mes = producao[producao["data"].dt.month == mes]
    producao_mes.to_excel(PASTA_DADOS / "producao_mensal" / f"producao_2025_{mes:02d}.xlsx", index=False)

print("Bases geradas em:", PASTA_DADOS)
