import pandas as pd

def find_churn_risk_customers(subscription_events: pd.DataFrame) -> pd.DataFrame:
    df=subscription_events
    df=df.groupby('user_id').agg(
        check_active=('event_type','last'),
        current_plan=('plan_name','last'),
        count_down=('event_type',lambda x: (x=='downgrade').sum()),
        current_monthly_amount=('monthly_amount','last'),
        max_historical_amount=('monthly_amount','max'),
        first=('event_date','first'),
        second=('event_date','last')).reset_index()
    df['ratio']=df['current_monthly_amount']/df['max_historical_amount']
    df['days_as_subscriber']=(pd.to_datetime(df['second'])-pd.to_datetime(df['first'])).dt.days
    df=df[~(df['check_active']=='cancel')]
    df=df[(df['count_down']>0) & (df['ratio']<0.5) & (df['days_as_subscriber']>59)]
    return df[['user_id','current_plan','current_monthly_amount','max_historical_amount','days_as_subscriber']].sort_values(by=['days_as_subscriber','user_id'],ascending=[False,True])