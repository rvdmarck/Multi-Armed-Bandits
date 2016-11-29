import numpy as np
import Plotter
from random import randint, gauss, uniform
import time

N = 4
Q_initial = 0
steps = 1000
nr_sim = 2000
Q_stars = [2.3, 2.1, 1.5, 1.3]
std_devs = [0.9, 0.6, 0.4, 2]
Qs = [Q_initial]*N
results = []

def main():

    start_time = time.time()
    random()
    print("\t--- %s seconds ---" % (time.time() - start_time))

    start_time = time.time()
    epsilon = 0
    greedy(epsilon)
    print("\t--- %s seconds ---" % (time.time() - start_time))

    start_time = time.time()
    epsilon = 0.1
    greedy(epsilon)
    print("\t--- %s seconds ---" % (time.time() - start_time))

    start_time = time.time()
    epsilon = 0.2
    greedy(epsilon)
    print("\t--- %s seconds ---" % (time.time() - start_time))

    Plotter.Plotter(results)


def random():
    print("RANDOM :")
    counts = [0]*N
    reward_history = [0]* (steps+1)

    for sim in range(nr_sim):
        Qs = [Q_initial] * N
        total_reward = 0
        for i in range(steps):
            rewards = [0] * N
            for j in range(N):
                mu = Q_stars[j]
                sigma = std_devs[j]
                rewards[j] = gauss(mu, sigma)

            chosen_action = randint(0, N - 1)
            counts[chosen_action] += 1
            current_reward = rewards[chosen_action]
            reward_history[i+1] += current_reward
            Qs[chosen_action] += current_reward
            total_reward += current_reward
    for i in range(len(reward_history)):
        reward_history[i] = reward_history[i]/nr_sim
    #Plotter.Plotter(reward_history)
    results.append(reward_history)

    """
    print("\tTotal Reward : "+str(total_reward))
    print("\tMean Total Reward : " + str(total_reward/steps))

    print("\tTotal Q values : "+str(Qs))

    for i in range(N):
        Qs[i] /= counts[i]

    print("\tMean Q values : "+str(Qs))

    deltas = [0]*N
    for i in range(N):
        deltas[i] = abs(Q_stars[i] - Qs[i])
    print("\tDeltas Q-Q* : " + str(deltas))
    """



def greedy(epsilon):
    print("GREEDY-"+str(epsilon)+" :")
    total_reward = 0
    counts = [0] * N
    reward_history = [0] * (steps+1)

    for sim in range(nr_sim):
        Qs = [Q_initial] * N
        total_reward = 0
        for i in range(steps):
            rewards = [0] * N
            for j in range(N):
                mu = Q_stars[j]
                sigma = std_devs[j]
                rewards[j] = gauss(mu, sigma)

            r = uniform(0,1)
            if(r < epsilon):
                chosen_action = rewards.index(max(rewards))
            else:
                chosen_action = randint(0, N - 1)

            counts[chosen_action] += 1
            current_reward = rewards[chosen_action]
            reward_history[i+1] += current_reward
            Qs[chosen_action] += current_reward
            total_reward += current_reward
    for i in range(len(reward_history)):
        reward_history[i] = reward_history[i] / nr_sim
    #Plotter.Plotter(reward_history)
    results.append(reward_history)

    """
    print("\tTotal Reward : " + str(total_reward))
    print("\tMean Total Reward : " + str(total_reward / steps))

    print("\tTotal Q values : " + str(Qs))

    for i in range(N):
        Qs[i] /= counts[i]

    print("\tMean Q values : " + str(Qs))

    deltas = [0] * N
    for i in range(N):
        deltas[i] = abs(Q_stars[i] - Qs[i])
    print("\tDeltas Q-Q* : " + str(deltas))
    """

if __name__ == '__main__':
  main()