# -*- coding: utf-8 -*-
"""
Created on Sat Feb 12 14:33:45 2022

@author: jindo
"""

import copy
import random
# Consider using the modules imported above.


class Hat:
    def __init__(self, **ballsin):
        ''' 
        Initialise a bag of balls with an amount of balls in 
        
        Args:
            self (str): Defined by the intialisation.

            ballsin (dict {str : int}): defines the number of balls in the bag
            str defining the colour or type and int defining the quantity.
        
        Returns:
            None
        '''
        self.contents = []
        # Create a number of instances/copy in a list equal to the values for 
        # each key
        balls = ballsin.items()
        for ball_quantity in balls:
            ball = ball_quantity[0]
            quantity = int(ball_quantity[1])
            instance = 0
            while instance < quantity:
                self.contents.append(ball)
                instance += 1
        self.drawn = {}
        self.drawn_list = []   

    def draw(self, no_of_balls):
        ''' 
        Creates a list of balls drawn randomly without replacement, reducing 
        the contents of the intial bag 
        
        Args:
            self (str): Defined by the intialisation.

            no_of_balls (int): defines the number of balls to be drawn.
        
        Returns:
            list: A list of the balls drawn
        '''
        quantity = len(self.contents)
        # Establish whether random drawing is nessecary 
        if no_of_balls >= quantity:
            for ball in self.contents:
                # Cycle through the balls and add them to a dict and a list 
                self.drawn[ball] = self.drawn.get(ball, 0) + 1
                self.drawn_list.append(ball)
            # Clear the contents of the first bag as all balls are drawn
            self.contents.clear()
        else:
            # Intialise a counter
            no_of_balls_drawn= 0
            while no_of_balls_drawn< no_of_balls:
                quantity = len(self.contents)
                # select a ball (list position) randomly
                random_ball = random.randint(0, quantity - 1)
                ball = self.contents[random_ball]
                # Add the ball to a dict and a list
                self.drawn[ball] = self.drawn.get(ball, 0) + 1
                self.drawn_list.append(ball)
                # Remove the ball to emulate drawing without replacement
                self.contents.remove(ball)
                no_of_balls_drawn+= 1
        return self.drawn_list


def experiment(**args):
    ''' 
    Approximates the probability that a set of balls are drawn from the hat by
    carring out a large number of experiments. Accuracy increases with 
    experiment count.
    
    Args:
        hat (hat): the intial hat to draw from
        
        expected_balls (dict): the exact group of balls to attempt to draw from
        the hat for the experiment
        
        num_balls_drawn (int): The number of balls to draw out of the hat in 
        each experiment.
        
        num_experiments(int): The number of experiments to perform. 
    
    Returns:
        flaot: The probability that the expected balls are drawn from the hat. 
    '''
    hat = args.get('hat')
    expected_balls = args.get('expected_balls')
    num_balls_drawn = args.get('num_balls_drawn')
    num_experiments = args.get('num_experiments')

    # Cycle through the expected balls and add them to a dict and a list 
    dictofballs = expected_balls.items()
    expected = []
    for ball_quantity in dictofballs:
        ball = ball_quantity[0]
        quantity = int(ball_quantity[1])
        instance = 0
        while instance < quantity:
            expected.append(ball)
            instance += 1

    # Intialise the counter of a successful draw    
    achieved = 0

    # Cycle through the experiments
    for experiment in range(0, num_experiments):
        # Create a copy of the hat which we can draw from and reduce repeating 
        # the process for each experiment
        pool = copy.deepcopy(hat)
        
        # Carry out the experiment
        actual = pool.draw(num_balls_drawn)
        
        # Check if all the balls expected were actually drawn by trying to 
        # remove them from the drawn balls. If an exception is thrown, a ball
        # that exists in the expected pool does not exist in the drawn pool.
        check = True
        for ball in expected:
            try:
                actual.remove(ball)
            except:
                check = False
        # add to the counter if the experiment was a success
        if check:
            achieved += 1
    # divide the number of successes over the total to get the probability
    return achieved/num_experiments


hat = Hat(blue=4, red=2, green=6)
probability = experiment(hat=hat,
                         expected_balls={"blue": 0, "red": 2},
                         num_balls_drawn=2,
                         num_experiments=300000)
print("Probability:", probability)



random.seed(95)
hat = Hat(blue=4, red=2, green=6)
probability = experiment(
    hat=hat,
    expected_balls={"blue": 2,
                    "red": 1},
    num_balls_drawn=4,
    num_experiments=3000)
print("Probability:", probability)
