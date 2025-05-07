# def process_text(text, prefix, suffix):
# #     prefixc=prefix[-2]
#       if text.startswith(prefixc):
#           result.append(prefixc)
#
#       suffixc=suffix[-3]
#      if text.endswith(suffixc):
#          result.append(prefixc)
#
# # Example 1: No overlap between prefix and suffix
# text1 = "nothing"
# prefix1 = "erino"
# suffix1 = "grding"
# result1 = process_text(text1, prefix1, suffix1)
# print("Processed Text 1:", result1)
#
# # Example 2: Overlapping prefix and suffix
# text2 = "banana"
# prefix2 = "bana"
# suffix2 = "nana"
# result2 = process_text(text2, prefix2, suffix2)
# print("Processed Text 2:", result2)
text = "wanted"
prefix = "trhwa"

# Get the last two characters of the prefix (e.g., "wa")
last_part_of_prefix = prefix[-2:]

# Check if the last part of the prefix is the start of the text
if text.startswith(last_part_of_prefix):
    print("The last part of the prefix matches the start of the text.")
else:
    print("The last part of the prefix does not match the start of the text.")
# suffix[-1:] would return the last character: "g"
# suffix[-2:] would return the last two characters: "ng"
# So, suffix[-3:] = "ing" is correct for "grading".