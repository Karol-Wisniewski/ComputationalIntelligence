import gym

env = gym.make('Pendulum-v1', render_mode="human")

observation, info = env.reset(seed=42)

for _ in range(300):
    action = env.action_space.sample()
    observation, reward, terminated, truncated, info = env.step(action)

    if terminated or truncated:
        observation, info = env.reset()
        
env.close()

# Przykład gry z ciągłą przestrzenią akcji i ciągłym stanem środowiska. Stan gry to pozycja i prędkość wahadła (obie są wartościami ciągłymi), a akcje to siła, którą należy przyłożyć do wahadła (również wartość ciągła).