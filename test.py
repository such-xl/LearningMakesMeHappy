import torch
import torch.nn as nn
import torch.nn.functional as F

class AttentionModule(nn.Module):
    def __init__(self, input_dim, output_dim):
        super(AttentionModule, self).__init__()
        self.query = nn.Linear(input_dim, output_dim)
        self.key = nn.Linear(input_dim, output_dim)
        self.value = nn.Linear(input_dim, output_dim)

    def forward(self, x):
        # x shape: (batch_size, seq_length, input_dim)
        q = self.query(x)  # (batch_size, seq_length, output_dim)
        k = self.key(x).transpose(-2, -1)  # (batch_size, output_dim, seq_length)
        v = self.value(x)  # (batch_size, seq_length, output_dim)
        
        attention_scores = torch.matmul(q, k) / (x.size(-1) ** 0.5)  # Scale by sqrt(d_k)
        attention_weights = F.softmax(attention_scores, dim=-1)
        output = torch.matmul(attention_weights, v)  # (batch_size, seq_length, output_dim)
        return output

class JobMachineRL(nn.Module):
    def __init__(self, job_dim, machine_dim, hidden_dim, output_dim):
        super(JobMachineRL, self).__init__()
        self.job_attention = AttentionModule(job_dim, hidden_dim)
        self.machine_attention = AttentionModule(machine_dim, hidden_dim)
        self.fc1 = nn.Linear(hidden_dim * 2, hidden_dim)  # Combine job and machine info
        self.fc2 = nn.Linear(hidden_dim, output_dim)  # Output Q values for each action

    def forward(self, jobs, machines):
        # jobs shape: (batch_size, num_jobs, job_dim)
        # machines shape: (batch_size, num_machines, machine_dim)
        job_features = self.job_attention(jobs)
        machine_features = self.machine_attention(machines)
        
        # Example: Summing over job and machine features (simple aggregation)
        job_features = job_features.sum(dim=1)
        machine_features = machine_features.sum(dim=1)
        
        combined_features = torch.cat([job_features, machine_features], dim=-1)
        hidden = F.relu(self.fc1(combined_features))
        q_values = self.fc2(hidden)
        return q_values

# Example usage
batch_size = 10
num_jobs = 5
num_machines = 3
job_dim = 4
machine_dim = 4
hidden_dim = 128
output_dim = num_jobs  # Assuming we output Q value for each job

jobs = torch.randn(batch_size, num_jobs, job_dim)
machines = torch.randn(batch_size, num_machines, machine_dim)

model = JobMachineRL(job_dim, machine_dim, hidden_dim, output_dim)
q_values = model(jobs, machines)
print(q_values)  # Output Q-values for each job
