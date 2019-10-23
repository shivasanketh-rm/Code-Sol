/*
You are given a table, BST, containing two columns: N and P, where N represents the value of a node in Binary Tree, and P is the parent of N.

Write a query to find the node type of Binary Tree ordered by the value of the node. Output one of the following for each node:

Root: If node is root node.
Leaf: If node is leaf node.
Inner: If node is neither root nor leaf node.


-----------------------------------
Output
-----------------------------------

1 Leaf 
2 Inner 
3 Leaf 
4 Inner 
5 Leaf 
6 Inner 
7 Leaf 
8 Leaf 
9 Inner 
10 Leaf 
11 Inner 
12 Leaf 
13 Inner 
14 Leaf 
15 Root





*/

SELECT N,
    CASE WHEN P IS NULL THEN "Root"
         WHEN N IN (SELECT P FROM BST) THEN "Inner"
         ELSE "Leaf"
    END
FROM BST
ORDER BY N
