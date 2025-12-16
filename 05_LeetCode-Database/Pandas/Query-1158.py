import pandas as pd

def market_analysis(users: pd.DataFrame, orders: pd.DataFrame, items: pd.DataFrame) -> pd.DataFrame:
    orders['order_date'] = pd.to_datetime(orders['order_date'])
    orders['year'] = orders['order_date'].dt.year

    # Get 2019 orders
    orders_2019 = {}

    for _, row in orders.iterrows():
        if row['year'] == 2019:
            buyer_id = row['buyer_id']

            orders_2019[buyer_id] = orders_2019.get(buyer_id, 0) + 1

    results = []

    for _, row in users.iterrows():
        user_id = row['user_id']
        join_date = row['join_date']
        cnts_2019 = orders_2019.get(user_id, 0) 

        results.append({
            "buyer_id": user_id,
            "join_date": join_date,
            "orders_in_2019": cnts_2019
        })
    

    results_df = pd.DataFrame(results)

    return results_df