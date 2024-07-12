import math

def eh_primo(numero):
    if numero < 2:
        return False, f"{numero} não é um número primo porque é menor que 2."
    if numero == 2:
        return True, f"{numero} é um número primo."
    if numero % 2 == 0:
        return False, f"{numero} não é um número primo porque é divisível por 2."
    for i in range(3, int(math.sqrt(numero)) + 1, 2):
        if numero % i == 0:
            return False, f"{numero} não é um número primo porque é divisível por {i}."
    return True, f"{numero} é um número primo."

def main():
   
        entrada = input("Digite um número natural: ")
        numero = int(entrada)
        primo,mensagem = eh_primo(numero)
        print(mensagem)
    

if __name__ == "__main__":
    main()
