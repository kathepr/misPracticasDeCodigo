line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3]
print("\nHiding your treasure! X marks the spot.")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆
# Write your code below this row 👇

letter = position[0].upper()
letter = ["A","B","C"]
letter_location = letter.index(position[0])
number_location = int(position[1])-1

map[number_location][letter_location] ="X"



# MI PRIMERA SOLUCIÓN
# map = [["A1", "B1", "C1"],["A2", "B2", "C2"],["A3", "B3", "C3"]]

# if position in map[0]:
#   ubicacionLine1 = map[0].index(position)
#   line1[ubicacionLine1]= "X"
# elif position in map[1]:
#   ubicacionLine2 = map[1].index(position)
#   line2[ubicacionLine2] = "X"
# elif position in map[2]:
#   ubicacionLine3 = map[2].index(position)
#   line3[ubicacionLine3] = "X"
  

# Write your code above this row 👆
# 🚨 Don't change the code below 👇

print(f"{line1}\n{line2}\n{line3}")