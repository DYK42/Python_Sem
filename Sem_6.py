import re

test = "Something to match"

pattern1 = r"^.*(thing).*"
pattern2 = r"^.*(not present).*"

# m = re.match(pattern1, test)
# if m:
#     print(f"Matched the 1st pattern: {m.group(1)}")
# else:
#     m = re.match(pattern2, test)
#     if m:
#         print(f"Matched the 2nd pattern: {m.group(1)}")

# ---------------------

# Чище

# if m := (re.match(pattern1, test)):
#     print(f"Matched 1st pattern: '{m.group(1)}'")
# elif m := (re.match(pattern2, test)):
#     print(f"Matched 2nd pattern: '{m.group(1)}'")

text = 'автобус ехал на автопилоте за авиабилетами СТОП'
# print(' '.join(filter(lambda x: not any(True if char in x else False for char in 'абв'), text.split())))

print(set('аббривиатура'))
# print(*filter(lambda x: not set(x) >= (set('абв')), text.split()), sep=' ') # issuperset
#
# print(*filter(lambda x: set(x).isdisjoint(set('абв')), text.split()), sep=' ')

#Task#5
# def rle_decode(string: str):
# decode_string = ''
# i = 0
# while len(string[i: i + 2]) == 2:
# num, char = string[i: i + 2]
# decode_string += char * int(num)
# i += 2
#
# return decode_string
