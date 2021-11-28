import numpy as np
from scipy.stats import poisson


def generate_task_arrival(seed, rate):
    # Gera a distribuição de poisson
    poisson_set = generate_poisson(rate)

    # Cria o arquivo
    task_arrival_file = open('task_arrival_seed_' + str(seed) + '_rate_' + str(rate) + '.txt', 'w')

    #Escreve no arquivo
    for i in poisson_set:
        task_arrival_file.write(str(i) + "\n")

    task_arrival_file.close()


def generate_poisson(rate):
    # taxa da esperança de ocorrência
    lamb = rate

    # tamanho (quantidade de valores a serem gerados)
    size = 10

    arrival = np.random.poisson(lamb, size)
    return arrival


SEED = [1, 2, 3, 4, 5]
RATE = [1, 2, 3, 4, 5]

for seed in SEED:
    for rate in RATE:
        generate_task_arrival(seed, rate)
