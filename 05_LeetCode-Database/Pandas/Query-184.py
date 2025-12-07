import pandas as pd

def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    df = employee.merge(department, left_on="departmentId", 
                        right_on="id", suffixes=("", "_dept"))
    max_salaries = df.groupby("departmentId")["salary"].max().reset_index()
    df = df.merge(max_salaries, on=["departmentId", "salary"])
    
    return df[["name_dept", "name", "salary"]].rename(
        columns={"name_dept": "Department", "name": "Employee", "salary": "Salary"}
    )