from tools.species_lookup import find_animal
from tools.formatter import format_animal

print("Welcome to the COTW Animal Lookup Tool!")
print("Type an animal name or nickname. Type 'exit' to quit.\n")

while True:
    user_input = input("Enter animal name: ").strip()
    if user_input.lower() == "exit":
        break

    name, data = find_animal(user_input)
    if data:
        print("\n" + format_animal(name, data) + "\n")
    else:
        print(f"I couldn’t find a species matching '{user_input}'. Please try again.\n")
