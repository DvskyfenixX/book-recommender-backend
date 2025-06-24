import networkx as nx 
import matplotlib.pyplot as plt
from io import BytesIO
import base64

def generar_grafo(rules, libro):
    G = nx.DiGraph()

    for r in rules:
        antecedentes = list(r['antecedents'])
        consecuentes = list(r['consequents'])
        conf = round(r['confidence'], 2)

        for a in antecedentes:
            for c in consecuentes:
                G.add_edge(a, c, weight=conf)

    pos = nx.spring_layout(G)
    plt.figure(figsize=(10, 6))
    nx.draw(G, pos, with_labels=True, node_color='lightblue', edge_color='gray', arrows=True)
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

    buf = BytesIO()
    plt.savefig(buf, format="png")
    plt.close()
    buf.seek(0)
    return base64.b64encode(buf.read()).decode("utf-8")
