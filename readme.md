# Lista 04 - Implementação em python do Algoritmo de cifra de bloco

Prob. 2 (6 pontos). Implemente (em C,C++ ou Python) o Algoritmo cifra de bloco explicado em aula. 

## Objetivo

Implementar o algoritmo de cifra de bloco explicado em aula usando Python (v3.11.9) e suas bibliotecas nativas.

## Estrutura do Projeto

DES_ALGORITHM/
│
│-- src/
│    ├── des_tables.py
│    ├── des_utils.py
│    ├── des_core.py
│    └── main.py         ## EXECUTAVEL ##
`-- README.md

## Detalhamento do código

Definições em `src/des_tables.py`:
    - `Guarda as matrizes e tabelas de permutação utilizadas no algoritmo (Tabelas e S-Boxes)`

Definições em `src/des_utils.py`:
    - `Funções auxiliares utilizadas para a manipulação de bits e arrays.`

Definições em `src/des_core.py`:
    - `Algoritmo de criptografia DES, contendo a geração de chaves, a função de rodada e o encriptador`

Definições em `src/main.py`:
    - `Executavel com entrada de dados para o teste do algoritmo.`
    - `Para testar diferentes chaves (56 bits) e mensagens (64 bits), basta inserir os dados nas variaveis de input`
