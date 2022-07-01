from datetime import datetime

data_str="09:15 01/07/2022"
dt_object1 = datetime.strptime(data_str, "%H:%M %d/%m/%Y")
print(dt_object1)