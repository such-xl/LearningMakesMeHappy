import torch
import torch.nn as nn
import torch.nn.functional as F

class JobMachineScheduler(nn.Module):
    def __init__(self, job_dim, machine_dim, num_heads, fc_output_dim):
        super(JobMachineScheduler, self).__init__()
        # 定义job信息的Attention层
        self.job_attention = nn.MultiheadAttention(embed_dim=job_dim, num_heads=num_heads)
        # 定义machine信息的Attention层
        self.machine_attention = nn.MultiheadAttention(embed_dim=machine_dim, num_heads=num_heads)
        # 定义全连接层，输入维度是两个Attention层输出维度之和
        self.job_fc = nn.Linear(10*5,5)
        self.machine_fc = nn.Linear(5*2,2)
        self.fc = nn.Linear(7, fc_output_dim)
        
    def forward(self, job_input, machine_input):
        # 假设job_input和machine_input的形状均为[seq_len, batch, embedding_dim]
        # Attention层的输入需要是(batch_size, seq_len, embedding_dim)，这里不需要调整，因为MultiheadAttention接受的就是这种形状
        
        # 处理job信息
        job_attn_output, _ = self.job_attention(job_input, job_input, job_input)
        # 处理machine信息
        machine_attn_output, _ = self.machine_attention(machine_input, machine_input, machine_input)
        job_output = self.job_fc(job_attn_output.reshape(-1))
        machine_output= self.machine_fc(machine_attn_output.reshape(-1))
        # 融合两个Attention的输出
        combined = torch.cat((job_output,machine_output))  # 沿着embedding维度拼接
        
        # 将融合后的输出通过全连接层
        #output = self.fc(combined.mean(dim=0))  # 假设我们通过平均序列长度的方式减少维度
        output = self.fc(combined)
        return output

# 模型参数
job_dim = 5
machine_dim = 2
num_heads = 1  # Attention的头数
fc_output_dim = 10  # 全连接层输出维度

# 创建模型实例
model = JobMachineScheduler(job_dim, machine_dim, num_heads, fc_output_dim)

# 示例输入
job_input = torch.rand(10, 32, 5)  # 假设序列长度为10，批次大小为32
machine_input = torch.rand(5, 32, 2)  # 序列长度为5，批次大小为32

# 前向传播
output = model(job_input, machine_input)
print(output.shape)  # 查看输出维度
