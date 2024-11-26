kv_ano = input("Qual o consumo Anual presente na etiqueta: ")
horas_de_uso = input("Quantas horas por dia o equipamento será usado: ")
TARIFA = 0.65
DIA_DO_ANO = 365
HORA_POR_DIA = 24
MEDIA_DIA_MES = 30

kv_dia = float(kv_ano) / DIA_DO_ANO

consumo_hora = kv_dia / HORA_POR_DIA

consumo_diario = float(horas_de_uso) * consumo_hora

consumo_mes = consumo_diario * MEDIA_DIA_MES

custo_por_mes = consumo_mes * TARIFA

custo_por_dia = consumo_diario * TARIFA

print("*************** CONSUMO DE ENERGIA POR MES ****************")
print(f"Seu Consumo de Energia por mês será de R${custo_por_dia:.2f}")
print(f"Seu Consumo de Energia por mês será de R${custo_por_mes:.2f}")