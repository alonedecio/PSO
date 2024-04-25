import numpy as np

class PSOResult(object):
    def __init__(self, best_particle, best_score, num_iterations):
        self.best_particle = best_particle
        self.best_score = best_score
        self.num_iterations = num_iterations

class Algotitmo_PSO(object):
    def __init__(self, obj_func, num_dimensions, num_particles, mode='min', inertia=0.72984, c1=2.05, c2=2.05):
        assert mode in ['min', 'max'], "mode deve ser 'min' ou 'max'"
        
        self.obj_func = obj_func
        self.num_dimensions = num_dimensions
        self.num_particles = num_particles
        self.mode = mode
        self.inertia = inertia
        self.c1 = c1
        self.c2 = c2

        self.X = np.random.uniform(size=(self.num_particles, self.num_dimensions))
        self.V = np.random.uniform(size=(self.num_particles, self.num_dimensions))

        self.Pbest = self.X.copy()
        self.fitness_value = self.obj_func(self.X)
        if self.mode == 'min':
            self.Gbest = self.Pbest[np.argmin(self.fitness_value)]
            self.best_score = np.min(self.fitness_value)
        else:
            self.Gbest = self.Pbest[np.argmax(self.fitness_value)]
            self.best_score = np.max(self.fitness_value)

    def _update(self):
        r1 = np.random.uniform(size=(self.num_particles, self.num_dimensions))
        r2 = np.random.uniform(size=(self.num_particles, self.num_dimensions))

        self.V = self.inertia * (self.V
                                + self.c1 * r1 * (self.Pbest - self.X)
                                + self.c2 * r2 * (self.Gbest - self.X))
        self.X = self.X + self.V

        scores = self.obj_func(self.X)
        
        if self.mode == 'min':
            better_scores_idx = scores < self.fitness_value
        else:
            better_scores_idx = scores > self.fitness_value

        self.Pbest[better_scores_idx] = self.X[better_scores_idx]
        self.fitness_value = scores

        if self.mode == 'min':
            self.Gbest = self.Pbest[np.argmin(self.fitness_value)]
            self.best_score = np.min(self.fitness_value)

        else:
            self.Gbest = self.Pbest[np.argmax(self.fitness_value)]
            self.best_score = np.max(self.fitness_value)

    def optimize(self, max_iter):
        for i in range(max_iter):
            self._update()

        return PSOResult(
            best_particle=self.Gbest,
            best_score=self.best_score,
            num_iterations=max_iter
        )