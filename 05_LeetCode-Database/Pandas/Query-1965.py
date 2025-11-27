import pandas as pd

def find_employees(employees: pd.DataFrame, salaries: pd.DataFrame) -> pd.DataFrame:
    new_df = pd.concat([employees,salaries],axis=0)
    new_df1  = new_df.groupby('employee_id').count().reset_index()
    result_df = new_df1[(new_df1['name']==0)|(new_df1['salary']==0)]
    result_df = result_df.drop(columns = ["name",'salary'])
    return result_df
        