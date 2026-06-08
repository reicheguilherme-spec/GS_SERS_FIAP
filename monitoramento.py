def verificar_sistema(temp, energia, comunicacao, modulo):
 
    alertas = []
    acoes = []

    if temp > 80:
        alertas.append("Temperatura muito alta")
        acoes.append("Ligar sistema de resfriamento")

    if energia < 20:
        alertas.append("Energia muito baixa")
        acoes.append("Ativar modo economia")

    if comunicacao == "ruim":
        alertas.append("Falha na comunicacao")
        acoes.append("Reiniciar comunicacao")

    if modulo == "falha":
        alertas.append("Modulo com defeito")
        acoes.append("Isolar modulo")

    return alertas, acoes


print("=" * 50)
print("MONITORAMENTO DA MISSAO ESPACIAL")
print("=" * 50)

temperatura = float(input("Temperatura (°C): "))
energia = float(input("Energia (%): "))
comunicacao = input("Comunicacao (boa/ruim): ").lower()
modulo = input("Modulo (ativo/falha): ").lower()

alertas, acoes = verificar_sistema(
    temperatura,
    energia,
    comunicacao,
    modulo
)

print("\nDADOS DA MISSAO")
print("-" * 50)

print("Temperatura:", temperatura, "°C")
print("Energia:", energia, "%")
print("Comunicacao:", comunicacao)
print("Modulo:", modulo)

print("\nALERTAS")

if len(alertas) == 0:
    print("Nenhum alerta encontrado")
else:
    for alerta in alertas:
        print("-", alerta)

print("\nACOES AUTOMATICAS")

if len(acoes) == 0:
    print("Sistema funcionando normalmente!")
else:
    for acao in acoes:
        print("-", acao)