# • Differentiate between append () and extend () methods?



# (append)
l = [1, 2, 3]
l.append([4, 5])
print(l)

#  output  [1,2,3,[4,5]]
# =========================
# (extend)
l = [1, 2, 3]
l.extend([4, 5])
print(l)

# output   [1,2,3,4,5]
