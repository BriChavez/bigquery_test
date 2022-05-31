
"""ask how many of each shape has been encountered in descending order"""
SELECT shape, COUNT(shape) AS COUNT
FROM `ughh-347120.ufo_dataset.ufo_table`
GROUP BY shape
ORDER By COUNT DESC;
-- returns that light and circle are over 10,000 sightings and that egg, cone, and cross have only a few hundred sightings


"""ask how many times each shape occures with the time stamp of less than a minute"""
SELECT shape, duration, COUNT(shape) AS COUNT
FROM `ughh-347120.ufo_dataset.ufo_table` 
WHERE duration LIKE '%seconds'
GROUP BY shape, duration
-- returns that only egg and cone shapes have been reported with a less than a minute time stamp


"""ask how many times the word chill is referenced in the texts"""
SELECT COUNT(text) as COUNT
FROM `ughh-347120.ufo_dataset.ufo_table` 
WHERE text LIKE '%chill%'
-- returns 346


"""ask what shapes have been reported in Portland"""
SELECT city, shape
FROM `ughh-347120.ufo_dataset.ufo_table` 
WHERE city LIKE '%Portland%'
ORDER BY shape
-- returns changing, cigar, chevron, and circle


"""ask what the last date recorded is"""
SELECT MAX(date_time)
FROM `ughh-347120.ufo_dataset.ufo_table` 
-- returns 2019-12-29


"""ask if any occurances have happened in guatemala"""
SELECT *
FROM `ughh-347120.ufo_dataset.ufo_table` 
WHERE city IN ("Guatemala")
-- returns that two have. 


"""ask how many of each shape has been reported in England"""
SELECT COUNT(shape) AS COUNT, shape
FROM `ughh-347120.ufo_dataset.ufo_table` 
WHERE city LIKE ("%England%")
GROUP BY shape
ORDER BY COUNT(shape) DESC
-- returns the top 4 are light, circle, sphere, and fireball


"""ask how many times a fireball has been the shape reported"""
SELECT COUNT(shape)
FROM `ughh-347120.ufo_dataset.ufo_table` 
WHERE shape IN ('fireball')
-- returns 7,052 times