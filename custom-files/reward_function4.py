import math 
way = {
    '0':  {'angles':  [-2, 0, 2], 'speed': [3.8, 4]},
    '1': {'angles': [-2, 0, 2], 'speed': [3.8, 4]}, 
    '2': {'angles': [-2, 0, 2], 'speed': [3.8, 4]},
    '3': {'angles': [-2, 0, 2], 'speed': [3.8, 4]},
    '4': {'angles': [-2, 0, 2], 'speed': [3.8, 4]},
    '5': {'angles': [-2, 0, 2], 'speed': [3.8, 4]},
    '6': {'angles': [-2, 0, 2], 'speed': [3.8, 4]},
    '7': {'angles': [-2, 0, 2], 'speed': [3.8, 4]},
    '8': {'angles': [-2, 0, 2], 'speed': [4]},
    '9': {'angles': [-2, 0, 2], 'speed': [4]},
    '10': {'angles': [-2, 0, 2, 5], 'speed': [4]},
    '11': {'angles': [0,5,10,15], 'speed': [1.3,1.5,2]},
    '12': {'angles': [0,5,10,15], 'speed': [1.3,1.5,2]},
    '13': {'angles': [0,5,10,15], 'speed': [1.3,1.5,2]},
    '14': {'angles': [0,5,10,15], 'speed': [1.3,1.5,2]},
    '15': {'angles': [0,5,10,15], 'speed': [1.3,1.5,2]},
    '16': {'angles': [0,5,10,15], 'speed': [1.3,1.5,2]},
    '17': {'angles': [0,5,10,15], 'speed': [1.3,1.5,2]},
    '18': {'angles': [0,5,10,15], 'speed': [1.3,1.5,2]},
    '19': {'angles': [0,5,10,15], 'speed': [1.3,1.5,2]},
    '20': {'angles': [0,5,10,15], 'speed': [1.3,1.5,2]},
    '21': {'angles': [0,5,10,15], 'speed': [1.3,1.5,2]},
    '22': {'angles': [0,5,10,15], 'speed': [1.3,1.5,2]},
    '23': {'angles': [0,5,10,15], 'speed': [1.3,1.5,2]},
    '24': {'angles': [0,5,10,15], 'speed': [1.3,1.5,2]},
    '25': {'angles': [0,5,10,15], 'speed': [1.3,1.5,2]},
    '26': {'angles': [0,5,10,15], 'speed': [1.3,1.5,2]},
    '27': {'angles': [0,5,10,15], 'speed': [1.3,1.5,2]},
    '28': {'angles': [0,5,10,15], 'speed': [1.3,1.5,2]},
    '29': {'angles': [0, 2], 'speed': [3.8, 4]},
    '30': {'angles': [0, 2], 'speed': [3.8, 4]},
    '31': {'angles': [0, 2], 'speed': [3.8, 4]},
    '32': {'angles': [0, 2], 'speed': [3.8, 4]},
    '33': {'angles': [0, 2], 'speed': [3.8, 4]},
    '34': {'angles': [0, 2], 'speed': [3.8, 4]},
    '35': {'angles': [0, 5, 10, 15], 'speed': [3,3.5,2.5]},
    '36': {'angles': [0,5,10,15], 'speed': [3,3.5,2.5]},
    '37': {'angles': [0,5,10,15], 'speed': [3,3.5,2.5]},
    '38': {'angles': [0,5,10,15], 'speed': [3,3.5,2.5]},
    '39': {'angles': [0,5,10,15], 'speed': [3,3.5,2.5]},
    '40': {'angles': [0,5,10,15], 'speed': [3,3.5,2.5]},
    '41': {'angles': [0,5,10,15], 'speed': [3,3.5,2.5]},
    '42': {'angles': [0,5,10,15], 'speed': [3,3.5,2.5]},
    '43': {'angles': [0,5,10,15], 'speed': [3,3.5,2.5]},
    '44': {'angles': [0,5,10,15], 'speed': [3,3.5,2.5]},
    '45': {'angles': [0,5,10,15], 'speed': [3,3.5,2.5]},
    '46': {'angles': [0,5,10,15], 'speed': [3,3.5,2.5]},
    '47': {'angles': [0,5,10,15], 'speed': [3,3.5,2.5]},
    '48': {'angles': [0,5,10,15], 'speed': [3,3.5,2.5]},
    '49': {'angles': [-2,0,2], 'speed': [3.8, 4]},
    '50': {'angles': [-2,0,2], 'speed': [3.8, 4]},
    '51': {'angles': [-2,0,2], 'speed': [3.8, 4]},
    '52': {'angles': [-2,0,2], 'speed': [3.8, 4]},
    '53': {'angles': [-2,0,2], 'speed': [3.8, 4]},
    '54': {'angles': [15,25,30], 'speed': [1.3,1.5,2]},
    '55': {'angles': [15,25,30], 'speed': [1.3,1.5,2]},
    '56': {'angles': [15,25,30], 'speed': [1.3,1.5,2]},
    '57': {'angles': [15,25,30], 'speed': [1.3,1.5,2]},
    '58': {'angles': [15,25,30], 'speed': [1.3,1.5,2]},
    '59': {'angles': [15,25,30], 'speed': [1.3,1.5,2]},
    '60': {'angles': [15,25,30], 'speed': [1.3,1.5,2]},
    '61': {'angles': [15,25,30], 'speed': [1.3,1.5,2]},
    '62': {'angles': [15,25,30], 'speed': [1.3,1.5,2]},
    '63': {'angles': [15,25,30], 'speed': [1.3,1.5,2]},
    '64': {'angles': [-10,-5,-2,0,2,5,10], 'speed': [1.5,2]},
    '65': {'angles': [-10,-5,-2,0,2,5,10], 'speed': [1.5,2]},
    '66': {'angles': [-10,-5,-2,0,2,5,10], 'speed': [1.5,2]},
    '67': {'angles': [-15,-10,-25], 'speed': [1.5,2]},
    '68': {'angles': [-15,-10,-25], 'speed': [1.5,2]},
    '69': {'angles': [-15,-10,-25], 'speed': [1.5,2]},
    '70': {'angles': [-15,-10,-25], 'speed': [1.5,2]},
    '71': {'angles': [-15,-10,-25], 'speed': [1.5,2]},
    '72': {'angles': [-15,-10,-25], 'speed': [1.5,2]},
    '73': {'angles': [-15,-10,-25], 'speed': [1.5,2]},
    '74': {'angles': [-15,-10,-25], 'speed': [1.5,2]},
    '75': {'angles': [-15,-10,-25], 'speed': [1.5,2]},
    '76': {'angles': [-15,-10,-25], 'speed': [1.5,2]},
    '77': {'angles': [-15,-10,-25], 'speed': [1.5,2]},
    '78': {'angles': [-15,-10,-25], 'speed': [1.5,2]},
    '79': {'angles': [-15,-10,-25], 'speed': [1.5,2]},
    '80': {'angles': [-15,-10,-25], 'speed': [1.5,2]},
    '81': {'angles': [-15,-10,-25], 'speed': [1.5,2]},
    '82': {'angles': [-15,-10,-25], 'speed': [1.5,2]},
    '83': {'angles': [-2,0,2], 'speed': [3.5,4]},
    '84': {'angles': [-2,0,2], 'speed': [3.5,4]},
    '85': {'angles': [-2,0,2], 'speed': [3.5,4]},
    '86': {'angles': [-2,0,2], 'speed': [3.5,4]},
    '87': {'angles': [-2,0,2], 'speed': [3.5,4]},
    '88': {'angles': [-2,0,2], 'speed': [3.5,4]},
    '89': {'angles': [-2,0,2], 'speed': [3.5,4]},
    '90': {'angles': [-2,0,2], 'speed': [3.5,4]},

    '91': {'angles': [-25,-15], 'speed': [1.6,2]},
    '92': {'angles': [-25,-15], 'speed': [1.6,2]},
    '93': {'angles': [-25,-15], 'speed': [1.6,2]},
    '94': {'angles': [-25,-15], 'speed': [1.6,2]},
    '95': {'angles': [-25,-15], 'speed': [1.6,2]},
    '96': {'angles': [-25,-15], 'speed': [1.6,2]},
    '97': {'angles': [-25,-15], 'speed': [1.6,2]},
    '98': {'angles': [-25,-15], 'speed': [1.6,2]},
    '99': {'angles': [-5,0,5], 'speed': [3]},
    '100': {'angles': [-5,0,5], 'speed': [3]},
    '101': {'angles': [-5,0,5], 'speed': [3]},
    '102': {'angles': [10,15,25,30], 'speed': [1.3,1.6,2]},
    '103': {'angles': [10,15,25,30], 'speed': [1.3,1.6,2]},
    '104': {'angles': [10,15,25,30], 'speed': [1.3,1.6,2]},
    '105': {'angles': [10,15,25,30], 'speed': [1.3,1.6,2]},
    '106': {'angles': [10,15,25,30], 'speed': [1.3,1.6,2]},
    '107': {'angles': [10,15,25,30], 'speed': [1.3,1.6,2]},
    '108': {'angles': [10,15,25,30], 'speed': [1.3,1.6,2]},
    '109': {'angles': [10,15,25,30], 'speed': [1.3,1.6,2]},
    '110': {'angles': [10,15,25,30], 'speed': [1.3,1.6,2]},
    '111': {'angles': [10,15,25,30], 'speed': [1.3,1.6,2]},
    '112': {'angles': [10,15,25,30], 'speed': [1.3,1.6,2]},
    '113': {'angles': [10,15,25,30], 'speed': [1.3,1.6,2]},
    '114': {'angles': [10,15,25,30], 'speed': [1.3,1.6,2]},
'115': {'angles': [-2,0,2], 'speed': [4]},
'116': {'angles': [-2,0,2], 'speed': [4]},
'117': {'angles': [-2,0,2], 'speed': [4]},
'118': {'angles': [-2,0,2], 'speed': [4]},
'119': {'angles': [-2,0,2], 'speed': [4]},
'120': {'angles': [-2,0,2], 'speed': [4]},
'121': {'angles': [-2,0,2], 'speed': [4]},
'122': {'angles': [-2,0,2], 'speed': [4]},
'123': {'angles': [-2,0,2], 'speed': [4]},
'124': {'angles': [-2,0,2], 'speed': [4]},
'125': {'angles': [-2,0,2], 'speed': [4]},
'126': {'angles': [-2,0,2], 'speed': [4]},
'127': {'angles': [-2,0,2], 'speed': [4]},
'128': {'angles': [-2,0,2], 'speed': [4]},
'129': {'angles': [-2,0,2], 'speed': [4]},
'130': {'angles': [-2,0,2], 'speed': [4]},
'131': {'angles': [-2,0,2], 'speed': [4]},
'132': {'angles': [-2,0,2], 'speed': [4]},
'133': {'angles': [0,2, 5,10], 'speed': [3,3.5,4]},
'134': {'angles': [0,2, 5,10], 'speed': [3,3.5,4]},
'135': {'angles': [0,2, 5,10], 'speed': [3,3.5,4]},
'136': {'angles': [0,2, 5,10], 'speed': [3,3.5,4]},
'137': {'angles': [0,2, 5,10], 'speed': [3,3.5,4]},
'138': {'angles': [0,2, 5,10], 'speed': [3,3.5,4]},
'139': {'angles': [0,2, 5,10], 'speed': [3,3.5,4]},
'140': {'angles': [0,2, 5,10], 'speed': [3,3.5,4]},
'141': {'angles': [0,2, 5,10], 'speed': [3,3.5,4]},
'142': {'angles': [0,2, 5,10], 'speed': [3,3.5,4]},
'143': {'angles': [0,2, 5,10], 'speed': [3,3.5,4]},
'144': {'angles': [0,2, 5,10], 'speed': [3,3.5,4]},
'145': {'angles': [0,2, 5,10], 'speed': [3,3.5,4]},
'146': {'angles': [0,2, 5,10], 'speed': [3,3.5,4]},
'147': {'angles': [0,2, 5,10], 'speed': [3,3.5,4]},
'148': {'angles': [0,2, 5,10], 'speed': [3,3.5,4]},
'149': {'angles': [0,2, 5,10], 'speed': [3,3.5,4]},
'150': {'angles': [0,2, 5,10], 'speed': [3,3.5,4]},
'151': {'angles': [0,2, 5,10], 'speed': [3,3.5,4]},
'152': {'angles': [0,2, 5,10], 'speed': [3,3.5,4]},
'153': {'angles': [0,2, 5,10], 'speed': [3,3.5,4]},
'154': {'angles': [0,2, 5,10], 'speed': [3,3.5,4]},
'155': {'angles': [0,2, 5,10], 'speed': [3,3.5,4]},
'156': {'angles': [0,2, 5,10], 'speed': [3,3.5,4]},
'157': {'angles': [0,2, 5,10], 'speed': [3,3.5,4]},
'158': {'angles': [0,2, 5,10], 'speed': [3,3.5,4]},
'159': {'angles': [0,2, 5,10], 'speed': [3,3.5,4]},
'160': {'angles': [0,2, 5,10], 'speed': [3,3.5,4]},
'161': {'angles': [0,2, 5,10], 'speed': [3,3.5,4]},
'162': {'angles': [0,2, 5,10], 'speed': [3,3.5,4]},
'163': {'angles': [-2,0,2], 'speed': [4]},
'164': {'angles': [-2,0,2], 'speed': [4]},
'165': {'angles': [-2,0,2], 'speed': [4]},
'166': {'angles': [-2,0,2], 'speed': [4]},
'167': {'angles': [-2,0,2], 'speed': [4]},
'168': {'angles': [-2,0,2], 'speed': [4]},
'169': {'angles': [-2,0,2], 'speed': [4]},
'170': {'angles': [-2,0,2], 'speed': [4]},
'171': {'angles': [-2,0,2], 'speed': [4]},
'172': {'angles': [-2,0,2], 'speed': [4]},
'173': {'angles': [-2,0,2], 'speed': [4]},
'174': {'angles': [-2,0,2], 'speed': [4]},
'175': {'angles': [-2,0,2], 'speed': [4]},
'176': {'angles': [-2,0,2], 'speed': [4]},
'177': {'angles': [-2,0,2], 'speed': [4]},
'178': {'angles': [-2,0,2], 'speed': [4]},
'179': {'angles': [-2,0,2], 'speed': [4]},
'180': {'angles': [-2,0,2], 'speed': [4]},
'181': {'angles': [-2,0,2], 'speed': [4]},
'182': {'angles': [-2,0,2], 'speed': [4]},
'183': {'angles': [-2,0,2], 'speed': [4]},
'184': {'angles': [-2,0,2], 'speed': [4]},
'185': {'angles': [-2,0,2], 'speed': [4]},
'186': {'angles': [-2,0,2], 'speed': [4]},
'187': {'angles': [-2,0,2], 'speed': [4]},
'188': {'angles': [-2,0,2], 'speed': [4]},
'189': {'angles': [15,25,30], 'speed': [1.3,1.6,2]},
'190':{'angles': [15,25,30], 'speed': [1.3,1.6,2]},
'191':{'angles': [15,25,30], 'speed': [1.3,1.6,2]},
'192':{'angles': [15,25,30], 'speed': [1.3,1.6,2]},
'193':{'angles': [15,25,30], 'speed': [1.3,1.6,2]},
'194':{'angles': [15,25,30], 'speed': [1.3,1.6,2]},
'195':{'angles': [15,25,30], 'speed': [1.3,1.6,2]},
'196':{'angles': [15,25,30], 'speed': [1.3,1.6,2]},
'197':{'angles': [15,25,30], 'speed': [1.3,1.6,2]},
'198':{'angles': [15,25,30], 'speed': [1.3,1.6,2]},
'199':{'angles': [15,25,30], 'speed': [1.3,1.6,2]},
'200':{'angles': [15,25,30], 'speed': [1.3,1.6,2]},
'201':{'angles': [15,25,30], 'speed': [1.3,1.6,2]},
'202':{'angles': [15,25,30], 'speed': [1.3,1.6,2]},
'203':{'angles': [15,25,30], 'speed': [1.3,1.6,2]},
'204':{'angles': [15,25,30], 'speed': [1.3,1.6,2]},
'205':{'angles': [-2,0,2], 'speed': [3.5,4]},
'206':{'angles': [-2,0,2], 'speed': [3.5,4]},
'207': {'angles': [-2,0,2], 'speed': [3.5,4]},
'208': {'angles': [-2,0,2], 'speed': [3.5,4]},
'209': {'angles': [-2,0,2], 'speed': [3.5,4]},
'210': {'angles': [-2,0,2], 'speed': [3.5,4]},
'211': {'angles': [-2,0,2], 'speed': [3.5,4]},
'212': {'angles': [-2,0,2], 'speed': [3.5,4]},
'213': {'angles': [-2,0,2], 'speed': [3.5,4]},
'214': {'angles': [-2,0,2], 'speed': [3.5,4]},
'215': {'angles': [-2,0,2], 'speed': [3.5,4]},
'216': {'angles': [-2,0,2], 'speed': [3.5,4]},
'217': {'angles': [-2,0,2], 'speed': [3.5,4]},
'218': {'angles': [-2,0,2], 'speed': [3.5,4]},
'219': {'angles': [-2,0,2], 'speed': [3.5,4]},
'220': {'angles': [-2,0,2], 'speed': [3.5,4]},
'221': {'angles': [-2,0,2], 'speed': [3.5,4]},
'222': {'angles': [-2,0,2], 'speed': [3.5,4]},
'223': {'angles': [-2,0,2], 'speed': [3.5,4]},
'224': {'angles': [-2,0,2], 'speed': [3.5,4]},
'225': {'angles': [-2,0,2], 'speed': [3.5,4]},
'226': {'angles': [-2,0,2], 'speed': [3.5,4]},
'227': {'angles': [-25,-15], 'speed': [1.6,2]},
'228': {'angles': [-25,-15], 'speed': [1.6,2]},
'229': {'angles': [-25,-15], 'speed': [1.6,2]},
'230': {'angles': [-25,-15], 'speed': [1.6,2]},
'231': {'angles': [-25,-15], 'speed': [1.6,2]},
'232': {'angles': [-25,-15], 'speed': [1.6,2]},
'233': {'angles': [-25,-15], 'speed': [1.6,2]},
'234': {'angles': [-25,-15], 'speed': [1.6,2]},
'235': {'angles': [-25,-15], 'speed': [1.6,2]},
'236': {'angles': [-25,-15], 'speed': [1.6,2]},
'237': {'angles': [-25,-15], 'speed': [1.6,2]},
'238': {'angles': [-25,-15], 'speed': [1.6,2]},
'239': {'angles': [-25,-15], 'speed': [1.6,2]},
'240': {'angles': [-25,-15], 'speed': [1.6,2]},
'241': {'angles': [-25,-15], 'speed': [1.6,2]},
'242': {'angles': [-25,-15], 'speed': [1.6,2]},
'243': {'angles': [-25,-15], 'speed': [1.6,2]},
'244': {'angles': [-25,-15], 'speed': [1.6,2]},
'245': {'angles': [-2,0,2], 'speed': [3.5,4]},
'246': {'angles': [-2,0,2], 'speed': [3.5,4]},
'247': {'angles': [-2,0,2], 'speed': [3.5,4]},
'248': {'angles': [-2,0,2], 'speed': [3.5,4]},
'249': {'angles': [-2,0,2], 'speed': [3.5,4]},
'250': {'angles': [-2,0,2], 'speed': [3.5,4]},
'251': {'angles': [-2,0,2], 'speed': [3.5,4]},
'252': {'angles': [-2,0,2], 'speed': [3.5,4]},
'253': {'angles': [-2,0,2], 'speed': [3.5,4]},
'254': {'angles': [-2,0,2], 'speed': [3.5,4]},
}

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

def reward_function(params):
    # Read input parameters
    waypoints = params['waypoints']
    speed = params['speed']
    closest_waypoints = _getClosestWaypoints(params)
    heading = _getHeading(params)

    #Calculate direction 
    track_direction = getTrackDirection(waypoints, closest_waypoints)
    angle = getDirectionDiff(track_direction, heading)
    
    reward = 1
    expected_waypoint = way.get(str(closest_waypoints[1]))
    if expected_waypoint:
        if angle in expected_waypoint.get('angles') and speed in expected_waypoint.get('speed'):
            reward +=25
        elif angle in expected_waypoint.get('angles'):
            reward +=10
        elif speed in expected_waypoint.get('speed'):
            reward +=10
    
    return float(reward)

