
def process_input(left=0, right=0, op=0):
    """
        The code in this function symbolically executed
        with Halfwaytree to discover inputs of death
    """

    if op == 0:
        #when op is +
        result = left + right

    if op == 1:
        #when op is -
        result = left - right

    if op == 2:
        #when op is *

        result = left * right

    if op == 3:
        #when op is /

        #-------------------represents errors caused by division by zero
        if right == 0:
            print "Error: Can not divide by zero"
            assert False
        #-------------------represents errors caused by division by zero

        result = left / right

    return result
