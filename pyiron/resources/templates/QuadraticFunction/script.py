import numpy as np
from pyiron_base import load, dump

#assuming stress/strain data

class QuadraticFunction():
    def __init__(self):
        """
                Simple test to compute the output of a quadratic
                function f = a*x²+b*x+c

                Input
                ----------
                inp : Input library
                        inp['x'] positions, at which the function is to be
                        evaluated
        """
        pass

    def __call__(self, inp):
        """
                Input
                ----------
                inp : Input library
                        inp['a'] coefficient a
                        inp['b'] coefficient b
                        inp['c'] coefficient c
                        inp['x'] the positions the function is evaluated at

                Output
                ----------
                response: Output library
                            response['f'] a float with the result a*x²+b*x+c

        """
        response = {'f':
                        inp['a'] * np.multiply(inp['x'], inp['x']) +
                        inp['a'] * inp['x'] +
                        np.full_like(inp['x'], inp['c'])
                    }
        #print("response", response)
        return response


#generate simulation object
function = QuadraticFunction()

# set input
input = load()

# run the model
model_answer = function(input)

dump(model_answer)

