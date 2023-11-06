class Matrix:
    def __init__(self, creation_list: list[list[int]]):
        self.content = creation_list
        self.y_size = len(creation_list)
        self.x_size = len(creation_list[0])

    def __add__(self, other):
        if self.x_size == other.x_size and self.y_size == other.y_size:
            for i in range(self.y_size):
                for j in range(self.x_size):
                    self.content[i][j] = self.content[i][j] + other.content[i][j]

            return self
        else:
            return "Матрицы неодинаковой размерности"

    def __sub__(self, other):
        if self.x_size == other.x_size and self.y_size == other.y_size:
            for i in range(self.y_size):
                for j in range(self.x_size):
                    self.content[i][j] = self.content[i][j] - other.content[i][j]

            return self
        else:
            return "Матрицы неодинаковой размерности"

    def __mul__(self, other):
        if isinstance(other, int):
            for i in range(self.y_size):
                for j in range(self.x_size):
                    self.content[i][j] = self.content[i][j] * other
            return self

    def __rmul__(self, other):
        if isinstance(other, int):
            for i in range(self.y_size):
                for j in range(self.x_size):
                    self.content[i][j] = other * self.content[i][j]
            return self

    def transpose(self):
        rows = self.x_size
        cols = self.y_size
        buffer_matrix_list = [[0] * cols for _ in range(rows)]
        # print(outer_buffer_list)

        for k in range(self.y_size):
            for l in range(self.x_size):
                # print(self.content[i][j])
                buffer_matrix_list[l][k] = self.content[k][l]
                # print(buffer_matrix_list)
        # print(self.content)
        self.content = buffer_matrix_list
        return self

    @classmethod
    def create_unar_matrix(cls, m, n):
        if m == n:
            rows = m
            cols = n
            buffer_matrix_list = [[1 if i == j else 0 for j in range(n)] for i in range(n)]
            # for i in range(m):
            #     buffer_matrix_list[i][i] = 1
            return cls(buffer_matrix_list)
        else:
            return "Из исходных данных не может быть создана квадратная матрица"

    @classmethod
    def create_null_matrix(cls, m, n):
        rows = m
        cols = n
        buffer_matrix_list = [[0 for j in range(n)] for i in range(n)]
        return cls(buffer_matrix_list)

    @classmethod
    def create_diagonal_matrix(cls, list_diag):
        buffer_matrix_list = [[list_diag[i] if i == j else 0 for j in range(len(list_diag))] for i in range(len(list_diag))]
        return cls(buffer_matrix_list)

    def get_size(self):
        return self.y_size, self.x_size

    def get_elements_amount(self):
        return self.y_size * self.x_size

    def get_elements_sum(self):
        sum = 0
        for i in range(self.y_size):
            for j in range(self.x_size):
                sum += self.content[i][j]
        return sum

    def change_negative(self):
        for i in range(self.y_size):
            for j in range(self.x_size):
                if self.content[i][j] < 0:
                    self.content[i][j] = 0
        return self

    def __eq__(self, other):
        if self.content == other.content:
            return True
        else:
            return False

    def __str__(self):
        result = """"""
        for i in range(self.y_size):
            result += f"{'{'} {', '.join(str(self.content[i][j]) for j in range(self.x_size)):^30} {'}'}\n"
        return result

m1 = Matrix([[-1, 3, 4, 1, 1, 1], [1, 1, 1, 0, 1, 7], [-2, 2, 21, 1, 1, 111]])
m2 = Matrix([[2, 0], [-1, 1], [3, -2]])
m3 = Matrix([[-1, 3], [0, 1], [-2, 2]])
# result = 2 * m1
# print(result.content, result.x_size, result.y_size)
# print(m1.transpose().content)
# new = Matrix.create_diagonal_matrix([1, 2, 3, 4, 5])
# print(new.content)
# m1.change_negative()
# print(m1.content)
# print(m1 == m3)
# print(str(m1))
