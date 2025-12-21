import pandas as pd

def find_students_who_improved(scores: pd.DataFrame) -> pd.DataFrame:
    min_date = scores.groupby(['student_id','subject']).agg(min_date=('exam_date','min')).reset_index()
    max_date = scores.groupby(['student_id','subject']).agg(max_date=('exam_date','max')).reset_index()
    first_score = scores.merge(min_date, how = 'inner', left_on = ['student_id','subject','exam_date'], right_on =  ['student_id','subject','min_date'])[['student_id','subject','score']].rename(columns={'score':'first_score'})
    latest_score = scores.merge(max_date, how = 'inner', left_on = ['student_id','subject','exam_date'], right_on =  ['student_id','subject','max_date'])[['student_id','subject','score']].rename(columns={'score':'latest_score'})
    output = first_score.merge(latest_score, on = ['student_id','subject'], how = 'inner')
    return output[output['latest_score'] > output['first_score']].sort_values(by = ['student_id','subject'])