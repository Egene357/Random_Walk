from random import choice
#Random walk finds practical application in special sciences: physics, biology, chemistry and economics
class RandomWalk(): 
    """"Class for generating random walks."""
    def __init__(self, amount_points=5000):
        """Initializes wander attributes."""
        self.amount_points = amount_points

        # All walks start from a point (0, 0).
        self.x_values = [0]
        self.y_values = [0]

    def get_step(self):
        """Determine the direction and distance for a step."""
        direction = choice([1, -1])
        distance = choice(range(8))
        step = direction * distance
        return step

    def all_walk_points(self):
        """Calculates all walk points."""

        # Steps are generated until the desired length is reached.
        while len(self.x_values) < self.amount_points:
            x_step = self.get_step()
            y_step = self.get_step()

            # Deviation of zero displacements.
            if x_step == 0 and y_step == 0: 
                continue

            # Calculating the next x and y values.
            x = self.x_values[-1] + x_step 
            y = self.y_values[-1] + y_step

            self.x_values.append(x) 
            self.y_values.append(y)

