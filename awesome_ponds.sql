SELECT ponds.ID as `POND_ID`, count(ducks.ID) as `HAPPY_DUCKS`
FROM ((ducks
INNER JOIN species ON ducks.SPECIES_ID = species.ID)
RIGHT JOIN ponds ON ducks.POND_ID = ponds.ID)
WHERE 
CASE
    WHEN species.TEMP_PREFERENCES = '-' THEN ponds.TEMPERATURE <= species.TEMP_LIMIT
    WHEN species.TEMP_PREFERENCES = '+' THEN ponds.TEMPERATURE >= species.TEMP_LIMIT
    ELSE 1
END
GROUP BY ponds.ID
;
