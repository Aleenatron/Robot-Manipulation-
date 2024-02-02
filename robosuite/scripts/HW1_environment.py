"""
This script shows you how to select gripper for an environment.
This is controlled by gripper_type keyword argument.
"""
import numpy as np
import random

import robosuite as suite
from robosuite import ALL_GRIPPERS
from HW1_starter import *


if __name__ == "__main__":

    gripper ='PandaGripper'

    # Notify user which gripper we're currently using
    print("Using gripper {}...".format(gripper))

    # create environment with selected grippers
    env = suite.make(
        "PickPlace",
        robots="Panda",
        gripper_types=gripper,
        has_renderer=True,  # make sure we can render to the screen
        has_offscreen_renderer=False,  # not needed since not using pixel obs
        use_camera_obs=False,  # do not use pixel observations
        control_freq=50,  # control should happen fast enough so that simulation looks smoother
        camera_names="frontview",
    )
    
    # Reset the env
    env.reset()
    randomJointPositions = np.random.rand(env.robots[0].dof-1,) * 2*np.pi - np.pi
    env.robots[0].set_robot_joint_positions(randomJointPositions)            
    action = np.zeros(env.robots[0].dof,)
    observation, reward, done, info = env.step(action)
    env.render() 


    print(observation.keys())

    # Problem 1       
    print(getTransformMatrix_from_eef_to_object(observation, objectOfInterest='Milk')) # This should work for other objects as well ('Milk', 'Can', 'Cereal', 'Bread')

    
    visitOrder = ['Milk', 'Can', 'Cereal', 'Bread']
    visitOrder = np.random.permutation(visitOrder).tolist()

    # Problem 2
    print(getTravelDistance(observation, visitOrder = visitOrder))

    #Problem 3
    print(getTravelTotalAngleChange(observation, visitOrder=visitOrder))



    while True:
        env.render()

    # # close window
    # env.close()
