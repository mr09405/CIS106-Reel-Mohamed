def displayarrays(lname, scores):
  for i in range(len(lname)):
      print(f"{lname[i]} - Exam Score: {scores[i]}")

def rdisplay(lname, scores):
  for i in reversed(range(len(lname))):
      print(f"{lname[i]} - Exam Score: {scores[i]}")

lname = ["Mohamed", "Patrick", "Addams", "Brown", "White", "Gonzalez", "Hernandez", "James", "Anderson", "Scott"]
scores = [90, 80, 85, 94, 81, 88, 95, 89, 92, 93]

print("Original Order:")
displayarrays(lname, scores)

print("\nReverse Order:")
rdisplay(lname, scores)