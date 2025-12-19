import pandas as pd

def capital_gainloss(stocks: pd.DataFrame) -> pd.DataFrame:
    buy_df= stocks[stocks.operation=='Buy'].groupby(['stock_name']).agg(
        total_buy_price=('price', 'sum')
    ).reset_index()
    sell_df= stocks[stocks.operation=='Sell'].groupby(['stock_name']).agg(
        total_sell_price=('price', 'sum')
    ).reset_index()
    res_df= buy_df.merge(sell_df, on=['stock_name'], how='inner')
    res_df['capital_gain_loss']= res_df['total_sell_price']- res_df['total_buy_price']
    return res_df[['stock_name', 'capital_gain_loss']]
    