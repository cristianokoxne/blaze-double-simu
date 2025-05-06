import numpy as np
import pandas as pd


payout_vermelho = 2
payout_preto = 2
payout_branco = 14
cores_possiveis = ["branco"] + ["vermelho"] * 7 + ["preto"] * 7


strategies = [
    {"nome": "100% Vermelho", "vermelho": 1.0, "preto": 0.0, "branco": 0.0},
    {"nome": "100% Preto", "vermelho": 0.0, "preto": 1.0, "branco": 0.0},
    {"nome": "100% Branco", "vermelho": 0.0, "preto": 0.0, "branco": 1.0},
    {"nome": "50% Vermelho, 50% Preto", "vermelho": 0.5, "preto": 0.5, "branco": 0.0},
    {"nome": "45% Vermelho, 45% Preto, 10% Branco", "vermelho": 0.45, "preto": 0.45, "branco": 0.10},
    {"nome": "R$7 Vermelho, R$7 Preto, R$1 Branco", "vermelho": 7/15, "preto": 7/15, "branco": 1/15},
]


extended_strategies = strategies + [
    {"nome": "70% Vermelho, 30% Preto", "vermelho": 0.7, "preto": 0.3, "branco": 0.0},
    {"nome": "60% Preto, 40% Branco", "vermelho": 0.0, "preto": 0.6, "branco": 0.4},
    {"nome": "90% Vermelho, 10% Branco", "vermelho": 0.9, "preto": 0.0, "branco": 0.1},
    {"nome": "33% para cada cor", "vermelho": 1/3, "preto": 1/3, "branco": 1/3},
    {"nome": "80% Preto, 20% Vermelho", "vermelho": 0.2, "preto": 0.8, "branco": 0.0},
]


aposta_base = 100
num_rodadas = 100000


sim_results = []

for strategy in extended_strategies:
    apostas = {
        "vermelho": aposta_base * strategy["vermelho"],
        "preto": aposta_base * strategy["preto"],
        "branco": aposta_base * strategy["branco"],
    }

    total_apostado = aposta_base * num_rodadas
    total_ganho = 0

    for _ in range(num_rodadas):
        resultado = np.random.choice(cores_possiveis)
        if resultado == "vermelho":
            total_ganho += apostas["vermelho"] * payout_vermelho
        elif resultado == "preto":
            total_ganho += apostas["preto"] * payout_preto
        elif resultado == "branco":
            total_ganho += apostas["branco"] * payout_branco

    lucro = total_ganho - total_apostado
    roi = lucro / total_apostado

    sim_results.append({
        "Estratégia": strategy["nome"],
        "Total Apostado (R$)": total_apostado,
        "Total Ganhado (R$)": round(total_ganho, 2),
        "Lucro/Prejuízo (R$)": round(lucro, 2),
        "ROI Simulado (%)": round(roi * 100, 2)
    })

# Exibir resultado
df_sim_100 = pd.DataFrame(sim_results)
print(df_sim_100.to_string(index=False))
