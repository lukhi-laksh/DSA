import pandas as pd

def employee_bonus(employee: pd.DataFrame, bonus: pd.DataFrame) -> pd.DataFrame:
    emp_bonus = employee.merge(bonus, how='left', on='empId')
    result = emp_bonus[(emp_bonus['bonus'] < 1000) | (emp_bonus['bonus'].isnull())]
    return result[['name', 'bonus']]