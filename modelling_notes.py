### Decision Trees

# Decision Tree would be the Algorithm,
# Trained Decision Tree would be the Model
# A series of yes/no questions are asked at each NODE unitl the end, a LEAF, is hit.

# PROS: Easy to interpret, Fast to Make Predictions, Minimal Preprocessing Needed
# CONS: Doesn't consider feature interactions, Complext to train, Prone to overfitting.

#EX:
# temp > 84.5?
# no == rain | yes == temp > 87.5?
# no == no rain | yes == rain

# Avoid getting it too specific to your training set. WE WANT THESE TO BE GENERALISED. Validation set will help flag when we have that overfitting.


# Gini
# Calcualte impurity for current node and each features
# If the current split has the lowest impurity, then this is a leaf node.
# Else choose the feature with the loewest impurity and split into 2 nodes
# Repeat for each remaining node

# To calculate impurity for a feature:
# -for a binary categorical feature, split and calculate impurity (Gini)
# otherwise calculate all possible splits; the one with lowest impurity

# ----

# For a given split, weighted Gini is G(lower w)

# Gini impurity algorithem
# for a leaf, gini impurity (G) is for each class i in k total classes.

# G = 1 - (SUM[with k on top of it, and i under it])p^2(with i under 2)

# For Binary Classification, this simplifies to:
# G = 1 - p^2 - q^2
# G(lower w) = (n1G1+ n2G2) / (n1 + n2)

# 


### Random Forest