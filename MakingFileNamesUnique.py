
class Solution:
    def getFolderNames(self, names: list) -> list:
        filenames = []
        filenames_map = {}

        for i in range(len(names)):
            if names[i] not in filenames_map.keys():
                filenames_map[names[i]] = 1
            else:
                j = filenames_map[names[i]]
                while names[i] + "(" + str(j) + ")" in filenames_map.keys():
                    j += 1
                filenames_map[names[i] + "(" + str(j) + ")"] = 1
                filenames_map[names[i]] = j

        filenames = filenames_map.keys()

        return filenames








