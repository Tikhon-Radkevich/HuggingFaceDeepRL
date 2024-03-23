from sample_factory.train import run_rl

from setup import register_vizdoom_components, parse_vizdoom_cfg
from eval_env import eval_doom_env


def main():
    # Start the training, this should take around 15 minutes
    register_vizdoom_components()

    # The scenario we train on today is health gathering
    # other scenarios include "doom_basic", "doom_two_colors_easy", "doom_dm", "doom_dwango5", "doom_my_way_home",
    #                           "doom_deadly_corridor", "doom_defend_the_center", "doom_defend_the_line"
    env = "doom_health_gathering_supreme"
    argv = [
        f"--env={env}",
        "--device=cpu",
        "--num_workers=8",
        "--num_envs_per_worker=4",
        "--train_for_env_steps=4000000"
    ]
    cfg = parse_vizdoom_cfg(argv=argv)
    train_status = run_rl(cfg)
    eval_status = eval_doom_env(env)

    print(f"Training status: {train_status}")
    print(f"Evaluation status: {eval_status}")


if __name__ == "__main__":
    main()
