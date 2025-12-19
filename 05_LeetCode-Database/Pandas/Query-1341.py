import pandas as pd

def movie_rating(movies: pd.DataFrame, users: pd.DataFrame, movie_rating: pd.DataFrame) -> pd.DataFrame:
    df1 = movie_rating.groupby('user_id').movie_id.count().reset_index(name='review_count')

    df1 = df1.merge(users, how='left', on='user_id')
    df1 = df1.sort_values(by=['review_count', 'name'], ascending=[False, True])

    df1 = df1.iloc[[0], [2]]
    print(df1)
    
    movie_rating['created_at'] = pd.to_datetime(movie_rating['created_at'])

    df2 = movie_rating[movie_rating['created_at'].dt.strftime('%m-%Y') == '02-2020']
    print(df2)
    df2 = df2.groupby('movie_id').rating.mean().reset_index(name='average_rating')
    print(df2)
    df2 = df2.merge(movies, how='left', on='movie_id')
    df2 = df2.sort_values(by=['average_rating', 'title'], ascending=[False, True])
    
    df2 = df2.iloc[[0], [2]].rename(columns={
        'title' : 'name'
    })
    print(df2)

    return pd.concat([df1, df2]).rename(columns={
        'name' : 'results'
    })