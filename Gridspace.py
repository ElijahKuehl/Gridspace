from time import sleep


def make_grid(x, y):
    grid = []
    for r in range(0, y+2):
        grid.append([])
        if r == 0 or r == y+1:
            for c in range(0, x+2):
                grid[r].append("-")
        else:
            for c in range(0, x+2):
                if c == 0 or c == x+1:
                    grid[r].append("|")
                else:
                    grid[r].append("O")
    return grid


def show_grid(current=None):
    if current is not None:
        print(current.position())
    for row in range(len(grid)-1, -1, -1):
        for column in range(0, len(grid[row])):
            if grid[row][column] in ["-", "|", "0"]:
                color = "\033[91m"
            elif grid[row][column] != "O":
                color = "\033[93m"
            else:
                color = ""
            if current is not None:
                if row == current.r and column == current.c:
                    color = "\033[92m"
            extra = ""
            for num in range(0, 3-len(str(grid[row][column]))):
                extra += " "
            print(color + str(grid[row][column]) + "\033[0m", end=extra)
        print()
    print()


def simulate():
    show_grid()
    t = 0.75
    try:
        RoboOne = Robot()
        sleep(t)
        RoboOne.move_north(6)
        sleep(t)
        RoboOne.move_east(2)
        sleep(t)
        RoboOne.move_south()
        sleep(t)
        RoboOne.move_west(1)
        sleep(t)
    except:
        pass
    try:
        RoboTwo = Robot()
        sleep(t)
        RoboTwo.move_north(2)
        sleep(t)
        RoboTwo.move_east(3)
        sleep(t)
    except:
        pass
    try:
        RoboThree = Robot()
        sleep(t)
        RoboThree.move_east(10)
        sleep(t)
    except:
        pass
    try:
        RoboFour = Robot()
        sleep(t)
        RoboFour.move_north(10)
        sleep(t)
    except:
        pass
    try:
        RoboFive = Robot()
        sleep(t)
    except:
        pass
    try:
        show_grid(RoboTwo)
        sleep(t)
        RoboTwo.move_south(10)
        sleep(t)
    except:
        pass
    try:
        RoboFive.move_east(10)
        sleep(t)
        RoboFive.move_north(10)
        sleep(t)
        RoboFive.move_east(10)
        sleep(t)
    except:
        pass
    print("Simulation complete")


def select_robo():
    while True:
        show_grid()
        print("(N)ew  (Q)uit  si(M)ulate  or select a robot.")
        alt_list = []
        for robot in robots:
            alt_list.append(robot.code)
        if len(robots) > 0:
            print("Robos:", end=" ")
        print(str(alt_list).replace("[", "").replace("]", ""))
        select = input()
        if select.upper() in ["N", "NEW", "+"]:
            Robot()
            return robots[-1]
        elif select.upper() in ["Q", "QUIT", "-"]:
            quit()
        elif select.upper() in ["M", "SIMULATE", "*"]:
            simulate()
        try:
            robo = robots[alt_list.index(int(select))]
            show_grid(robo)
            return robo
        except:
            pass


def ui():
    current_robo = select_robo()
    while True:
        print("Operating Robo " + str(current_robo.code))
        print("(S)elect  (U)p  (D)own  (L)eft  (R)ight  (K)ill  lo(C)k")
        select = input()
        print()
        if select.upper() in ["S", "SELECT", "+"]:
            current_robo = select_robo()
        elif select.upper() in ["U", "UP", "8"]:
            current_robo.move_north()
        elif select.upper() in ["D", "DOWN", "2"]:
            current_robo.move_south()
        elif select.upper() in ["L", "LEFT", "4"]:
            current_robo.move_west()
        elif select.upper() in ["R", "RIGHT", "6"]:
            current_robo.move_east()
        elif select.upper() in ["K", "KILL", "-"]:
            current_robo = current_robo.kill()
        elif select.upper() in ["C", "LOCK", "/"]:
            current_robo = current_robo.lock()


class Robot:
    def __init__(self, column=1, row=1):
        if grid[column][row] == "O":
            if len(robots) == 0:
                self.code = 1
            else:
                self.code = robots[-1].code + 1
            self.r = row
            self.c = column
            print("Robo '" + str(self.code) + "' created!")
            robots.append(self)
            grid[self.r][self.c] = self.code
            show_grid(self)
        else:
            print("Couldn't create Robo, (1,1) is occupied.")
            show_grid()

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

    def kill(self):
        print("Robo '" + str(self.code) + "' destroyed.")
        grid[self.r][self.c] = "O"
        robots.remove(self)
        return select_robo()

    def lock(self):
        # TODO: Unlocked
        if not (self.c == 1 and self.r == 1):
            print("Robo '" + str(self.code) + "' locked in position.")
            grid[self.r][self.c] = "0"
            robots.remove(self)
            return select_robo()
        else:
            print("Cannot lock on (1,1)")
            return self

    def position(self):
        return "'{0}' currently at: ({1},{2})".format(self.code, self.c, self.r)


if __name__ == "__main__":
    robots = []
    print("What size do you want your grid?")
    grid = make_grid(int(input("X dimension: ")), int(input("Y dimension: ")))
    ui()
