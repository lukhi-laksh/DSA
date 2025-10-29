import pandas as pd

def project_employees_i(project: pd.DataFrame, employee: pd.DataFrame) -> pd.DataFrame:
    df=pd.merge(project,employee,left_on="employee_id",right_on="employee_id",how="left")
    df=df.groupby("project_id")["experience_years"].mean().reset_index().round(2)
    df=pd.DataFrame(df)
    df=df.rename(columns={"experience_years":"average_years"})
    return df