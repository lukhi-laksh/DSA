import pandas as pd

def tree_node(tree: pd.DataFrame) -> pd.DataFrame:
    tree['type']=tree.apply(lambda x: 'Root' if pd.isnull(x['p_id']) else "Inner" if tree['p_id'].isin([x['id']]).any() else 'Leaf',axis=1)
    return(tree[['id','type']])