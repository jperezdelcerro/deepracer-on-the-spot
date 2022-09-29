import math

action_space = [
        {"steering_angle": -30, "speed": 1.1},
        {"steering_angle": -25, "speed": 1.2},
        {"steering_angle": -20, "speed": 1.3},
        {"steering_angle": -15, "speed": 1.5},
        {"steering_angle": -10, "speed": 2},        
        {"steering_angle": -5, "speed": 2.5},
        {"steering_angle": 0, "speed": 3.0},
        {"steering_angle": 5,  "speed": 2.5},
        {"steering_angle": 10,   "speed": 2},
        {"steering_angle": 15,   "speed": 1.5},
        {"steering_angle": 20,  "speed": 1.3},
        {"steering_angle": 25,  "speed": 1.2},
        {"steering_angle": 30,  "speed": 1.1}
]

LEFT_LANE = [14,15,16,17,18,19,20,21,22,23,24,25,26,27,
            38,39,40,41,42,43,57,58,59,60,61,62,63,85,86,87,88,89,90,91,  
            102,103,104,105,106,107,108,109,110,111,112,  
            133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,  
            159,160,161,162,163,164, 194,195,196,197,198,199,200,201,   
            225,226,227,228,243,244,245,246,247,248,249,250 ]

CENTER_LANE = [1,2,3,4,5,6,7,8,9,10,11,12,13,28,29,30,31,
                32,33,34,35,36,37, 
                44,45,46,
                47,48,49,50,51,
                52,53,54, 55,56,64,65,66,67,68,69,70,79,80,81, 82,83,84,  92,93,   
                101, 112,113,114,  
                114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129, 
                130,131,132, 144,145,146,147,148,149, 
                150,151,152,153,154,  157,158,  165,166,167,168, 
                176,177,178,179,180,181,182,183,184,185,186, 
                191,192,193, 202,203, 210,211,212,213,214,215,216,218,219,220,221,222,223,224,225,226,227,228,229,230, 
                240,241,242,  250,251,252,253,254]


RIGHT_LANE = [
                71,72,73,74,75,76,77,78,
                93,94,95,96,97,
                98,99,100,  
                154,155,156,   168,169,170,171,172,173,174,175,  
                187,188,189,190,  204,205,206,207,208,209,210,211,212, 
                231,232,233,234,235,236,237,238,239
                                    ]

FAST = [1,2,3,4,5,6,7,8,9,10,11,12,   
        27,28,29,30,31,32,33,34,35, 
        46,47,48,49,
        81,82,83,84,85,86,87,88,
        114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,
        155,156,157,158,  
        164,165,166,167,168,169,170,171,172,173,174,175,176,177,178,179,180,181,182,183,184,  
        202,203,204,205,206,207,208,209,210,211,212,213,214,214,215,216,217,218,219,220,221,222,223,224,225,226, 
        242,243,244,245,246,247,248,249,250,251,252,253,254        ] 



SLOW = [50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,  
        70,71,72,73,74,75,76,77,78,79,80, 89,90,91,92,93,94,95,96,  
        103,104,105,106,107,108,109,110,111,112,  191,192,193,194,195,196,197,198,199,200,201,202, 
        227,228,229,230,231,232,233,234,235,236,237,238,239,240,241
                ] 

MIDDLE = [13,14,15,16,17,18,19,20,21,22,24,25,26,
            65,66,67,
            97,98,99,100,101,102, 113,114 ]


MIDDLE1  = [36,37,38,39,40,41,42,43,44,45,
            144,145,146,147,148,149,150,151,152,153,154,155,
            159,160,161,162,163,164, 185,186,187,188, 189,190,191]

def getTrackDirection(waypoints, closest_waypoints):
    # Calculate the direction of the center line based on the closest waypoints
    next_point = waypoints[closest_waypoints[1]]
    prev_point = waypoints[closest_waypoints[0]]
    
    # Calculate the direction in radius, arctan2(dy, dx), the result is (-pi, pi) in radians
    track_direction = math.atan2(next_point[1] - prev_point[1], next_point[0] - prev_point[0])
    # Convert to degree
    return math.degrees(track_direction)

def getDirectionDiff(track_direction, heading):
    # Calculate the difference between the track direction and the heading direction of the car
    direction_diff = abs(track_direction - heading)
    if direction_diff > 180:
        direction_diff = 360 - direction_diff
        
    return direction_diff

def getSpeedThereshold(speed):
    return 0.5 if 1.5 >= speed >= 3 else 0.1

def curveSpeedPenalty(direction_diff, speed, reward):  #combinar con lo de dav id, chequear reinforment positivo
  #if the car isnt going staight, and the speed is 
    threshold = 5
    for space in action_space:
        if direction_diff == space["steering_angle"] and speed == space['speed']:
            reward += 20
        elif direction_diff - threshold >= space["steering_angle"] >=  direction_diff + threshold: 
            threshold = getSpeedThereshold(space['speed'])
            if space['speed'] - threshold >= speed >= space['speed'] + threshold:
                reward += 10
            else:
                reward -= 10
            return reward
    return reward



def _getClosestWaypoints(params):
    # closest_waypoints
    # Type:  [int, int]
    # Range: [(0:Max-1),(1:Max-1)]
    # The zero-based indices of the two neighboring waypoints closest to the agent's current position of (x, y).
    # The distance is measured by the Euclidean distance from the center of the agent. The first element refers to the
    # closest waypoint behind the agent and the second element refers the closest waypoint in front of the agent.
    return params['closest_waypoints']

def _getHeading(params):
    # heading
    # Type: float
    # Range: -180:+180
    # Heading direction, in degrees, of the agent with respect to the x-axis of the coordinate system.
    return params['heading']

def reward_function(params):
    '''
    Example of rewarding the agent to follow center line
    '''
    # Read input parameters
    waypoints = params['waypoints']
    speed = params['speed']
    closest_waypoints = _getClosestWaypoints(params)
    heading = _getHeading(params)
    center_variance = params["distance_from_center"] / params["track_width"]
    is_left_of_center = params["is_left_of_center"]

    #Calculate direction 
    track_direction = getTrackDirection(waypoints, closest_waypoints)
    direction_diff = getDirectionDiff(track_direction, heading) 
    
    reward = 1
    


    if closest_waypoints[1] in LEFT_LANE and is_left_of_center:
        if direction_diff > 0 and speed <= 1.7:
            reward+=20
        else:
            reward+=5
    elif closest_waypoints[1] in RIGHT_LANE and not is_left_of_center:
        if direction_diff < 0 and speed <= 1.7:
            reward+=20
        else:
            reward+=5
    elif closest_waypoints[1] in CENTER_LANE and center_variance < 0.4:
        if -5 >= direction_diff >= 5 and 2.5 >= speed >= 3:
            reward+=25
        else:
            reward+=5
    else:
        reward = 1e-03


    return float(reward)