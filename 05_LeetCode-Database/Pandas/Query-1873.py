import pandas as pd

def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
    employees['bonus'] = employees[(~employees['name'].str.lower().str.startswith('m')) & (employees['employee_id']%2==1)]['salary']
    return employees.fillna(0)[['employee_id', 'bonus']].sort_values(by='employee_id', ascending = True)