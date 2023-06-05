import gym

env = gym.make("LunarLander-v2", render_mode="human")

env.reset(seed=42)

for _ in range(100):
    action = 1 #odpal lewy silnik
    env.step(action)
    
for _ in range(100):
    action = 0 #odpal prawy silnik
    env.step(action)
    
env.close()

# Gra z poprawnym działaniem (beczka w powietrzu i eleganckie lądowanie)