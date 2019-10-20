/*
Generate NUmbers


-----------------------------------
Output
-----------------------------------

2 
3 
4 
5 
.
.
.
.1001





*/

SET @NUM = 1;

SELECT * FROM
(SELECT @NUM := @NUM + 1 AS NUMBERS 
FROM 
information_schema.tables t1,
information_schema.tables t2
LIMIT 1000) list_of_numbers
