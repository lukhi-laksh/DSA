import pandas as pd

def find_books_with_no_available_copies(library_books: pd.DataFrame, borrowing_records: pd.DataFrame) -> pd.DataFrame:
    borrowing_records = borrowing_records[borrowing_records.return_date.isnull()]
    df = borrowing_records.groupby('book_id').count().reset_index()
    df = df.merge(library_books).rename(columns = {'total_copies': 'current_borrowers'})
    df = df[df.record_id == df.current_borrowers]
    return df.sort_values(['current_borrowers', 'title'], ascending = [0,1]).iloc[:,[0,5,6,7,8,9]]