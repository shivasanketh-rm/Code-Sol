/*
Two pairs (X1, Y1) and (X2, Y2) are said to be symmetric pairs if X1 = Y2 and X2 = Y1.

Write a query to output all such symmetric pairs in ascending order by the value of X.
-----------------------------------
Output
-----------------------------------

2 24 
4 22 
5 21 
6 20 
8 18 
9 17 
11 15
13 13





*/

SELECT F1.x, F1.y
FROM
    functions F1, functions F2
WHERE 
    F1.x = F2.y
    AND
    F1.y = F2.x
    AND
    F1.x <= F1.y
GROUP BY
    F1.x, F1.y
HAVING 
    count(*) > 1 OR (f1.y != f1.x)
ORDER BY 
    F1.x
