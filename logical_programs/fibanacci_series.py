feb_series = [0,1]
for i in range(10-1):
    if i not in feb_series:
        next_number = feb_series[i-1] +  feb_series[i-2]
        feb_series.append(next_number)

print(feb_series)