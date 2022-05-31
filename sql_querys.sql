
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




