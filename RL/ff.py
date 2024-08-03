import torch
import torch.nn.functional as F
from torch.nn import MultiheadAttention

class AttentionNet(torch.nn.Module):
    def __init__(self, state_dim, hidden_dim, action_dim, num_heads):
        super(AttentionNet, self).__init__()
        self.attention1 = MultiheadAttention(embed_dim=state_dim, num_heads=num_heads)
        self.attention2 = MultiheadAttention(embed_dim=state_dim, num_heads=num_heads)
        self.fc = torch.nn.Linear(state_dim, action_dim)
        
    def forward(self, x, mask=None):
        # x shape: (batch_size, seq_len, state_dim) (seq_len, batch_size, embed_dim)
        x = x.permute(1, 0, 2)  # Permute to (seq_len, batch_size, state_dim) for MultiheadAttention
        
        # Attention layer 1
        attn_output1, _ = self.attention1(x, x, x, attn_mask=mask)
        attn_output1 = F.relu(attn_output1)
        
        # Attention layer 2
        attn_output2, _ = self.attention2(attn_output1, attn_output1, attn_output1, attn_mask=mask)
        attn_output2 = attn_output2.permute(1, 0, 2)  # Permute back to (batch_size, seq_len, state_dim)
        
        # Assuming seq_len is 1 for simplicity, otherwise you may need additional processing
        attn_output2 = attn_output2.squeeze(1)  # Remove the seq_len dimension if it's 1
        
        
        #x = F.relu(attn_output2)
        return F.softmax(self.fc(attn_output2), dim=1)

# Example usage
state_dim = 128
hidden_dim = 64
action_dim = 10
num_heads = 8

# Create a random input tensor and a mask
batch_size = 8
seq_len = 1  # Assuming a sequence length of 1 for simplicity
x = torch.randn(batch_size, seq_len, state_dim)
mask = torch.zeros(seq_len, seq_len)  # Example mask (you can customize it)

# Initialize the network
attention_net = AttentionNet(state_dim, hidden_dim, action_dim, num_heads)
output = attention_net(x, mask)
print(output)
