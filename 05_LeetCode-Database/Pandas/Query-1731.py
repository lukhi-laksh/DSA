import pandas as pd

def count_employees(employees: pd.DataFrame) -> pd.DataFrame:
    df = employees.groupby('reports_to').agg(
        reports_count = ('employee_id','count'),
        average_age = ('age',lambda x:x.mean() + 1e-9)
    ).reset_index()
    result = df.merge(employees, how = 'inner',left_on = 'reports_to',right_on = 'employee_id')\
    [['reports_to_x','name','reports_count','average_age']].rename(columns = {'reports_to_x':'employee_id'}).round()
    
   
    return result