from time import sleep

robots = []
grid = []
for r in range(0, 7):
    grid.append([])
    if r == 0 or r == 6:
        for c in range(0, 7):
            grid[r].append("-")
    else:
        for c in range(0, 7):
            if c == 0 or c == 6:
                grid[r].append("|")
            else:
                grid[r].append("O")


def show_grid(current=None):
    if current is None:
        for row in grid[::-1]:
            for column in row:
                if len(str(column)) == 1:
                    print(column, end="  ")
                elif len(str(column)) == 2:
                    print(column, end=" ")
            print()
    else:
        print(current.position())
        for row in range(len(grid)-1, -1, -1):
            for column in range(0, len(grid[row])):
                if row == current.r and column == current.c:
                    if len(str(grid[row][column])) == 1:
                        print("\033[92m" + str(grid[row][column]) + "\033[0m", end="  ")
                    elif len(str(grid[row][column])) == 2:
                        print("\033[92m" + str(grid[row][column]) + "\033[0m", end=" ")
                else:
                    print(grid[row][column], end="  ")
            print()
    print()
    sleep(1)


def simulate():
    show_grid()
    try:
        RoboOne = Robot()
        RoboOne.move_north(6)
        RoboOne.move_east(2)
        RoboOne.move_south()
        RoboOne.move_west(1)
    except:
        pass
    try:
        RoboTwo = Robot()
        RoboTwo.move_north(2)
        RoboTwo.move_east(3)
    except:
        pass
    try:
        RoboThree = Robot()
        RoboThree.move_east(10)
    except:
        pass
    try:
        RoboFour = Robot()
        RoboFour.move_north(10)
    except:
        pass
    try:
        RoboFive = Robot()
    except:
        pass
    try:
        RoboTwo.move_south(10)
    except:
        pass
    try:
        RoboFive.move_east(10)
        RoboFive.move_north(10)
        RoboFive.move_east(10)
    except:
        pass
    show_grid()


def select_robo():
    while True:
        print("(N)ew  (Q)uit  si(M)ulate  or select a robot.")
        for robot in robots:
            print(robot.code, end="  ")
        print()
        select = input()
        if select.upper() in ["N", "NEW"]:
            Robot()
            return robots[-1]
        elif select.upper() in ["Q", "QUIT"]:
            quit()
        elif select.upper() in ["M", "SIMULATE"]:
            simulate()
        try:
            show_grid(robots[int(select)-1])
            return robots[int(select)-1]
        except:
            pass


def ui():
    current_robo = select_robo()
    while True:
        print("(S)elect  (U)p  (D)own  (L)eft  (R)ight")
        select = input()
        if select.upper() in ["S", "SELECT"]:
            current_robo = select_robo()
        elif select.upper() in ["U", "UP"]:
            current_robo.move_north()
        elif select.upper() in ["D", "DOWN"]:
            current_robo.move_south()
        elif select.upper() in ["L", "LEFT"]:
            current_robo.move_west()
        elif select.upper() in ["R", "RIGHT"]:
            current_robo.move_east()


class Robot:
    def __init__(self, column=1, row=1):
        if grid[column][row] == "O":
            robots.append(self)
            self.code = len(robots)
            print("Robo '" + str(self.code) + "' created!")
            self.r = row
            self.c = column
            grid[self.c][self.r] = self.code
            show_grid(self)
        else:
            print("Couldn't create Robo, (1,1) is occupied.")

    def move_south(self, distance=1):
        moved = 0
        for i in range(0, distance):
            if grid[self.r - 1][self.c] == "O":
                grid[self.r][self.c] = "O"
                self.r -= 1
                grid[self.r][self.c] = str(self.code)
                moved += 1
            else:
                break
        print("'{0}' moved down {1} spaces.".format(self.code, moved))
        show_grid(self)

    def move_east(self, distance=1):
        moved = 0
        for i in range(0, distance):
            if grid[self.r][self.c + 1] == "O":
                grid[self.r][self.c] = "O"
                self.c += 1
                grid[self.r][self.c] = str(self.code)
                moved += 1
            else:
                break
        print("'{0}' moved right {1} spaces.".format(self.code, moved))
        show_grid(self)

    def move_north(self, distance=1):
        moved = 0
        for i in range(0, distance):
            if grid[self.r + 1][self.c] == "O":
                grid[self.r][self.c] = "O"
                self.r += 1
                grid[self.r][self.c] = str(self.code)
                moved += 1
            else:
                break
        print("'{0}' moved up {1} spaces.".format(self.code, moved))
        show_grid(self)

    def move_west(self, distance=1):
        moved = 0
        for i in range(0, distance):
            if grid[self.r][self.c - 1] == "O":
                grid[self.r][self.c] = "O"
                self.c -= 1
                grid[self.r][self.c] = str(self.code)
                moved += 1
            else:
                break
        print("'{0}' moved left {1} spaces.".format(self.code, moved))
        show_grid(self)

    def position(self):
        return "'{0}' currently at: ({1},{2})".format(self.code, self.c, self.r)


if __name__ == "__main__":
    ui()
