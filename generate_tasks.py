import numpy as np
import random


def generate_tasks(task_n, memo_n, proc_n, stor_n, deadline, seed_n):

    print("Configuration:")
    print(" * " + str(task_n) + " tasks")
    print(" * " + str(memo_n) + " memory")
    print(" * " + str(proc_n) + " processment")
    print(" * " + str(stor_n) + " storage")
    print(" * " + str(seed_n) + " seed")

    # Cria o arquivo
    task_file = open('TASKS_SIZE_' + str(task_n) + '_MEMO_' + str(memo_n) + '_PROC_' + str(proc_n) + '_STOR_' + str(stor_n) + '_SEED_' + str(seed_n) + '.txt', 'w')

    # Gera as tarefas no loop
    for i in range(task_n):
        task_memo = random.randint(1, memo_n)
        task_proc = random.randint(1, proc_n)
        task_stor = random.randint(1, stor_n)
        task_dead = random.randint(5, deadline)

        # <id, memoria, processamento, armazenamento, deadline>
        #Escreve no arquivo
        task_file.write(str(i) + "\t" + str(task_memo) + "\t" + str(task_proc) + "\t" + str(task_stor) + "\t" + str(task_dead) + "\n")

    task_file.close()

#Numero de tasks a serem geradas
number = 10

#Valores para memoria, processamento, armazenamento e deadline
memory = [10, 15, 20, 25, 30]
processment = [10, 15, 20, 25, 30]
storage = [10, 15, 20, 25, 30]
deadline = 9

SEED = [1, 2, 3, 4, 5]

for seed in SEED:
    for i in range(len(memory)):
        for j in range(len(processment)):
            for k in range(len(storage)):
                generate_tasks(number, memory[i], processment[j], storage[k], deadline, seed)
