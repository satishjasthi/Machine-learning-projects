import random
from environment import Environment,Agent

class RoutePlanner(object):
    """ Complex route planner that is meant for a perpendicular grid network. """

    def __init__(self, env, agent):
        self.env = env
        self.agent = agent
        self.destination = None

    def route_to(self, destination=None):
        """ Select the destination if one is provided, otherwise choose a random intersection. """

        self.destination = destination if destination is not None else random.choice(self.env.intersections.keys())

        #here intersection.keys = [(1, 2), (1, 3), (1, 4), (1, 5), (1, 6),
        #  (1, 7), (1, 8), (1, 9), (2, 2), (2, 3), (2, 4), (2, 5), (2, 6),
        #  (2, 7), (2, 8), (2, 9), (3, 2), (3, 3), (3, 4), (3, 5), (3, 6),
        # (3, 7), (3, 8), (3, 9), (4, 2), (4, 3), (4, 4), (4, 5), (4, 6),
        #  (4, 7), (4, 8), (4, 9), (5, 2), (5, 3), (5, 4), (5, 5), (5, 6),
        # (5, 7), (5, 8), (5, 9), (6, 2), (6, 3), (6, 4), (6, 5), (6, 6),
        # (6, 7), (6, 8), (6, 9), (7, 2), (7, 3), (7, 4), (7, 5), (7, 6),
        # (7, 7), (7, 8), (7, 9), (8, 2), (8, 3), (8, 4), (8, 5), (8, 6),
        # (8, 7), (8, 8), (8, 9)]
        #these are the various positions within grid world



    def next_waypoint(self):
        """ Creates the next waypoint based on current heading, location,
            intended destination and L1 distance from destination. """

        # Collect global location details
        bounds = self.env.grid_size

        #here bounds = (8,6),becuase Environment object has an attribute grid_size = (8,6)

        location = self.env.agent_states[self.agent]['location']#selecting location key
        #from agent_states dictinoary

        #agent_states is an attribute of Environment object
        #agent_states is a orderedDict()
        #agent_states take Learning_agent as a key, here it is self.agent
        #agent_state looks something like
        #agent_state = {'agent':{'location':value,'heading':value2}}

        #print "location",location
        heading = self.env.agent_states[self.agent]['heading']
        #print "heading",heading


        delta_a = (self.destination[0] - location[0], self.destination[1] - location[1])

        #here destination is list of intersection.keys as mentioned above
        #location is also a list of intersection.keys

        #print "delta_a",delta_a
        delta_b = (bounds[0] + delta_a[0] if delta_a[0] <= 0 else delta_a[0] - bounds[0], \
                   bounds[1] + delta_a[1] if delta_a[1] <= 0 else delta_a[1] - bounds[1])
        #print "delta_b",delta_b

        # Calculate true difference in location based on world-wrap
        # This will pre-determine the need for U-turns from improper headings
        dx = delta_a[0] if abs(delta_a[0]) < abs(delta_b[0]) else delta_b[0]
        dy = delta_a[1] if abs(delta_a[1]) < abs(delta_b[1]) else delta_b[1]

        #here we are calculating the difference in x and y co-ordinates of destination and location

        # First check if destination is at location
        if dx == 0 and dy == 0:
            return None
        
        # Next check if destination is cardinally East or West of location    
        elif dx != 0:

            if dx * heading[0] > 0:  # Heading the correct East or West direction
                return 'forward'
            elif dx * heading[0] < 0 and heading[0] < 0: # Heading West, destination East
                if dy > 0: # Destination also to the South
                    return 'left'
                else:
                    return 'right'
            elif dx * heading[0] < 0 and heading[0] > 0: # Heading East, destination West
                if dy < 0: # Destination also to the North
                    return 'left'
                else:
                    return 'right'
            elif dx * heading[1] > 0: # Heading North destination West; Heading South destination East
                return 'left'
            else:
                return 'right'

        # Finally, check if destination is cardinally North or South of location
        elif dy != 0:

            if dy * heading[1] > 0:  # Heading the correct North or South direction
                return 'forward'
            elif dy * heading[1] < 0 and heading[1] < 0: # Heading North, destination South
                if dx < 0: # Destination also to the West
                    return 'left'
                else:
                    return 'right'
            elif dy * heading[1] < 0 and heading[1] > 0: # Heading South, destination North
                if dx > 0: # Destination also to the East
                    return 'left'
                else:
                    return 'right'
            elif dy * heading[0] > 0: # Heading West destination North; Heading East destination South
                return 'right'
            else:
                return 'left'


#the code from  if dx == 0 and dy == 0:return None,tells how the agent should reach its
#destination based on the co-ordinates of location and destination