import pandas as pd

def sum_daily_odd_even(transactions: pd.DataFrame) -> pd.DataFrame:
    transactions.loc[transactions["amount"] % 2 == 0, "type"] = "even"
    transactions["type"] = transactions["type"].fillna("odd")
    odd = transactions[transactions["type"] == "odd"].groupby("transaction_date", as_index=False).agg(odd_sum = ("amount", "sum" ))
    even = transactions[transactions["type"] == "even"].groupby("transaction_date", as_index=False).agg(even_sum = ("amount", "sum" ))
    return transactions.drop_duplicates(subset="transaction_date").merge(odd, how="left").merge(even, how="left")[[ "transaction_date", "odd_sum", "even_sum"]].fillna(0).sort_values(by="transaction_date")