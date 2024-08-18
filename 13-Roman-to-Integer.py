class Solution:
    def romanToInt(self, s: str) -> int:
        roman_numerals = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        result = 0
        i = 0
        while i < len(s):
            if i < len(s) - 1 and roman_numerals[s[i]] < roman_numerals[s[i + 1]]:
                result += roman_numerals[s[i + 1]] - roman_numerals[s[i]]
                i += 2
            else:
                result += roman_numerals[s[i]]
                i += 1

        return result

# Runtime 44ms, beats %70.82
# Memory 16.52MB, beats %43.26
