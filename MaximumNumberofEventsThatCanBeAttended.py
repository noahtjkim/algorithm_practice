
import heapq

class Solution:
    def maxEvents(self, events: list) -> int:
        max_day = len(events)
        attend_list = []
        events.sort(key=lambda x: x[0])

        attend = i = 0
        today_ = events[0][0]

        while i < max_day:
            # iterate all events that start today
            while i < max_day and events[i][0] == today_:
                # insert end day into the heap
                heapq.heappush(attend_list, events[i][1])
                i += 1

            heapq.heappop(attend_list)
            attend += 1
            today_ += 1

            # remove all events which were expired
            while attend_list and attend_list[0] < today_: heapq.heappop(attend_list)

            # reset today if there is no attendable events
            if i < max_day and not attend_list: today_ = events[i][0]

        end = 0
        while attend_list and today_ <= attend_list[0]:
            end = attend_list[0]
            attend += 1
            today_ += 1
            heapq.heappop(attend_list)
            while attend_list and attend_list[0] == end and today_ > attend_list[0]:
                heapq.heappop(attend_list)

        return attend

sol = Solution()
# res = sol.maxEvents([[1,2],[2,3],[3,4]])
# res = sol.maxEvents([[1,2],[1,2],[1,6],[1,2],[1,2]])
res = sol.maxEvents([[27,27],[8,10],[9,11],[20,21],[25,29],[17,20],[12,12],[12,12],[10,14],[7,7],[6,10],
                     [7,7],[4,8],[30,31],[23,25],[4,6],[17,17],[13,14],[6,9],[13,14]])
print(res)





