import torch
import torch.nn as nn
import torch.nn.functional as F

class SimpleAttention(nn.Module):
    def __init__(self, job_features, machine_features, hidden_dim):
        super(SimpleAttention, self).__init__()
        self.job_linear = nn.Linear(job_features, hidden_dim)
        self.machine_linear = nn.Linear(machine_features, hidden_dim)
        self.score_linear = nn.Linear(hidden_dim, 1)

    def forward(self, jobs, machines):
        # jobs: (batch_size, num_jobs, job_features)
        # machines: (batch_size, num_machines, machine_features)

        # Transform jobs and machines features to hidden dimension
        job_transform = self.job_linear(jobs)  # (batch_size, num_jobs, hidden_dim)
        machine_transform = self.machine_linear(machines)  # (batch_size, num_machines, hidden_dim)

        # Compute attention scores
        # We need to compute the dot product between all jobs and all machines
        # To do this efficiently, we can expand both tensors and use batch matrix multiplication
        job_expand = job_transform.unsqueeze(2)  # (batch_size, num_jobs, 1, hidden_dim)
        machine_expand = machine_transform.unsqueeze(1)  # (batch_size, 1, num_machines, hidden_dim)

        # Broadcasting and element-wise multiplication followed by sum
        scores = torch.tanh(job_expand + machine_expand)  # (batch_size, num_jobs, num_machines, hidden_dim)
        scores = self.score_linear(scores).squeeze(-1)  # (batch_size, num_jobs, num_machines)

        # Apply softmax over machines dimension to normalize scores
        attention_weights = F.softmax(scores, dim=-1)  # (batch_size, num_jobs, num_machines)

        return attention_weights

# Example usage
batch_size = 1
num_jobs = 3
num_machines = 4
job_features = 5
machine_features = 6
hidden_dim = 10

jobs = torch.randn(batch_size, num_jobs, job_features)
machines = torch.randn(batch_size, num_machines, machine_features)

attention_model = SimpleAttention(job_features, machine_features, hidden_dim)
attention_weights = attention_model(jobs, machines)
print(attention_weights)
