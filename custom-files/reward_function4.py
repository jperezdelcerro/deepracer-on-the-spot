import math 



CENTRO                  = [-2, 0, 2]
CENTRO_LIBERAL          = [-5, 0, 5]
CENTRO_DERECHA          = [0, 2]
CENTRO_DERECHA_SIMPLE   = [0, 2, 5, 10]
DERECHA                 = [0, 5, 10, 15]
DERECHA_DOBLE           = [15, 25, 30]
IZQUIERDA_DOBLE         = [-25, -15,-10]
IZQUIERDA_SUPER         = [-25,-15]
MASSA                   = [-10, -5, -2, 0, 2, 5, 10]


way = {
    '0':  {'angles':  CENTRO, 'speed': [3.8, 4]},
    '1': {'angles': CENTRO, 'speed': [3.8, 4]}, 
    '2': {'angles': CENTRO, 'speed': [3.8, 4]},
    '3': {'angles': CENTRO, 'speed': [3.8, 4]},
    '4': {'angles': CENTRO, 'speed': [3.8, 4]},
    '5': {'angles': CENTRO, 'speed': [3.8, 4]},
    '6': {'angles': CENTRO, 'speed': [3.8, 4]},
    '7': {'angles': CENTRO, 'speed': [3.8, 4]},
    '8': {'angles': CENTRO, 'speed': [4]},
    '9': {'angles': CENTRO, 'speed': [4]},
    '10': {'angles': CENTRO + [5], 'speed': [4]},
    '11': {'angles': DERECHA, 'speed': [2.5, 3]},
    '12': {'angles': DERECHA, 'speed': [2.5, 3]},
    '13': {'angles': DERECHA, 'speed': [2.5, 3]},
    '14': {'angles': DERECHA, 'speed': [2.5, 3]},
    '15': {'angles': DERECHA, 'speed': [2.5, 3]},
    '16': {'angles': DERECHA, 'speed': [2.5, 3]},
    '17': {'angles': DERECHA, 'speed': [2.5, 3]},
    '18': {'angles': DERECHA, 'speed': [2.5, 3]},
    '19': {'angles': DERECHA, 'speed': [2.5, 3]},
    '20': {'angles': DERECHA, 'speed': [2.5, 3]},
    '21': {'angles': DERECHA, 'speed': [2.5, 3]},
    '22': {'angles': DERECHA, 'speed': [2.5, 3]},
    '23': {'angles': DERECHA, 'speed': [2.5, 3]},
    '24': {'angles': DERECHA, 'speed': [2.5, 3]},
    '25': {'angles': DERECHA, 'speed': [2.5, 3]},
    '26': {'angles': DERECHA, 'speed': [2.5, 3]},
    '27': {'angles': DERECHA, 'speed': [2.5, 3]},
    '28': {'angles': DERECHA, 'speed': [2.5, 3]},
    '29': {'angles': CENTRO_DERECHA, 'speed': [3.8, 4]},
    '30': {'angles': CENTRO_DERECHA, 'speed': [3.8, 4]},
    '31': {'angles': CENTRO_DERECHA, 'speed': [3.8, 4]},
    '32': {'angles': CENTRO_DERECHA, 'speed': [3.8, 4]},
    '33': {'angles': CENTRO_DERECHA, 'speed': [3.8, 4]},
    '34': {'angles': CENTRO_DERECHA, 'speed': [3.8, 4]},
    '35': {'angles': DERECHA, 'speed': [3,3.5,2.5]},
    '36': {'angles': DERECHA, 'speed': [3,3.5,2.5]},
    '37': {'angles': DERECHA, 'speed': [3,3.5,2.5]},
    '38': {'angles': DERECHA, 'speed': [3,3.5,2.5]},
    '39': {'angles': DERECHA, 'speed': [3,3.5,2.5]},
    '40': {'angles': DERECHA, 'speed': [3,3.5,2.5]},
    '41': {'angles': DERECHA, 'speed': [3,3.5,2.5]},
    '42': {'angles': DERECHA, 'speed': [3,3.5,2.5]},
    '43': {'angles': DERECHA, 'speed': [3,3.5,2.5]},
    '44': {'angles': DERECHA, 'speed': [3,3.5,2.5]},
    '45': {'angles': DERECHA, 'speed': [3,3.5,2.5]},
    '46': {'angles': DERECHA, 'speed': [3,3.5,2.5]},
    '47': {'angles': DERECHA, 'speed': [3,3.5,2.5]},
    '48': {'angles': DERECHA, 'speed': [3,3.5,2.5]},
    '49': {'angles':CENTRO, 'speed': [3.8, 4]},
    '50': {'angles':CENTRO, 'speed': [3.8, 4]},
    '51': {'angles':CENTRO, 'speed': [3.8, 4]},
    '52': {'angles':CENTRO, 'speed': [3.8, 4]},
    '53': {'angles':CENTRO, 'speed': [3.8, 4]},
    '54': {'angles': DERECHA_DOBLE, 'speed': [1.3,1.5,2]},
    '55': {'angles': DERECHA_DOBLE, 'speed': [1.3,1.5,2]},
    '56': {'angles': DERECHA_DOBLE, 'speed': [1.3,1.5,2]},
    '57': {'angles': DERECHA_DOBLE, 'speed': [1.3,1.5,2]},
    '58': {'angles': DERECHA_DOBLE, 'speed': [1.3,1.5,2]},
    '59': {'angles': DERECHA_DOBLE, 'speed': [1.3,1.5,2]},
    '60': {'angles': DERECHA_DOBLE, 'speed': [1.3,1.5,2]},
    '61': {'angles': DERECHA_DOBLE, 'speed': [1.3,1.5,2]},
    '62': {'angles': DERECHA_DOBLE, 'speed': [1.3,1.5,2]},
    '63': {'angles': DERECHA_DOBLE, 'speed': [1.3,1.5,2]},
    '64': {'angles': MASSA, 'speed': [1.5,2]},
    '65': {'angles': MASSA, 'speed': [1.5,2]},
    '66': {'angles': MASSA, 'speed': [1.5,2]},
    '67': {'angles': IZQUIERDA_DOBLE, 'speed': [1.5,2]},
    '68': {'angles': IZQUIERDA_DOBLE, 'speed': [1.5,2]},
    '69': {'angles': IZQUIERDA_DOBLE, 'speed': [1.5,2]},
    '70': {'angles': IZQUIERDA_DOBLE, 'speed': [1.5,2]},
    '71': {'angles': IZQUIERDA_DOBLE, 'speed': [1.5,2]},
    '72': {'angles': IZQUIERDA_DOBLE, 'speed': [1.5,2]},
    '73': {'angles': IZQUIERDA_DOBLE, 'speed': [1.5,2]},
    '74': {'angles': IZQUIERDA_DOBLE, 'speed': [1.5,2]},
    '75': {'angles': IZQUIERDA_DOBLE, 'speed': [1.5,2]},
    '76': {'angles': IZQUIERDA_DOBLE, 'speed': [1.5,2]},
    '77': {'angles': IZQUIERDA_DOBLE, 'speed': [1.5,2]},
    '78': {'angles': IZQUIERDA_DOBLE, 'speed': [1.5,2]},
    '79': {'angles': IZQUIERDA_DOBLE, 'speed': [1.5,2]},
    '80': {'angles': IZQUIERDA_DOBLE, 'speed': [1.5,2]},
    '81': {'angles': IZQUIERDA_DOBLE, 'speed': [1.5,2]},
    '82': {'angles': IZQUIERDA_DOBLE, 'speed': [1.5,2]},
    '83': {'angles':CENTRO, 'speed': [3.5,4]},
    '84': {'angles':CENTRO, 'speed': [3.5,4]},
    '85': {'angles':CENTRO, 'speed': [3.5,4]},
    '86': {'angles':CENTRO, 'speed': [3.5,4]},
    '87': {'angles':CENTRO, 'speed': [3.5,4]},
    '88': {'angles':CENTRO, 'speed': [3.5,4]},
    '89': {'angles':CENTRO, 'speed': [3.5,4]},
    '90': {'angles':CENTRO, 'speed': [3.5,4]},
    '91': {'angles': IZQUIERDA_SUPER, 'speed': [1.6,2]},
    '92': {'angles': IZQUIERDA_SUPER, 'speed': [1.6,2]},
    '93': {'angles': IZQUIERDA_SUPER, 'speed': [1.6,2]},
    '94': {'angles': IZQUIERDA_SUPER, 'speed': [1.6,2]},
    '95': {'angles': IZQUIERDA_SUPER, 'speed': [1.6,2]},
    '96': {'angles': IZQUIERDA_SUPER, 'speed': [1.6,2]},
    '97': {'angles': IZQUIERDA_SUPER, 'speed': [1.6,2]},
    '98': {'angles': IZQUIERDA_SUPER, 'speed': [1.6,2]},
    '99': {'angles': CENTRO_LIBERAL, 'speed': [3]},
    '100': {'angles': CENTRO_LIBERAL, 'speed': [3]},
    '101': {'angles': CENTRO_LIBERAL, 'speed': [3]},
    '102': {'angles': DERECHA_DOBLE + [10], 'speed': [1.3,1.6,2]},
    '103': {'angles': DERECHA_DOBLE + [10], 'speed': [1.3,1.6,2]},
    '104': {'angles': DERECHA_DOBLE + [10], 'speed': [1.3,1.6,2]},
    '105': {'angles': DERECHA_DOBLE + [10], 'speed': [1.3,1.6,2]},
    '106': {'angles': DERECHA_DOBLE + [10], 'speed': [1.3,1.6,2]},
    '107': {'angles': DERECHA_DOBLE + [10], 'speed': [1.3,1.6,2]},
    '108': {'angles': DERECHA_DOBLE + [10], 'speed': [1.3,1.6,2]},
    '109': {'angles': DERECHA_DOBLE + [10], 'speed': [1.3,1.6,2]},
    '110': {'angles': DERECHA_DOBLE + [10], 'speed': [1.3,1.6,2]},
    '111': {'angles': DERECHA_DOBLE + [10], 'speed': [1.3,1.6,2]},
    '112': {'angles': DERECHA_DOBLE + [10], 'speed': [1.3,1.6,2]},
    '113': {'angles': DERECHA_DOBLE + [10], 'speed': [1.3,1.6,2]},
    '114': {'angles': DERECHA_DOBLE + [10], 'speed': [1.3,1.6,2]},
    '115': {'angles':CENTRO, 'speed': [4]},
    '116': {'angles':CENTRO, 'speed': [4]},
    '117': {'angles':CENTRO, 'speed': [4]},
    '118': {'angles':CENTRO, 'speed': [4]},
    '119': {'angles':CENTRO, 'speed': [4]},
    '120': {'angles':CENTRO, 'speed': [4]},
    '121': {'angles':CENTRO, 'speed': [4]},
    '122': {'angles':CENTRO, 'speed': [4]},
    '123': {'angles':CENTRO, 'speed': [4]},
    '124': {'angles':CENTRO, 'speed': [4]},
    '125': {'angles':CENTRO, 'speed': [4]},
    '126': {'angles':CENTRO, 'speed': [4]},
    '127': {'angles':CENTRO, 'speed': [4]},
    '128': {'angles':CENTRO, 'speed': [4]},
    '129': {'angles':CENTRO, 'speed': [4]},
    '130': {'angles':CENTRO, 'speed': [4]},
    '131': {'angles':CENTRO, 'speed': [4]},
    '132': {'angles':CENTRO, 'speed': [4]},
    '133': {'angles': CENTRO_DERECHA_SIMPLE, 'speed': [3,3.5,4]},
    '134': {'angles': CENTRO_DERECHA_SIMPLE, 'speed': [3,3.5,4]},
    '135': {'angles': CENTRO_DERECHA_SIMPLE, 'speed': [3,3.5,4]},
    '136': {'angles': CENTRO_DERECHA_SIMPLE, 'speed': [3,3.5,4]},
    '137': {'angles': CENTRO_DERECHA_SIMPLE, 'speed': [3,3.5,4]},
    '138': {'angles': CENTRO_DERECHA_SIMPLE, 'speed': [3,3.5,4]},
    '139': {'angles': CENTRO_DERECHA_SIMPLE, 'speed': [3,3.5,4]},
    '140': {'angles': CENTRO_DERECHA_SIMPLE, 'speed': [3,3.5,4]},
    '141': {'angles': CENTRO_DERECHA_SIMPLE, 'speed': [3,3.5,4]},
    '142': {'angles': CENTRO_DERECHA_SIMPLE, 'speed': [3,3.5,4]},
    '143': {'angles': CENTRO_DERECHA_SIMPLE, 'speed': [3,3.5,4]},
    '144': {'angles': CENTRO_DERECHA_SIMPLE, 'speed': [3,3.5,4]},
    '145': {'angles': CENTRO_DERECHA_SIMPLE, 'speed': [3,3.5,4]},
    '146': {'angles': CENTRO_DERECHA_SIMPLE, 'speed': [3,3.5,4]},
    '147': {'angles': CENTRO_DERECHA_SIMPLE, 'speed': [3,3.5,4]},
    '148': {'angles': CENTRO_DERECHA_SIMPLE, 'speed': [3,3.5,4]},
    '149': {'angles': CENTRO_DERECHA_SIMPLE, 'speed': [3,3.5,4]},
    '150': {'angles': CENTRO_DERECHA_SIMPLE, 'speed': [3,3.5,4]},
    '151': {'angles': CENTRO_DERECHA_SIMPLE, 'speed': [3,3.5,4]},
    '152': {'angles': CENTRO_DERECHA_SIMPLE, 'speed': [3,3.5,4]},
    '153': {'angles': CENTRO_DERECHA_SIMPLE, 'speed': [3,3.5,4]},
    '154': {'angles': CENTRO_DERECHA_SIMPLE, 'speed': [3,3.5,4]},
    '155': {'angles': CENTRO_DERECHA_SIMPLE, 'speed': [3,3.5,4]},
    '156': {'angles': CENTRO_DERECHA_SIMPLE, 'speed': [3,3.5,4]},
    '157': {'angles': CENTRO_DERECHA_SIMPLE, 'speed': [3,3.5,4]},
    '158': {'angles': CENTRO_DERECHA_SIMPLE, 'speed': [3,3.5,4]},
    '159': {'angles': CENTRO_DERECHA_SIMPLE, 'speed': [3,3.5,4]},
    '160': {'angles': CENTRO_DERECHA_SIMPLE, 'speed': [3,3.5,4]},
    '161': {'angles': CENTRO_DERECHA_SIMPLE, 'speed': [3,3.5,4]},
    '162': {'angles': CENTRO_DERECHA_SIMPLE, 'speed': [3,3.5,4]},
    '163': {'angles':CENTRO, 'speed': [4]},
    '164': {'angles':CENTRO, 'speed': [4]},
    '165': {'angles':CENTRO, 'speed': [4]},
    '166': {'angles':CENTRO, 'speed': [4]},
    '167': {'angles':CENTRO, 'speed': [4]},
    '168': {'angles':CENTRO, 'speed': [4]},
    '169': {'angles':CENTRO, 'speed': [4]},
    '170': {'angles':CENTRO, 'speed': [4]},
    '171': {'angles':CENTRO, 'speed': [4]},
    '172': {'angles':CENTRO, 'speed': [4]},
    '173': {'angles':CENTRO, 'speed': [4]},
    '174': {'angles':CENTRO, 'speed': [4]},
    '175': {'angles':CENTRO, 'speed': [4]},
    '176': {'angles':CENTRO, 'speed': [4]},
    '177': {'angles':CENTRO, 'speed': [4]},
    '178': {'angles':CENTRO, 'speed': [4]},
    '179': {'angles':CENTRO, 'speed': [4]},
    '180': {'angles':CENTRO, 'speed': [4]},
    '181': {'angles':CENTRO, 'speed': [4]},
    '182': {'angles':CENTRO, 'speed': [4]},
    '183': {'angles':CENTRO, 'speed': [4]},
    '184': {'angles':CENTRO, 'speed': [4]},
    '185': {'angles':CENTRO, 'speed': [4]},
    '186': {'angles':CENTRO, 'speed': [4]},
    '187': {'angles':CENTRO, 'speed': [4]},
    '188': {'angles':CENTRO, 'speed': [4]},
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
    '205':{'angles':CENTRO, 'speed': [3.5,4]},
    '206':{'angles':CENTRO, 'speed': [3.5,4]},
    '207': {'angles':CENTRO, 'speed': [3.5,4]},
    '208': {'angles':CENTRO, 'speed': [3.5,4]},
    '209': {'angles':CENTRO, 'speed': [3.5,4]},
    '210': {'angles':CENTRO, 'speed': [3.5,4]},
    '211': {'angles':CENTRO, 'speed': [3.5,4]},
    '212': {'angles':CENTRO, 'speed': [3.5,4]},
    '213': {'angles':CENTRO, 'speed': [3.5,4]},
    '214': {'angles':CENTRO, 'speed': [3.5,4]},
    '215': {'angles':CENTRO, 'speed': [3.5,4]},
    '216': {'angles':CENTRO, 'speed': [3.5,4]},
    '217': {'angles':CENTRO, 'speed': [3.5,4]},
    '218': {'angles':CENTRO, 'speed': [3.5,4]},
    '219': {'angles':CENTRO, 'speed': [3.5,4]},
    '220': {'angles':CENTRO, 'speed': [3.5,4]},
    '221': {'angles':CENTRO, 'speed': [3.5,4]},
    '222': {'angles':CENTRO, 'speed': [3.5,4]},
    '223': {'angles':CENTRO, 'speed': [3.5,4]},
    '224': {'angles':CENTRO, 'speed': [3.5,4]},
    '225': {'angles':CENTRO, 'speed': [3.5,4]},
    '226': {'angles':CENTRO, 'speed': [3.5,4]},
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
    '245': {'angles':CENTRO, 'speed': [3.5,4]},
    '246': {'angles':CENTRO, 'speed': [3.5,4]},
    '247': {'angles':CENTRO, 'speed': [3.5,4]},
    '248': {'angles':CENTRO, 'speed': [3.5,4]},
    '249': {'angles':CENTRO, 'speed': [3.5,4]},
    '250': {'angles':CENTRO, 'speed': [3.5,4]},
    '251': {'angles':CENTRO, 'speed': [3.5,4]},
    '252': {'angles':CENTRO, 'speed': [3.5,4]},
    '253': {'angles':CENTRO, 'speed': [3.5,4]},
    '254': {'angles':CENTRO, 'speed': [3.5,4]},
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

