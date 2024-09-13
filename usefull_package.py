import csv
from dataclasses import dataclass
from typing import List, Dict


@dataclass
class Action:
    action: str
    cost: float
    pourcent: float
    benefite: float = 0

    @classmethod
    def from_dict(cls, data_dict: Dict[str, tuple]) -> List["Action"]:
        return [
            cls(action, cout, benefice)
            for action, (benefice, cout) in data_dict.items()
            
        ]

    def calcule_benefice(self) -> None:
        self.benefice_en_euro = self.benefite * self.cost

    def get_actions_objects_from_csv(file_name: str) -> list["Action"]:
        """Return a list of Action object from a csv file"""
        actions = []
        with open(file_name, newline="") as csv_File:
            reader = csv.reader(csv_File, delimiter=",")
            for row in reader:
                cost = float(row[1])
                # percent = float(row[2][0:-1])
                percent = float(row[2])
                if cost <= 0.0 or percent <= 0:
                    continue
                row[1] = cost
                row[2] = percent
                # income = cost * percent / 100
                # row.append(income)

                action = Action(row[0], cost, percent)
                actions.append(action)

        # return sorted(actions, key=lambda action: action.profit, reverse=True)
        return actions