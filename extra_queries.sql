
-- 3. Most Claimed Food Types
SELECT Food_Type, COUNT(*) AS Total_Claims
FROM claims
JOIN food_listings ON claims.Food_ID = food_listings.Food_ID
GROUP BY Food_Type
ORDER BY Total_Claims DESC;

-- 4. Most Active Receivers
SELECT receivers.Name, COUNT(*) AS Claims
FROM claims
JOIN receivers ON claims.Receiver_ID = receivers.Receiver_ID
GROUP BY claims.Receiver_ID
ORDER BY Claims DESC;

-- 5. Listings per Provider
SELECT providers.Name, COUNT(*) AS Listings
FROM food_listings
JOIN providers ON food_listings.Provider_ID = providers.Provider_ID
GROUP BY food_listings.Provider_ID;

-- 6. Unclaimed Food Listings
SELECT * FROM food_listings
WHERE Food_ID NOT IN (SELECT Food_ID FROM claims);

-- 7. Food Quantity Summary by Type
SELECT Food_Type, SUM(Quantity) AS Total_Quantity
FROM food_listings
GROUP BY Food_Type;

-- 8. Receiver Requests by City
SELECT City, COUNT(*) AS Total_Receivers
FROM receivers
GROUP BY City;

-- 9. Provider Contribution Summary
SELECT Provider_ID, COUNT(*) AS Listings_Contributed
FROM food_listings
GROUP BY Provider_ID;

-- 10. Most Common Meal Type
SELECT Meal_Type, COUNT(*) AS Count
FROM food_listings
GROUP BY Meal_Type
ORDER BY Count DESC;
