import random
from os import system
from time import sleep

grid = [["#"] * 4 for i in range(4) ]
letters_dict = {"A": 0, "B" : 1, "C" : 2, "D" : 3}
special_symbols = ["!","@","№","$","%","₴","&","?"]
grid_symbols = [["0"] * 4 for i in range(4)]

def valid_input(value : str):
    letters = ["A","B","C","D"]
    while True:
        value = value.upper()
        if value[0] in letters and value[1].isdecimal() and (0 < int(value[1]) < 5) and len(value) == 2:
            return [letters_dict[value[0]],int(value[1]) - 1]
        else:
            print("Sorry you have entered an inappropriate value! It should look like this (A1),(b2). ")
            value = input("Please, enter coordinate: ")

for i in special_symbols:
    counter = 0
    while counter != 2:
        cord1 = random.randint(0, 3)
        cord2 = random.randint(0, 3)
        if grid_symbols[cord1][cord2] == "0":
            grid_symbols[cord1][cord2] = i
            counter +=1

def grid_output():
    l = ["A","B","C","D"]
    print(" ", "1", "2", "3", "4")
    for i in range(len(grid)):
        print(l[i], *grid[i])

#print(grid_symbols) cheat for win game faster

steps = 0

print("Concentration is a round game in which all of the cards are laid face down on a surface and two cards are flipped face up over each turn. The object of the game is to turn over pairs of matching cards.")

while "#" in grid[0] or "#" in grid[1] or "#"  in grid[2] or "#" in grid[3] :
    grid_output()
    int_cord1 = valid_input(input("Please, enter coordinate: "))
    steps +=1
    system("clear")
    grid[int_cord1[0]][int_cord1[1]]= grid_symbols[int_cord1[0]][int_cord1[1]]
    grid_output()

    int_cord2 = valid_input(input("Please, enter coordinate: "))
    steps += 1
    system("clear")
    grid[int_cord2[0]][int_cord2[1]] = grid_symbols[int_cord2[0]][int_cord2[1]]
    grid_output()

    if int_cord1 == int_cord2:
        print("You have entered the same coordinate")
        sleep(2)
        system("clear")
        grid[int_cord1[0]][int_cord1[1]] = "#"
        continue

    for i in range(3,0,-1):
        print(i)
        sleep(1)
    system("clear")

    if grid_symbols[int_cord1[0]][int_cord1[1]] == grid_symbols[int_cord2[0]][int_cord2[1]]:
        grid[int_cord1[0]][int_cord1[1]] = grid_symbols[int_cord1[0]][int_cord1[1]]
        grid[int_cord2[0]][int_cord2[1]] = grid_symbols[int_cord2[0]][int_cord2[1]]
    else:
        grid[int_cord1[0]][int_cord1[1]] = "#"
        grid[int_cord2[0]][int_cord2[1]] = "#"

print(f"Congratulations!!! You won!!! You accomplished this task in {steps} steps.")
