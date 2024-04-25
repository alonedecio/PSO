import numpy as np
from PSO import Algotitmo_PSO

def test_minimization():
    # Define a função objetivo para minimização
    def sphere_function(X):
        return np.sum(X**2, axis=1)  # Função esfera: f(x) = sum(x_i^2)

    # Cria uma instância de PSO para minimização
    pso = Algotitmo_PSO(obj_func=sphere_function, num_dimensions=5, num_particles=20, mode='min')
    result = pso.optimize(50)  # Executa a otimização por 50 iterações

    print("Teste de Minimização")
    print(f"Melhor partícula: {result.best_particle}")
    print(f"Melhor score (deve ser próximo de 0): {result.best_score}\n")

def test_maximization():
    # Define a função objetivo para maximização
    def simple_max_function(X):
        return -np.sum(X**2, axis=1)  # Inverte a função esfera para maximização

    # Cria uma instância de PSO para maximização
    pso = Algotitmo_PSO(obj_func=simple_max_function, num_dimensions=5, num_particles=20, mode='max')
    result = pso.optimize(50)  # Executa a otimização por 50 iterações

    print("Teste de Maximização")
    print(f"Melhor partícula: {result.best_particle}")
    print(f"Melhor score (deve ser próximo de 0, pois é a inversão da função esfera): {result.best_score}\n")

if __name__ == "__main__":
    test_minimization()
    test_maximization()
