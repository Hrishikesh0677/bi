import time
import random

# List of server names
servers = ["Server-1", "Server-2", "Server-3"]

# Function to simulate client requests
def generate_requests(num_requests):
    return [f"Request-{i+1}" for i in range(num_requests)]

# Round Robin Load Balancer
def round_robin(requests, servers):
    distribution = {server: [] for server in servers}
    for i, req in enumerate(requests):
        selected_server = servers[i % len(servers)]  # Rotate among servers
        distribution[selected_server].append(req)
        print(f"{req} assigned to {selected_server}")
        time.sleep(0.2)  # simulate delay
    return distribution

# Simulate the process
requests = generate_requests(10)  # You can adjust the number of requests here
print("\nDistributing requests using Round Robin load balancing...\n")
distribution_result = round_robin(requests, servers)

# Final Distribution output
print("\nFinal Distribution:")
for server, reqs in distribution_result.items():
    print(f"{server}: {reqs}")
