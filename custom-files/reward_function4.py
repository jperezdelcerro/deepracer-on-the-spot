import math 





DE_2_A_2                  = [-2, 0, 2]
DE_0_A_5   = [0, 2, 5]
DE_2_A_5   = [-2, 0, 2, 5]
DE_25_A_30 = [25, 30]
DE_10_A_25 = [10, 15, 25]

DE_15_A_25 = [-15, -25]
DE_15_A_2 = [-15, -10, -2]

CENTRO_DERECHA          = [0, 2]
CENTRO_LIBERAL          = [-5, 0, 5]
DERECHA                 = [0, 5, 10, 15]
DERECHA_DOBLE           = [15, 25, 30]
IZQUIERDA_DOBLE         = [-25, -15,-10]
IZQUIERDA_SUPER         = [-25,-15]
MASSA                   = [-10, -5, -2, 0, 2
, 5, 10]

angle_to_speed = {
                    '-25' : [1.6,2],
                    '-15' : [1.6],
                    '-10' : [2],
                    '-2' : [4],
                    '0' : [4, 2],
                    '2' : [4, 2],
                    '5' : [2, 3, 4],
                    '10' : [2, 4, 1.6],
                    '15' : [3.5, 1.6],
                    '25' : [1.6,],
                    '30' : [1.6,2],
                    }

