from datetime import datetime
agora = datetime.now()
data = agora.strftime("%d/%m/%Y")
hora = agora.strftime("%H:%M")

# Exibe o resultado
print(f"Data: {data}")
print(f"Hora: {hora}")
