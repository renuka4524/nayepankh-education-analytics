import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv(r"D:\NAYEPANKH NGO Data Analytics internship\RBI DATA states_wise_population_Income.csv")

# Basic exploration
print("Shape:", df.shape)
print("\nColumns:", df.columns.tolist())
print("\nFirst 5 rows:")
print(df.head())
print("\nData Info:")
print(df.info())

print("Missing Values:")
print(df.isnull().sum())

print("\nDuplicates:", df.duplicated().sum())

# Analysis 1: Literacy Growth 2001 to 2011
df['Literacy_Growth'] = df['2011- LIT'] - df['2001 - LIT']

# Top 5 states with highest literacy growth
top_literacy = df[['States_Union Territories', 'Literacy_Growth']].sort_values(
    by='Literacy_Growth', ascending=False).head(5)

print("Top 5 States - Literacy Growth:")
print(top_literacy)

# Analysis 2: Income Growth
df['Income_Growth'] = df['2011-12-INC'] - df['2000-01-INC']

top_income = df[['States_Union Territories', 'Income_Growth']].sort_values(
    by='Income_Growth', ascending=False).head(5)

print("Top 5 States - Income Growth:")
print(top_income)

# Analysis 3: Literacy vs Unemployment relationship
print("Literacy vs Unemployment 2011:")
print(df[['States_Union Territories', '2011- LIT', '2011 -UNEMP']].sort_values(
    by='2011- LIT', ascending=False).head(30))

# Analysis 4: Poverty vs Literacy
print("Poverty vs Literacy 2011:")
print(df[['States_Union Territories', '2011- LIT', '2011 -Poverty']].sort_values(
    by='2011 -Poverty', ascending=False).head(10))

# Chart 1: Literacy Rate Comparison 2001 vs 2011 - Top 10 States
top_lit = df.nlargest(10, '2011- LIT')

x = range(len(top_lit))
width = 0.35

plt.bar(x, top_lit['2001 - LIT'], width, label='2001', color='salmon', edgecolor='black')
plt.bar([i + width for i in x], top_lit['2011- LIT'], width, label='2011', color='skyblue', edgecolor='black')

plt.title('Literacy Rate Comparison: 2001 vs 2011 (Top 10 States)')
plt.xlabel('State')
plt.ylabel('Literacy Rate (%)')
plt.xticks([i + width/2 for i in x], top_lit['States_Union Territories'], rotation=45, ha='right')
plt.legend()
plt.tight_layout()
plt.show()

# Chart 2: Poverty vs Literacy Scatter Plot
plt.figure(figsize=(10, 6))
plt.scatter(df['2011- LIT'], df['2011 -Poverty'], 
            color='red', edgecolor='black', s=100)

# Add state name labels
for i, row in df.iterrows():
    plt.annotate(row['States_Union Territories'], 
                (row['2011- LIT'], row['2011 -Poverty']),
                fontsize=7, ha='right')

plt.title('Literacy Rate vs Poverty Rate 2011')
plt.xlabel('Literacy Rate (%)')
plt.ylabel('Poverty Rate (%)')
plt.tight_layout()
plt.show()

# Chart 3: Income Growth by State
plt.figure(figsize=(12, 6))

# Sort by income growth
df_sorted = df.sort_values(by='Income_Growth', ascending=False)

plt.bar(df_sorted['States_Union Territories'], 
        df_sorted['Income_Growth'],
        color='lightgreen', edgecolor='black')

plt.title('Income Growth by State (2001 to 2011)')
plt.xlabel('State')
plt.ylabel('Income Growth (Rs)')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

# Chart 4: Unemployment Comparison 2001 vs 2011
plt.figure(figsize=(12, 6))

x = range(len(df))
width = 0.35

plt.bar(x, df['2001 -UNEMP'], width, 
        label='2001', color='salmon', edgecolor='black')
plt.bar([i + width for i in x], df['2011 -UNEMP'], width, 
        label='2011', color='skyblue', edgecolor='black')

plt.title('Unemployment Comparison: 2001 vs 2011')
plt.xlabel('State')
plt.ylabel('Unemployment Rate')
plt.xticks([i + width/2 for i in x], 
           df['States_Union Territories'], 
           rotation=45, ha='right')
plt.legend()
plt.tight_layout()
plt.show()

