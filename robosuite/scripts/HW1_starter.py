import numpy as np
import robosuite.utils.transform_utils as tfutil

#This function should returen the homogeneous transform matrix (4X4) from the robot end-effector to an object of interest
def getTransformMatrix_from_eef_to_object(observation, objectOfInterest = 'Milk'):
    if objectOfInterest+'_pos' not in observation.keys():
        print("======== Wrong Input Ojbect Name ============")
        return False
    T_from_eef_to_obj = np.identity(4) # This should be modified with your input
    print(observation.keys())

    #====================== Your code Input here =============================================
    # Write your code to change the T_from_eef_to_obj (or generate new one if you like) 
    # You may want to use tfutil.

    # Extract end-effector position and rotation from the observation
    eef_pos = observation['eef_pos']
    eef_rot = observation['eef_quat']

    # Extract object position from the observation
    obj_pos = observation[objectOfInterest+'_pos']

    # Create a transform matrix from end-effector to object
    T_from_eef_to_obj = tfutil.pose2mat((obj_pos, [0, 0, 0, 1])) @ np.linalg.inv(tfutil.pose2mat((eef_pos, eef_rot)))
    
    #============================================================================================
    return T_from_eef_to_obj






# This function should return the list of objects in the order that are closest to the robot endeffector
def getTravelDistance(observation, visitOrder = ['Milk', 'Can', 'Cereal', 'Bread']):    
    print("getObjectList_closestPosition First")
    print(visitOrder)
    travelDistance = 0.0
    #====================== Your code Input here =============================================
    # Write your code to change the travelDistance
    # You may want to use tfutil.




    #============================================================================================
    return travelDistance # This should be in meter by default




# This function should return the list of objects in the order that are in the closest orientation to the robot endeffector orientation
def getTravelTotalAngleChange(observation, visitOrder = ['Milk', 'Can', 'Cereal', 'Bread']):    
    print("getObjectList_closestOrientationFirst")
    print(visitOrder)
    totalRotAngle = 0.0
    #====================== Your code Input here =============================================
    # Write your code to change totalRotAngle
    # You may want to use tfutil.
    


    #============================================================================================
    return totalRotAngle # in radian


