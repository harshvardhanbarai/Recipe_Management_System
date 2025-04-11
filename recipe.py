import csv
import os

CSV_FILE = "recipes.csv"


if not os.path.exists(CSV_FILE):
    with open(CSV_FILE, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Recipe Name", "Ingredients", "Instructions"])  # Header row



def add_recipe():
    name = input("Enter Recipe Name: ")
    ingredients = input("Enter Ingredients (comma-separated): ")
    instructions = input("Enter Cooking Instructions: ")

    with open(CSV_FILE, mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([name, ingredients, instructions])

    print(f"✅ Recipe '{name}' added successfully!")



def view_recipes():
    with open(CSV_FILE, mode="r") as file:
        reader = csv.reader(file)
        recipes = list(reader)

    if len(recipes) <= 1:
        print("📂 No recipes found.")
    else:
        print("\n📜 Recipe List:")
        for i, (name, ingredients, instructions) in enumerate(recipes[1:], start=1):
            print(f"\n🔹 {i}. {name}")
            print(f"   🥕 Ingredients: {ingredients}")
            print(f"   🍳 Instructions: {instructions}")



def update_recipe():
    name = input("Enter Recipe Name to Update: ")
    updated = False
    recipes = []

    with open(CSV_FILE, mode="r") as file:
        reader = csv.reader(file)
        recipes = list(reader)

    for i in range(1, len(recipes)):
        if recipes[i][0].lower() == name.lower():
            print(f"Editing Recipe: {recipes[i][0]}")
            recipes[i][1] = input("Enter New Ingredients (comma-separated): ")
            recipes[i][2] = input("Enter New Instructions: ")
            updated = True

    if updated:
        with open(CSV_FILE, mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(recipes)
        print(f"✅ Recipe '{name}' updated successfully!")
    else:
        print("❌ Recipe not found.")



def delete_recipe():
    name = input("Enter Recipe Name to Delete: ")
    found = False
    recipes = []

    with open(CSV_FILE, mode="r") as file:
        reader = csv.reader(file)
        recipes = list(reader)

    recipes_new = [recipes[0]]  # Keep header row

    for i in range(1, len(recipes)):
        if recipes[i][0].lower() == name.lower():
            found = True
        else:
            recipes_new.append(recipes[i])

    if found:
        with open(CSV_FILE, mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(recipes_new)
        print(f"✅ Recipe '{name}' deleted successfully!")
    else:
        print("❌ Recipe not found.")


def exit_program():
    print("🚪 Exiting program. Goodbye!")
    exit()



operations = {
    "1": add_recipe,
    "2": view_recipes,
    "3": update_recipe,
    "4": delete_recipe,
    "5": exit_program
}


while True:
    print("\n🍽️ Recipe Organizer")
    print("1. Add Recipe")
    print("2. View Recipes")
    print("3. Update Recipe")
    print("4. Delete Recipe")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice in operations:
        operations[choice]()
    else:
        print("❌ Invalid choice. Please try again.")
