def queries_stats(queries: pd.DataFrame) -> pd.DataFrame:
    queries['quality'] = queries['rating'] / queries['position'] + 1e-10
    queries['poor_query_percentage'] = (queries['rating'] < 3).astype(int)

    return (
        queries.groupby('query_name', as_index=False)
        .agg({
            'quality': lambda x: round(x.mean(), 2),
            'poor_query_percentage': lambda x: round(x.mean() * 100, 2)
        })
    )