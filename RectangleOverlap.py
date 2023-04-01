
class Solution:
    def isRectangleOverlap(self, rec1: list, rec2: list) -> bool:
        x_flag = False
        y_flag = False

        if (rec2[0] > rec1[0] and rec2[0] < rec1[2]) \
                or (rec2[0] < rec1[0] and rec2[0] > rec1[2]) \
                or (rec2[2] > rec1[0] and rec2[0] < rec1[2]) \
                or (rec2[2] < rec1[0] and rec2[0] > rec1[2]):
            x_flag = True

        if (rec2[1] > rec1[1] and rec2[1] < rec1[3]) \
                or (rec2[1] < rec1[1] and rec2[1] > rec1[3]) \
                or (rec2[3] > rec1[1] and rec2[3] < rec1[3]) \
                or (rec2[3] < rec1[1] and rec2[3] > rec1[3]):
            y_flag = True

        if (rec1[0] > rec2[0] and rec1[0] < rec2[2]) \
                or (rec1[0] < rec2[0] and rec1[0] > rec2[2]) \
                or (rec1[2] > rec2[0] and rec1[0] < rec2[2]) \
                or (rec1[2] < rec2[0] and rec1[0] > rec2[2]):
            x_flag = True

        if (rec1[1] > rec2[1] and rec1[1] < rec2[3]) \
                or (rec1[1] < rec2[1] and rec1[1] > rec2[3]) \
                or (rec1[3] > rec2[1] and rec1[3] < rec2[3]) \
                or (rec1[3] < rec2[1] and rec1[3] > rec2[3]):
            y_flag = True

        print(x_flag, y_flag)
        if x_flag and y_flag:
            return True
        else:
            return False



