import pandas as pd

def recomendar_libros(input_books, rules, top_n=3):
    input_books = set(input_books)
    
    # Buscar reglas donde el antecedente completo está en el input
    reglas_exacto = rules[rules['antecedents'].apply(lambda x: x.issubset(input_books))]

    # Si no hay suficientes, buscar reglas donde haya al menos un libro en común
    if len(reglas_exacto) < top_n:
        reglas_relajadas = rules[rules['antecedents'].apply(lambda x: len(input_books & x) > 0)]
        reglas_usar = pd.concat([reglas_exacto, reglas_relajadas]).drop_duplicates()
    else:
        reglas_usar = reglas_exacto

    # Ordenar por confianza y lift
    reglas_ordenadas = reglas_usar.sort_values(by=['confidence', 'lift'], ascending=False).head(top_n)

    # Devolver reglas como lista de dicts para graficar y recomendar
    return reglas_ordenadas[['antecedents', 'consequents', 'confidence', 'lift']].to_dict(orient='records')
