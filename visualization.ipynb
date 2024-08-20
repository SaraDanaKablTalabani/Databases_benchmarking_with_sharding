import pandas as pd
import matplotlib.pyplot as plt
import numpy as np  # Import numpy for color mapping

# List of CSV file paths
csv_paths = [
    '/content/single-node-transaction-phase-workloada_runtime_throughput_exp1.csv',
    '/content/single-node-transaction-phase-workloadb_runtime_throughput_exp1.csv',
    '/content/single-node-transaction-phase-workloadc_runtime_throughput_exp1.csv',
    '/content/single-node-transaction-phase-workloadd_runtime_throughput_exp1.csv',
    '/content/runtime_workloade_single_node_transaction_phase_exp1.csv',
    '/content/runtime_workloadf_single_node_transaction_phase_exp1.csv'
]

# Create an empty list to store DataFrames
dfs = []

# Read data from CSV files and store in the dfs list
for csv_path in csv_paths:
    df = pd.read_csv(csv_path)
    dfs.append(df)

# Create figure and plot
plt.figure(figsize=(10, 6))

# Define labels for the curves
labels = ['Workload A','Workload B','Workload C','Workload D', 'Workload E','Workload F']

# Create a color map based on the number of DataFrames
cmap = plt.get_cmap('tab10', len(dfs))

# Iterate through DataFrames and plot their data with labels
for i, df in enumerate(dfs):
    recordcount = df['operationcount']
    avg_read_latency = df['RunTime']
    plt.plot(recordcount, avg_read_latency, marker='o', label=f'RunTime - {labels[i]}', color=cmap(i), linewidth=2.2)  # Increase line thickness

# Set title and labels
plt.title('Single Node-Transaction Phase')
plt.xlabel('operationcount')
plt.ylabel('RunTime (ms)')

# Add legend
plt.legend()

# Show the plot
plt.show()
