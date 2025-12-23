import pandas as pd
import numpy as np
def find_golden_hour_customers(restaurant_orders: pd.DataFrame) -> pd.DataFrame:
    def func(x):
        hr = int(x[11:13])
        minn = int(x[14:16])
        sec = int(x[17:19])
        time = (hr,minn,sec)
        if ((11,0,0) <= time <= (14,0,0)) or ((18,0,0) <= time <= (21,0,0)):
            return 1
        return 0

    gr = restaurant_orders.groupby("customer_id").agg(total_orders = ("order_id" , "count")).reset_index()
    df = pd.merge(restaurant_orders , gr , on = "customer_id")
    df = df[df["total_orders"] >= 3]
    
    gr = restaurant_orders.groupby("customer_id").agg(average_rating = ("order_rating" , "mean")).reset_index()
    df = pd.merge(df , gr , on = "customer_id")
    df = df[df["average_rating"] >= 4]
    df["average_rating"] = df["average_rating"].round(2)

    gr = restaurant_orders.groupby("customer_id").agg(orderingr = ("order_rating" , "count")).reset_index()
    df = pd.merge(df , gr , on = "customer_id")
    df = df[(df["orderingr"]/df["total_orders"]) >= 0.5]

    df["new"] = df["order_timestamp"].map(func)
    gr = df.groupby("customer_id").agg(temp = ("new" , "sum")).reset_index()
    df = pd.merge(df , gr , on = "customer_id")
    df["peak_hour_percentage"] = np.ceil(df["temp"] / df["total_orders"] * 100).astype(int)
    df = df[df["peak_hour_percentage"] >= 60]


    df = df.groupby("customer_id", as_index=False).first()
    df = df[["customer_id" ,"total_orders" , "peak_hour_percentage" , "average_rating"]]
    df = df.sort_values(["average_rating" , "customer_id"] , ascending = False)

    return df