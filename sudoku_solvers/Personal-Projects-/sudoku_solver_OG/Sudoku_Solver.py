# Shohum Boker
# 2/19/20

# initializing lists
box0 = [0] * 9
box1 = [0] * 9
box2 = [0] * 9
box3 = [0] * 9
box4 = [0] * 9
box5 = [0] * 9
box6 = [0] * 9
box7 = [0] * 9
box8 = [0] * 9
boxes = [box0, box1, box2, box3, box4, box5, box6, box7, box8]


# Okay function
def okay(b, sq):
    # box test
    bs = [int(s) for s in b]
    for s in b:
        if bs.count(s) > 1 and s != 0: return False
    # Initializing helper lists lists
    rt = []
    ct = []
    for box in boxes:
        tbi = boxes.index(box)
        bi = boxes.index(b)
        if b is box:
            continue
        if tbi % 3 == bi % 3: ct.append(box)  # Column adjacent Boxes
        if tbi // 3 == bi // 3: rt.append(box)  # Row adjacent Boxes
    sqi = b.index(sq)
    ri = [i for i in range(9) if i // 3 == sqi // 3]  # Row helper list
    ci = [i for i in range(9) if i % 3 == sqi % 3]  # Column helper list
    # Using helper lists for column and row test
    for x in range(6):
        y = x // 3
        cb = ct[y]
        rb = rt[y]
        c = ci[x % 3]
        r = ri[x % 3]
        if int(rb[r]) == sq or int(cb[c]) == sq: return False
    return True


# Finding the last integer if the entry goes out of bounds
def lastInt(b, ind):
    ind -= 1
    while isinstance(b[ind], str) or ind < 0:
        if ind < 0:
            b = boxes[boxes.index(b) - 1]
            ind = 8
        if isinstance(b[ind], str):
            ind -= 1
    return [b, ind]


def printr():
    # Checking if the board was Solvable
    for box in boxes:
        for s in box:
            if s ==0:
                print("----------------------------------")
                print("Unsolvable")
                quit()
    # Helper list
    row = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
    s = "----------------------"
    for x in range(81):
        # Every row has nine entries
        if x % 9 == 0:
            s += "\n"
        # Complex formula taking advantage of the helper list to convert boxes into rows
        s += str(boxes[row[x // 27][(x // 3) % 3]][row[(x // 9) % 3][x % 3]])
    print(s)

# Instructions for the user to operate the UI system (hopefully in the future the UI will be better)
print("Welcome to Sudoku Solver:")
print("Enter the rows in your Sudoku Board from the top to the bottom and all blank entries should be'0'")
print("For example: 104005007 is a valid row")
row = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
x = 0
boo = False
while x < 9:
    n = input("row" + str(x + 1) + ": ")
    # Check for proper length
    while len(n) != 9:
        print("Error: Row is not of size 9")
        n = input("row" + str(x + 1) + ": ")
    for y in range(9):
        if boo:
            boo = False
            break
        try:
            # Check for proper data type and have all values as ints
            bs = [int(s) for s in n]
        except ValueError:
            print("Error: Invalid input, characters are not acceptable. ")
            # Allows the user to redo the row
            x -= 1
            break
        else:
            # Checks that the row is valid
            for s in bs:
                if bs.count(s) > 1 and s != 0:
                    print("Error: Repeating value found: " + str(s))
                    x -= 1
                    boo = True
                    break
        # Converts all 0's to ints
        if n[y] == "0":
            r = int(n[y])
        else:
            r = n[y]
        # Complex formula to put to rows in the forms of boxes
        boxes[row[x // 3][y // 3]][row[x % 3][y % 3]] = r
    x += 1

# Initializing index of "boxes"
q = -1
while True:
    # Moving to the next box
    q += 1
    # If all boxes are filled print
    if q == 9:
        printr()
        break
    else:
        box = boxes[q]
        # Initializing index of "boxes"
        p = -1
        while True:
            # Moving to the next square in the box
            p += 1
            # If all squares are filled up then move on to the next box
            if p == 9:
                break
            else:
                while True:
                    # Checking if the value was entered by the user
                    if isinstance(box[p], str):
                        break
                    else:
                        # Add one to the current value in the square
                        box[p] += 1
                        # If the value is to big: backtrack
                        if box[p] == 10:
                            box[p] = 0
                            cord = lastInt(box, p)
                            box = cord[0]
                            p = cord[1]
                            q = boxes.index(box)
                        # Check if the value in the square is valid in rules of Sudoku at its current index
                        elif okay(box, box[p]):
                            break
