import json
from statistics import mean

def calcular_estatisticas_faturamento(dados):
    # Filtrar dias sem faturamento
    faturamento_valido = [dia['valor'] for dia in dados if dia['valor'] > 0]
    
    if not faturamento_valido:
        return None, None, 0
    
    menor_valor = min(faturamento_valido)
    maior_valor = max(faturamento_valido)
    
    media_mensal = mean(faturamento_valido)
    dias_acima_media = sum(1 for valor in faturamento_valido if valor > media_mensal)
    
    return menor_valor, maior_valor, dias_acima_media

# Carregar dados do arquivo JSON
with open('faturamento.json', 'r') as file:
    dados_faturamento = json.load(file)

menor, maior, dias_acima = calcular_estatisticas_faturamento(dados_faturamento)

if menor is not None:
    print(f"Menor valor de faturamento: R$ {menor:.2f}")
    print(f"Maior valor de faturamento: R$ {maior:.2f}")
    print(f"Número de dias acima da média mensal: {dias_acima}")
else:
    print("Não há dados de faturamento válidos.")