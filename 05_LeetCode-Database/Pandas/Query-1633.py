import pandas as pd

def users_percentage(users: pd.DataFrame, register: pd.DataFrame) -> pd.DataFrame:
    df= register.groupby('contest_id')['user_id'].count().reset_index(name='total_user')
    total = users.shape[0]
    df['percentage']= ((df['total_user']/total)*100).round(2)
    df=df.sort_values(by=['percentage','contest_id'], ascending= [False, True])
    return df[['contest_id','percentage']]