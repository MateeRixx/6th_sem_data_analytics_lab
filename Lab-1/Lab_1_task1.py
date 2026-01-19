
records=[45, 52, 48, 55, 60, 58, 62, 65, 70, 68, 72, 150]
n=len(records)
mean=0
for i in range(len(records)):
    mean=mean+records[i]

print("mean:",mean/len(records))



#2nd task for median
median=0

records.sort()
if(len(records)%2==0):
    #means our array has even number of records 
    median = (records[n//2 - 1] + records[n//2]) / 2
else:
    median = records[n//2]
print(f"Median: {median}")


#task 3 is for mode calcualtion 

from collections import Counter
mode_data = Counter(records)
mode = mode_data.most_common(1)
if mode and mode[0][1] > 1:
    print(f"Mode: {mode[0][0]}")
else:
    print("No mode")

#code for range

range_val = max(records) - min(records)
print(f"Range: {range_val}")

#calcuation for variance:
variance = sum((x - mean) ** 2 for x in records) / len(records)
print(f"Variance: {variance:.2f}")


#calcualtion for standard deviation

import math
std_dev = math.sqrt(variance)
print(f"Standard Deviation: {std_dev:.2f}")

sorted_rec=records.sort()

sorted_sales = sorted(records)
#calculation for IQ:
q1 = sorted_sales[int((n+1)*0.25) - 1] if (n+1)*0.25 % 1 == 0 else (sorted_sales[int((n+1)*0.25) - 1] + sorted_sales[int((n+1)*0.25)]) / 2
q3 = sorted_sales[int((n+1)*0.75) - 1] if (n+1)*0.75 % 1 == 0 else (sorted_sales[int((n+1)*0.75) - 1] + sorted_sales[int((n+1)*0.75)]) / 2
iqr = q3 - q1
print(f"IQR: {iqr}")
