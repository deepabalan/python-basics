# Complement of gather is scatter

print divmod(7, 3)

t = (7, 3)
# print divmod(t)    # produces error

# Scatter the tuple
print divmod(*t)
