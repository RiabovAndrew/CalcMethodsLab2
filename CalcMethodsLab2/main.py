import matplotlib.pyplot as plt
from prettytable import PrettyTable

from config import h
from config import to
from config import x_0
from config import y_0


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    class accurate_method:

        def __init__(self, x_0, y_0, to, h):
            self.h = h
            self.to = to
            self.x = float(x_0)
            self.y = float(y_0)
            self.epsilon = 0.0001
            if to <= x_0:
                self.combinate = lambda a, b: a - b
            else:
                self.combinate = lambda a, b: a + b
            if to < x_0:
                self.compare = lambda: self.x > self.to
            else:
                self.compare = lambda: self.x < self.to

        def info(self):
            print(self.h, self.x, self.y)

        def function(self, x, y):
            return float(1.2 * pow(x, 3) + 3.1 * x * y - 2.2)

        def __fi_0(self, h):
            return h * self.function(self.x, self.y)

        def __fi_1(self, h):
            return h * self.function(self.combinate(self.x, h / 2), self.combinate(self.y, self.__fi_0(h) / 2))

        def __fi_2(self, h):
            return h * self.function(self.combinate(self.x, h / 2), self.combinate(self.y, self.__fi_1(h) / 2))

        def __fi_3(self, h):
            return h * self.function(self.combinate(self.x, h), self.combinate(self.y, self.__fi_2(h)))

        def y_i(self, h):
            return self.combinate(self.y,
                                  (self.__fi_0(h) + 2 * self.__fi_1(h) + 2 * self.__fi_2(h) + self.__fi_3(h)) / 6)

        def epsilon_h(self):
            tmp_y = self.y
            tmp_x = self.x
            self.y = self.y_i(self.h / 2)
            self.x = self.combinate(self.x, self.h / 2)
            y_h2 = self.y_i(self.h / 2)
            self.y = tmp_y
            self.x = tmp_x
            y_h = self.y_i(self.h)
            return (y_h2 - y_h) * pow(2, 3) / (pow(2, 3) - 1)

        def epsilon_h2(self):
            tmp_y = self.y
            tmp_x = self.x
            self.y = self.y_i(self.h / 2)
            self.x = self.combinate(self.x, self.h / 2)
            y_h2 = self.y_i(self.h / 2)
            self.y = tmp_y
            self.x = tmp_x
            y_h = self.y_i(self.h)
            return (y_h2 - y_h) / (pow(2, 3) - 1)

        def delta(self):
            if self.to < self.x:
                return self.x - self.to
            else:
                return self.to - self.x



    class drawing(accurate_method):

        def __init__(self):
            self.X_I = []
            self.Y_I = []
            self.X_F = []
            self.Y_F = []
            self.X_A = []
            self.Y_A = []


    class table:

        def __init__(self):
            self.X_I = []
            self.Step_I = []
            self.Y_I = []
            self.Error_I = []
            self.X_A = []
            self.Step_A = []
            self.Y_A = []


    # Инициализация нужных переменных
    am = accurate_method(x_0(), y_0(), to(), h())
    table = table()
    drawing = drawing()
    tbl = PrettyTable()



    while am.delta() >= 0.000001:
        if am.h > am.delta():
            am.h = am.delta()
        if abs(am.epsilon_h2()) > am.epsilon:
            am.h = am.h / 2
            continue
        am.y = am.y_i(am.h)
        am.x = am.combinate(am.x, am.h)
        table.X_A.append(am.x)
        table.Step_A.append(am.h)
        table.Y_A.append(am.y)
        if abs(am.epsilon_h() <= am.epsilon):
            am.h = am.h * 2


    tbl.field_names = ["\033[36mX\033[0m", "\033[36mШаг\033[0m", "\033[36mНеточный Y\033[0m"]
    tbl.add_row(
        ["\033[33m" + str(x_0()) + "\033[0m", "\033[33m" + str(h()) + "\033[0m", "\033[33m" + str(y_0()) + "\033[0m"])
    i = 0
    for element in table.X_A:
        tbl.add_row(["\033[33m" + str(element) + "\033[0m", "\033[33m" + str(table.Step_A[i]) + "\033[0m",
                     "\033[33m" + str(table.Y_A[i]) + "\033[0m"])
        i += 1
    print(tbl)


    am = accurate_method(x_0(), y_0(), to(), 0.001)
    drawing.Y_A.append(am.y)
    drawing.X_A.append(am.x)
    while (am.delta() >= 0.000001):
        if am.h > am.delta():
            am.h = am.delta()
        am.y = am.y_i(am.h)
        am.x = am.combinate(am.x, am.h)
        drawing.Y_A.append(am.y)
        drawing.X_A.append(am.x)


    plt.xlabel("X")
    plt.title("Графики приближенного и точного решения")
    plt.plot(drawing.X_I, drawing.Y_I, 'r-o', label="Integral", linewidth=1.0)
    plt.plot(drawing.X_F, drawing.Y_F, 'g-x', label="Integral Fixed", linewidth=2.0)
    plt.plot(drawing.X_A, drawing.Y_A, 'b', label="Accurate", linewidth=1.0)
    plt.ylabel("F[x, f(x)]")
    plt.grid(True)
    plt.legend()
    #plt.show()
