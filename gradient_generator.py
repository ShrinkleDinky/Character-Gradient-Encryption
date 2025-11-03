import numpy as np
from PIL import Image
import argparse
import hashlib
import random

def seed_to_int(seed_str):
    """Convert a string seed to a consistent integer using SHA-256."""
    hash_obj = hashlib.sha256(seed_str.encode('utf-8'))
    return int(hash_obj.hexdigest(), 16) % (2**32)

def generate_gradient(seed_str):
    seed = seed_to_int(seed_str)
    random.seed(seed)
    gradient = np.zeros((1, 256), dtype=np.uint8)

    # Generate a random black-and-white gradient
    start = random.randint(0, 255)
    end = random.randint(0, 255)
    gradient[0] = np.linspace(start, end, 256).astype(np.uint8)

    # Convert to vertical gradient (256x256)
    gradient_image = np.repeat(gradient, 256, axis=0)

    return Image.fromarray(gradient_image, mode='L')

def main():
    parser = argparse.ArgumentParser(description="Generate a seed-based black-and-white gradient.")
    parser.add_argument("seed", type=str, help="Seed string to generate the gradient")
    parser.add_argument("--output", type=str, default="gradient.png", help="Output PNG filename")
    args = parser.parse_args()

    image = generate_gradient(args.seed)
    image.save(args.output)
    print(f"Gradient saved as '{args.output}' using seed '{args.seed}'.")

if __name__ == "__main__":
    main()
