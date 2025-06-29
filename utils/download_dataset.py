from datasets import load_dataset

# Download the full dataset (includes test labels)
dataset = load_dataset("slegroux/tiny-imagenet-200-clean")

# Save the entire dataset to disk
dataset.save_to_disk("tiny-imagenet-200-clean-local")