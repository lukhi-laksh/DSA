import pandas as pd

def count_unique_subjects(teacher: pd.DataFrame) -> pd.DataFrame:
    df_grouped = teacher.groupby("teacher_id", as_index=False).agg(cnt=("subject_id",pd.Series.nunique))
    return df_grouped[["teacher_id", "cnt"]]