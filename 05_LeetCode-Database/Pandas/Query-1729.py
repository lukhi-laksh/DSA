import pandas as pd

def count_followers(followers: pd.DataFrame) -> pd.DataFrame:
    # df = followers.groupby('user_id', as_index=False).agg({'follower_id':'count'}).reset_index()
    df = followers.groupby('user_id', as_index=False).count()
    print(df)
    df['followers_count'] = df['follower_id']
    return df[['user_id','followers_count']]
    