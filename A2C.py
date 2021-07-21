from Bus3 import Bus3
from Bus import Bus
from Animator import Animator
from City import City
import gym
import torch
import torch.nn as nn
import torch.nn.functional as F

from collections import defaultdict
import torch

from PyQt5.QtCore import QRectF, QThread
from PyQt5.QtGui import QBrush, QColor
import numpy as np
import pandas as pd
from PyQt5.QtWidgets import QWidget,QApplication,QGraphicsView,QGraphicsScene
import sys





env=City()
#animator=Animator(city)
bus = Bus3(3,1,env.chart,env.Halts,env.Roads)
env.AddBus([bus])


app = QApplication(sys.argv)

n_episode=5000
#q_learning
gamma=1
alpha=0.4
epsilon=0.01

#sarsa
# epsilon=0.03
# alpha=0.4
# gamma=0.05

length_episode=[0] * n_episode
total_reward_episode=[0] * n_episode

class ActorCriticModel(nn.Module):
    def __init__(self, n_input, n_output, n_hidden):
        super(ActorCriticModel, self).__init__()
        self.fc = nn.Linear(n_input, n_hidden)
        self.action = nn.Linear(n_hidden, n_output)
        self.value = nn.Linear(n_hidden, 1)
    def forward(self, x):
        x = torch.Tensor(x)
        x = F.relu(self.fc(x))
        action_probs = F.softmax(self.action(x), dim=-1)
        state_values = self.value(x)
        return action_probs, state_values

    
class PolicyNetwork():
    def __init__(self, n_state, n_action, n_hidden=50, lr=0.001):
        self.model = ActorCriticModel(n_state, n_action, n_hidden)
        self.optimizer = torch.optim.Adam(self.model.parameters(), lr)
        self.scheduler = torch.optim.lr_scheduler.StepLR(self.optimizer, step_size=10, gamma=0.9)

    def predict(self, s):
        """
        Вычисляет выход, применяя модель исполнитель–критик
        @param s: входное состояние
        @return: вероятности действий, ценность состояния
        """
        return self.model(torch.Tensor(s))

    def update(self, returns, log_probs, state_values):
        """
        Обновляет веса сети исполнитель–критик на основе переданных
        обучающих примеров
        @param returns: доход (накопительное вознаграждение) на
                        каждом шаге эпизода
        @param log_probs: логарифм вероятности на каждом шаге
        @param state_values: ценности состояний на каждом шаге
        """
        loss = 0
        for log_prob, value, Gt in zip(log_probs, state_values, returns):
            advantage = Gt - value.item()
            policy_loss = -log_prob * advantage
            value_loss = F.smooth_l1_loss(value, Gt)
            loss += policy_loss + value_loss
        self.optimizer.zero_grad()
        loss.backward()
        self.optimizer.step()

    def get_action(self, s):
        """
        Предсказывает стратегию, выбирает действие и вычисляет логарифм
        его вероятности
        @param s: входное состояние
        @return: выбранное действие и логарифм его вероятности
        """
        action_probs, state_value = self.predict(s)
        action = torch.multinomial(action_probs, 1).item()
        log_prob = torch.log(action_probs[action])
        return action, log_prob, state_value


def actor_critic(env, estimator, n_episode, gamma=1.0):
    """
    Алгоритм исполнитель–критик
    @param env: имя окружающей среды Gym
    @param estimator: сеть стратегии
    @param n_episode: количество эпизодов
    @param gamma: коэффициент обесценивания
    """
    Scheduler=0
    Bonus=5
    for episode in range(n_episode):
        log_probs = []
        rewards = []
        state_values = []
        env=City()
        bus = Bus3(3,1,env.chart,env.Halts,env.Roads)#!!!!!!!!!!!!!!!!!
        #bus2 = Bus2(0,1,2,env.chart,env.Halts)#!!!!!!!!!!!!!!!!!
        env.AddBus([bus])
        state=env.posPlayer()
        is_done=False
        
        while True:
            one_hot_state = [0]*env.observation
            one_hot_state[state[0]] = 1
            action, log_prob, state_value = estimator.get_action(one_hot_state)
            r = env.step([action])
            next_state, reward, is_done = r[0]
            total_reward_episode[episode] += reward
            log_probs.append(log_prob)
            state_values.append(state_value)
            rewards.append(reward)
            if is_done:
                returns = []
                Gt = 0
                pw = 0
                for reward in rewards[::-1]:
                    Gt += gamma ** pw * reward
                    pw += 1
                    returns.append(Gt)
                returns = returns[::-1]
                returns = torch.tensor(returns)
                returns = (returns - returns.mean()) / (returns.std() + 1e-9)
                estimator.update(returns, log_probs, state_values)
                print('Эпизод: {}, полное вознаграждение: {}'.format(episode, total_reward_episode[episode]))
                if total_reward_episode[episode] >= Bonus:
                    estimator.scheduler.step()
                    Scheduler+=1
                    if Scheduler>=10:
                        Bonus=Bonus+1
                        Scheduler=0
                break
            state[0] = next_state

n_state = env.observation
n_action = env.busses[0].action_space
n_hidden = 32

lr = 0.01
policy_net = PolicyNetwork(n_state, n_action, n_hidden, lr)

gamma = 0.95

n_episode = 3000
total_reward_episode = [0] * n_episode
actor_critic(env, policy_net, n_episode, gamma)

torch.save(policy_net.model,'model/A2C')

import matplotlib.pyplot as plt
plt.plot(total_reward_episode)
plt.title('Зависимость вознаграждения в эпизоде от времени')
plt.xlabel('Эпизод')
plt.ylabel('Полное вознаграждение')
plt.show()


class AThread(QThread):
    
    def run(self,animator,action):
        self.sleep(1)   
        re=env.step(action)
        self.Data=[]
        self.reward=[]
        self.is_done=[]
        for i in range(len(env.busses)):
            next_state,reward,is_done=re[i]
            self.Data.append(next_state)
            self.reward.append(reward)
            self.is_done.append(is_done)     
        animator.Update()
        QApplication.processEvents()
        
        


env=City()
bus = Bus3(3,1,env.chart,env.Halts,env.Roads)
#bus2 = Bus2(0,1,2,env.chart,env.Halts)#!!!!!!!!!!!!!!!!!
t = AThread()
total_reward=0
env.AddBus([bus])
state=env.posPlayer()
animator=Animator(env)
is_done=False
step=0
while not (is_done):
    one_hot_state = [0]*env.observation
    one_hot_state[state[0]] = 1
    action, log_prob, state_value = policy_net.get_action(one_hot_state)


    
    t.run(animator=animator,action=[action])
    t.wait()
    state=t.Data
    is_done=t.is_done[0]
    for index in range(len(env.busses)):
        total_reward+=t.reward[index]
    print('Эпизод: {}, полное вознаграждение: {}'.format(step, total_reward))
    step+=1



plt.plot(total_reward_episode)
plt.title('Зависимсоть вознаграждения в эпизоде от времени')
plt.xlabel('Эпизод')
plt.ylabel('Полное вознаграждение')
plt.savefig('Зависимсоть вознаграждения в эпизоде от времени A2C')
plt.show()

data={'Полное вознаграждение':total_reward_episode}
df = pd.DataFrame(data)
df.to_csv('A2C')

sys.exit(app.exec())