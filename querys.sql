
-- SHOW USERS AND TOTAL DONORS BROUGHT
SELECT 
users.id, users.name, count(donors.id) as 'total donors'
FROM
Users,Donors
WHERE 
users.id = donors.users_id 
GROUP BY 
users.id
;
-- SHOW USERS AND TOTAL DONORS BROUGHT

-- SHOW DONORS AND TOTAL PRODUCTS DONATED
SELECT 
donors.id, donors.first_name, count(products.id) as 'total products'
FROM
Donors, Products
WHERE
donors.id = products.donors_id
GROUP BY 
donors.id
;

-- SHOW DONORS AND TOTAL PRODUCTS DONATED

SELECT
users.id, users.name, count(donors.id) as 'total donors', count(products.id) as 'total products'
FROM
Users,Donors, Products
WHERE
users.id = donors.users_id , donors.id = products.donors_id
GROUP BY
users.id
;