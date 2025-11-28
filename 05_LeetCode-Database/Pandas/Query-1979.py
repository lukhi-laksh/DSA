import pandas as pd

def find_employees(employees: pd.DataFrame) -> pd.DataFrame:

    return (employees.dropna()
                     .loc[employees.salary < 30_000]
                     .loc[~employees.manager_id.isin(
                                        employees.employee_id)]
                     .iloc[:,[0]].sort_values('employee_id'))