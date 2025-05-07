# def count_valid_pairs(arr, resistance):
#     count = 0
#     for i in range(len(arr)):
#         for j in range(len(arr)):
#             if i>j:
#                 ans=arr[i]
#                while ans >=arr[j] and ans%resistance==0:
#                    ans=ans//resistance
#                    if ans==arr[j]:
#                         count+=1
#                         break
#                if ans<arr[j]:
#                    continue
#
#     return count
#
#
#
#
# # Test the function with examples
# arr = [1, 2, 4, 3, 6]
# resistance = 2
# result = count_valid_pairs(arr, resistance)
# print(result)  # Expected output: 4
def count_valid_pairs(arr, resistance):
    count = 0
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i] > arr[j]:
                temp = arr[i]
                # Keep dividing as long as possible and check if we reach arr[j]
                while temp >= arr[j] and temp % resistance == 0:
                    temp = temp // resistance
                    if temp == arr[j]:
                        count += 1
                        break
                # If temp becomes less than arr[j], no match possible
                if temp < arr[j]:
                    continue
    return count

arr = [1,2,4,3,6]
resistance = 2
result = count_valid_pairs(arr, resistance)
print(result)  # Output: 4