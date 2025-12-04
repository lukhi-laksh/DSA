import pandas as pd
import numpy as np

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:

    col_name = f"getNthHighestSalary({N})"

    if employee["salary"].nunique() < N or N <= 0:
        return pd.DataFrame({col_name: [np.nan]})

    employee = employee.drop_duplicates(subset = ["salary"]).sort_values(by="salary", ascending = False)

    n_largest = employee.nlargest(N, columns = "salary").iloc[-1, 1]

    return pd.DataFrame({col_name: [n_largest]})