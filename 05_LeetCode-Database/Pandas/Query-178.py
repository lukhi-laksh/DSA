import pandas as pd

def order_scores(scores: pd.DataFrame) -> pd.DataFrame:
    scores = scores.sort_values(by="score", ascending=False)
    new_scores = []
    curr_rank = 1
    for _, group_df in scores.groupby('score', sort=False):
        group_df['rank'] = curr_rank
        new_scores.append(group_df)
        curr_rank += 1
    
    if len(new_scores) >= 1:
        scores = pd.concat(new_scores)
        scores = scores[['score', 'rank']]
    else:
        scores = pd.DataFrame([], columns=['score', 'rank'])
    return scores