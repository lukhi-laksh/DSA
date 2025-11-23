import pandas as pd

def find_primary_department(employee: pd.DataFrame) -> pd.DataFrame:
    y_mask = employee['primary_flag'] == 'Y'
    y_employee = employee.loc[y_mask,['employee_id', 'department_id']]

    df_grouped = employee.groupby('employee_id',as_index=False).agg(count_dep=('department_id','count')).reset_index()
    
    df_filtered = df_grouped.loc[df_grouped['count_dep'] == 1,['employee_id']]

    single_dep = employee.merge(df_filtered, on='employee_id',how='inner')[['employee_id','department_id']]

    result = pd.concat([y_employee,single_dep], ignore_index=True).drop_duplicates()

    return result
