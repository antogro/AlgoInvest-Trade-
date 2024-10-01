from itertools import combinations
from dataclasses import dataclass
from typing import List
from action_object import Action
import argparse


class Application:

    def __init__(self) -> None:
        self.actions: List[Action] = []

    def calcul_benefice(self, file_name) -> None:
        dict_action = Action.parse_csv(file_name)
        self.actions = Action.from_dict(
            [
                {"action": data.action, "cost": data.cost, "percent": data.percent}
                for data in dict_action
            ]
        )

        for action in self.actions:
            action.calcule_benefice

    def meilleure_combinaison(self, budget) -> None:
        max_benefice = 0
        meilleure_combinaison = []

        for r in range(1, len(self.actions) + 1):
            for combinaison in combinations(self.actions, r):
                cout_total = sum(action.cost for action in combinaison)
                if cout_total <= budget:
                    benefice_total = sum(action.benefite for action in combinaison)
                    if benefice_total > max_benefice:
                        max_benefice = benefice_total
                        meilleure_combinaison = combinaison

        if meilleure_combinaison:
            print(f"Meilleure combinaison :")
            cout_total = sum(action.cost for action in meilleure_combinaison)
            for action in meilleure_combinaison:
                print(
                    f"Action : {action.action}, coût : {action.cost:.2f}"
                    f", bénéfice : {action.benefite:.2f}"
                )
            print(f"Coût total : {cout_total:.2f}")
            print(f"Bénéfice Total: {max_benefice:.2f}")
        else:
            print("Aucune combinaison n'est possible")


def main():
    parser = argparse.ArgumentParser(
        description="Algorithme brute force pour maximiser le "
        "benefice lors d'achat d'action"
    )
    parser.add_argument(
        "file_name",
        type=str,
        help="Chemin d'accés vers le fichier CSV " "contenant les actions à analiser",
    )
    parser.add_argument(
        "budget", type=int, help="budget maximal pour la selection des actions"
    )

    args = parser.parse_args()

    app = Application()
    app.calcul_benefice(args.file_name)
    app.meilleure_combinaison(args.budget)


if __name__ == "__main__":
    main()
