import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    employee["rank"] = employee["salary"].rank(method="dense", ascending=False)
    res = employee[employee["rank"] == 2][["salary"]].rename(columns={"salary": "SecondHighestSalary"})
    if res.empty:
        return pd.DataFrame({"SecondHighestSalary":  [None]})
    else:
        res = res.iloc[[0]]
        return res