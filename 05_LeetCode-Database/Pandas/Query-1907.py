import pandas as pd

def count_salary_categories(accounts: pd.DataFrame) -> pd.DataFrame:
    accounts.loc[accounts['income']<20000,'category']='Low Salary'
    accounts.loc[(accounts['income']>=20000) & (accounts['income']<=50000),'category']='Average Salary'
    accounts.loc[(accounts['income']>50000),'category']='High Salary'
    category_df=pd.DataFrame({'category':['High Salary','Low Salary','Average Salary']})
    final=pd.merge(left=category_df,right=accounts,left_on='category',right_on='category',how='left')
    final=final.groupby(['category']).agg(
        accounts_count=('account_id','count')
    ).reset_index()
    return final