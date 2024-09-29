import torch
from torch.utils.data import DataLoader, random_split, TensorDataset


def create_mock_dataloaders(
    n_dimensions: int, n_points: int = 1000, batch_size: int = 32
) -> tuple[DataLoader, DataLoader]:
    """
    Creates two mock dataloaders (train and val) for a classification
    task with 2 classes. By mock dataloaders, we mean that the data is
    randomly generated.
    """
    x = torch.randn(n_points, n_dimensions)
    y = torch.randint(0, 2, (n_points,))
    dataset = TensorDataset(x, y)

    train_size = int(0.8 * len(dataset))
    val_size = len(dataset) - train_size
    train_dataset, val_dataset = random_split(dataset, [train_size, val_size])

    train_loader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True)
    val_loader = DataLoader(val_dataset, batch_size=batch_size)

    return train_loader, val_loader