way = {
    '0': {'angles':  DE_2_A_2, 'speed': [4]},
    '1': {'angles': DE_2_A_2, 'speed': [4]}, 
    '2': {'angles': DE_2_A_2, 'speed': [4]},
    '3': {'angles': DE_2_A_2, 'speed': [4]},
    '4': {'angles': DE_2_A_2, 'speed': [4]},
    '5': {'angles': DE_2_A_2, 'speed': [4]},
    '6': {'angles': DE_2_A_2, 'speed': [4]},
    '7': {'angles': DE_2_A_2, 'speed': [4]},
    '8': {'angles': DE_2_A_2, 'speed': [4]},
    '9': {'angles': DE_2_A_2, 'speed': [4]},
    '10': {'angles': DE_2_A_2, 'speed': [4]},
    '11': {'angles': DE_2_A_2, 'speed': [4]},
    '12': {'angles': DE_2_A_2, 'speed': [4]},
    '13': {'angles': DE_2_A_2, 'speed': [4]},
    '14': {'angles': DE_2_A_2, 'speed': [4]},

    '15': {'angles': DE_0_A_5, 'speed': [3, 2, 1.6]},
    '16': {'angles': DE_0_A_5, 'speed': [3, 2, 1.6]},
    '17': {'angles': DE_0_A_5, 'speed': [3, 2, 1.6]},

    '18': {'angles': DE_25_A_30, 'speed': [3, 2, 1.6]},
    '19': {'angles': DE_25_A_30, 'speed': [3, 2, 1.6]},
    '20': {'angles': DE_25_A_30, 'speed': [3, 2, 1.6]},
    '21': {'angles': DE_25_A_30, 'speed': [3, 2, 1.6]},
    '22': {'angles': DE_25_A_30, 'speed': [3, 2, 1.6]},

    '23': {'angles': DE_2_A_2, 'speed': [2, 4]},
    '24': {'angles': DE_2_A_2, 'speed': [2, 4]},
    '25': {'angles': DE_2_A_2, 'speed': [2, 4]},
    '26': {'angles': DE_2_A_2, 'speed': [2, 4]},

    '27': {'angles': DE_25_A_30, 'speed': [3, 2, 1.6]},
    '28': {'angles': DE_25_A_30, 'speed': [3, 2, 1.6]},
    '29': {'angles': DE_25_A_30, 'speed': [3, 2, 1.6]},

    '30': {'angles': DE_2_A_2, 'speed': [3, 2, 1.6]},
    '31': {'angles': DE_2_A_2, 'speed': [3, 2, 1.6]},
    '32': {'angles': DE_2_A_2, 'speed': [3, 2, 1.6]},

    '33': {'angles': DE_2_A_5, 'speed': [3, 2, 4]},
    '34': {'angles': DE_2_A_5, 'speed': [3, 2, 4]},
    '35': {'angles': DE_2_A_5, 'speed': [3, 2, 4]},
    '36': {'angles': DE_2_A_5, 'speed': [3, 2, 4]},
    '37': {'angles': DE_2_A_5, 'speed': [3, 2, 4]},
    '38': {'angles': DE_2_A_5, 'speed': [3, 2, 4]},
    '39': {'angles': DE_2_A_5, 'speed': [3, 2, 4]},
    '40': {'angles': DE_2_A_5, 'speed': [3, 2, 4]},
    '41': {'angles': DE_2_A_5, 'speed': [3, 2, 4]},
    '42': {'angles': DE_2_A_5, 'speed': [3, 2, 4]},

    '43': {'angles': DE_10_A_25, 'speed': [2, 4, 1.6, 3.5]},
    '44': {'angles': DE_10_A_25, 'speed': [2, 4, 1.6, 3.5]},
    '45': {'angles': DE_10_A_25, 'speed': [2, 4, 1.6, 3.5]},
    '46': {'angles': DE_10_A_25, 'speed': [2, 4, 1.6, 3.5]},
    '47': {'angles': DE_10_A_25, 'speed': [2, 4, 1.6, 3.5]},
    '48': {'angles': DE_10_A_25, 'speed': [2, 4, 1.6, 3.5]},
    
    '49': {'angles':DE_2_A_2, 'speed': [2, 4]},
    '50': {'angles':DE_2_A_2, 'speed': [2, 4]},
    '51': {'angles':DE_2_A_2, 'speed': [2, 4]},
    '52': {'angles':DE_2_A_2, 'speed': [2, 4]},
    '53': {'angles':DE_2_A_2, 'speed': [2, 4]},

    '54': {'angles': [30], 'speed':  [1.6,2]},
    '55': {'angles': [25], 'speed': [1.3,1.5,2]},
    '56': {'angles': [25], 'speed': [1.3,1.5,2]},

    '57': {'angles': DE_2_A_2, 'speed': [1.6, 2]},
    '58': {'angles': DE_2_A_2, 'speed': [1.6, 2]},
    '59': {'angles': DE_2_A_2,  'speed': [1.6, 2]},

    '60': {'angles': [10], 'speed': [1.6, 2]},
    '61': {'angles': [10], 'speed': [1.6, 2]},
    '62': {'angles': [10], 'speed': [1.6, 2]},
    '63': {'angles': [10], 'speed': [1.6, 2]},

    '64': {'angles': [30], 'speed':  [1.6,2]},
    '65': {'angles': [30], 'speed': [1.6,2]},
    '66': {'angles': [30], 'speed': [1.6,2]},

    '67': {'angles': [-25], 'speed': [2]},
    '68': {'angles': [-25], 'speed': [2]},
    '69': {'angles': [-25], 'speed': [2]},
    '70': {'angles': [-25], 'speed': [2]},
    '71': {'angles': [-25], 'speed': [2]},
    '72': {'angles': [-25], 'speed': [2]},
    '73': {'angles': [-25], 'speed': [2]},
    '74': {'angles': [-25], 'speed': [2]},
    '75': {'angles': [-25], 'speed': [2]},
    '76': {'angles': [-25], 'speed': [2]},
    '77': {'angles': [-25], 'speed': [2]},
    '78': {'angles': [-25], 'speed': [2]},
    '79': {'angles': [-25], 'speed': [2]},
    
    '80': {'angles': DE_2_A_2, 'speed': [2, 4]},
    '81': {'angles': DE_2_A_2, 'speed': [2, 4]},
    '82': {'angles': DE_2_A_2, 'speed': [2, 4]},
    '83': {'angles':DE_2_A_2, 'speed': [2, 4]},
    '84': {'angles':DE_2_A_2, 'speed': [2, 4]},
    '85': {'angles':DE_2_A_2, 'speed': [2, 4]},
    '86': {'angles':DE_2_A_2, 'speed': [2, 4]},
    '87': {'angles':DE_2_A_2, 'speed': [2, 4]},
    '88': {'angles':DE_2_A_2, 'speed': [2, 4]},
    '89': {'angles':DE_2_A_2, 'speed': [2, 4]},
    '90': {'angles':DE_2_A_2, 'speed': [2, 4]},
    '91': {'angles': DE_2_A_2, 'speed': [2, 4]},
    '92': {'angles': DE_2_A_2, 'speed': [2, 4]},
    '93': {'angles': DE_2_A_2, 'speed': [2, 4]},
    '94': {'angles': DE_2_A_2, 'speed': [2, 4]},

    '95': {'angles': DE_15_A_25, 'speed': [2]},
    '96': {'angles': DE_15_A_25, 'speed': [2]},
    '97': {'angles': DE_15_A_25, 'speed': [2]},
    '98': {'angles': DE_15_A_25, 'speed': [2]},
    '99': {'angles': DE_15_A_25, 'speed': [2]},
    '100': {'angles': DE_15_A_25, 'speed': [2]},
    '101': {'angles': DE_15_A_25, 'speed': [2]},
    '102': {'angles': DE_15_A_25, 'speed': [2]},

    '103': {'angles': DE_25_A_30, 'speed': [3, 2, 1.6]},
    '104': {'angles': DE_25_A_30, 'speed': [3, 2, 1.6]},
    '105': {'angles': DE_25_A_30, 'speed': [3, 2, 1.6]},
    '106': {'angles': DE_25_A_30, 'speed': [3, 2, 1.6]},

    '107': {'angles': [10], 'speed': [1.6,2]},
    '108': {'angles': [10], 'speed': [1.6,2]},
    '109': {'angles': [10], 'speed': [1.6,2]},
    '110': {'angles': [10], 'speed': [1.6,2]},
    '111': {'angles': [10], 'speed': [1.6,2]},
    '112': {'angles': [10], 'speed': [1.6,2]},
    '113': {'angles': [10], 'speed': [1.6,2]},
    '114': {'angles': [10], 'speed': [1.6,2]},

    '115': {'angles':DE_2_A_2, 'speed': [4]},
    '116': {'angles':DE_2_A_2, 'speed': [4]},
    '117': {'angles':DE_2_A_2, 'speed': [4]},
    '118': {'angles':DE_2_A_2, 'speed': [4]},
    '119': {'angles':DE_2_A_2, 'speed': [4]},
    '120': {'angles':DE_2_A_2, 'speed': [4]},
    '121': {'angles':DE_2_A_2, 'speed': [4]},
    '122': {'angles':DE_2_A_2, 'speed': [4]},
    '123': {'angles':DE_2_A_2, 'speed': [4]},
    '124': {'angles':DE_2_A_2, 'speed': [4]},
    '125': {'angles':DE_2_A_2, 'speed': [4]},
    '126': {'angles':DE_2_A_2, 'speed': [4]},
    '127': {'angles':DE_2_A_2, 'speed': [4]},
    '128': {'angles':DE_2_A_2, 'speed': [4]},
    '129': {'angles':DE_2_A_2, 'speed': [4]},
    '130': {'angles':DE_2_A_2, 'speed': [4]},
    '131': {'angles':DE_2_A_2, 'speed': [4]},
    '132': {'angles':DE_2_A_2, 'speed': [4]},
    '133': {'angles': DE_2_A_2, 'speed': [4]},
    '134': {'angles': DE_2_A_2, 'speed': [4]},
    '135': {'angles': DE_2_A_2, 'speed': [4]},
    '136': {'angles': DE_2_A_2, 'speed': [4]},
    '137': {'angles': DE_2_A_2, 'speed': [4]},
    
    '138': {'angles': [10], 'speed': [4]},
    '139': {'angles': [10], 'speed': [2, 4]},
    '140': {'angles': [10], 'speed': [2, 4]},
    '141': {'angles': [10], 'speed': [2, 4]},
    '142': {'angles': [10], 'speed': [2, 4]},
    '143': {'angles': [10], 'speed': [2, 4]},
    '144': {'angles': [10], 'speed': [2, 4]},
    '145': {'angles': [10], 'speed': [2, 4]},
    '146': {'angles': [10], 'speed': [2, 4]},
    '147': {'angles': [10], 'speed': [2, 4]},
    '148': {'angles': [10], 'speed': [2, 4]},
    '149': {'angles': [10], 'speed': [2, 4]},
    '150': {'angles': [10], 'speed': [2, 4]},
    '151': {'angles': [10], 'speed': [2, 4]},
    '152': {'angles': [10], 'speed': [2, 4]},
    '153': {'angles': [10], 'speed': [2, 4]},
    '154': {'angles': [10], 'speed': [2, 4]},
    '155': {'angles': [10], 'speed': [2, 4]},
    '156': {'angles': [10], 'speed': [2, 4]},
    '157': {'angles': [10], 'speed': [2, 4]},
    '158': {'angles': [10], 'speed': [2, 4]},

    '159': {'angles': DE_2_A_2, 'speed': [4]},
    '160': {'angles': DE_2_A_2, 'speed': [4]},
    '161': {'angles': DE_2_A_2, 'speed': [4]},
    '162': {'angles': DE_2_A_2, 'speed': [4]},
    '163': {'angles':DE_2_A_2, 'speed': [4]},
    '164': {'angles':DE_2_A_2, 'speed': [4]},
    '165': {'angles':DE_2_A_2, 'speed': [4]},
    '166': {'angles':DE_2_A_2, 'speed': [4]},
    '167': {'angles':DE_2_A_2, 'speed': [4]},
    '168': {'angles':DE_2_A_2, 'speed': [4]},
    '169': {'angles':DE_2_A_2, 'speed': [4]},
    '170': {'angles':DE_2_A_2, 'speed': [4]},
    '171': {'angles':DE_2_A_2, 'speed': [4]},
    '172': {'angles':DE_2_A_2, 'speed': [4]},
    '173': {'angles':DE_2_A_2, 'speed': [4]},
    '174': {'angles':DE_2_A_2, 'speed': [4]},
    '175': {'angles':DE_2_A_2, 'speed': [4]},
    '176': {'angles':DE_2_A_2, 'speed': [4]},
    '177': {'angles':DE_2_A_2, 'speed': [4]},
    '178': {'angles':DE_2_A_2, 'speed': [4]},
    '179': {'angles':DE_2_A_2, 'speed': [4]},

    '180': {'angles':DE_2_A_2, 'speed': [4]},
    '181': {'angles':DE_2_A_2, 'speed': [4]},
    '182': {'angles':DE_2_A_2, 'speed': [4]},
    '183': {'angles':DE_2_A_2, 'speed': [4]},
    '184': {'angles':DE_2_A_2, 'speed': [4]},
    '185': {'angles':DE_2_A_2, 'speed': [4]},
    '186': {'angles':DE_2_A_2, 'speed': [4]},
    '187': {'angles':DE_2_A_2, 'speed': [4]},
    '188': {'angles':DE_2_A_2, 'speed': [4]},
    '189': {'angles': DERECHA_DOBLE, 'speed': [1.3,1.6,2]},
    '190':{'angles': DERECHA_DOBLE, 'speed': [1.3,1.6,2]},
    '191':{'angles': DERECHA_DOBLE, 'speed': [1.3,1.6,2]},
    '192':{'angles': DERECHA_DOBLE, 'speed': [1.3,1.6,2]},
    '193':{'angles': DERECHA_DOBLE, 'speed': [1.3,1.6,2]},
    '194':{'angles': DERECHA_DOBLE, 'speed': [1.3,1.6,2]},
    '195':{'angles': DERECHA_DOBLE, 'speed': [1.3,1.6,2]},
    '196':{'angles': DERECHA_DOBLE, 'speed': [1.3,1.6,2]},
    '197':{'angles': DERECHA_DOBLE, 'speed': [1.3,1.6,2]},
    '198':{'angles': DERECHA_DOBLE, 'speed': [1.3,1.6,2]},
    '199':{'angles': DERECHA_DOBLE, 'speed': [1.3,1.6,2]},
    '200':{'angles': DERECHA_DOBLE, 'speed': [1.3,1.6,2]},
    '201':{'angles': DERECHA_DOBLE, 'speed': [1.3,1.6,2]},
    '202':{'angles': DERECHA_DOBLE, 'speed': [1.3,1.6,2]},
    '203':{'angles': DERECHA_DOBLE, 'speed': [1.3,1.6,2]},
    '204':{'angles': DERECHA_DOBLE, 'speed': [1.3,1.6,2]},
    '205':{'angles':DE_2_A_2, 'speed': [3.5,4]},
    '206':{'angles':DE_2_A_2, 'speed': [3.5,4]},
    '207': {'angles':DE_2_A_2, 'speed': [3.5,4]},
    '208': {'angles':DE_2_A_2, 'speed': [3.5,4]},
    '209': {'angles':DE_2_A_2, 'speed': [3.5,4]},
    '210': {'angles':DE_2_A_2, 'speed': [3.5,4]},
    '211': {'angles':DE_2_A_2, 'speed': [3.5,4]},
    '212': {'angles':DE_2_A_2, 'speed': [3.5,4]},
    '213': {'angles':DE_2_A_2, 'speed': [3.5,4]},
    '214': {'angles':DE_2_A_2, 'speed': [3.5,4]},
    '215': {'angles':DE_2_A_2, 'speed': [3.5,4]},
    '216': {'angles':DE_2_A_2, 'speed': [3.5,4]},
    '217': {'angles':DE_2_A_2, 'speed': [3.5,4]},
    '218': {'angles':DE_2_A_2, 'speed': [3.5,4]},
    '219': {'angles':DE_2_A_2, 'speed': [3.5,4]},
    '220': {'angles':DE_2_A_2, 'speed': [3.5,4]},
    '221': {'angles':DE_2_A_2, 'speed': [3.5,4]},
    '222': {'angles':DE_2_A_2, 'speed': [3.5,4]},
    '223': {'angles':DE_2_A_2, 'speed': [3.5,4]},
    '224': {'angles':DE_2_A_2, 'speed': [3.5,4]},
    '225': {'angles':DE_2_A_2, 'speed': [3.5,4]},
    '226': {'angles':DE_2_A_2, 'speed': [3.5,4]},
    '227': {'angles': IZQUIERDA_SUPER, 'speed': [1.6,2]},
    '228': {'angles': IZQUIERDA_SUPER, 'speed': [1.6,2]},
    '229': {'angles': IZQUIERDA_SUPER, 'speed': [1.6,2]},
    '230': {'angles': IZQUIERDA_SUPER, 'speed': [1.6,2]},
    '231': {'angles': IZQUIERDA_SUPER, 'speed': [1.6,2]},
    '232': {'angles': IZQUIERDA_SUPER, 'speed': [1.6,2]},
    '233': {'angles': IZQUIERDA_SUPER, 'speed': [1.6,2]},
    '234': {'angles': IZQUIERDA_SUPER, 'speed': [1.6,2]},
    '235': {'angles': IZQUIERDA_SUPER, 'speed': [1.6,2]},
    '236': {'angles': IZQUIERDA_SUPER, 'speed': [1.6,2]},
    '237': {'angles': IZQUIERDA_SUPER, 'speed': [1.6,2]},
    '238': {'angles': IZQUIERDA_SUPER, 'speed': [1.6,2]},
    '239': {'angles': IZQUIERDA_SUPER, 'speed': [1.6,2]},
    '240': {'angles': IZQUIERDA_SUPER, 'speed': [1.6,2]},
    '241': {'angles': IZQUIERDA_SUPER, 'speed': [1.6,2]},
    '242': {'angles': IZQUIERDA_SUPER, 'speed': [1.6,2]},
    '243': {'angles': IZQUIERDA_SUPER, 'speed': [1.6,2]},
    '244': {'angles': IZQUIERDA_SUPER, 'speed': [1.6,2]},
    '245': {'angles':DE_2_A_2, 'speed': [3.5,4]},
    '246': {'angles':DE_2_A_2, 'speed': [3.5,4]},
    '247': {'angles':DE_2_A_2, 'speed': [3.5,4]},
    '248': {'angles':DE_2_A_2, 'speed': [3.5,4]},
    '249': {'angles':DE_2_A_2, 'speed': [3.5,4]},
    '250': {'angles':DE_2_A_2, 'speed': [3.5,4]},
    '251': {'angles':DE_2_A_2, 'speed': [3.5,4]},
    '252': {'angles':DE_2_A_2, 'speed': [3.5,4]},
    '253': {'angles':DE_2_A_2, 'speed': [3.5,4]},
    '254': {'angles':DE_2_A_2, 'speed': [3.5,4]},
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

