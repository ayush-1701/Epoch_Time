import pandas as pd
import numpy as np
import datetime

df = pd.read_csv("./sample-data.csv")
time_list = []
for ele in df["time"]:
    time_list.append(datetime.datetime.fromtimestamp(ele))

df["new_Col1"] = time_list

start = int(input("Start Row: "))
end = int(input("End Row: "))
label = int(input("Label: "))

print("Start Row:", start)
print("Ending Row:", end)

print("Appending", label, "in Rows:", start, "to", end)

input_list = []
df_len = len(df["time"])
df_len

for i in range(df_len):
    if i < start or i > end:
        input_list.append("")  # BLANK CELLS
    else:
        input_list.append(label)

df["col2"] = input_list
print(df)

df.to_csv("./solution.csv")
