import torch
import torch.nn as nn
from torch.nn import functional as F


torch.manual_seed(42)

vocab = list("YaH1%XfqFwLN(jZ'J,*OP_;.x8B-uI:GE|W=cAnDi&T#7y}K2gCQmUo56!M\9]l>k0`V^R[p+<$tr@{4S/b)dhsvz3e?")


class BiModel(nn.Module):

    def __init__(self, vocab_size):
        super().__init__()
        self.embedding = nn.Embedding(vocab_size, vocab_size)

    def forward(self, idx, targets=None):

        logits = self.embedding(idx)

        if targets is None:
            loss = None
        else:
            B, T, C = logits.shape
            logits = logits.view(B * T, C)
            targets = targets.view(B * T)
            loss = F.cross_entropy(logits, targets)
        return logits


def recover_train():
    state_dict = torch.load("question4.pt",map_location="cpu")
    model = BiModel(92)
    model.state_dict(state_dict)
    return model


if __name__ == "__main__":
    model = recover_train()
    print(model)

