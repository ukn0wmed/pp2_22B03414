def solve(numheads, numlegs):
    for chickens in range(numheads + 1):
        rabbits = numheads - chickens
        if 2 * chickens + 4 * rabbits == numlegs:
            return (chickens, rabbits)
    return (None, None)

(chickens, rabbits) = solve(35, 94)
if chickens is not None and rabbits is not None:
    print("There are", chickens, "chickens and", rabbits, "rabbits in the farm.")
else:
    print("There is no solution to the puzzle.")