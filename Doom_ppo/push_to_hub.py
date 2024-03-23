from sample_factory.enjoy import enjoy

from setup import parse_vizdoom_cfg, register_vizdoom_components


register_vizdoom_components()

hf_username = "TikhonRadkevich"
argv = [
    f"--env=doom_health_gathering_supreme",
    "--num_workers=1",
    "--save_video",
    "--no_render",
    "--max_num_episodes=10",
    "--max_num_frames=100000",
    "--push_to_hub",
    "--experiment=default_experiment",
    "--train_dir=train_dir",
    f"--hf_repository={hf_username}/rl_course_vizdoom_health_gathering_supreme"
]

cfg = parse_vizdoom_cfg(argv=argv, evaluation=True)
status = enjoy(cfg)
