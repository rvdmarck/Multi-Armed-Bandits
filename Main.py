import Plotter
from random import randint, gauss, uniform
import math

N = 4
Q_initial = 0
steps = 1000
nr_sim = 500
Q_stars = [2.3, 2.1, 1.5, 1.3]
std_devs = [0.9, 0.6, 0.4, 2]
Qs = [Q_initial] * N
results = []

qstar_arm1 = [Q_stars[0]] * steps
qstar_arm2 = [Q_stars[1]] * steps
qstar_arm3 = [Q_stars[2]] * steps
qstar_arm4 = [Q_stars[3]] * steps

Q_history_arm_random = [0] * N
for i in range(len(Q_history_arm_random)):
    Q_history_arm_random[i] = [0] * steps

Q_history_arm_greedy0 = [0] * N
for i in range(len(Q_history_arm_greedy0)):
    Q_history_arm_greedy0[i] = [0] * steps
Q_history_arm_greedy01 = [0] * N
for i in range(len(Q_history_arm_greedy01)):
    Q_history_arm_greedy01[i] = [0] * steps
Q_history_arm_greedy02 = [0] * N
for i in range(len(Q_history_arm_greedy02)):
    Q_history_arm_greedy02[i] = [0] * steps
Q_history_arm_greedyVar = [0] * N
for i in range(len(Q_history_arm_greedyVar)):
    Q_history_arm_greedyVar[i] = [0] * steps

Q_history_arm_softmax1 = [0] * N
for i in range(len(Q_history_arm_softmax1)):
    Q_history_arm_softmax1[i] = [0] * steps
Q_history_arm_softmax01 = [0] * N
for i in range(len(Q_history_arm_softmax01)):
    Q_history_arm_softmax01[i] = [0] * steps
Q_history_arm_softmaxVar = [0] * N
for i in range(len(Q_history_arm_softmaxVar)):
    Q_history_arm_softmaxVar[i] = [0] * steps


def main():
    random()

    epsilon = 0
    greedy(epsilon)

    epsilon = 0.1
    greedy(epsilon)

    epsilon = 0.2
    greedy(epsilon)

    #greedy(-1, True)

    tau = 1
    softmax(tau)

    tau = 0.1
    softmax(tau)

    #softmax(-1, True)

    Plotter.Plotter1(results)

    """
    Plotter.Plotter2([qstar_arm1, Q_history_arm_random[0], Q_history_arm_greedy0[0], Q_history_arm_greedy01[0],
                      Q_history_arm_greedy02[0], Q_history_arm_softmax1[0],
                      Q_history_arm_softmax01[0]])

    Plotter.Plotter2([qstar_arm2, Q_history_arm_random[1], Q_history_arm_greedy0[1], Q_history_arm_greedy01[1],
                      Q_history_arm_greedy02[1], Q_history_arm_softmax1[1],
                      Q_history_arm_softmax01[1]])

    Plotter.Plotter2([qstar_arm3, Q_history_arm_random[2], Q_history_arm_greedy0[2], Q_history_arm_greedy01[2],
                      Q_history_arm_greedy02[2], Q_history_arm_softmax1[2],
                      Q_history_arm_softmax01[2]])

    Plotter.Plotter2([qstar_arm4, Q_history_arm_random[3], Q_history_arm_greedy0[3], Q_history_arm_greedy01[3],
                      Q_history_arm_greedy02[3], Q_history_arm_softmax1[3],
                      Q_history_arm_softmax01[3]])

    Plotter.Plotter5([qstar_arm1, Q_history_arm_random[0], Q_history_arm_greedy0[0], Q_history_arm_greedy01[0],
                      Q_history_arm_greedy02[0], Q_history_arm_greedyVar[0], Q_history_arm_softmax1[0],
                      Q_history_arm_softmax01[0], Q_history_arm_softmaxVar[0]])

    Plotter.Plotter5([qstar_arm2, Q_history_arm_random[1], Q_history_arm_greedy0[1], Q_history_arm_greedy01[1],
                      Q_history_arm_greedy02[1], Q_history_arm_greedyVar[1], Q_history_arm_softmax1[1],
                      Q_history_arm_softmax01[1], Q_history_arm_softmaxVar[1]])

    Plotter.Plotter5([qstar_arm3, Q_history_arm_random[2], Q_history_arm_greedy0[2], Q_history_arm_greedy01[2],
                      Q_history_arm_greedy02[2], Q_history_arm_greedyVar[2], Q_history_arm_softmax1[2],
                      Q_history_arm_softmax01[2], Q_history_arm_softmaxVar[2]])

    Plotter.Plotter5([qstar_arm4, Q_history_arm_random[3], Q_history_arm_greedy0[3], Q_history_arm_greedy01[3],
                      Q_history_arm_greedy02[3], Q_history_arm_greedyVar[3], Q_history_arm_softmax1[3],
                      Q_history_arm_softmax01[3], Q_history_arm_softmaxVar[3]])
    """

