
def process_input(left=0, right=0, op=0):
    """
        The code in this function symbolically executed
        with Halfwaytree to discover inputs of death
    """

    if op == 0:
        #when op is +
        result = left + right

    elif op == 1:
        #when op is -
        result = left - right

    elif op == 2:
        #when op is *
        result = left * right

    elif op == 3:
        #when op is /
        result = left / right

    else:
        #when op is neither
        assert False

    return result
