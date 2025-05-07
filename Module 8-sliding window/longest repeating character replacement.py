#
# def solution(nums,k):
#     count=0
#     l=0
#     r=0
#     arr=[]
#     for r in range(len(nums)):
#         if nums[l]==nums[r]:
#             count+=1
#             arr.append(nums[r])
#         else:
#             if k>0:
#                 count+=1
#                 k-=1
#                 arr.append(nums[r])
#
#
#     return count
#
#
# input="xyyxyx"
# k=2
# obj=solution(input,k)
# print(obj)
def solution(nums, k):
    # Dictionary to count character frequencies in current window
    char_count = {}
    max_count = 0  # Count of most frequent character in current window
    max_length = 0  # Longest valid substring length
    l = 0  # Left pointer

    # Iterate through string with right pointer
    for r in range(len(nums)):
        # Add current character to count
        char_count[nums[r]] = char_count.get(nums[r], 0) + 1
        # Update max_count if current char count is higher
        max_count = max(max_count, char_count[nums[r]])

        # Current window size is (r - l + 1)
        # If window size - count of most frequent char > k, we need to shrink window
        while (r - l + 1) - max_count > k:
            char_count[nums[l]] -= 1
            l += 1

        # Update max_length if current window is longer
        max_length = max(max_length, r - l + 1)

    return max_length


# Test
input_str = "xyyxyx"
k = 2
obj = solution(input_str, k)
print(obj)


# I M NT GETTING THIS ITS QUTE DIFFICULT