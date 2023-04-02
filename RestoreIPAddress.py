
class Solution:
    def restoreIpAddresses(self, s: str) -> list:
        res = []

        def backtracking(ipstr, ip):
            # print(ipstr, ip)

            if len(ip) == 4:
                ip_member = ".".join(ip)
                if len(ip_member) == len(s) + 3:
                    if str(ip_member) not in res:
                        res.append(str(ip_member))
                return

            if not ipstr:
                return

            for i in range(len(ipstr)):
                for j in range(0, 3):
                    if int(ipstr[i:i + j + 1]) <= 255:
                        ip.append(str(int(ipstr[i:i + j + 1])))
                        backtracking(ipstr[i + j + 1:], ip)
                        del ip[-1]

                if len(ip) == 4:
                    ip = []

        backtracking(s, [])

        return res








