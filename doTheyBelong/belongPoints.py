from math import sqrt


class BelongPoints:
    def __init__(self):
        self.p = None
        self.q = None

    def do_they_belong(self, x1, y1, x2, y2, x3, y3, xp, yp, xq, yq):
        """
        if p √, q x, -> 1
        p x, q √ -> 2
        p √ q √ -> 3
        p x q x -> 4

        :return:
        """

        def triangle(x1, y1, x2, y2, x3, y3):
            a, b, c = sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2), \
                      sqrt((x1 - x3) ** 2 + (y1 - y3) ** 2), \
                      sqrt((x2 - x3) ** 2 + (y2 - y3) ** 2)
            return abs(a - b) < c < a + b

        def area(x1, y1, x2, y2, x3, y3):
            return abs((x1 * (y2 - y3) + x2 * (y3 - y1)
                        + x3 * (y1 - y2)) / 2.0)

        def within(x, y, x1, y1, x2, y2, x3, y3):
            # Calculate area of triangle ABC
            A = area(x1, y1, x2, y2, x3, y3)

            # Calculate area of triangle PBC
            A1 = area(x, y, x2, y2, x3, y3)

            # Calculate area of triangle PAC
            A2 = area(x1, y1, x, y, x3, y3)

            # Calculate area of triangle PAB
            A3 = area(x1, y1, x2, y2, x, y)

            # Check if sum of A1, A2 and A3
            # is same as A
            if A == A1 + A2 + A3:
                return True
            else:
                return False

        p, q = within(xp, yp, x1, y1, x2, y2, x3, y3), \
               within(xq, yq, x1, y1, x2, y2, x3, y3)
        if not triangle(x1, y1, x2, y2, x3, y3):
            return 0
        if p:
            if q:
                return 3
            else:
                return 1
        else:
            if q:
                return 2
            else:
                return 4


if __name__ == '__main__':
    bp = BelongPoints()
    assert bp.do_they_belong(2, 2, 7, 2, 5, 4, 4, 3, 7, 4) == 1
