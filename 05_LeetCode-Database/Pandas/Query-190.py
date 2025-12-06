import pandas as pd

def consecutive_numbers(logs: pd.DataFrame) -> pd.DataFrame:
    arr = [] 
    for i,row in logs.iterrows():
        if i==0:
            count = 1
            last = row['num'] 
            continue 
        if row['num'] == last:
            count += 1
            if count >= 3 and last not in arr:
                arr.append(last)
        else:
            last = row['num']
            count = 1 
    return pd.DataFrame({'ConsecutiveNums': arr})  
    