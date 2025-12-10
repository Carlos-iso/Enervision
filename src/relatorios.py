def exibir(consumo, otimizado, pico, anomalia):
    print("================ d-_-b ================")
    print(f"\nConsumo atual: {consumo} W")
    print(f"Consumo otimizado: {otimizado:.2f} W\n")
    if pico:
        print("⚠️ Pico de demanda detectado!\n")
    if anomalia:
        print("🔧 Anomalia detectada! Manutenção preventiva recomendada.\n")
    print("=======================================")