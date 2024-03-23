from sample_factory.enjoy import enjoy

from setup import parse_vizdoom_cfg


def eval_doom_env(env):
    cfg = parse_vizdoom_cfg(
        argv=[f"--env={env}", "--num_workers=1", "--save_video", "--no_render", "--max_num_episodes=10"], evaluation=True
    )
    status = enjoy(cfg)
    return status
