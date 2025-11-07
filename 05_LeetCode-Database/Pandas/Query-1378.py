import pandas as pd

def replace_employee_id(employees: pd.DataFrame, 
                        employee_uni: pd.DataFrame) -> pd.DataFrame:

    return employees.merge(employee_uni, how = 'left').iloc[:,[2, 1]]