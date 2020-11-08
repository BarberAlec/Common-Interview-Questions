# https://medium.com/@data.scientist/solving-the-interesting-bytedance-interview-question-bb30b31cdf5

'''10 small balls are randomly divided into 12 boxes. You need to find the probability that exactly 10 boxes are empty with a program. 
   The program is required to simulate 100,000 times in order to calculate the probability with “brute-force”.'''

# Note this can be caluclated using ordinary rules of probability, but the objective is to use Monte-Carlo Methods
# The task is hard as the prob is quite low, so after running 100,000 times, you will typically get a prob of 0,
# Which is not true. The task is to use 100,000 iterations, but get a good result.
import random
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
import math

random.seed()


class byteDanceMC:
    def simple(self, iter_num):
        return self._run_naive_(iter_num)

    def TOTP_advancment(self, iter_num):
        return self._run_multiEvents_(iter_num)

    def medium_original(self, iter_num):
        return self._run_medium_(iter_num)

    # medium original
    def _run_medium_(self, iter_num):
        prob_part1, states_part1 = self.simulations_part1(10000)
        prob_part2 = self.simulations_part2(90000, states_part1)
        return prob_part1 * prob_part2

    def simulations_part1(self, number):
        five_empty_boxes = 0
        states = []
        for i in range(number):
            result = self._stimulation_(5, [0] * 12)
            if self._emptyBoxes_(result) >= 10:
                five_empty_boxes += 1
                states.append(result)
        return float(five_empty_boxes) / number, states

    def simulations_part2(self, number, states):
        ten_empty_boxes = 0
        for i in range(number):
            index = random.randint(0, len(states)-1)
            state = states[index][:]
            result = self._stimulation_(5, state)
            if self._emptyBoxes_(result) == 10:
                ten_empty_boxes += 1
        return float(ten_empty_boxes) / number

    def _stimulation_(self, balls=10, boxes=[0] * 12):
        for i in range(balls):
            index = random.randint(0, 11)
            boxes[index] += 1
        return boxes

    def _emptyBoxes_(self, boxes):
        number = 0
        for item in boxes:
            if item == 0:
                number += 1
        return number

    # Naive
    def _run_naive_(self, iter_num):
        '''Run naive approach.
        Note: this will probably result in zero as the true probability is so low.'''
        summ = 0
        for i in range(iter_num):
            summ += self._run_once_naive_()

        return summ/iter_num

    def _run_once_naive_(self):
        '''Return 0 for False, return 1 for True'''
        box_list = np.zeros(12)
        for i in range(10):
            index = random.randint(0, 11)
            box_list[index] += 1

        # Check if exactly 10 are empty
        count = 0
        for box in box_list:
            if box == 0:
                count += 1

        if count == 10:
            return 1
        else:
            return 0

    # TOTP advancment (legacy)
    def _run_multiEvents_(self, iter_num):
        '''This is inspired by link on top of page, but expanded'''
        p1 = 0
        p2 = 0
        for _ in range(iter_num):
            fir, sec = self._run_once_p1p2_probs_()
            p1 += fir
            p2 += sec

        p1 /= iter_num
        p2 /= iter_num
        # print(f"p1: {p1}, p2: {p2}")

        pa1 = 0
        pa2 = 0
        for _ in range(iter_num):
            fir, sec = self._run_once_cond_prob_()
            pa1 += fir
            pa2 += sec

        pa1 /= iter_num
        pa2 /= iter_num
        # print(f"pa1: {pa1}, pa2: {pa2}")

        return pa1*p1 + pa2*p2

    def _run_once_p1p2_probs_(self):
        '''Returns P(exactly 10 empty after 5) and P(exactly 11 empty after 5)'''
        box_list = np.zeros(12)
        for _ in range(5):
            index = random.randint(0, 11)
            box_list[index] += 1

        count = 0
        for box in box_list:
            if box == 0:
                count += 1

        if count == 10:
            return 1, 0
        elif count == 11:
            return 0, 1
        else:
            return 0, 0

    def _run_once_cond_prob_(self):
        '''Returns P(A|p1) and P(A|p2)'''
        # p1 --> P(exactly 10 empty after 5)
        # p2 --> P(exactly 11 empty after 5)

        box_list_1 = np.zeros(12)
        box_list_1[0] = 1
        box_list_1[1] = 1

        box_list_2 = np.zeros(12)
        box_list_2[0] = 1

        for _ in range(5):
            index = random.randint(0, 11)
            box_list_1[index] += 1
            box_list_2[index] += 1

        count_1 = 0
        count_2 = 0
        for box_1, box_2 in zip(box_list_1, box_list_2):
            if box_1 == 0:
                count_1 += 1
            if box_2 == 0:
                count_2 += 1

        result = [0, 0]
        if count_1 == 10:
            result[0] = 1
        if count_2 == 10:
            result[1] = 1

        return tuple(result)

    # TOTP effiencent
    def _run_totp_(self, iter_num):
        # Count number of times each event occur
        P_C = 0
        P_D = 0
        P_AC = 0
        P_AD = 0
        for i in range(iter_num):
            fir, sec, thr, four = self._run_once_totp_()
            P_C += fir
            P_D += sec
            P_AC += thr
            P_AD += four
        
        # Normalise to get probabilities
        P_C /= iter_num
        P_D /= iter_num
        P_AC /= iter_num
        P_AD /= iter_num
        # Return P(A) = P(A|C)P(C)+P(A|D)P(D)
        return P_AC*P_C + P_AD*P_D

    def _run_once_totp_(self):
        # Simulate 12 empty boxes
        # Note: this list unaltered is testing for P(C) and P(D)
        box_list = np.zeros(12)
        
        # Throw 5 balls
        for i in range(5):
            index = random.randint(0, 11)
            box_list[index] += 1
        
        #Simulate P(A|C) - Equivalent to saying exactly two boxes are never empty 
        box_list_AC = box_list.copy()
        box_list_AC[0] += 1
        box_list_AC[1] += 1
        # Simulate P(A|D) - Equivalent to saying exactly one box is never empty
        box_list_AD = box_list.copy()
        box_list_AD[0] += 1
        
        # Count empty boxes for each experiment
        count_0 = 0
        count_AC = 0
        count_AD = 0
        for box_0, box_AC, box_AD in zip(box_list, box_list_AC, box_list_AD):
            if box_0 == 0:
                count_0 += 1
            if box_AC == 0:
                count_AC += 1
            if box_AD == 0:
                count_AD += 1
        
        # Return tuple showing which events occured in this iteration
        result = [0, 0, 0, 0]
        if count_0 == 10:
            result[0] = 1
        if count_0 == 11:
            result[1] = 1
        if count_AC == 10:
            result[2] = 1
        if count_AD == 10:
            result[3] = 1
        return tuple(result)


