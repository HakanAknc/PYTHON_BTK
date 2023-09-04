# x = 5
# y = 10
# z = 20

# x, y, z = 5, 16, 20

# x, y = y, x
# x += 5          # x = x + 5
# x -= 5          # x = x - 5
# x *= 5          # x = x * 5
# x /= 5          # x = x / 5      #bölme
# x %= 5          # x = x % 5      #mod alma
# y //= 5         # y = y // 5     #kalansız bölme
# y **= z         # y = y ** z     #üs alma

# and => &     #ve
# or  => |     #veya

values = 1, 2, 3, 4, 5

print(values)
print(type(values))

x, y, *z = values

print(x, y, z)
print(x, y, z[1])