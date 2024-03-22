import sys

from rl_zoo3.enjoy import enjoy

sys.argv = [
    "python",
    "--device", "cpu",
    "--num-threads", "4",
    "--algo", "dqn",
    "--env", "ALE/BeamRider-v5",
    # "--no-render",
    "--folder", "unit3_dqn/logs/",
    "--custom-objects",
    "--n-timesteps", "5000",
]

enjoy()
