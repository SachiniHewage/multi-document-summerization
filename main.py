"""

"""

from datasets import load_dataset
import matplotlib.pyplot as plt

if __name__ == "__main__":
    dataset = load_dataset("multi_news")
    print(dataset["train"].column_names)
    print(dataset["train"][0])