class metaMCComparison:
    def __init__(self, mc_runs):
        self.byteDance = byteDanceMC()
        self.MC_runs = mc_runs

        self.med_mean = None
        self.totp_mean = None
        self.eff_mean = None
        self.med_var = None
        self.totp_var = None
        self.eff_var = None

        self.mse_med = None
        self.mse_totp = None
        self.mse_eff = None

        self.true_ans = 1.089387e-6

    def run_MC(self):
        runs = 100000

        medium_list = np.zeros(self.MC_runs)
        TOTP_list = np.zeros(self.MC_runs)
        eff_list = np.zeros(self.MC_runs)

        for i in range(self.MC_runs):
            print(f"iteration: {i} of {self.MC_runs}")
            medium_list[i] = self.byteDance.medium_original(runs)
            TOTP_list[i] = self.byteDance.TOTP_advancment(runs)
            eff_list[i] = self.byteDance._run_totp_(runs)

        np.save('medium_list', medium_list)
        np.save('TOTP_list', TOTP_list)
        np.save('eff_list', eff_list)

        self.med_mean = np.mean(medium_list)
        self.totp_mean = np.mean(TOTP_list)
        self.eff_mean = np.mean(eff_list)
        self.med_var = np.var(medium_list)
        self.totp_var = np.var(TOTP_list)
        self.eff_var = np.var(eff_list)

        self.mse_med = abs(medium_list-self.true_ans)
        self.mse_med = np.square(self.mse_med)
        self.mse_med = np.mean(self.mse_med)

        self.mse_totp = abs(TOTP_list-self.true_ans)
        self.mse_totp = np.square(self.mse_totp)
        self.mse_totp = np.mean(self.mse_totp)

        self.mse_eff = abs(eff_list-self.true_ans)
        self.mse_eff = np.square(self.mse_eff)
        self.mse_eff = np.mean(self.mse_eff)

        print(
            f"mse_med: {self.mse_med}, mse_totp: {self.mse_totp}, mse_eff: {self.mse_eff}")

        return self.med_mean, self.totp_mean, self.eff_mean, self.med_var, self.totp_var, self.eff_var

    def plot(self):
        if not self.med_mean:
            print("run sims first pls")
            return

        mu = self.med_mean
        variance = self.med_var
        sigma = math.sqrt(variance)
        x = np.linspace(mu - 3*sigma, mu + 3*sigma, 100)
        plt.plot(x, stats.norm.pdf(x, mu, sigma))

        mu = self.totp_mean
        variance = self.totp_var
        sigma = math.sqrt(variance)
        x = np.linspace(mu - 3*sigma, mu + 3*sigma, 100)
        plt.plot(x, stats.norm.pdf(x, mu, sigma))

        mu = self.eff_mean
        variance = self.eff_var
        sigma = math.sqrt(variance)
        x = np.linspace(mu - 3*sigma, mu + 3*sigma, 100)
        plt.plot(x, stats.norm.pdf(x, mu, sigma))

        plt.legend(['Medium', 'TOTP', 'eff'])
        plt.ticklabel_format(axis="x", style="sci", scilimits=(0, 0))
        plt.yticks([])
        plt.xlabel('Probability of event A')
        plt.title('Medium vs TOTP-alternative MC PDF')
        plt.show()

    def plot_bar(self):
        # do somthing
        print('')

    def plot_fromMem(self):
        TOTP_list = np.load('TOTP_list.npy')
        medium_list = np.load('medium_list.npy')
        eff_list = np.load('eff_list.npy')

        med_mean = np.mean(medium_list)
        totp_mean = np.mean(TOTP_list)
        eff_mean = np.mean(eff_list)
        med_var = np.var(medium_list)
        totp_var = np.var(TOTP_list)
        eff_var = np.var(eff_list)

        mu = med_mean
        variance = med_var
        sigma = math.sqrt(variance)
        x = np.linspace(mu - 3*sigma, mu + 3*sigma, 100)
        plt.plot(x, stats.norm.pdf(x, mu, sigma))

        mu = totp_mean
        variance = totp_var
        sigma = math.sqrt(variance)
        x = np.linspace(mu - 3*sigma, mu + 3*sigma, 100)
        plt.plot(x, stats.norm.pdf(x, mu, sigma))

        mu = eff_mean
        variance = eff_var
        sigma = math.sqrt(variance)
        x = np.linspace(mu - 3*sigma, mu + 3*sigma, 100)
        plt.plot(x, stats.norm.pdf(x, mu, sigma))

        plt.legend(['Medium', 'TOTP', 'eff'])
        plt.ticklabel_format(axis="x", style="sci", scilimits=(0, 0))
        plt.yticks([])
        plt.xlabel('Probability of event A')
        plt.title('Medium vs TOTP-alternative MC PDF')
        plt.show()


def simulation(iter_num):
    meta = metaMCComparison(iter_num)
    med_mean, totp_mean, eff_mean, med_var, totp_var, eff_var = meta.run_MC()
    print(
        f'med_mean: {med_mean},totp_mean: {totp_mean},eff_mean: {eff_mean},med_var: {med_var},totp_var: {totp_var},eff_var: {eff_var}')
    meta.plot()


def plotMem():
    meta = metaMCComparison(None)
    meta.plot_fromMem()


if __name__ == '__main__':
    simulation(3000)
    # plotMem()
