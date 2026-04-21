"""
Ponto de entrada principal para testar o algoritmo DES.

Para rodar os casos definidos na lista de exercícios basta comentar ou descomentar as variáveis.

Caso 1:
    chave_K = "10010010010010010010010010010010010010010010010010010010"
    mensagem_M = "1001001001001001001001001001001001001001001001001001001001001001"

Caso 2:
    chave_K = "10111011101111011110101110111101110111101011011101110111"
    mensagem_M = "1001001001001001001001001001001001001001001001001001001001001001"
"""

from des_core import des_encrypt

def main():
    # Casos definidos na lista de exercícios

    ## Caso 1:
    chave_K = "10010010010010010010010010010010010010010010010010010010"
    mensagem_M = "1001001001001001001001001001001001001001001001001001001001001001"

    ## Caso 2:
    # chave_K = "10111011101111011110101110111101110111101011011101110111"
    # mensagem_M = "1001001001001001001001001001001001001001001001001001001001001001"

    print("=======================================")
    print("      SIMULADOR DES - MODO BLOCO       ")
    print("=======================================\n")
    
    print(f"[INPUT] Chave (K):    {chave_K} ({len(chave_K)} bits)")
    print(f"[INPUT] Mensagem (M): {mensagem_M} ({len(mensagem_M)} bits)\n")
    
    try:
        # Executa a criptografia
        texto_cifrado = des_encrypt(mensagem_M, chave_K)
        print(f"[OUTPUT] Cifrado (C): {texto_cifrado} ({len(texto_cifrado)} bits)")
        print("\nProcesso finalizado com sucesso!")
        
    except ValueError as e:
        print(f"\n[ERRO] Falha na validação: {e}")

if __name__ == "__main__":
    main()