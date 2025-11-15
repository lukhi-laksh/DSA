import pandas as pd

def get_average_time(activity: pd.DataFrame) -> pd.DataFrame:
    return (
        activity.assign(
            timestamp = activity.apply(
                lambda x: x.timestamp if x.activity_type == 'end' else -x.timestamp
            , axis=1)
        ).groupby(['machine_id', 'process_id'], as_index=False)
        .agg(processing_time = ('timestamp', 'sum'))
        .groupby('machine_id', as_index=False)
        .processing_time.mean()
        .round(3)
    )