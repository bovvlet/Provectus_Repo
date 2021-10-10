SELECT lastname
FROM user
GROUP BY lastname
HAVING COUNT(DISTINCT firstname) > 1