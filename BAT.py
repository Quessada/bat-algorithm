# -*- coding: utf-8 -*-
"""
author = Matheus Sanches Quessada
email = matheus.quessada@unesp.br

"""
import math
import numpy
import random
import time

def F5(x):
    dim  = len(x)
    o = numpy.sum(100*(x[1:dim]-(x[0:dim-1]**2))**2+(x[0:dim-1]-1)**2)
    return o;

def euclidiana(y,z):
    # x, y, z = C, XP, X
    return (numpy.sqrt(sum((y - z) ** 2))) #distancia euclidiana

#def BAT(objf, lb, ub, dim, N, Max_iteration):
def BAT(sw, Serv_List):
    MaxIter = 5
    dim = 4
    n = dim
    Nro_serv = len(Serv_List)


    # Population size

    N_gen = MaxIter  # Number of generations

    A = 0.5
    # Loudness  (constant or decreasing)
    r = 0.5
    # Pulse rate (constant or decreasing)

    Qmin = 0  # Frequency minimum
    Qmax = 2  # Frequency maximum

    d = dim  # Number of dimensions

    # Initializing arrays
    Q = numpy.zeros(Nro_serv)  # Frequency
    v = numpy.zeros((Nro_serv, dim))  # Velocities
    Convergence_curve = []
    
    l = 0

    # Initialize the population/solutions
    Sol = numpy.zeros((Nro_serv, dim))
    for j in Serv_List:
        for i in range (0, dim):
            y = numpy.array([Serv_List[j][i] / 100])
            z = numpy.array([sw[0][i]])
            Sol[i, l] = euclidiana(y,z)
        l += 1

    S = numpy.zeros((Nro_serv, dim))
    S = numpy.copy(Sol)
    Fitness = numpy.zeros(Nro_serv)

    # Initialize timer for the experiment
    timerStart = time.time()

    # Evaluate initial random solutions
    for i in range(0, Nro_serv):
        Fitness[i] = F5(Sol[i, :])
        print("SOL = ", Sol[i, :])
        print("FITNESS = ", Fitness[i])

    # Find the initial best solution and minimum fitness
    I = numpy.argmin(Fitness)
    best = Sol[I, :]
    fmin = min(Fitness)
    Best = I

    # Main loop
    for t in range(0, Nro_serv):
        print("SERV_LIST = ", Serv_List)
        print("NRO_SERV = ", Nro_serv)
        # Loop over all bats(solutions)
        for i in range(0, dim):
            Q[i] = Qmin + (Qmin - Qmax) * random.random()
            v[i, :] = v[i, :] + (Sol[i, :] - best) * Q[i]
            S[i, :] = Sol[i, :] + v[i, :]

            # Pulse rate
            if random.random() > r:
                S[i, :] = best + 0.001 * numpy.random.randn(d)

            # Evaluate new solutions
            Fnew = F5(S[i, :])

            # Update if the solution improves
            if (Fnew <= Fitness[i]) and (random.random() < A):
                Sol[i, :] = numpy.copy(S[i, :])
                Fitness[i] = Fnew
                Best = i

            # Update the current best solution
            if Fnew <= fmin:
                best = numpy.copy(S[i, :])
                fmin = Fnew
                Best = i


        # update convergence curve
        Convergence_curve.append(fmin)

        if t % 1 == 0:
            print(["At iteration " + str(t) + " the best fitness is " + str(fmin)])

    timerEnd = time.time()

    selected = ""

    if(Best == 0):
        selected = "atual"
    elif(Best == 1):
        selected = "Fog1"
    elif(Best == 2):
        selected = "Fog2"
    elif(Best == 3):
        selected = "Fog3"
    else:
        selected = "erro"

    return selected