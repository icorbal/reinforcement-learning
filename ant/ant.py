import gymnasium as gym
from stable_baselines3 import PPO

env = gym.make('Ant-v4')
env.reset()

model = PPO('MlpPolicy', env, verbose=1)
model.learn(total_timesteps=10000)

episodes = 100

for ep in range(episodes):
    obs = env.reset()
    done = False
    while not done:
        # pass observation to model to get predicted action
        action, _states = model.predict(obs)

        # pass action to env and get info back
        obs, rewards, done, info = env.step(action)

        # show the environment on the screen
        env.render()
