import pandas as pd
import calendar
def reformat_table(department: pd.DataFrame) -> pd.DataFrame:
    columns =  pd.DataFrame(columns = ['id'] + [calendar.month_abbr[i] + '_Revenue' for i in range(1,13)])
    department = department.pivot(index='id',columns='month',values='revenue').add_suffix('_Revenue').reset_index()
    return pd.concat([columns, department])