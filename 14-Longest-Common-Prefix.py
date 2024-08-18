class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        longest_prefix = ""
        char_index = 0

        while True:
            try:
                char_to_check = strs[0][char_index]
                for string in strs[1:]:
                    if string[char_index] != char_to_check:    
                        return longest_prefix
                
                longest_prefix += char_to_check
                char_index += 1 
            except:
                return longest_prefix

# I know that using try block instead of checking if index is out of bounds is not a good idea,
# but as Uncle Bob said "Do not touch it if it is working. If you touch it, it becomes yours" :)

# Runtime 39ms, beats %48.66
# Memory 16.58MB, beats %68.21
