import json
import os

# Couleurs ANSI
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
RESET = "\033[0m"
BOLD = "\033[1m"

FILE_PATH = os.path.join("data", "finances.json")

def load_data():
    if not os.path.exists(FILE_PATH):
        return {}
    with open(FILE_PATH, "r") as file:
        return json.load(file)

def save_data(data):
    os.makedirs("data", exist_ok=True)
    with open(FILE_PATH, "w") as file:
        json.dump(data, file, indent=4)

def banner():
    print(CYAN + BOLD)
    print("╔══════════════════════════════════════╗")
    print("║      💸  BUDGET APP  💸             ║")
    print("╚══════════════════════════════════════╝")
    print(RESET)

def run_simple_flow():
    banner()

    print(YELLOW + "✨ Bienvenue dans votre suivi financier mensuel ✨" + RESET)

    # 1. Revenu
    income = float(input("\n💰 Entrez votre revenu mensuel : "))

    # 2. Dépenses
    categories = {
        "rent": "🏠 Loyer",
        "food": "🍽️ Nourriture",
        "utilities": "💡 Factures",
        "leisure": "🎮 Loisirs"
    }

    expenses = {}

    print("\n📂 Entrez vos dépenses pour chaque catégorie :")
    for key, label in categories.items():
        amount = float(input(f" - {label} : "))
        expenses[key] = amount

    # 3. Calculs
    total_expenses = sum(expenses.values())
    savings = income - total_expenses

    # 4. Résumé stylé
    print("\n" + CYAN + BOLD + "📊 RÉSUMÉ FINANCIER" + RESET)
    print("──────────────────────────────────────────")

    print(f"💵 Revenu total     : {GREEN}{income:.2f} €{RESET}")
    print(f"🧾 Dépenses totales : {RED}{total_expenses:.2f} €{RESET}")

    if savings >= 0:
        print(f"🎉 Économies        : {GREEN}{savings:.2f} €{RESET}")
    else:
        print(f"⚠️ Solde négatif    : {RED}{savings:.2f} €{RESET}")

    print("──────────────────────────────────────────")

    # 5. Sauvegarde
    data = {
        "income": income,
        "expenses": expenses,
        "total_expenses": total_expenses,
        "savings": savings
    }

    save_data(data)
    print("\n💾 Données sauvegardées dans finances.json.\n")

if __name__ == "__main__":
    run_simple_flow()