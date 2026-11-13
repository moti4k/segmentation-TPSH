# Satellite image segmentation

**PyTorch · U-Net · image augmentation · Dice/BCE losses**

A satellite-image segmentation project combining training and inference notebooks with a small Flask presentation interface. The notebooks contain a custom U-Net, image/mask data loading, augmentation and model-checkpoint handling.

## Implementation

- **Training:** U-Net experiments with PyTorch data loaders, Adam optimisation and Dice/BCE losses.
- **Augmentation:** Albumentations transforms applied during image preparation.
- **Inference:** load a saved checkpoint, predict pixel masks and inspect the output alongside the source imagery.
- **Interface:** a separate Flask page under `frontend/server/`.

## Repository guide

| Path | Purpose |
| --- | --- |
| [`used_to_train.ipynb`](used_to_train.ipynb) | Training experiments, datasets, losses and checkpoints. |
| [`run.ipynb`](run.ipynb) | Model definition, checkpoint loading and mask inference. |
| [`frontend/server/server.py`](frontend/server/server.py) | Flask presentation page. |
| [`parse.py`](parse.py) | Optional geocoding/property-data helper, separate from model training. |

## Running the notebooks

Use a Python environment with PyTorch, torchvision, NumPy, pandas, matplotlib, OpenCV, Pillow, Albumentations, tqdm and segmentation-models-pytorch. Review the notebook cells and adjust the image, mask, CSV and checkpoint paths for your environment before running them.

Training requires the input imagery and masks referenced by the notebook. The original checkpoint link is preserved here: [model weights on Google Drive](https://drive.google.com/file/d/1_-af_URKBDNxwgQbQ2a4mykeQFKZeXdq/view?usp=sharing).

The notebooks preserve the project's experiment history. A complete training run has not been revalidated as part of this documentation update.

## Presentation interface

Install Flask in your environment and run:

```bash
cd frontend/server
python server.py
```

The interface is separate from notebook execution.

## Optional geocoding helper

`parse.py` requires a Yandex geocoder API key supplied through the environment:

```bash
export YANDEX_GEOCODER_API_KEY='your-own-api-key'
python parse.py
```

The core segmentation notebooks do not require this key. Keep local credentials out of version control.
