import pandas as pd

# Given list of tuples
data = [('Food & Beverages', 3), ('Inflight Entertainment', 3), ('Seat Comfort', 3), ('Staff Service', 3), ('Value for Money', 3), ('Seat Comfort', 1), ('Cabin Staff Service', 1), ('Ground Service', 1), ('Value For Money', 1), ('Seat Comfort', 1), ('Cabin Staff Service', 1), ('Food & Beverages', 1), ('Inflight Entertainment', 1), ('Ground Service', 2), ('Wifi & Connectivity', 1), ('Value For Money', 1), ('Seat Comfort', 3), ('Cabin Staff Service', 3)]
# # Convert list of tuples to DataFrame
# df = pd.DataFrame(data, columns=['Category', 'Rating'])

# # Print the DataFrame
# print(df)
import pandas as pd

# Assuming your initial DataFrame is named 'df'
df = pd.DataFrame(data, columns=['Category', 'Rating'])

# Pivot the DataFrame
df_pivot = df.pivot_table(index=df.index // 2, columns='Category', values='Rating', aggfunc='first')

# Print the reshaped DataFrame
print(df_pivot)

