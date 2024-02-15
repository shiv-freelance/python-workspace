
stmt = "Hare Krishna Hare rama"

# reverse a string
# print(stmt[::-1]) # entire string get reversed. (anhsirK eraH)

# output: eraH anhsirK
#         eraH anhsirK

def reverse_string(string: str) -> str:
    return string[::-1]

wrd_lst = stmt.split()
print(wrd_lst)
result = ""

for word in wrd_lst:
    result = result + " "+reverse_string(word)

print(result)