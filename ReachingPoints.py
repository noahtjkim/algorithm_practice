
class Solution:
    def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        while sx < tx and sy < ty:
            tx, ty = tx % ty, ty % tx

            # one last calculation
        if (sx == tx and sy <= ty and (ty - sy) % sx == 0) \
                or (sy == ty and sx <= tx and (tx - sx) % sy == 0):
            return True
        else:
            return False

