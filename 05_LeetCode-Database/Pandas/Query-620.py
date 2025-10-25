import pandas as pd

def not_boring_movies(cinema: pd.DataFrame) -> pd.DataFrame:

    return (cinema[(cinema.id%2 == 1)                   # <-- 1.
            & (cinema.description != 'boring')]         # <-- 2.
            .sort_values('rating', ascending = False))  # <-- 3.