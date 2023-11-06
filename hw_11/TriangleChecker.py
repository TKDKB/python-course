class TriangleChecker:
    @staticmethod
    def __init__(side_a: int, side_b: int, side_c: int):
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c

    @staticmethod
    def are_all_positive(side_a: int, side_b: int, side_c: int):
        if side_a < 0 or side_b < 0 or side_c < 0:
            return False
        else:
            return True

    @staticmethod
    def is_triangle_possible(side_a: int, side_b: int, side_c: int):
        if side_a + side_b <= side_c or side_b + side_c <= side_a or side_a + side_c <= side_b:
            return False
        else:
            return True

    @staticmethod
    def is_triangle(side_a: int, side_b: int, side_c: int):
        if not(isinstance(side_a, int) and isinstance(side_b, int) and isinstance(side_c, int)):
            print("Нужно вводить только числа!")
        else:
            if not(TriangleChecker.are_all_positive(side_a, side_b, side_c)):
                print("С отрицательными числами ничего не выйдет!")
            else:
                if TriangleChecker.is_triangle_possible(side_a, side_b, side_c):
                    print("Ура, можно построить треугольник!")
                else:
                    print("Жаль, но из этого треугольник не сделать.")


TriangleChecker.is_triangle(-1, 2, 3)
