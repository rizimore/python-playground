"""
First Come First Served

@author Mubashir Rasool Razvi <sp19-bse-006@cuilahore.edu.pk>
@date 03-08-2021

Instructions:
====

1) Take input from user
    - number of processes
    - and burst time of each process

2) We need to find out following information:
    - arrival time
    - waiting time
    - average waiting time
    - turn around time
    - response time
"""

# init chart
import matplotlib.pyplot as plt

# Requirements
arrival_times = []
burst_times = []
completion_times = []
waiting_times = []
turnaround_times = []
avg_waiting_time = None


# Take input from user
no_of_processes = int(input("Enter number of processes: "))
for i in range(0, no_of_processes):
    arrival_time = int(input(f"Enter arrival time of process {i+1}: "))
    burst_time = int(input(f"Enter burst time of process {i+1}: "))

    arrival_times.append(arrival_time)
    burst_times.append(burst_time)


# Calculate completion time of every process
for i in range(0, no_of_processes):
    x = 0
    for j in range(0, i+1):
        x += burst_times[j]
    completion_times.append(x)


# Calculate turn around time of every process
for i in range(0, no_of_processes):
    turnaround_times.append(completion_times[i] - arrival_times[i])


# Calculate waiting time of every process
for i in range(0, no_of_processes):
    waiting_times.append(turnaround_times[i] - burst_times[i])


# Calculate average time
sum_of_waiting_times = 0
count_of_waiting_times = len(waiting_times)
for i in range(0, no_of_processes):
    sum_of_waiting_times += waiting_times[i]
avg_waiting_time = sum_of_waiting_times/count_of_waiting_times


# configure chart
fig, gnt = plt.subplots()

gnt.set_xlim(0, completion_times[-1])
gnt.set_ylim(0, no_of_processes)

gnt.set_xlabel('P ID')
gnt.set_ylabel('BURST TIME')

gnt.grid(True)

for i in range(0, no_of_processes):
    if i == 0:
        start_time = 0
    else:
        start_time = completion_times[i-1]
    duration = burst_times[i]
    lower_yaxis = i
    height = 1
    gnt.broken_barh([(start_time, duration)], (lower_yaxis, height))

plt.show()
