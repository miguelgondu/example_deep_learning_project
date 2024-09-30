import pytorch_lightning as pl
from lightning.pytorch.loggers import WandbLogger

import wandb
from example_package.dataloaders.mock_dataloader import create_mock_dataloaders
from example_package.models.mlp import MLP


def main():
    train_loader, test_loader = create_mock_dataloaders(
        n_dimensions=28 * 28,
        n_points=10_000,
        batch_size=256,
    )

    mlp = MLP(
        input_dim=28 * 28,
        hidden_dim=128,
        output_dim=2,
    )

    wandb.init(entity="miguelgondu", project="example_package")

    wandb_logger = WandbLogger(log_model="all")
    wandb_logger.watch(mlp, log="all")

    trainer = pl.Trainer(max_epochs=50, logger=wandb_logger, log_every_n_steps=1)
    trainer.fit(mlp, train_loader, test_loader)


if __name__ == "__main__":
    main()
