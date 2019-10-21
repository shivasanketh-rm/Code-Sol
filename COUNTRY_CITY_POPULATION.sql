/*
Given the CITY and COUNTRY tables, query the names of all the continents (COUNTRY.Continent) and their respective average city populations (CITY.Population) rounded down to the nearest integer.

Note: CITY.CountryCode and COUNTRY.Code are matching key columns.

Input Format


-----------------------------------
Output
-----------------------------------


Oceania 109189 
South America 147435 
Europe 175138 
Africa 274439 
Asia 693038 




*/

SELECT COUNTRY.CONTINENT, FLOOR(AVG(CITY.POPULATION))
FROM COUNTRY INNER JOIN CITY
ON CITY.CountryCode = COUNTRY.Code
GROUP BY COUNTRY.CONTINENT;
