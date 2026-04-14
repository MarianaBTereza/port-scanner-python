import socket

alvo = input("Digite o IP ou site: ")
print(f"Escaneando portas em {alvo}...\n")

for porta in range(1, 2025):
    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cliente.settimeout(1)

    resultado = cliente.connect_ex((alvo, porta))

    if resultado == 0:
        print(f"Porta {porta} está aberta")

    cliente.close()