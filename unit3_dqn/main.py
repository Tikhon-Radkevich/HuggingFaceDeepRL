import sys

from rl_zoo3.train import train


sys.argv = [
    "python",
    "--device", "cpu",
    "--num-threads", "4",
    "--algo", "dqn",
    "--env", "ALE/BeamRider-v5",
    "-f", "unit3_dqn/logs/",
    "-c", "unit3_dqn/dqn.yml",
]

train()
