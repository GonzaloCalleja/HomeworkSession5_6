
print("**********MAZE GAME**********")
print("\nWelcome to the Maze game:\nYou are lost and you must escape to survive"
      "\nYou can only go North, South, East and West."
      "\nTo move you can input a sequence of characters (N, S, E, W), but be careful only one is correct!!\n")

solution = "SSNWES"
direction = ""

moves = 0
lives = 3

while True:

    temp = input("You're in the maze, where do you want to go? (N,S,E,W): ")

    if temp != "N" and temp != "S" and temp != "E" and temp != "W":
        print("Direction invalid")
        continue

    direction = direction + temp
    moves += 1

    if direction.__contains__(solution):
        print("CONGRATS!! You made it outside!! It only took you", moves, "moves!")
        break

    if moves % 10 == 0:
        lives -= 1
        print("Life lost!! You have ", lives, "lives left!")
        continue

    if lives == 0:
        print("You just lost the game!!")
        break
