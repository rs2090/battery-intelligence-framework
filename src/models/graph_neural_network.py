"""
Graph Neural Network model for electrolyte optimization.

This module defines a basic graph neural network using PyTorch and DGL to operate on battery chemistry graphs.
"""
import torch
import torch.nn as nn
import dgl
import dgl.nn as dglnn


class GraphNeuralNetwork(nn.Module):
    def __init__(self, in_feats, hidden_feats, out_feats):
        super().__init__()
        self.conv1 = dglnn.GraphConv(in_feats, hidden_feats)
        self.conv2 = dglnn.GraphConv(hidden_feats, out_feats)

    def forward(self, g, features):
        """
        Forward pass of the GNN.
        :param g: DGLGraph representing the molecular graph.
        :param features: Input node features tensor.
        :return: Output tensor.
        """
        h = self.conv1(g, features)
        h = torch.relu(h)
        h = self.conv2(g, h)
        return h
