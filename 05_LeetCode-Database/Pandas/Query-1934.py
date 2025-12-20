import pandas as pd

def confirmation_rate(signups: pd.DataFrame, confirmations: pd.DataFrame) -> pd.DataFrame:
    

    confirmations['conf']=np.where(confirmations['action']=='confirmed',1,0)
    
    df=(confirmations.groupby('user_id').agg({'conf':'sum','action':'count'}).reset_index())
   
    df['confirmation_rate']=((df['conf']/df['action'])*1.00).round(2)
    print(df)

    df2 = pd.merge(signups,df,how='left',on='user_id').fillna(0.0)
    print(df2)
    return df2[['user_id','confirmation_rate']]
