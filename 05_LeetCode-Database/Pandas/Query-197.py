"""
Rising Temperature

"""
import pandas as pd

def rising_temperature(weather: pd.DataFrame) -> pd.DataFrame:
    weather.sort_values(by='recordDate',ascending=True,inplace=True)
    weather['recordDate']=pd.to_datetime(weather['recordDate'])

    weather['Previous_day_temp']= weather['temperature'].shift(1)
    weather['Previous_date'] = weather['recordDate'].shift(1)
    result=weather[(weather['temperature']>weather['Previous_day_temp']) & (weather['recordDate']-weather['Previous_date'] == pd.Timedelta(days=1))]
    return result[['id']]
    