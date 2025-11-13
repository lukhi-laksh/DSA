import pandas as pd

def account_summary(users: pd.DataFrame, transactions: pd.DataFrame) -> pd.DataFrame:
    total = transactions.groupby('account')['amount'].sum().reset_index()
    result = total.merge(users,on='account')[['name','amount']]
    return result[result['amount']>10000].rename(columns={'amount':'balance'})