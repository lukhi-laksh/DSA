import pandas as pd

def last_passenger(queue: pd.DataFrame) -> pd.DataFrame:
    df = queue.sort_values(by = 'turn')
    df['total_weight'] = df['weight'].cumsum()
    df = df[df['total_weight'] <= 1000]
    df['rank'] = df['total_weight'].rank(method = 'dense',ascending = False)
    return df[df['rank'] == 1][['person_name']]