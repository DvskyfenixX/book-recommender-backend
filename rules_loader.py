import pandas as pd

_rules_cache = None

def get_rules():
    global _rules_cache
    if _rules_cache is None:
        _rules_cache = pd.read_pickle('modelos/rules.pkl.gz')
    return _rules_cache