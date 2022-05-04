from sqlalchemy import intersect

k = intersect.distance((1, 2), (5, 4))
print(k)