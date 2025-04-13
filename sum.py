import torch
from torchvision import transforms
from PIL import Image
import matplotlib.pyplot as plt

# Load the pre-trained model (from TorchHub)
model = torch.hub.load('pytorch/vision:v0.10.0', 'fast_neural_style', model='candy')
model.eval()

# Image preprocessing
def image_loader(image_path, max_size=512):
    image = Image.open(image_path).convert("RGB")

    size = min(max(image.size), max_size)
    in_transform = transforms.Compose([
        transforms.Resize(size),
        transforms.ToTensor(),
        transforms.Lambda(lambda x: x.mul(255))
    ])

    image = in_transform(image).unsqueeze(0)
    return image

# Image deprocessing
def im_convert(tensor):
    image = tensor.clone().detach().cpu().squeeze(0)
    image = image.permute(1, 2, 0).numpy()
    image = image.clip(0, 255).astype('uint8')
    return Image.fromarray(image)

# Main conversion function
def convert_to_ghibli_style(input_path, output_path='ghibli_output.jpg'):
    image = image_loader(input_path)

    with torch.no_grad():
        output = model(image)

    final_img = im_convert(output)
    final_img.save(output_path)
    final_img.show()

# Example use
convert_to_ghibli_style('your_input_image.jpg')
