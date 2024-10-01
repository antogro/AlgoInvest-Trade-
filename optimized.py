from dataclasses import dataclass
from action_object import Action
import argparse


class Application:
    """Application class to  handle the application's functionality:
    calculate, sorted, and find the best combinaison to a set of action"""

    def __init__(self):
        self.action: List[Action] = []

    def sorted_ratio(self, file_name) -> list[Action]:
        dict_action = Action.parse_csv(file_name)
        self.action = Action.from_dict(
            [
                {"action": data.action, "cost": data.cost, "percent": data.percent}
                for data in dict_action
            ]
        )

        for action in self.action:
            action.calcule_benefice

    def greedy_algo(self, budget):
        sorted_action = sorted(
            self.action, key=lambda action: action.percent, reverse=True
        )

        total_benefite = 0.0
        total_cost = 0.0
        selected_action = []

        for action in sorted_action:
            if total_cost + action.cost <= budget:
                selected_action.append(action)
                total_cost += action.cost
                total_benefite += action.benefite
        return total_cost, total_benefite, selected_action


def main():
    parser = argparse.ArgumentParser(
        description="Algorithme glouton pour maximiser le "
        "benefice lors d'achat d'action"
    )
    parser.add_argument(
        "file_name",
        type=str,
        help="Chemin d'accés vers le fichier CSV contenant les actions à analyser",
    )
    parser.add_argument(
        "budget", type=int, help="budget maximal pour la selection des actions"
    )

    args = parser.parse_args()

    app = Application()
    app.sorted_ratio(args.file_name)
    total_cost, total_benefite, selected_action = app.greedy_algo(args.budget)
    if total_cost < args.budget:
        for action in selected_action:
            print(
                f"Action : {action.action}, coût : {action.cost:.2f}"
                f", bénéfice : {action.benefite:.2f}"
            )
        print(f"Coût total : {total_cost:.2f}")
        print(f"Bénéfice Total: {total_benefite:.2f}")
        print(f"Nombre d'action: {len(selected_action)}")
    else:
        print("Aucune combinaison n'est possible")


if __name__ == "__main__":
    main()
