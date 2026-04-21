"""
Núcleo do algoritmo de criptografia DES (Data Encryption Standard).
Contém a geração de chaves, a função de rodada e o encriptador principal.
"""

from des_tables import IP, IP_INV, E_TABLE, P_TABLE, PC1, PC2, S_BOXES
from des_utils import permute, xor_bits

def keyschedule(k_56):
    """Gera as 16 subchaves de 48 bits a partir da chave inicial de 56 bits."""
    k_pc1 = ""
    for b in PC1:
        q = b // 8
        idx = (b - q) - 1 
        k_pc1 += k_56[idx]
    
    C, D = k_pc1[:28], k_pc1[28:]
    subkeys = []
    
    for r in range(1, 17):
        shift = 1 if r in [1, 2, 9, 16] else 2
        C = C[shift:] + C[:shift]
        D = D[shift:] + D[:shift]
        
        k_r = permute(C + D, PC2)
        subkeys.append(k_r)
        
    return subkeys

def f_function(R, J):
    """Função de rodada de Feistel (f)."""
    R_exp = permute(R, E_TABLE)
    xored = xor_bits(R_exp, J)
    
    s_output = ""
    for i in range(8):
        block = xored[i*6 : (i+1)*6]
        row = int(block[0] + block[5], 2)
        col = int(block[1:5], 2)
        val = S_BOXES[i][row][col]
        s_output += f"{val:04b}"
        
    return permute(s_output, P_TABLE)

def des_encrypt(M, K):
    """
    Criptografa um bloco utilizando o algoritmo DES.
    
    Args:
      M (str): Plaintext de 64 bits composto por "0"s e "1"s.
      K (str): Chave de 56 bits composta por "0"s e "1"s.
      
    Returns:
      str: Ciphertext resultante de 64 bits.
    """
    if len(K) != 56 or len(M) != 64:
        raise ValueError("Erro: A chave K deve ter exatos 56 bits e a mensagem M exatos 64 bits.")
        
    K_rounds = keyschedule(K)
    M = permute(M, IP)
    L, R = M[:32], M[32:]
    
    for r in range(16):
        L_next = R
        R_next = xor_bits(L, f_function(R, K_rounds[r]))
        L, R = L_next, R_next
        
    return permute(L + R, IP_INV)