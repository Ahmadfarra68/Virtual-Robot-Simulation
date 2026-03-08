import time
from enum import Enum

# --- البيئة (Core Requirements) ---
class CellType(Enum):
    EMPTY = 0; OBSTACLE = 1; GOAL = 2

class Environment:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.grid = [[CellType.EMPTY for _ in range(width)] for _ in range(height)]
    
    def is_within_bounds(self, x, y):
        return 0 <= x < self.width and 0 <= y < self.height

    def display(self, robot):
        print("\033[H\033[J", end="") # مسح الشاشة
        for y in range(self.height):
            for x in range(self.width):
                if robot.x == x and robot.y == y: print("R", end=" ")
                elif self.grid[y][x] == CellType.OBSTACLE: print("#", end=" ")
                elif self.grid[y][x] == CellType.GOAL: print("G", end=" ")
                else: print(".", end=" ")
            print()

# --- الروبوت (Robot Model & Logic) ---
class Direction(Enum):
    NORTH = 0; EAST = 1; SOUTH = 2; WEST = 3

class RobotState(Enum): # (Extension: Finite State Machine)
    IDLE = 0; MOVING = 1; AVOIDING = 2; FINISHED = 3

class Robot:
    def __init__(self, x, y):
        self.x, self.y = x, y
        self.direction = Direction.EAST
        self.state = RobotState.IDLE

    def sense(self, env):
        dx, dy = {Direction.NORTH:(0,-1), Direction.SOUTH:(0,1), Direction.EAST:(1,0), Direction.WEST:(-1,0)}[self.direction]
        nx, ny = self.x + dx, self.y + dy
        if not env.is_within_bounds(nx, ny) or env.grid[ny][nx] == CellType.OBSTACLE: return "BLOCK"
        if env.grid[ny][nx] == CellType.GOAL: return "GOAL"
        return "CLEAR"

    def decide(self, sensor): # (Extension: Obstacle Avoidance logic)
        if sensor == "GOAL":
            self.state = RobotState.FINISHED
        elif sensor == "BLOCK":
            self.state = RobotState.AVOIDING
            self.direction = Direction((self.direction.value + 1) % 4) # دور لليمين
        else:
            self.state = RobotState.MOVING
            dx, dy = {Direction.NORTH:(0,-1), Direction.SOUTH:(0,1), Direction.EAST:(1,0), Direction.WEST:(-1,0)}[self.direction]
            self.x += dx; self.y += dy

# --- التشغيل (Simulation Loop) ---
def main():
    env = Environment(10, 10)
    env.grid[5][5] = CellType.GOAL # الهدف
    for i in range(3, 7): env.grid[i][3] = CellType.OBSTACLE # عوائق
    
    robot = Robot(0, 0)
    while robot.state != RobotState.FINISHED:
        env.display(robot)
        sensor = robot.sense(env)
        robot.decide(sensor)
        time.sleep(0.3)
    print("وصلنا للهدف بنجاح!")

if __name__ == "__main__": main()