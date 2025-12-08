import pandas as pd

def gameplay_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    activity = activity.sort_values(['player_id', 'event_date'], ascending=True)
    summary = activity.groupby('player_id').apply(
        lambda g: pd.Series({
            'first_date': g['event_date'].iloc[0],
            'second_date': g['event_date'].iloc[1] if len(g) > 1 else pd.NaT
        })
    )
    cnt_df = pd.DataFrame({
        'player_cnt': [len(summary)],
        'back_player_cnt': [len(summary[(summary['second_date'] - summary['first_date']).dt.days == 1])]
    })
    res_df = pd.DataFrame({
        'fraction': round(cnt_df['back_player_cnt'] / cnt_df['player_cnt'], 2)
    })
    return res_df