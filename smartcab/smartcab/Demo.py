import random
import math
import matplotlib.pyplot as plt
from collections import OrderedDict

from environment import Agent,Environment
from planner import RoutePlanner
from simulator import Simulator


class LearningAgent(Agent):
    """ An agent that learns to drive in the Smartcab world.
        This is the object you will be modifying. """

    def __init__(self,env,learning = False,epsilon = 1.0,alpha = 0.5):
        super(LearningAgent,self).__init__(env)
        self.planner = RoutePlanner(self.env,self)
        self.valid_actions = self.env.valid_actions

        self.learning = learning
        self.Q = dict()
        self.epsilon = epsilon
        self.alpha = alpha

        self.t = 0

    def reset(self,destination = None,testing = False):
        """ The reset function is called at the beginning of each trial.
            'testing' is set to True if testing trials are being used
            once training trials have completed. """

        self.planner.route_to(destination)

        ###########
        # Update epsilon using a decay function of your choice
        # Update additional class parameters as needed
        # If 'testing' is True, set epsilon and alpha to 0

        if testing:
            self.epsilon = 0.0
            self.alpha = 0.0

        else:
            self.t += 1.0
            self.epsilon = math.fabs(math.cos(self.alpha*self.t))

        return None
    

    def build_state(self):
        """The build_state function is called when the agent requests data from the
            environment. The next waypoint, the intersection inputs, and the deadline
            are all features available to the agent."""

        #Collect the data about the environment
        waypoint = self.planner.next_waypoint()
        inputs = self.env.sense(self)
        deadline = self.env.get_deadline(self)

        def xstr(s):
            if s is None:
                return None
            else:
                return str(s)
        state = xstr(waypoint) + "_" + inputs['light'] + "_" + xstr(inputs['left']) + "_" + xstr(inputs['oncoming'])

        if self.learning:
            self.Q[state] = self.Q.get(state,{None:0.0,'forward':0.0,'left':0.0,'right':0.0})
        return state


    def get_maxQ(self,state):
        maxQ = -1000.0
        for action in self.Q[state]:
            if maxQ < self.Q[state][action]:
                maxQ = self.Q[state][action]
        return maxQ


    def createQ(self,state):
        if self.learning:
            self.Q[state] = self.Q.get(state,{None:0.0,'forward':0.0,'left':0.0,'right':0.0})

        return

    def action(self,state):
        self.state = state
        self.next_waypoint = self.planner.next_waypoint()
        action = None

        if not self.learning:
            action = random.choice(self.valid_actions)

        else:
            if self.epsilon >0.01 and self.epsilon > random.radnom():
                action = random.choice(self.valid_actions)

            else:
                valid_actions = []
                maxQ = self.get_maxQ(state)
                for action in self.Q[state]:
                    if maxQ == self.Q[state][action]:
                        valid_actions.append(action)
                action = random.choice(valid_actions)

            return action


    def learn(self,state,action,reward):
        if self.learning:
            self.Q[state][action] = self.Q[state][action] + self.alpha * (reward - self.Q[state][action])

        return

    def update(self):
        state = self.build_state()
        self.createQ()
        action = self.choose_action(state)
        reward = self.env.act(self,action)
        self.learn(state,action,reward)

        return

def run():
    env = Environment(verbose=True,num_dummies= 1000,grid_size= (12,12))

    agent = env.create_agent(LearningAgent,learning = True,epsilon = 1.0,alpha = 0.01)

    env.set_priamry_agent(agent,enforce_deadline = True)

    sim = Simulator(env,update_delay=0.01,log_metrics=True,optimized=True)

    sim.run(n_test = 50,tolerance=0.001)

    if __name__ == '__main__':
        run()






