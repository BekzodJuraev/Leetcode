class Solution(object):

    def multiply(self, l1):
        l1_number = 0
        for item in range(len(l1) - 1, -1, -1):
            l1_number += l1[item]
            l1_number *= 10
        return int(l1_number / 10)

    def addTwoNumbers(self, l1, l2):
        reverse = []
        sum = self.multiply(l1) + self.multiply(l2)
        print(sum)
        x = 0
        while (sum > 0):
            x = sum % 10
            sum = int(sum / 10)
            reverse.append(x)

        return reverse


s=Solution()
print(s.addTwoNumbers([9,9,9,9,9,9,9],[9,9,9,9]))