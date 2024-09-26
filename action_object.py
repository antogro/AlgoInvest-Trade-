import csv
from dataclasses import dataclass
from typing import List, Dict


@dataclass
class Action:
    action: str
    cost: float
    percent: float
    benefite: float = 0.0
    ratio: float = 0.0

    @classmethod
    def from_dict(cls, data_dict: Dict[str, tuple]) -> List["Action"]:
        return [
            cls(data["action"], data["cost"], data["percent"]) for data in data_dict 
        ]
    
    @property
    def calcule_benefice(self) -> None:
        self.benefite = self.percent * self.cost

    @property
    def calcul_ratio(self) -> float:
        self.ratio = self.benefite / self.cost

    def parse_csv(file_name: str) -> list["Action"]:
        """Return a list of Action object from a csv file"""
        actions = []
        with open(file_name, newline="") as csv_File:
            reader = csv.reader(csv_File, delimiter=",")
            next(reader)
            for row in reader:
                action, cost, percent = row
                cost = float(cost)
                percent = float(percent.rstrip("%")) / 100
                if cost <= 0.1 or percent <= 0:
                    continue

                action = Action(row[0], cost, percent)
                actions.append(action)

        # return sorted(actions, key=lambda action: action.profit, reverse=True)
        return actions
