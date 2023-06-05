import gym

gym.make('MountainCar-v0', render_mode="human")

env = gym.make('MountainCar-v0', render_mode="human")

observation, info = env.reset(seed=42)

for _ in range(300):
    action = env.action_space.sample()
    observation, reward, terminated, truncated, info = env.step(action)
    
    if terminated or truncated:
        observation, info = env.reset()
        
env.close()

# Przykład gry z dyskretną przestrzenią akcji i ciągłym stanem środowiska. Stan gry to pozycja i prędkość samochodu (obie są wartościami ciągłymi), a zestaw akcji jest dyskretny (samochód może jechać w lewo, w prawo lub nie ruszać się).