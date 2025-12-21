import pandas as pd

def seasonal_sales_analysis(products: pd.DataFrame, sales: pd.DataFrame) -> pd.DataFrame:
    df = sales.copy()

    months = ['Winter', 'Winter', 'Spring', 'Spring', 'Spring', 'Summer', 'Summer', 'Summer', 'Fall', 'Fall', 'Fall', 'Winter']
    df['season'] = df['sale_date'].apply(lambda date: months[date.month - 1])
    df['revenue'] = df['quantity'] * df['price']
    df = df.merge(products, on='product_id', how='left')

    df = df.groupby(['category', 'season']).agg(total_quantity=('quantity', 'sum'), total_revenue=('revenue', 'sum')).reset_index()

    df['popularity'] =  list(zip(df['total_quantity'], df['total_revenue']))
    idx_max = df.groupby('season')['popularity'].idxmax()
    df = df.loc[idx_max]

    return df[['season', 'category', 'total_quantity', 'total_revenue']]