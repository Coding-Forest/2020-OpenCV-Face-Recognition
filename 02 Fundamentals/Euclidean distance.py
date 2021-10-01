import numpy as np

# Euclidean distance is a way of measuring "dissimilarity" between two objects.
# The higher the eud. distance is, the more dissimilar they are.
# in the sigma notation (i=1, n): n is the number of dimensions (attributes).

# The greatest advantage of Euclidean distsance is, it generalises the number of dimensions.
# You can apply it to things with more than 2 features!

def euclidean_distance(p, q):
    return np.sqrt((p[0] - q[0])**2 + (p[1] - q[1])**2)


# Example 1: between 2 points
p = [23, 64]
q = [65, 33]

print("# Example 1: between 2 points")
print(euclidean_distance(p, q), "\n")


# Example 2: amongst multiple points
p1 = [0, 2]
p2 = [2, 0]
p3 = [3, 1]
p4 = [5, 1]

points = [p1, p2, p3, p4]

print("# Example 2: amongst multiple points")
for point in points:
    ed = []
    for i in range(len(points)):
        ed_val = np.round(euclidean_distance(point, points[i]), 3)
        ed.append(ed_val)
    print(ed)
print()

# Cosine Similarity
# (in the context of documents)
# If d1 and d2 are two document vectors, then:
# cos(d1, d2) = (d1 * d2) / ||d1|| ||d2||       # asterisk (*) in this formula represents vector dot product. ||d|| = the length of vector d
# denominator: divide by the product of "magnitude".


# Example 3: Cosine Similarity
d1 = [3, 2, 0, 5, 0, 0, 0, 2, 0, 0]
d2 = [1, 0, 0, 0, 0, 0, 0, 1, 0, 2]

print("# Example 3: Cosine Similarity")
print("dot product of two distances: ", np.dot(d1, d2))

# ||d|| = d**2
def square_array(array):
    return [element**2 for element in array]

def cosine_similarity(d1, d2):
    denom1 = np.sqrt(np.sum([element**2 for element in d1]))
    denom2 = np.sqrt(np.sum([element**2 for element in d2]))
    return np.round(np.dot(d1, d2) / (denom1 * denom2), 4)

print("cosine_similarity btw d1 & d2: ", cosine_similarity(d1, d2))

"""
# Example 1: between 2 points
52.20153254455275 

# Example 2: amongst multiple points
[0.0, 2.828, 3.162, 5.099]
[2.828, 0.0, 1.414, 3.162]
[3.162, 1.414, 0.0, 2.0]
[5.099, 3.162, 2.0, 0.0]

# Example 3: Cosine Similarity
dot product of two distances:  5
cosine_similarity btw d1 & d2:  0.315

Process finished with exit code 0

"""



"""
"Cosine similarity is a really nice metric for documents
because it gives us this very clean 0 to 1 measurement 
that suffers less from the curse of dimensionality than something like Euclidean distance does.
...Document vectors tend to get very, very long because there's a lot of different words in a given language, 
and given documents might have lots of different words in them, 
cosine similarity is a way to avoid some of the curse of dimensionality (Data Science Dojo, 2017)."


References: 
Data Science Dojo (2017) Euclidean Distance & Cosine Similarity | Introduction to Data Mining part 18
"""
