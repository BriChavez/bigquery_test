
"""show how many of each shape has been encountered in descending order"""
-- From this we can determine that light and circle are over 10,000 sightings and that egg, cone, and cross have only a few hundred sightings
SELECT shape, COUNT(shape) AS COUNT
FROM `ughh-347120.ufo_dataset.ufo_table`
GROUP BY shape
ORDER By COUNT DESC;