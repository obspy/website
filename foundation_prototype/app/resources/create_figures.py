import matplotlib.pylab as plt
import numpy as np

fig = plt.figure(frameon=False)
fig.set_size_inches(4, 4)

ax = plt.Axes(fig, [0., 0., 1., 1.])
ax.set_axis_off()
fig.add_axes(ax)

for i in np.linspace(0.1, 1, 15):
    ax.plot(i * np.sin(np.linspace(0, 2 * np.pi, 1000)), color="k", lw=(0.0 + 4 * i**2), alpha=i)
ax.set_xlim(-50, 1050)
ax.set_ylim(-1.6, 1.6)
ax.set_xticks([])
ax.set_yticks([])
fig.savefig("waveform_iconic.png", dpi=100, transparent=True)
