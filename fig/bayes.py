#!/usr/bin/env python3

import matplotlib.pyplot as plt
import numpy as np

plt.style.use('seaborn')

fig = plt.figure(figsize=(4, 9/4.))

x = np.linspace(-4, 4., 1000)
y = np.exp(-x**2)

plt.plot(x, y)
plt.fill_between(x, np.zeros_like(x), y)
plt.xlabel('$x_\star$')
plt.ylabel(r'$P(x_\star|\mathrm{model}, \mathrm{data})$')
plt.ylim(0, 1.01)
plt.xlim(-4, 4)
fig.gca().set_yticklabels([])
plt.tight_layout()
plt.savefig('bayes.pdf')
