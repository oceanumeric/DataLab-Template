# %%
# this is a demo file for python
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


# write a function to plot a fansy figure
def plot_fansy_figure():
    # Fixing random state for reproducibility
    np.random.seed(19680801)

    # Compute pie slices
    N = 20
    θ = np.linspace(0.0, 2 * np.pi, N, endpoint=False)
    radii = 10 * np.random.rand(N)
    width = np.pi / 4 * np.random.rand(N)
    colors = plt.cm.viridis(radii / 10.)

    ax = plt.subplot(111, projection='polar')
    ax.bar(θ, radii, width=width, bottom=0.0, color=colors, alpha=0.5)

    plt.show()


if __name__ == "__main__":
    # inline retina for jupyter
    # %config InlineBackend.figure_format = 'retina'
    plot_fansy_figure()
    print("Hello World!")
# %%
