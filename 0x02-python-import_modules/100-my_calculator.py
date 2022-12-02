#!/usr/bin/python3
if __name__ == "__main__":
    """Print the number of and list of arguments."""
    import sys
    from calculator_1.py import add
    from calculator_1.py import sub
    from calculator_1.py import mul
    from calculator_1.py import div
    
    count = len(sys.argv) - 1
    if count != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
	exit(1)
    else:
        a = int(sys.argv[1])
	b = int(sys.argv[3])
	result = 0
	opp = sys.argv[2]
	opps = "+-*/"
	if opp == "+":
	    result = add(a, b)
	elif opp == "-":
	    result = sub(a, b)
	elif opp == "*":
	    result = mul(a, b)
	elif opp == "/":
	    result = div(a, b)
	else:
	    print("Unknown operator. Available operators: +, -, * and /")
	    exit(1)
	if opps.find(opp) != -1
	    print("{} {} {} = {}".format(a, opp, b, result))