def generateRewards():
    rewards = [0] * N
    for j in range(N):
        mu = Q_stars[j]
        sigma = std_devs[j]
        rewards[j] = gauss(mu, sigma)
    return rewards


def computeQ(tmpQ, counts):
    realQ = [0] * N
    for j in range(N):
        if counts[j] != 0:
            realQ[j] = tmpQ[j] / counts[j]
    return realQ


def random():
    print("RANDOM :")
    global_counts = [0] * N
    reward_history = [0] * (steps + 1)

    for sim in range(nr_sim):

        counts = [0] * N
        Qs = [Q_initial] * N
        for i in range(steps):
            rewards = generateRewards()
            realQ = computeQ(Qs, counts)
            for j in range(N):
                Q_history_arm_random[j][i] += realQ[j]
            chosen_action = randint(0, N - 1)
            counts[chosen_action] += 1
            global_counts[chosen_action] += 1
            current_reward = rewards[chosen_action]
            reward_history[i + 1] += current_reward
            Qs[chosen_action] += current_reward
    for i in range(len(reward_history)):
        reward_history[i] = reward_history[i] / nr_sim
    results.append(reward_history)
    for i in range(len(Q_history_arm_random)):
        for j in range(len(Q_history_arm_random[i])):
            Q_history_arm_random[i][j] /= nr_sim

    """
    hist_values = []
    for i in range(N):
        global_counts[i] /= nr_sim
    for i in range(N):
        hist_values += [i]*math.ceil(global_counts[i])
    Plotter.Plotter3(hist_values)
    """


def greedy(epsilon, varying=False):
    print("GREEDY-" + str(epsilon) + " :")
    global_counts = [0] * N
    reward_history = [0] * (steps + 1)
    if varying:
        epsilon = -1

    for sim in range(nr_sim):

        counts = [0] * N
        Qs = [Q_initial] * N
        for i in range(steps):
            rewards = generateRewards()
            realQ = computeQ(Qs, counts)
            if epsilon == 0 and not varying:
                for j in range(N):
                    Q_history_arm_greedy0[j][i] += realQ[j]
            elif epsilon == 0.1 and not varying:
                for j in range(N):
                    Q_history_arm_greedy01[j][i] += realQ[j]
            elif epsilon == 0.2 and not varying:
                for j in range(N):
                    Q_history_arm_greedy02[j][i] += realQ[j]
            elif varying:
                for j in range(N):
                    Q_history_arm_greedyVar[j][i] += realQ[j]
            if varying:
                epsilon = 1 / math.sqrt(i + 1)

            chosen_action = greedy_selection(epsilon, realQ)
            counts[chosen_action] += 1
            global_counts[chosen_action] += 1
            current_reward = rewards[chosen_action]
            reward_history[i + 1] += current_reward
            Qs[chosen_action] += current_reward
    for i in range(len(reward_history)):
        reward_history[i] /= nr_sim
    results.append(reward_history)

    if varying:
        epsilon = -1
    if epsilon == 0:
        for i in range(len(Q_history_arm_greedy0)):
            for j in range(len(Q_history_arm_greedy0[i])):
                Q_history_arm_greedy0[i][j] /= nr_sim
    elif epsilon == 0.1:
        for i in range(len(Q_history_arm_greedy01)):
            for j in range(len(Q_history_arm_greedy01[i])):
                Q_history_arm_greedy01[i][j] /= nr_sim
    elif epsilon == 0.2:
        for i in range(len(Q_history_arm_greedy0)):
            for j in range(len(Q_history_arm_greedy0[i])):
                Q_history_arm_greedy02[i][j] /= nr_sim
    elif epsilon == -1:
        for i in range(len(Q_history_arm_greedyVar)):
            for j in range(len(Q_history_arm_greedyVar[i])):
                Q_history_arm_greedyVar[i][j] /= nr_sim

    """
    hist_values = []
    for i in range(N):
        global_counts[i] /= nr_sim
    for i in range(N):
        hist_values += [i] * math.ceil(global_counts[i])
    Plotter.Plotter3(hist_values)
    """


