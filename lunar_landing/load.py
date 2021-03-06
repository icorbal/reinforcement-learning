import gym
from stable_baselines3 import PPO

models_dir = "models/PPO-3"

env = gym.make('LunarLander-v2')  # continuous: LunarLanderContinuous-v2
env.reset()

model_path = f"{models_dir}/3960000.zip"
model = PPO.load(model_path, env=env)

episodes = 30

for ep in range(episodes):
    obs = env.reset()
    done = False
    while not done:
        action, _states = model.predict(obs)
        obs, rewards, done, info = env.step(action)
        env.render()
        # print(rewards)
