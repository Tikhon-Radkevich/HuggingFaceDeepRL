import gymnasium as gym
from stable_baselines3.common.vec_env import VecVideoRecorder, DummyVecEnv
from sb3_contrib import TQC


def record_video(env_kwargs, model, video_length=500, prefix="", video_folder="videos/"):
    eval_env = DummyVecEnv([lambda: gym.make(**env_kwargs)])

    eval_env = VecVideoRecorder(
        eval_env,
        video_folder=video_folder,
        record_video_trigger=lambda step: step == 0,
        video_length=video_length,
        name_prefix=prefix,
    )

    obs = eval_env.reset()
    for _ in range(video_length):
        action, _ = model.predict(obs)
        obs, _, _, _ = eval_env.step(action)

    eval_env.close()


def main():
    model_path = "../box/downloads/tqc_BipedalWalker_24"

    env_kwargs = {
        "id": "BipedalWalker-v3",
        "hardcore": True,
        "render_mode": "rgb_array"
    }

    model = TQC.load(model_path)

    record_video(env_kwargs, model, video_length=1000, prefix="tqc_BipedalWalker")


if __name__ == "__main__":
    main()