def greedy_selection(epsilon, realQ):
    r = uniform(0, 1)
    if r > epsilon:
        indexes = [i for i, a in enumerate(realQ) if a == max(realQ)]
        if len(indexes) == 1:
            chosen_action = indexes[0]
        else:
            index = randint(0, len(indexes) - 1)
            chosen_action = index
    else:
        chosen_action = randint(0, N - 1)
    return chosen_action


def softmax(tau, varying=False):
    print("SOFTMAX-" + str(tau) + " :")
    global_counts = [0] * N
    reward_history = [0] * (steps + 1)
    if varying:
        tau = -1

    for sim in range(nr_sim):

        counts = [0] * N
        Qs = [Q_initial] * N
        for i in range(steps):
            rewards = generateRewards()
            realQ = computeQ(Qs, counts)

            if tau == 1 and not varying:
                for j in range(N):
                    Q_history_arm_softmax1[j][i] += realQ[j]
            elif tau == 0.1 and not varying:
                for j in range(N):
                    Q_history_arm_softmax01[j][i] += realQ[j]
            elif varying:
                for j in range(N):
                    Q_history_arm_softmaxVar[j][i] += realQ[j]

            if varying:
                tau = 4 * ((1000 - i + 1) / 1000)
            chosen_action = softmax_selection(tau, realQ)
            counts[chosen_action] += 1
            global_counts[chosen_action] += 1
            current_reward = rewards[chosen_action]
            reward_history[i + 1] += current_reward
            Qs[chosen_action] += current_reward
    for i in range(len(reward_history)):
        reward_history[i] /= nr_sim
    results.append(reward_history)

    if varying:
        tau = -1
    if tau == 1:
        for i in range(len(Q_history_arm_softmax1)):
            for j in range(len(Q_history_arm_softmax1[i])):
                Q_history_arm_softmax1[i][j] /= nr_sim
    elif tau == 0.1:
        for i in range(len(Q_history_arm_softmax01)):
            for j in range(len(Q_history_arm_softmax01[i])):
                Q_history_arm_softmax01[i][j] /= nr_sim
    elif tau == -1:
        for i in range(len(Q_history_arm_softmaxVar)):
            for j in range(len(Q_history_arm_softmaxVar[i])):
                Q_history_arm_softmaxVar[i][j] /= nr_sim

    """
    hist_values = []
    for i in range(N):
        global_counts[i] /= nr_sim
    for i in range(N):
        hist_values += [i] * math.ceil(global_counts[i])
    Plotter.Plotter3(hist_values)
    """


def softmax_selection(tau, realQ):
    probs = [0] * N
    denominator = 0
    for j in range(N):
        denominator += math.exp(realQ[j] / tau)
    for j in range(N):
        probs[j] = math.exp(realQ[j] / tau) / denominator
    sum = 0
    for j in range(N):
        sum += probs[j]
    return weighted_choice(probs)


def weighted_choice(weights):
    totals = []
    running_total = 0

    for w in weights:
        running_total += w
        totals.append(running_total)

    rnd = uniform(0, 1)
    for i, total in enumerate(totals):
        if rnd < total:
            return i


if __name__ == '__main__':
    main()
