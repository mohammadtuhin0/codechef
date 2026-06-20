# Read the four integers from the input
a, b, c, x = map(int, input().split())

# Calculate volumes
cuboid_volume = a * b * c
cube_volume = x * x * x

# Compare and print the result
if cuboid_volume > cube_volume:
    print("Cuboid")
elif cube_volume > cuboid_volume:
    print("Cube")
else:
    print("Equal")