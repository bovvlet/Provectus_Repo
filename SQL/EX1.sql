SELECT id
FROM users
JOIN departments
ON id = user_id AND department_id != 1