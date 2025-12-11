import pandas as pd

def most_friends(request_accepted: pd.DataFrame) -> pd.DataFrame:
    sent = request_accepted.groupby('requester_id',as_index=False).agg(friends_r=('accepter_id','nunique')).rename(columns={'requester_id':'id'})
    recd = request_accepted.groupby('accepter_id',as_index=False).agg(friends_s=('requester_id','nunique')).rename(columns={'accepter_id':'id'})
    df = sent.merge(recd,how='outer',on='id').fillna(0)
    df['friends']=df['friends_r']+df['friends_s']
    most_friends=df['friends'].max()
    df = df[df['friends']==most_friends]
    return df[['id','friends']].rename(columns={'friends':'num'})