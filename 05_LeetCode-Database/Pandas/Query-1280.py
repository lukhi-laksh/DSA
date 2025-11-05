import pandas as pd

def students_and_examinations(students: pd.DataFrame, subjects: pd.DataFrame, examinations: pd.DataFrame) -> pd.DataFrame:
    df = students.merge(subjects, how = 'cross')
    examinations = examinations.groupby(['student_id','subject_name']).agg(attended_exams=('student_id','value_counts')).reset_index()
    df1 = df.merge(examinations, on = ['student_id','subject_name'], how='left')
    df1['attended_exams'] = df1['attended_exams'].fillna(0)
    df1 = df1.sort_values(['student_id','subject_name'])
    return df1[['student_id','student_name','subject_name','attended_exams']]