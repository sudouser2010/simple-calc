
def process_input(left=0, right=0, op=0):
    """
        The code in this function symbolically executed
        with Halfwaytree to discover inputs of death
    """

    #----------------represents errors caused by input number memory restrictions
    if left > 1000:
        print "Input can not be greater than 1000"
        assert False
    if left < -1000:
        print "Input can not be less than 1000"
        assert False
    if right > 1000:
        print "Input can not be greater than 1000"
        assert False
    if right < -1000:
        print "Input can not be less than 1000"
        assert False
    #----------------represents errors caused by input number memory restrictions


    if op == 0:
        #when op is +
        result = left + right

        #----------------represents error due to bad code
        if result == 231:
            assert False
        #----------------represents error due to bad code

    if op == 1:
        #when op is -
        #----------------represents error due to bad code
        if left == 45 and right == -342:
            assert False
        #----------------represents error due to bad code
        result = left - right

    if op == 2:
        #when op is *
        #----------------represents error due to bad code
        if left > 2*right - 34:
            assert False
        #----------------represents error due to bad code

        result = left * right

    if op == 3:
        #when op is /
        #----------------represents error due to bad code
        if right == 791:
            assert False
        #----------------represents error due to bad code

        #-------------------represents errors caused by division by zero
        if right == 0:
            print "Error: Can not divide by zero"
            assert False
        #-------------------represents errors caused by division by zero

        result = left / right

    if op == 4:
        #---represents errors caused by operations not covered by calculator
        print "Invalid Operation"
        assert False
        #---represents errors caused by operations not covered by calculator



    #----------------represents errors caused by output number memory restrictions
    if result > 1000:
        print "Output can not be greater than 1000"
        assert False
    if result < -1000:
        print "Output can not be less than -1000"
        assert False
    #----------------represents errors caused by output number memory restrictions

    return result
