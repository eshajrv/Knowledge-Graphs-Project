# %%
import pandas as pandas
import matplotlib.pyplot as plt
import numpy as np

# %%
main_file = '/Users/eshav/Downloads/curated_Disgenet.csv'

df = pandas.read_csv(main_file, delimiter=';')
print(df.head())

# %%
df.describe()

# %%
print(df.isnull().sum())

#%%
dsi_values = df['DSI']
plt.hist(dsi_values, bins=10, edgecolor='black')
plt.xlabel('DSI (Disease Specificity Index)')
plt.ylabel('Frequency')
plt.title('Distribution of DSI')
plt.grid(True)
plt.show()

#%%
dpi_values = df['DPI']
plt.hist(dpi_values, bins=10, edgecolor='black')
plt.xlabel('DPI (Disease Pleiotropy Index)')
plt.ylabel('Frequency')
plt.title('Distribution of DPI')
plt.grid(True)
plt.show()

# %%
plt.scatter(df['NofPmids'], df['YearFinal'])
plt.xlabel('Number of PMIDs')
plt.ylabel('Year')
plt.title('Relationship between PMIDs and the Year')
plt.show()

# %%
plt.subplot(3, 3, 3)
plt.hist(df['score'], bins=10, edgecolor='black')
plt.xlabel('Score')
plt.ylabel('Frequency')
plt.title('Distribution of Score')

# %%
df.plot(x="YearFinal", y="NofPmids", kind="scatter")
plt.xlabel("Year")
plt.ylabel("NofPmids")
plt.title("PubMed ID Trend Over Time")
plt.show()

# %%
plt.figure(figsize=(10, 6))
# Scatter plot for NofSnps vs DSI
plt.scatter(df['NofSnps'], df['DSI'], color='blue', label='DSI')

plt.xlabel('Number of SNPs')
plt.ylabel('Index Value')
plt.title('Correlation between NofSnps and DSI')
plt.legend()
plt.grid(True)
plt.show()

# %%
plt.figure(figsize=(10, 6))
bar_width = 0.35
index = np.arange(len(df['YearFinal']))

plt.bar(index, df['score'], bar_width, label='Average Score', color='blue')
plt.bar(index + bar_width, df['EI'], bar_width, label='Cumulative EI', color='red')

plt.xlabel('Year')
plt.ylabel('Value')
plt.title('Comparison of Average Score and Cumulative EI over Years')
plt.xticks(index + bar_width / 2, df['YearFinal'])
plt.legend()

plt.grid(True)
plt.tight_layout()
plt.show()

# %%
associations_per_year = df.groupby('YearInitial')['geneId'].nunique().reset_index()

associations_per_year.rename(columns={'geneId': 'Number of Associations'}, inplace=True)

top_10_years = associations_per_year.sort_values(by='Number of Associations', ascending=False).head(10)

plt.figure(figsize=(10, 6))
plt.bar(top_10_years['YearInitial'], top_10_years['Number of Associations'], color='skyblue')

plt.xlabel('Year')
plt.ylabel('Number of Associations')
plt.title('Top 10 Years with Highest Number of Associations')

plt.grid(True)
plt.xticks(top_10_years['YearInitial'])
plt.show()

# %%
min_year = int(df['YearFinal'].min())
max_year = int(df['YearFinal'].max())

for start_year in range(min_year, max_year + 1, 10):
    end_year = start_year + 9
    interval_label = f'{start_year}-{end_year}'
    
    subset_df = df[(df['YearFinal'] >= start_year) & (df['YearFinal'] <= end_year)]
    
    if not subset_df.empty:
        associations_per_gene = subset_df['geneId'].value_counts()
        
        plt.figure(figsize=(10, 6))
        associations_per_gene.plot(kind='bar', color='skyblue')
        
        plt.xlabel('Gene ID')
        plt.ylabel('Number of Associations')
        plt.title(f'Number of Associations per Gene in {interval_label}')
        
        plt.xticks([])

        plt.tight_layout()
        plt.show()

#%%
