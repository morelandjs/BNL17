#!/usr/bin/env python3

import matplotlib.pyplot as plt
import numpy as np

plt.style.use('seaborn')

sizes = 10**2, 10**3, 10**6
nbins = 20, 40, 100
labels = "not enough", "better", "better still"

fig, axes = plt.subplots(ncols=3, sharey=True, figsize=(6, 2))

for size, nbin, ax, label in zip(sizes, nbins, axes, labels):
    samples = np.random.normal(size=size)
    ax.hist(samples, bins = np.linspace(-4, 4, nbin), normed=True)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_xlabel(label)
plt.tight_layout()
plt.savefig("mcmc.pdf")
