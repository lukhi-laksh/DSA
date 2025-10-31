import pandas as pd

def user_activity(activity: pd.DataFrame) -> pd.DataFrame:
    # a period of 30 days ending 2019-07-27 inclusively
    endD = pd.to_datetime('2019-07-27')
    startD = endD - pd.DateOffset(days=29)

    # find unique users made at least one activity on that day
    active = activity.groupby('activity_date')['user_id'].nunique().reset_index()
    
    # active in the period
    result = active[active['activity_date'].isin(pd.date_range(startD, endD))].rename(columns={'activity_date':'day', 'user_id':'active_users'})
    return result