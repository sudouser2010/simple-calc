
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
        result = left / right

    if op == 4:
        #when op is not operation covered by calculator
        assert False

    return result
