import pandas as pd

def find_polarized_books(books: pd.DataFrame, reading_sessions: pd.DataFrame) -> pd.DataFrame:
    merge_result = books.merge(reading_sessions, how='outer', on='book_id')
    total_group = merge_result.groupby('book_id')['session_id'].agg(['count']).reset_index()
    total_group.rename(columns={'count': 'total_ses_count'}, inplace=True)

    merge_result = merge_result.merge(total_group, how='left', on='book_id')
    merge_result = merge_result.loc[merge_result.total_ses_count >= 5]

    resulta = merge_result.loc[merge_result.session_rating.isin([1, 2])][['book_id', 'session_rating']]
    resultb = merge_result.loc[merge_result.session_rating.isin([4, 5])][['book_id', 'session_rating']]
    result1 = pd.merge(resulta, resultb, on='book_id', how='outer')
    result1 = result1.loc[result1.session_rating_x.notnull() & result1.session_rating_y.notnull()][['book_id']]
    result1 = result1.drop_duplicates(subset=['book_id'])
    result1 = pd.merge(result1, merge_result, on='book_id', how='left')

    result_ = result1[result1['session_rating'] != 3]
    result_ = result_.groupby('book_id')['session_id'].agg(['count']).reset_index()
    result_.rename(columns={'count': 'polarized_sessions'}, inplace=True)
    result1 = pd.merge(result1, result_, on='book_id', how='left')

    group_result = result1.groupby('book_id')['session_rating'].agg(['max', 'min']).reset_index()
    group_result['rating_spread'] = group_result['max'] - group_result['min']
    group_result = group_result.drop(['min', 'max'], axis=1)
    result2 = result1.merge(group_result, how='left', on='book_id')

    result2['polarization_score'] = ((result2['polarized_sessions'] / result2['total_ses_count']) + 0.0001)
    result2['polarization_score'] =  result2['polarization_score'].round(2)
    result2 = result2.loc[result2.polarization_score >= 0.6]
    result2 = result2.drop_duplicates(subset=['book_id'])

    return result2[['book_id', 'title', 'author', 'genre', 'pages', 'rating_spread', 'polarization_score']].sort_values(by=['polarization_score', 'title'], ascending=[False, False])