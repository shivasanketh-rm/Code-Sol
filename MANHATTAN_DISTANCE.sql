Consider p1(A,B)  and p2(C,D) to be two points on a 2D plane.

A happens to equal the minimum value in Northern Latitude (LAT_N in STATION).
B happens to equal the minimum value in Western Longitude (LONG_W in STATION).
C happens to equal the maximum value in Northern Latitude (LAT_N in STATION).
D happens to equal the maximum value in Western Longitude (LONG_W in STATION).
Query the Manhattan Distance between points  and  and round it to a scale of  4 decimal places.

-----------------------------------
Output
-----------------------------------

259.6859





*/

SELECT ROUND(ABS(MAX(LAT_N) - MIN(LAT_N)) + ABS(MAX(LONG_W) - MIN(LONG_W)),4)
FROM STATION;
