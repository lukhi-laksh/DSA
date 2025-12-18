import pandas as pd

def immediate_food_delivery(delivery: pd.DataFrame) -> pd.DataFrame:
    delivery["immorsched"] = delivery.apply(lambda row: 1 if row["order_date"] == row["customer_pref_delivery_date"] else 0, axis=1)
    first_df = delivery.groupby(by="customer_id").agg(first_order=("order_date","min")).reset_index()
    df = pd.merge(delivery, first_df, how="left", on="customer_id")
    df_imm = df[df["order_date"]==df["first_order"]]
    result = ((df_imm["immorsched"].sum() / df_imm["immorsched"].count())*100).round(2)
    return pd.DataFrame(data=[result], columns=['immediate_percentage'])

    