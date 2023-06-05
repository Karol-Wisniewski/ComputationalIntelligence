import gym
import numpy as np 
    
env = gym.make('FrozenLake8x8-v1', is_slippery=False, render_mode="human")

observation, info = env.reset(seed=42)

actions = [2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 2, 1, 1, 1]

for action in actions:
   observation, reward, terminated, truncated, info = env.step(action)

   if terminated or truncated:
      observation, info = env.reset()
env.close()


# Przykład gry z dyskretną przestrzenią akcji i dyskretnym stanem środowiska. Stan gry to obecna lokalizacja agenta, a akcje to kierunki, w których agent może się poruszyć (góra, dół, lewo, prawo).