#page 153
import random
for i in range(10000):
    x=random.random()
    #between 0(inclusive) and 1(exclusive)
    #print(x)
y=random.randint(5,10)
#print(y)
t=[1,2,3]
z=random.choice(t)
#print(z)
word="bdnd- nm-"
a=word.replace("-","")
#print(a)

s1={"a","b","c"}
s2={"a","c","d"}
print(s2-s1)



import random

# Define a node for the probability tree
class TreeNode:
    def __init__(self, suffix=None, probability=0, left=None, right=None):
        self.suffix = suffix
        self.probability = probability  # Probability weight for this node
        self.left = left
        self.right = right

# Build a probability tree
def build_probability_tree(freq_map):
    suffixes = sorted(freq_map.items(), key=lambda x: x[1], reverse=True)
    total = sum(freq for suffix, freq in suffixes)

    def build_tree(suffixes, total):
        if len(suffixes) == 1:
            return TreeNode(suffix=suffixes[0][0], probability=suffixes[0][1] / total)
        mid = len(suffixes) // 2
        left = build_tree(suffixes[:mid], total)
        right = build_tree(suffixes[mid:], total)
        return TreeNode(left=left, right=right)

    return build_tree(suffixes, total)

# Traverse the probability tree based on a random number
def traverse_tree(node, rand_val, total_prob=1):
    if node.suffix:  # Leaf node, return suffix
        return node.suffix
    left_prob = node.left.probability if node.left else 0
    if rand_val < left_prob / total_prob:
        return traverse_tree(node.left, rand_val, left_prob)
    else:
        return traverse_tree(node.right, rand_val - left_prob / total_prob, total_prob - left_prob)

# Example usage
freq_map = {"suffix1": 2, "suffix2": 5, "suffix3": 3}
tree = build_probability_tree(freq_map)
rand_val = random.random()
print(traverse_tree(tree, rand_val))
