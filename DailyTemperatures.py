class Solution(object):
    def dailyTemperaturesNaive(self, temperatures):
        size = len(temperatures)
        result = [0] * size

        for i in range(0, size):
            for j in range(i + 1, size):
                if temperatures[j] > temperatures[i]:
                    result[i] = j - i
                    break

        return result

    def dailyTemperatures(self, temperatures):
        size = len(temperatures)
        result = [0] * size

        stack = [-1] * size
        stackIndex = -1

        for i in range(0, size):
            # When we hit a temperature warmer than the top of our stack,
            # Update result for the matching position and pop the stack
            # We pop as many dates with this current warm temp as possible
            while stackIndex != -1 and temperatures[i] > temperatures[stack[stackIndex]]:
                index = stack[stackIndex]
                stackIndex -= 1
                result[index] = i - index

            # Put the current date on top of the stack
            stackIndex += 1
            stack[stackIndex] = i

        return result
