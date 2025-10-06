# SPDX-FileCopyrightText: Copyright (c) 2025 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
# All rights reserved.
#
# SPDX-License-Identifier: Apache-2.0

from isaac_lab_tutorial.robots.jetbot import JETBOT_CONFIG

from isaaclab.assets import ArticulationCfg
from isaaclab.envs import DirectRLEnvCfg
from isaaclab.scene import InteractiveSceneCfg
from isaaclab.sim import SimulationCfg
from isaaclab.utils import configclass

# NOTE: this is the config class of the environment and subsequently used by isaac_lab_tutorial_env.py
@configclass # defines class as config class
class IsaacLabTutorialEnvCfg(DirectRLEnvCfg): # we use DirectRLEnvCfg  config class as want to use direct workflow
    # NOTE: can define any desired field but must always define three things: sim, scene, robot (which are also configuration classes)
    # env
    decimation = 2
    episode_length_s = 5.0

    # - spaces definition
    action_space = 2

    #observation_space = 9
    observation_space = 3
    state_space = 0

    # simulation (SimulationCfg defines things like timestep, direction of gravity, how physics should be simulated, render interval)
    sim: SimulationCfg = SimulationCfg(dt=1 / 120, render_interval=decimation)

    # robot(s) (define a regex path to the robot, and replace the prim_path attribute in the base configuration. In this case, CARTPOLE_CFG is a configuration defined in isaaclab_assets.robots.cartpole and by replacing the prim path with /World/envs/env_.*/Robot we are implicitly saying that every copy of the scene will have a robot named Robot)
    robot_cfg: ArticulationCfg = JETBOT_CONFIG.replace(prim_path="/World/envs/env_.*/Robot")

    # scene (InteractiveSceneCfg defines numer and spacing of copies of teh scene)
    scene: InteractiveSceneCfg = InteractiveSceneCfg(num_envs=100, env_spacing=2.0, replicate_physics=True)

    # custom parameters/scales
    # - controllable joint
    dof_names = ["left_wheel_joint", "right_wheel_joint"]