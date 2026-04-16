# Import stuff I need
import pandas as pd

# Load the csv, fix the header issue!
# header=None
df = pd.read_csv('dataset1.csv', header=None)

df.columns = ['C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8']
df.insert(0, 'Label', ['R1', 'R2', 'R3', 'R4', 'R5'])

# --- First check what size it is (teacher asked for this) ---
print("Original data shape:", df.shape)
# print(df) # commented out just to test, uncomment if u want to see

# Get only the number columns, skip the label text
num_cols = df.select_dtypes(include=['number']).columns

# --- Calculate for each row ---
df['Row_Total'] = df[num_cols].sum(axis=1).round(2)
df['Row_Mean'] = df[num_cols].mean(axis=1).round(2)

# --- Calculate for each column ---
col_sum = df[num_cols].sum(axis=0).round(2)
col_avg = df[num_cols].mean(axis=0).round(2)

# Add new rows at the bottom
df.loc['Col_Sum'] = pd.Series(dtype='object')
df.loc['Col_Avg'] = pd.Series(dtype='object')

# Name the new rows so teacher knows what they are
df.loc['Col_Sum', 'Label'] = 'Sum_Per_Col'
df.loc['Col_Avg', 'Label'] = 'Avg_Per_Col'

# Fill in the numbers
df.loc['Col_Sum', num_cols] = col_sum
df.loc['Col_Avg', num_cols] = col_avg

# Also fill the last two cells just to be safe idk
df.loc['Col_Sum', 'Row_Total'] = df['Row_Total'].iloc[:-2].sum().round(2)
df.loc['Col_Sum', 'Row_Mean'] = df['Row_Mean'].iloc[:-2].mean().round(2)
df.loc['Col_Avg', 'Row_Total'] = df['Row_Total'].iloc[:-2].mean().round(2)
df.loc['Col_Avg', 'Row_Mean'] = df['Row_Mean'].iloc[:-2].mean().round(2)

# --- Show final result (teacher wants to see this) ---
print("\nFinal result:")
print(df)

# Save it, fixed version!
df.to_csv('dataset1_done.csv', index=False)
print("\nSaved fixed file as dataset1_done.csv")