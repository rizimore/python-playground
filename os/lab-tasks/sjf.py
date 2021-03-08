# init chart
import matplotlib.pyplot as plt

burst_times = []
burst_times_unsorted = []
completion_times = []
waiting_times = []
turnaround_times = []

no_of_processes = int(input("Enter number of processes: "))

if no_of_processes == 0:
    print("Processes can't be 0 or negative, please try again.")
    exit(1)

for i in range(0, no_of_processes):
    burst_time = int(input(f"Enter burst time of process {i+1}: "))
    burst_times.append(burst_time)

burst_times_unsorted = burst_times.copy()
burst_times.sort()

# Calculate completion time of every process
for i in range(0, no_of_processes):
    x = 0
    for j in range(0, i+1):
        x += burst_times[j]
    completion_times.append(x)


# Calculate turn around time of every process
for i in range(0, no_of_processes):
    turnaround_times.append(completion_times[i] - 0)


# Calculate waiting time of every process
for i in range(0, no_of_processes):
    waiting_times.append(turnaround_times[i] - burst_times[i])

# configure chart
fig, gnt = plt.subplots()

gnt.set_xlim(0, completion_times[-1])
gnt.set_ylim(0, no_of_processes)

gnt.set_xlabel('BURST TIME')
gnt.set_ylabel('P ID')

y_tickers = []
y_tickers_labels = []
for i in range(0, no_of_processes):
    y_tickers.append(i+1)
    y_tickers_labels.append(burst_times_unsorted.index(burst_times[i]) + 1)

gnt.set_yticks(y_tickers)
gnt.set_yticklabels(y_tickers_labels)

for i in range(0, no_of_processes):
    if i == 0:
        start_time = 0
    else:
        start_time = completion_times[i-1]
    duration = burst_times[i]
    lower_yaxis = i
    height = 1
    gnt.broken_barh([(start_time, duration)], (lower_yaxis, height))

    print(i, start_time, duration, lower_yaxis, height)

plt.show()
