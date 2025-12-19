import pandas as pd

def monthly_transactions(transactions: pd.DataFrame) -> pd.DataFrame:
    
    df = transactions.copy()

    df['month'] = pd.to_datetime(df['trans_date']).dt.strftime('%Y-%m')

    df = df.groupby(['month', 'country'], dropna = False).apply(lambda x: pd.Series({
        'trans_count' : x['id'].count(), 
        'approved_count' : (x['state'] == 'approved').sum(), 
        'trans_total_amount' : x['amount'].sum(), 
        'approved_total_amount': x.loc[x['state'] == 'approved', 'amount'].sum()
    })).reset_index()
    return df
