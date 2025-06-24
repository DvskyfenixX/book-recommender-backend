import pandas as pd
from mlxtend.frequent_patterns import apriori, association_rules

# Cargar tus datos ya tratados
df = pd.read_pickle('modelos/df.pkl.gz')
te_df = df.apply(lambda x: x.dropna().tolist(), axis=1)

# Preparar datos
from mlxtend.preprocessing import TransactionEncoder
te = TransactionEncoder()
te_ary = te.fit(te_df).transform(te_df)
df_tf = pd.DataFrame(te_ary, columns=te.columns_)

# Ejecutar Apriori
frequent_itemsets = apriori(df_tf, min_support=0.01, use_colnames=True)
rules = association_rules(frequent_itemsets, metric="confidence", min_threshold=0.3)

def recomendar_libros(libro):
    result = rules[rules['antecedents'].apply(lambda x: libro in x)]
    return result[['antecedents', 'consequents', 'confidence', 'lift']].to_dict(orient='records')
