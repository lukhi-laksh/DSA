import pandas as pd

def tree_node(tree: pd.DataFrame) -> pd.DataFrame:


    tree['type'] = tree['p_id'].apply(lambda x: 'Root' if pd.isna(x) else None)
    parent_ids = tree['p_id'].dropna().unique()
    tree.loc[tree['type'].isna() & ~tree['id'].isin(parent_ids), 'type'] = 'Leaf'
    tree.loc[tree['type'].isna(), 'type'] = 'Inner'

    return tree[['id','type']]