import pandas as pd

def find_investments(insurance: pd.DataFrame) -> pd.DataFrame:

    geo = (
        insurance
        .groupby(['lat','lon'])['pid']
        .nunique()
        .reset_index(name='n_pairs')
    )
    tiv_15 = (
        insurance
        .groupby(['tiv_2015'])['pid']
        .nunique()
        .reset_index(name='n_tiv')
    )
    output = (
        insurance
        .merge(geo,on=['lat','lon'],how = 'left')
        .merge(tiv_15,on=['tiv_2015'],how = 'left')
        .query("n_pairs == 1")
        .query("n_tiv != 1")
        .agg(tiv_2016 = ('tiv_2016','sum'))
        .assign(tiv_2016 = lambda x:x['tiv_2016'].round(2))
    )
    return(output)