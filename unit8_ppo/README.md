---
tags:
- LunarLander-v2
- ppo
- deep-reinforcement-learning
- reinforcement-learning
- custom-implementation
- deep-rl-course
model-index:
- name: PPO
  results:
  - task:
      type: reinforcement-learning
      name: reinforcement-learning
    dataset:
      name: LunarLander-v2
      type: LunarLander-v2
    metrics:
    - type: mean_reward
      value: 65.54 +/- 73.90
      name: mean_reward
      verified: false
---

  # PPO Agent Playing LunarLander-v2

  This is a trained model of a PPO agent playing LunarLander-v2.

  # Hyperparameters
  ```python
  {'exp_name': 'main'
'seed': 1
'torch_deterministic': True
'cuda': False
'track': False
'wandb_project_name': 'cleanRL'
'wandb_entity': None
'capture_video': False
'env_id': 'LunarLander-v2'
'total_timesteps': 700000
'learning_rate': 0.0003
'num_envs': 16
'num_steps': 1024
'anneal_lr': True
'gae': True
'gamma': 0.999
'gae_lambda': 0.98
'num_minibatches': 256
'update_epochs': 2
'norm_adv': True
'clip_coef': 0.2
'clip_vloss': True
'ent_coef': 0.0
'vf_coef': 0.5
'max_grad_norm': 0.5
'target_kl': None
'repo_id': 'TikhonRadkevich/ppo_v2_LunarLander-v2'
'batch_size': 16384
'minibatch_size': 64}
  ```
  