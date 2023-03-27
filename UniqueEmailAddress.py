
class Solution:
    def numUniqueEmails(self, emails: list) -> int:
        res = 0

        email_map = {}

        for i in range(len(emails)):
            name = emails[i].split("@")[0].replace(".", "").split("+")[0]
            domain = emails[i].split("@")[1]
            email = name + "@" + domain
            if email not in email_map.keys():
                email_map[email] = 1

        res = sum(email_map.values())

        return res







