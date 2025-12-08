# loss.py
import torch
import torch.nn as nn

class YOLOLoss(nn.Module):
    def __init__(self, S=7, B=2, C=20,
                 lambda_coord=5, lambda_noobj=0.5):
        super().__init__()
        self.S = S
        self.B = B
        self.C = C
        self.lambda_coord = lambda_coord
        self.lambda_noobj = lambda_noobj
        self.mse = nn.MSELoss(reduction="sum")

    def forward(self, pred, target):
        obj_mask = target[..., 4] == 1
        noobj_mask = target[..., 4] == 0

        coord_loss = self.mse(
            pred[obj_mask][..., :2],
            target[obj_mask][..., :2]
        )

        size_loss = self.mse(
            torch.sqrt(pred[obj_mask][..., 2:4]),
            torch.sqrt(target[obj_mask][..., 2:4])
        )

        obj_conf_loss = self.mse(
            pred[obj_mask][..., 4],
            target[obj_mask][..., 4]
        )

        noobj_conf_loss = self.mse(
            pred[noobj_mask][..., 4],
            target[noobj_mask][..., 4]
        )

        class_loss = self.mse(
            pred[obj_mask][..., 5:],
            target[obj_mask][..., 5:]
        )

        loss = (
            self.lambda_coord * coord_loss +
            self.lambda_coord * size_loss +
            obj_conf_loss +
            self.lambda_noobj * noobj_conf_loss +
            class_loss
        )

        return loss
