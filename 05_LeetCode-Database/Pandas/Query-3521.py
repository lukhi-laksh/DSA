import pandas as pd

def find_product_recommendation_pairs(product_purchases: pd.DataFrame, product_info: pd.DataFrame) -> pd.DataFrame:
    self_join = product_purchases.merge(product_purchases, how ='cross', suffixes=('_1','_2'))
    self_join_filter = self_join[(self_join['user_id_1'] == self_join['user_id_2']) & (self_join['product_id_1'] < self_join['product_id_2'])]
    self_join_agg = self_join_filter.groupby(['product_id_1','product_id_2']).agg(customer_count=('user_id_1','nunique')).reset_index()[['product_id_1','product_id_2','customer_count']]
    join_category_1 = self_join_agg.merge(product_info, how = 'left', left_on = 'product_id_1', right_on = 'product_id').rename(columns={'category':'product1_category'})[['product_id_1','product_id_2','product1_category','customer_count']]
    join_category_2 = join_category_1.merge(product_info, how = 'left', left_on = 'product_id_2', right_on = 'product_id').rename(columns={'category':'product2_category'})[['product_id_1','product_id_2','product1_category','product2_category','customer_count']]
    return join_category_2[join_category_2['customer_count'] >= 3].rename(columns={'product_id_1':'product1_id','product_id_2':'product2_id'}).sort_values(by=['customer_count','product1_id','product2_id'], ascending = [False,True,True])