#!/usr/bin/env python3

pp = [('Leborn James', 98), ('Kevin Durant', 97), ('James Harden', 96), ('Stephen Curry', 95), ('Anthony Davis', 94)]

# def Panduang(i):
#     # for a in i:
#     #     print(a)
#     #     if a[1] >= 96:
#     if i[1] >= 96:
#         return True
#     else:
#         return False

# a = list(filter(Panduang,pp))
# print(a)

# def a(i):
#     if isinstance(i[0],str):
#         return i[0].lower()
# out_list = list(map(a,pp))
# print(out_list)

a = sorted(list(map(lambda i: i[0].upper(),pp)),key=None,reverse=True)
print(a)