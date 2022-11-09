# import random


# referece_id = str(random.randrange(1000000000,9999999999))
# # print(referece_id)
# enc_key = {
# '1':'a',
# '2':'b',
# '3':'c',
# '4':'d',
# '5':'e',
# '6':'f',
# '7':'g',
# '8':'h',
# '9':'i',
# '0':'j',
# }

# ent = ''
# result = ''
# print('data before encryption: ',enc_key.keys(),end='')

# def encrypt():
#     global ent,result
#     result = ''
#     for charecter in referece_id:
#         if charecter in enc_key.keys():
#             ent = enc_key[charecter]
#             result = result + ent
#     print('data after encryption: ',result,end='')

# def decrypt():
#     global result
#     out = ''
#     for charecter in result:
#         if charecter in enc_key.values():
#             out = out+ str(list(enc_key.values()).index(charecter))
#     print('data after decription : ',out,end='')

# encrypt()
# decrypt()