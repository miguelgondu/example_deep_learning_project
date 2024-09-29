import pytorch_lightning as pl

from example_package.dataloaders.mock_dataloader import create_mock_dataloaders
from example_package.models.mlp import MLP


def test_mlp_trains_one_batch_on_mock_data():
    train_loader, val_loader = create_mock_dataloaders(n_dimensions=20, n_points=32)
    model = MLP(input_dim=20, hidden_dim=64, output_dim=2)

    trainer = pl.Trainer(max_epochs=1)
    trainer.fit(model, train_loader, val_loader)
