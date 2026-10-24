# Biomedical Knowledge Graphs

Building and exploring gene-disease knowledge graphs with NetworkX, starting from curated DisGeNET associations.

| File | What it does |
|---|---|
| `networkx_intro.py` | NetworkX basics: building graphs and drawing layouts |
| `initial_KG.py` | A small drug-gene-disease knowledge graph built from (head, relation, tail) triples |
| `data_analysis.py` | Exploratory analysis of the DisGeNET gene-disease table |
| `sample_graphs.py` | Builds a gene-disease graph from high-confidence edges (`score > 0.7`, `DSI > 0.5`) |
| `curated_Disgenet.csv` | Curated gene-disease associations from [DisGeNET](https://www.disgenet.org/) (CC BY-NC-SA 4.0) |

**Stack:** Python · NetworkX · pandas · matplotlib

The scripts use local paths for the CSV. Point them at `curated_Disgenet.csv` in this repo.
