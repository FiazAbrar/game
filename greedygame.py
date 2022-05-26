import random
import math

class Point:
    def __init__(self, name):
        self.name = name
        self.lines_w = []
        self.colors_of_connections = []

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

class Line:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.color = None
        self.name = "line" + str(p1) + "w" + str(p2)
        self.connect_points()

    def set_color(self, color):
        self.color = color
        self.p1.colors_of_connections.append(color)
        self.p2.colors_of_connections.append(color)

    def unset_color(self):
        self.color = None
        self.p1.colors_of_connections.pop()
        self.p2.colors_of_connections.pop()

    def connect_points(self):
        self.p1.lines_w.append(self.p2)
        self.p2.lines_w.append(self.p1)


def game(A_WON, B_WON, num_of_points):
    total_game_rounds = math.comb(num_of_points, 2)
    points = []
    lines = []

    for i in range(num_of_points):
        points.append(Point(f"{i}"))

    for i in range(len(points)):
        for j in range(len(points)):
            if not i == j:
                if (not points[j] in points[i].lines_w) and (not points[i] in points[j].lines_w):
                    lines.append(Line(points[i], points[j]))

    def check_same(arr):
        for i in range(len(arr) - 1):
            if not arr[i] == arr[i+1]:
                return False
        return True

    def game_terminated():
        for point in points:
            if len(point.colors_of_connections) == num_of_points - 1:
                if check_same(point.colors_of_connections):
                    if point.colors_of_connections[0] == "red":
                        return True
        return False

    def game_terminated_if_red(chosen_line):
        chosen_line.set_color("red")
        if game_terminated():
            chosen_line.unset_color()
            return True
        chosen_line.unset_color()
        return False

    def check_two_vertex(chosen_line):
        chosen_line.set_color("red")

        two_vert_points = []
        for point in points:
            if len(point.colors_of_connections) == 2:
                two_vert_points.append(point)

        if len(two_vert_points) == num_of_points - 2:
            chosen_line.unset_color()
            return True
        chosen_line.unset_color()
        return False


    game_round_count = 0
    while game_round_count != total_game_rounds:
        chosen_line = lines[random.randint(0, len(lines) - 1)]

        if chosen_line.color == None:
            if not game_round_count == total_game_rounds:
                if game_terminated_if_red(chosen_line):
                    if game_round_count == total_game_rounds - 1:
                        b_colors = "red"
                    else: b_colors = "blue"
                else:
                    b_colors = "red"
                    if game_round_count < num_of_points - 1:
                        print("two vertex check, move num ", game_round_count)
                        if check_two_vertex(chosen_line):
                            b_colors = "blue"
                        else: b_colors = "red"


            chosen_line.set_color(b_colors)
            game_round_count += 1
            print(f"{game_round_count}.", b_colors, chosen_line.name)
            if game_terminated():
                if game_round_count == total_game_rounds:
                    print("terminated at the last move", "B won")
                    B_WON += 1
                    break
                else:
                    print("terminated somewhere middle", "A won")
                    A_WON += 1
                    break
            if not game_terminated():
                if game_round_count == total_game_rounds:
                    print("did not terminate", "A won")
                    A_WON += 1

    return A_WON, B_WON


A_WON = 0
B_WON = 0

def game_for_a_n(num_of_points, A_WON, B_WON):
    for i in range(10000):
        a_game = game(A_WON, B_WON, num_of_points)
        A_WON = a_game[0]
        B_WON = a_game[1]
    print("A er jitar percentage --", (A_WON*100)/10000, "B er jitar percentage --", (B_WON)*100/10000, "jekhane, number of points ", num_of_points, "ta")


#for num_of_points in range(50):
    #game_for_a_n(num_of_points, A_WON, B_WON)
    #A_WON, B_WON = 0, 0


game(0, 0, 4)
