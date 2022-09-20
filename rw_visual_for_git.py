import matplotlib.pyplot as plt
from random_walk_for_git import RandomWalk

while True:

    # Construction of a random walk.
    rw = RandomWalk(5000)
    rw.all_walk_points()

    # Plotting points on a chart.
    plt.style.use('classic')
    fig, ax = plt.subplots(figsize=(12, 7))
    point_amount = range(rw.amount_points)
    ax.plot(rw.x_values, rw.y_values, linewidth=1)

    # Selecting the first and last points.
    ax.scatter(0, 0, c='orange', edgecolors='none', s=150)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='green', edgecolors='none',
        s=150)

    # Deleting axes.
    ax.get_xaxis().set_visible(False) 
    ax.get_yaxis().set_visible(False)

    plt.savefig('Random Walk.png', bbox_inches='tight')
    plt.show()

    keep_running = input("Another walk??? (y/n): ")
    if keep_running == 'n':
        break
