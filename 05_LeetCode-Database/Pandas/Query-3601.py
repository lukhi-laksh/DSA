import pandas as pd

def find_improved_efficiency_drivers(drivers: pd.DataFrame, trips: pd.DataFrame) -> pd.DataFrame:
    def segmenter(dat):
        if dat < '2023-07-01':
            return 'first'
        else:
            return 'second'
        
    trips['trip_date'] = trips['trip_date'].apply(segmenter)
    trips['fuel_efficiency'] = trips['distance_km'] / trips['fuel_consumed']
    trips = trips[['driver_id','trip_date','fuel_efficiency']]

    lst_driver_ids = list(trips['driver_id'].unique())

    result = pd.DataFrame(columns=['driver_id','first_half_avg','second_half_avg','efficiency_improvement'])
    for driver_id in lst_driver_ids:
        tmp_df = trips[trips['driver_id'] == driver_id]
        if (len(tmp_df[tmp_df['trip_date'] == 'first']) == 0) | (len(tmp_df[tmp_df['trip_date'] == 'second']) == 0):
            continue

        tmp_df = tmp_df.groupby('trip_date').agg('mean')

        result = pd.concat([result, pd.DataFrame({'driver_id': [driver_id], 'first_half_avg': [tmp_df.loc['first','fuel_efficiency']], 'second_half_avg': [tmp_df.loc['second','fuel_efficiency']], 'efficiency_improvement': [tmp_df.loc['second','fuel_efficiency'] - tmp_df.loc['first','fuel_efficiency']]})],axis=0)

    result = pd.merge(result, drivers, on='driver_id', how='left')
    result.sort_values(['efficiency_improvement', 'driver_name'], ascending=[False,True], inplace=True)

    result = result[['driver_id','driver_name','first_half_avg','second_half_avg','efficiency_improvement']]
    result = result[result['efficiency_improvement'] > 0]

    def rounder(q):
        if (round((q - round(q, 2)),10) == 0.005):
            return round(q, 2) + 0.01
        else:
            return round(q, 2)

    result['first_half_avg'] = result['first_half_avg'].apply(rounder)
    result['first_half_avg'] = round(result['first_half_avg'], 2)
    result['second_half_avg'] = result['second_half_avg'].apply(rounder)
    result['second_half_avg'] = round(result['second_half_avg'], 2)
    result['efficiency_improvement'] = result['efficiency_improvement'].apply(rounder)
    result['efficiency_improvement'] = round(result['efficiency_improvement'], 2)

    return pd.DataFrame(result)