import pandas as pd

def tree_node(tree: pd.DataFrame) -> pd.DataFrame:
    condition_1 = tree.groupby('id').size() >= 1
    condition_2 = tree.groupby('p_id')['id'].count() >= 1

    tree['type'] = tree['p_id'].apply(lambda x: 'Root' if pd.isna(x) else None)
    parent_ids = tree['p_id'].dropna().unique()
    tree.loc[tree['type'].isna() & ~tree['id'].isin(parent_ids), 'type'] = 'Leaf'
    tree.loc[tree['type'].isna(), 'type'] = 'Inner'

    #tree['type'] = tree['p_id'].fillna('')
    #print(df)

    return tree[['id','type']]