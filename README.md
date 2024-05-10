## Deep Reinforcement Learning

![Deep Reinforcement Learning](img.png)

This repository is dedicated to the [Deep Reinforcement Learning Course](https://huggingface.co/learn/deep-rl-course/en/unit0/introduction) offered by Hugging Face.

Here, I showcase three units:
- [Unit 3: DQN](unit3_dqn/README.md)
- [Unit 8: PPO](unit8_ppo/README.md)
- [Doom: PPO](Doom_ppo/README.md)

## Unit 3: DQN
Instead of relying on a Q-table, Deep Q-Learning utilizes a Neural Network to approximate the Q-values for each action based on the current state. I trained the model to play Space Invaders among other Atari games using RL-Zoo, a training framework for reinforcement learning that utilizes Stable-Baselines. This framework provides scripts for training, evaluating agents, tuning hyperparameters, plotting results, and recording gameplay.

![DQN Replay](unit3_dqn/replay.mp4)

## Unit 8: PPO
In this unit, I explored Proximal Policy Optimization (PPO), an algorithm that enhances training stability by limiting the extent of policy updates. This is achieved using a ratio that reflects the change from the old to the current policy, which is then clipped to stay within the range `[1−ϵ,1+ϵ]`. Such control ensures that the updates are not overly drastic, promoting more stable training. Initially, I learned the theoretical aspects of PPO and then implemented a PPO agent from scratch using the CleanRL framework to test on LunarLander-v2.

![PPO Replay](unit8_ppo/replay.mp4)

## Doom: PPO
I delved deeper into PPO optimization by applying the Sample-Factory, an asynchronous PPO implementation, to train an agent in VizDoom—a community-based open source Doom game. My first project involved training the agent to survive the Health Gathering scenario, where the objective is to collect health packs to prolong survival. Subsequently, I expanded to more complex scenarios like Deathmatch.

![Doom PPO Replay](Doom_ppo/pretrained_model/doom_health_gathering_supreme_2222/replay.mp4)
