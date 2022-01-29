

#
# alef = [(i-ord("A"),chr(i)) for i in range(ord("A"), ord("Z")+1)]
# print(alef)
# CN = {x[1]:x[0] for x in alef}
# NC = {x[0]:x[1] for x in alef}
# print(CN, NC)
# M, k = 'GOOD', 3
# print([NC[(CN[m]+k)%len(alef)] for m in M])

# alef = [chr(i) for i in range(ord('A'), ord('Z')+1)]
# CN = {c:ord(c) - ord('A') for c in alef}
# NC = {ord(c) - ord('A'):c for c in alef}
# for i in range(0, 3):
#     k = int(input())
#     M = input().upper()
#     print ("".join([NC[(CN[m] + k) % 26] if m in alef else m for m in M]))

# def ECeasar(M,k):
#     alef = [chr(i) for i in range(ord("A"), ord("Z")+1)]
#     CN = {c:ord(c) - ord("A") for c in alef}
#     NC = {ord(c) - ord("A"):c for c in alef}
#     print(CN,NC,sep="\n")
#
#     return "".join([NC[(CN[m]+k)%26] if m in alef else m for m in M ])
#
# k = int(input("I:"))
# M = input("S").upper()
# print(ECeasar(M,k))

#
# alef = [chr(i)for i in range(ord("A"), ord("Z")+1)]
# print(alef)
# print()
# CN = {c:ord(c) - ord("A") for  c in alef}
# print(CN)
# print()
#
# NC = {ord(c) - ord("A"):c for  c in alef}
# print(NC)
# print()
# k1, k2 = 1,3
# M = 'REgular Expression(RegEx/RegExp)'.upper()
# print("".join([NC[(CN[m]+k1)*k2%26] if m in alef else m for m in M]))


# def findModInverse(a, n):
#     from math import gcd
#     if gcd(a, n) != 1:
#         return None
#     u1, u2, u3 = 1, 0, a
#     v1, v2, v3 = 0, 1, n
#     while v3 != 0:
#         q = u3 // v3
#         v1, v2, v3, u1, u2, u3 = (u1 - q * v1), (u2 - q * v2), (u3 - q * v3), v1, v2, v3
#     return u1 % n
# alef = [chr(i) for i in range(ord('A'), ord('Z')+1)]
# CN = {c:ord(c) - ord('A') for c in alef}
# NC = {ord(c) - ord('A'):c for c in alef}
# k1, k2 = list(map(int, input().split()))
# C = f'CPVLKDC PUWCPFFBTQF (CPVPU / CPVPUW)'
# k2_1 = findModInverse(k2, 26)
# print ("".join([NC[((CN[c] * k2_1) - k1) % 26] if c in alef else c for c in C]))


alef = [chr(i) for i in range(ord("A"), ord("Z")+1)]
print(alef)
print()
CN = {c:ord(c)-ord("A") for c in alef}
print(CN, len(CN))

NC = {ord(c)-ord("A"):c for c in alef}
print(NC, len(NC))

M = "REGILAR EXPRESSIONS (REGEX/REGEXP)"
key = 'ONETWO'
print("фраза: ", M, "Ключ:",key,len(key))
print()
key = key*(len(M)//len(key)+1)
print("Фраза: ", M, "Ключ: ", key, len(key))
C = "".join([NC[(CN[m]+CN[k])%26] if m in alef else m for(m,k) in zip(M, key)])
print(C)


