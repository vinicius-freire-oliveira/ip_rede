import psutil  # Importa a biblioteca psutil para obter informações sobre o sistema, como interfaces de rede
import socket  # Importa a biblioteca socket para identificar tipos de endereços IP (IPv4, IPv6)

# Função para obter endereços IP
def obter_enderecos_ip():
    enderecos = []  # Inicializa uma lista vazia para armazenar os endereços IP
    interfaces = psutil.net_if_addrs()  # Obtém informações sobre todas as interfaces de rede disponíveis
    for interface, info in interfaces.items():  # Itera sobre cada interface de rede
        for endereco in info:  # Itera sobre cada endereço associado à interface
            # Verifica se o endereço é IPv4 ou IPv6
            if endereco.family == socket.AF_INET or endereco.family == socket.AF_INET6:
                enderecos.append((interface, endereco.address))  # Adiciona o endereço à lista de endereços
    return enderecos  # Retorna a lista de endereços IP

# Código principal
if __name__ == "__main__":
    print("Endereços IP encontrados:")  # Imprime uma mensagem inicial
    for interface, endereco in obter_enderecos_ip():  # Chama a função e itera sobre os endereços IP retornados
        print(f"{interface}: {endereco}")  # Imprime cada interface e seu endereço IP correspondente
