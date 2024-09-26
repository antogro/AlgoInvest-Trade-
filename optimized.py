from dataclasses import dataclass
from typing import List
from usefull_package import Action

class Application:
    def __init__(self):
        self.action: List[Action] = []

    def ratio_benefite_cost(self, file_name):
        dict_action = Action.parse_csv(file_name)
        self.action = Action.from_dict([
                {"action": data.action,
                "cost": data.cost,
                "percent": data.percent}
                for data in dict_action ])
        for action in self.action:
            action.calcule_benefice
            action.calcul_ratio



    def greedy_algo(self, budget):
        sorted_action = sorted(
                    self.action,
                    key=lambda action: action.ratio,
                    reverse=True)

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
    budget = 500

    app = Application()
    app.ratio_benefite_cost("data_set\Liste_actions_3.csv")
    total_cost, total_benefite, selected_action = app.greedy_algo(budget)
    if total_cost < budget:
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
