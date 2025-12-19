import pandas as pd

def restaurant_growth(customer: pd.DataFrame) -> pd.DataFrame:
    customer = customer.copy()


    customer = customer.sort_values(by='visited_on')

    all_days = pd.date_range(
        customer['visited_on'].min(),
        customer['visited_on'].max(),
        freq='D'
    )

    rolling = []

    for day in all_days:
        start = day - pd.Timedelta(days=6)

        users = customer.loc[
            (customer['visited_on'] >= start) &
            (customer['visited_on']<= day),
            'amount'
        ].sum()

        rolling.append({
            "visited_on": day,
            "amount": users
        })

    final = pd.DataFrame(rolling)
    final = final[final['visited_on'] >= (customer['visited_on'].min() + pd.Timedelta(days=6))]
    final['average_amount']=(final['amount']/7).round(2)
    return final