import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
df = pd.read_csv (r'Genes.csv')
print(df.head(5))
df2 = df[['Chromosomes','Start','Count']]
heatmap2_data = pd.pivot_table(df2,values='Count', index=['Chromosomes'], columns='Start')
heatmap2_data.head(n=5)
sns.heatmap(heatmap2_data, cmap="coolwarm")
plt.show()
