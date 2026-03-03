import json
import os

FILE_PATH = os.path.join("data", "finances.json")

# ---------------------------------------------------------
# Chargement / Sauvegarde JSON
# ---------------------------------------------------------
def load_data():
    if not os.path.exists(FILE_PATH):
        return {}
    with open(FILE_PATH, "r") as file:
        return json.load(file)

def save_data(data):
    os.makedirs("data", exist_ok=True)
    with open(FILE_PATH, "w") as file:
        json.dump(data, file, indent=4)

# ---------------------------------------------------------
# Flux simple : revenu → dépenses → résumé
# ---------------------------------------------------------
def run_simple_flow():
    print("\n=== Suivi financier mensuel ===")

    # 1. Revenu
    income = float(input("Entrez votre revenu mensuel : "))

    # 2. Dépenses par catégorie
    categories = ["rent", "food", "utilities", "leisure"]
    expenses = {}

    print("\nEntrez vos dépenses pour chaque catégorie :")
    for cat in categories:
        amount = float(input(f" - {cat} : "))
        expenses[cat] = amount

    # 3. Calculs
    total_expenses = sum(expenses.values())
    savings = income - total_expenses

    # 4. Résumé
    print("\n=== Résumé financier ===")
    print(f"Revenu total : {income:.2f} €")
    print(f"Dépenses totales : {total_expenses:.2f} €")
    print(f"Économies : {savings:.2f} €")

    # 5. Sauvegarde JSON
    data = {
        "income": income,
        "expenses": expenses,
        "total_expenses": total_expenses,
        "savings": savings
    }

    save_data(data)
    print("\nDonnées sauvegardées dans finances.json.")

# ---------------------------------------------------------
# Lancement
# ---------------------------------------------------------
if __name__ == "__main__":
    run_simple_flow()