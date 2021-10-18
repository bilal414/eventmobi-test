import string
import uuid


class Plateau:
    rovers = []

    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns

    def can_move(self, coord_x, coord_y):
        return 0 <= coord_x <= self.rows and 0 <= coord_y <= self.columns

    def add_rover(self, rover, instructions):
        for instruction in instructions:
            if instruction == "m":
                possible_step = rover.possible_step()
                coord_x = possible_step[0]
                coord_y = possible_step[1]

                if self.can_move(coord_x, coord_y):
                    rover.move(coord_x, coord_y)
            else:
                rover.set_orientation(instruction)

        self.rovers.append(rover)

    def get_rover(self, name):
        rover = None

        for item in self.rovers:
            if item.name == name:
                rover = item
                break

        return rover


class Rover:
    def __init__(self, name, x, y, orientation):
        self.name = name
        self.x = x
        self.y = y
        self.orientation = orientation

    def move(self, x, y):
        self.x = x
        self.y = y

    def possible_step(self):
        steps = dict(
            n=[self.x, self.y + 1],
            s=[self.x, self.y - 1],
            e=[self.x + 1, self.y],
            w=[self.x - 1, self.y],
        )
        return steps[self.orientation]

    def set_orientation(self, instruction):
        options = dict(nr="e", nl="w", sr="w", sl="e", er="s", el="n", wr="n", wl="s")
        self.orientation = options[f"{self.orientation}{instruction}"]


def add_rover(landing, instructions, plateau):
    rover = Rover(
        f"rover_{random.choice(string.ascii_letters)}",
        int(landing[0]),
        int(landing[1]),
        landing[2],
    )
    plateau.add_rover(rover, instructions)


def start():
    # Plateau
    plateau_input = input("Plateau: ").replace(" ", "")
    
    plateau_x, plateau_y = [int(a) for a in str(plateau_input)]
    plateau = Plateau(plateau_x, plateau_y)

    # Landing
    landing_input = input("Rover Landing: ").replace(" ", "")

    if len(landing_input) != 3:
        raise Exception("Landing input must be 3 characters long.")

    # Check if char is in input and change to lowercase
    directions = ['n', 's', 'e', 'w']
    landing_x, landing_y, landing_d = [(a.lower() if a.lower() in directions and a.isalpha() else int(a)) for a in str(landing_input)]

    # Rover
    instructions = input("Rover Instructions: ").lower().strip().replace(" ", "")
    rover = Rover(
        uuid.uuid4().hex,
        landing_x,
        landing_y,
        landing_d,
    )
    plateau.add_rover(rover, instructions)

    print(f"Rover_{rover.name}: {rover.x} {rover.y} {rover.orientation.upper()}")

    # return for unit test
    return plateau


if __name__ == "__main__":
    start()
