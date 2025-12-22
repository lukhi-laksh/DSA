import pandas as pd

def find_loyal_customers(customer_transactions: pd.DataFrame) -> pd.DataFrame:
    
    def customer_info(values_per_customer):
        valid_number_of_purchases = len(values_per_customer[values_per_customer['transaction_type'] == 'purchase']) >= 3
        refund_rate_below_threshold = (len(values_per_customer[values_per_customer['transaction_type'] == 'refund']) / len(values_per_customer)) < 0.2
        been_active_for_while = (max(pd.to_datetime(values_per_customer['transaction_date'])) - min(pd.to_datetime(values_per_customer['transaction_date']))).days >= 30
        return pd.Series({'valid_number_of_purchases': valid_number_of_purchases, 'refund_rate_below_threshold': refund_rate_below_threshold, 'been_active_for_while': been_active_for_while})


    result = customer_transactions.groupby('customer_id').apply(customer_info).reset_index()
    result = result[(result['valid_number_of_purchases']) & (result['refund_rate_below_threshold']) & (result['been_active_for_while'])]
    return result[['customer_id']]