# Purpose of the application is to return the total num of chips needed per color given specific outputs stated below
# Note to Self: Have two functions; one will return total num of chips per color given a set number of chips 
# INPUT: 20 - White, 15 - Red, 12 Green, etc. | the other will return the same but the input will be a given number INPUT: '469'
# 1 - white, 5 - red, 25 - green, 100 - black, 500 - blue

def color_input(whites, reds, greens, blacks, blues):
    chip_total = (1*whites) + (5*reds) + (25*greens) + (100*blacks) + (500*blues)
    print("Total Count: " + str(chip_total))
    print("Number of 500s(Blues) needed: " + str(chip_total//500))
    chip_total = chip_total%500
    print("Number of 100s(Blacks) needed: " + str(chip_total//100))
    chip_total = chip_total%100
    print("Number of 25s(Greens) needed: " + str(chip_total//25))
    chip_total = chip_total%25
    print("Number of 5s(Reds) needed: " + str(chip_total//5))
    chip_total = chip_total%5
    print("Number of 1s(Whites) needed: " + str(chip_total//1))

def num_input(chip_total):
    print("Total Count: " + str(chip_total))
    print("Number of 500s(Blues) needed: " + str(chip_total//500))
    chip_total = chip_total%500
    print("Number of 100s(Blacks) needed: " + str(chip_total//100))
    chip_total = chip_total%100
    print("Number of 25s(Greens) needed: " + str(chip_total//25))
    chip_total = chip_total%25
    print("Number of 5s(Reds) needed: " + str(chip_total//5))
    chip_total = chip_total%5
    print("Number of 1s(Whites) needed: " + str(chip_total//1))

#call the main method
if __name__ == "__main__":
    #Input: #s of whites, #s of reds, #s of green, #s of black, #s of blues
    color_input(12, 20, 3, 6, 3)

    #Input: chip total
    #num_input(2136)