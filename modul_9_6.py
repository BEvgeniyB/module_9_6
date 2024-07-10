# def all_variants(text):
#     for i in range(len(text)):
#         for k in range(i,len(text)):
#                 yield text[i:k+1]
def all_variants(text):
    for i in range(len(text)):
        for k in range(len(text) - i):
            yield text[k:k + i + 1]


a = all_variants("abc")
for i in a:
    print(i)
# # просто что бы не забыть
# str_text = 'abc'
# a = [str_text[k:k + i + 1] for i in range(len(str_text)) for k in range(len(str_text) - i)]
# print(*a)
