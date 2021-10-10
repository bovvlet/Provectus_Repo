SELECT username, salary
FROM user
JOIN Salary
ON id = user_id
ORDER BY salary DESC
LIMIT 1 OFFSET 1