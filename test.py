# Write code below 💖
Gryffindor = 0
Ravenclaw = 0
Hufflepuff = 0
Slytherin = 0
print("F.1) Magst du 1.Dawn oder 2.Dusk?")
print("1) Dawn")
print("2) Dusk")
question_one = int(input("Eingabe:")) 
if question_one == 1:
  Gryffindor += 1  
  Ravenclaw += 1
elif question_one == 2:
  Hufflepuff += 1  
  Slytherin += 1
else:
  print("falscher Eintrag! (1 oder 2)")

print("Wenn ich tot bin, möchte ich das ich als ... erinnert werde")
print("1) der Gute")
print("2) der Großartige")
print("3) der Weise")
print("4) der Mutige")
question_two = int(input("Eingabe:"))
if question_two == 1:
  Hufflepuff += 2
elif question_two == 2:
  Slytherin += 2
elif question_two == 3:
  Ravenclaw += 2
elif question_two == 4:
  Gryffindor += 2
else:
  print("falscher Eintrag! (1,2,3 oder 4)")

print("Welches Instrument klingt am besten?")
print("1) Violine")
print("2) Trompete")
print("3) Piano")
print("4) Trommel")
question_three = int(input("Eingabe:"))
if question_three == 1:
  Slytherin += 4
elif question_three == 2:
  Hufflepuff += 4
elif question_three == 3:
  Ravenclaw += 4
elif question_three == 4:
  Gryffindor += 4
else:
  print("falscher Eintrag! (1,2,3 oder 4)")

print("🦁 Gryffindor", Gryffindor)
print("🦅 Ravenclaw", Ravenclaw )
print("🦡 Hufflepuff", Hufflepuff)
print("🐍 Slytherin", Slytherin)