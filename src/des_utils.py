"""
Funções auxiliares para manipulação de bits e arrays.
"""

def permute(bits_str, table):
    """
    Aplica uma tabela de permutação/expansão sobre uma string de bits.
    
    Args:
        bits_str (str): A string binária original.
        table (list): A lista de inteiros representando os índices da permutação (base-1).
        
    Returns:
        str: A nova string de bits permutada.
    """
    return "".join(bits_str[i - 1] for i in table)

def xor_bits(b1, b2):
    """
    Aplica a operação XOR bit a bit entre duas strings binárias de mesmo tamanho.
    
    Args:
        b1 (str): Primeira string binária.
        b2 (str): Segunda string binária.
        
    Returns:
        str: Resultado do XOR.
    """
    return "".join("1" if x != y else "0" for x, y in zip(b1, b2))