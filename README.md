# Otimização por Enxame de Partículas (PSO)
## Descrição
Este repositório contém uma implementação do algoritmo de Otimização por Enxame de Partículas (PSO) em Python. PSO é um algoritmo de otimização estocástico baseado em população, inspirado no comportamento social de pássaros em bandos ou peixes em cardumes. É comumente utilizado para resolver problemas de otimização em diversos domínios.

O algoritmo PSO implementado aqui consiste em duas classes principais:

PSOResult: Uma classe para armazenar os resultados da otimização PSO, incluindo a melhor partícula encontrada, sua pontuação correspondente e o número de iterações executadas.
Algotitmo_PSO: A classe do algoritmo PSO, que recebe a função objetivo a ser otimizada, o número de dimensões no espaço de busca, o número de partículas na população e parâmetros opcionais como o peso da inércia (inertia), coeficiente de aceleração cognitiva (c1) e coeficiente de aceleração social (c2).

## Funções Objetivo
Dois exemplos de funções objetivo são fornecidos no arquivo test.py para fins de demonstração:

sphere_function: Uma função simples que representa um problema de otimização convexa. Ela calcula a soma dos quadrados de todas as variáveis de entrada.
simple_max_function: Esta função é derivada da função esfera, mas invertida para representar um problema de maximização.

## Uso
Para usar o algoritmo PSO, basta criar uma instância da classe Algotitmo_PSO com a função objetivo desejada, dimensões e outros parâmetros. Em seguida, chame o método optimize com o número desejado de iterações. Por fim, recupere os resultados do objeto PSOResult retornado.

## Exemplo
Um exemplo de uso do algoritmo PSO é fornecido no arquivo test.py. Ele inclui duas funções de teste, uma para minimização e outra para maximização, juntamente com suas respectivas funções objetivo.

## Requisitos
Python 3.x
NumPy

## Licença
Este projeto está licenciado sob a Licença MIT - consulte o arquivo LICENSE para obter mais detalhes.
