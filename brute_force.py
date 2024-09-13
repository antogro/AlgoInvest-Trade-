from itertools import combinations
import data
from dataclasses import dataclass
from typing import List
from usefull_package import Action



@dataclass
class Client:
    name: str
    somme_total_action: float = 500
    actions_achetees: List[Action] = None

    @property
    def control_somme_max(self) -> bool:
        if self.somme_total_action > 500:
            print("Solde maximum dépassé")
            return False
        return True


class Application:
    def __init__(self) -> None:
        self.actions: List[Action] = []
        self.clients: List[Client] = [Client("Client1")]

    def calcul_benefice(self) -> None:
        self.actions = Action.from_dict(data.actions)
        
        for action in self.actions:
            action.calcule_benefice()

        for client in self.clients:
            if client.control_somme_max:
                print(
                    f"\nLe client {client.name} peut "
                    "acheter les combinaisons suivantes:"
                )
                self.meilleure_combinaison(client, self.actions)

    def meilleure_combinaison(self,
                              client: Client,
                              actions: List[Action]) -> None:
        max_benefice = 0
        meilleure_combinaison = []

        for r in range(1, len(actions) + 1):
            for combinaison in combinations(actions, r):
                cout_total = sum(action.cost for action in combinaison)
                if cout_total <= client.somme_total_action:
                    benefice_total = sum(
                        action.benefite for action in combinaison
                    )
                    if benefice_total > max_benefice:
                        max_benefice = benefice_total
                        meilleure_combinaison = combinaison

        if meilleure_combinaison:
            print(f"Meilleure combinaison pour {client.name} :")
            cout_total = sum(action.cost for
                             action in meilleure_combinaison)
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
    app = Application()
    app.calcul_benefice()


if __name__ == "__main__":
    main()
