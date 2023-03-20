
class Solution:
    def maximumUnits(self, boxTypes: list[list[int]], truckSize: int) -> int:
        """
        find max boxes
        and calculate the units
        """
        sum_box = 0
        unit = 0
        o_flag = False

        boxTypes = sorted(boxTypes, key=lambda x: (x[1], x[0]), reverse=True)

        for i in range(len(boxTypes)):
            sum_box += boxTypes[i][0]

            if sum_box > truckSize:
                boxes = boxTypes[i][0] - (sum_box - truckSize)
                print(i, sum_box, boxes, truckSize, unit, boxTypes[i][0], boxTypes[i][1])
                o_flag = True
            else:
                boxes = boxTypes[i][0]

            unit += boxes * boxTypes[i][1]

            if o_flag:
                break

        return unit








