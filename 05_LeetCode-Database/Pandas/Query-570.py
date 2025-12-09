import pandas as pd

def find_managers(employee: pd.DataFrame) -> pd.DataFrame:
    
    count_df = employee['managerId'].value_counts().reset_index()
    
    result = []
    ids = list(employee['id'])
    for idx, i in count_df.iterrows():
        if i['count'] >= 5 and i['managerId'] in ids:
            result.append(employee.loc[employee["id"] == i['managerId'], "name"].iloc[0])
    
    if len(result) > 0:
        return pd.DataFrame(result, columns = ["name"])
    else:
        return pd.DataFrame(columns = ["name"])