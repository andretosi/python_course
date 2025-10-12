---
tags:
  - resource
Areas:
  - "[[Programming]]"
Projects:
  - "[[Corso Python x BEA_old]]"
  - "[[Spot Micro]]"
Creation Date: 2024-12-17 18:37
References:
---
`transforms.ToTensor()` in PyTorch serves several important purposes:

1. Converts [[PIL Images]] or NumPy arrays into PyTorch tensors. This is necessary because PyTorch models operate on tensors, not regular images or arrays.
2. Changes the dimensions from (Height x Width x Channels) to (Channels x Height x Width). For example, if you have an RGB image of size 64x64, it will go from (64, 64, 3) to (3, 64, 64). This is PyTorch's preferred format for image data.
3. Scales the pixel values from the range [0, 255] to [0.0, 1.0]. It does this by dividing all values by 255. This normalization helps with model training stability.

Here's a simple example:

```python
from torchvision import transforms
from PIL import Image

# Create transform
transform = transforms.ToTensor()

# Load image
image = Image.open('example.jpg')

# Convert to tensor
tensor_image = transform(image)

# Now tensor_image is a PyTorch tensor with:
# - Values scaled to [0.0, 1.0]
# - Dimensions rearranged to (C, H, W)
# - Type changed to torch.FloatTensor
```

This transform is commonly used as part of a larger transformation pipeline when preparing image data for deep learning models.