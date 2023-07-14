import pandas as pd

df = pd.read_excel("Iterator-Lab.xlsx",sheet_name = 0)
device_list = list(df['Device'])
current_list = list(df['Current'])
power_list = list(df['Power'])

sorted_power_list = sorted(power_list,reverse = True)

highest_power_dx = power_list.index(sorted_power_list[0])
second_power_dx = power_list.index(sorted_power_list[1])
print(f"Top power rating devices are \n{device_list[highest_power_dx]}  Current- {current_list[highest_power_dx]}\n"
      f"{device_list[second_power_dx]}  Current- {current_list[second_power_dx]}" )
