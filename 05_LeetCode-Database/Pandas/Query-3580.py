import pandas as pd

def find_consistently_improving_employees(employees: pd.DataFrame, performance_reviews: pd.DataFrame) -> pd.DataFrame:
    df = performance_reviews.copy()
    df['review_date'] = pd.to_datetime(df['review_date'])
    df['n'] = df.groupby('employee_id')['review_date'].transform('size')
    df['rnk'] = df.groupby('employee_id')['review_date'].transform(lambda x: x.rank(method='dense', ascending=False))
    mask = (df['n'] >= 3) & (df['rnk'].between(1,3, inclusive='both'))
    df = df.loc[mask]

    df['improvement'] = df.groupby('employee_id')['rating'].transform(lambda x: x.diff().fillna(1))
    mask2 = df.groupby("employee_id")["improvement"].transform(lambda x: (x > 0).all())
    df2 = df.loc[mask2]

    df2['improvement_score'] = df2.groupby('employee_id')['rating'].transform(lambda x: x.iloc[-1]-x.iloc[0])
    out = df2.drop_duplicates(subset=['employee_id'])[['employee_id', 'improvement_score']]
    joined = pd.merge(out, employees, how='left', on='employee_id')
    joined = joined.sort_values(['improvement_score', 'name'], ascending=[False, True])
    joined = joined[['employee_id', 'name', 'improvement_score']]
    return joined