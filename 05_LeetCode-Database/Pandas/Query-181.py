"""
Combine Two Tables

"""

import pandas as pd

def find_employees(employee: pd.DataFrame) -> pd.DataFrame:
    result_df = employee[employee['salary'] > employee['managerId'].map(employee.set_index('id')['salary'])]
    result_df = result_df[['name']].rename(columns={'name': 'Employee'})
    return result_df
    