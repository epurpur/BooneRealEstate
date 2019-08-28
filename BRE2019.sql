-- Database: BRE2019

-- DROP DATABASE "BRE2019";

CREATE DATABASE "BRE2019"
    WITH 
    OWNER = postgres
    ENCODING = 'UTF8'
    LC_COLLATE = 'en_US.UTF-8'
    LC_CTYPE = 'en_US.UTF-8'
    TABLESPACE = pg_default
    CONNECTION LIMIT = -1;
	
	
CREATE EXTENSION postgis;

DROP TABLE public."zone1akeepers"
SELECT res.* 
INTO Zone1aKeepers
FROM public."Zone1a" AS z1a, public."AllResidential2019" AS res
WHERE st_intersects(z1a.geom, res.geom)
	AND res."PARVAL" > 150000;
	
DROP TABLE public."zone1bkeepers"
SELECT res.* 
INTO Zone1bKeepers
FROM public."Zone1b" AS z1b, public."AllResidential2019" AS res
WHERE st_intersects(z1b.geom, res.geom)
	AND res."PARVAL" > 225000;
	
DROP TABLE public."zone1ckeepers"
SELECT res.* 
INTO Zone1cKeepers
FROM public."Zone1c" AS z1c, public."AllResidential2019" AS res
WHERE st_intersects(z1c.geom, res.geom)
	AND res."PARVAL" > 250000;
	
DROP TABLE public."zone1dkeepers"
SELECT res.* 
INTO Zone1dKeepers
FROM public."Zone1d" AS z1d, public."AllResidential2019" AS res
WHERE st_intersects(z1d.geom, res.geom)
	AND res."PARVAL" > 250000;
	
DROP TABLE public."zone1ekeepers"
SELECT res.* 
INTO Zone1eKeepers
FROM public."Zone1e" AS z1e, public."AllResidential2019" AS res
WHERE st_intersects(z1e.geom, res.geom)
	AND res."PARVAL" > 400000;
	
DROP TABLE public."zone1fkeepers"
SELECT res.* 
INTO Zone1fKeepers
FROM public."Zone1f" AS z1f, public."AllResidential2019" AS res
WHERE st_intersects(z1f.geom, res.geom)
	AND res."PARVAL" > 400000;
	
DROP TABLE public."zone1gkeepers"
SELECT res.* 
INTO Zone1gKeepers
FROM public."Zone1g" AS z1g, public."AllResidential2019" AS res
WHERE st_intersects(z1g.geom, res.geom)
	AND res."PARVAL" > 250000;
	
DROP TABLE public."zone1hkeepers"
SELECT res.* 
INTO Zone1hKeepers
FROM public."Zone1h" AS z1h, public."AllResidential2019" AS res
WHERE st_intersects(z1h.geom, res.geom)
	AND res."PARVAL" > 500000;
	
DROP TABLE public."zone1ikeepers"
SELECT res.* 
INTO Zone1iKeepers
FROM public."Zone1i" AS z1i, public."AllResidential2019" AS res
WHERE st_intersects(z1i.geom, res.geom)
	AND res."PARVAL" > 350000;
	
DROP TABLE public."zone1jkeepers"
SELECT res.* 
INTO Zone1jKeepers
FROM public."Zone1j" AS z1j, public."AllResidential2019" AS res
WHERE st_intersects(z1j.geom, res.geom)
	AND res."PARVAL" > 500000;
	
DROP TABLE public."zone2akeepers"
SELECT res.* 
INTO Zone2aKeepers
FROM public."Zone2a" AS z2a, public."AllResidential2019" AS res
WHERE st_intersects(z2a.geom, res.geom)
	AND res."PARVAL" > 150000;
	
DROP TABLE public."zone2bkeepers"
SELECT res.* 
INTO Zone2bKeepers
FROM public."Zone2b" AS z2b, public."AllResidential2019" AS res
WHERE st_intersects(z2b.geom, res.geom)
	AND res."PARVAL" > 225000;
	
DROP TABLE public."zone2ckeepers"
SELECT res.* 
INTO Zone2cKeepers
FROM public."Zone2c" AS z2c, public."AllResidential2019" AS res
WHERE st_intersects(z2c.geom, res.geom)
	AND res."PARVAL" > 275000;
	
DROP TABLE public."zone2dkeepers"
SELECT res.* 
INTO Zone2dKeepers
FROM public."Zone2d" AS z2d, public."AllResidential2019" AS res
WHERE st_intersects(z2d.geom, res.geom)
	AND res."PARVAL" > 300000;
	
DROP TABLE public."zone2ekeepers"
SELECT res.* 
INTO Zone2eKeepers
FROM public."Zone2e" AS z2e, public."AllResidential2019" AS res
WHERE st_intersects(z2e.geom, res.geom)
	AND res."PARVAL" > 350000;
	
DROP TABLE public."zone2fkeepers"
SELECT res.* 
INTO Zone2fKeepers
FROM public."Zone2f" AS z2f, public."AllResidential2019" AS res
WHERE st_intersects(z2f.geom, res.geom)
	AND res."PARVAL" > 350000;
	
DROP TABLE public."zone2gkeepers"
SELECT res.* 
INTO Zone2gKeepers
FROM public."Zone2g" AS z2g, public."AllResidential2019" AS res
WHERE st_intersects(z2g.geom, res.geom)
	AND res."PARVAL" > 400000;
	
DROP TABLE public."zone2hkeepers"
SELECT res.* 
INTO Zone2hKeepers
FROM public."Zone2h" AS z2h, public."AllResidential2019" AS res
WHERE st_intersects(z2h.geom, res.geom)
	AND res."PARVAL" > 500000;
	
DROP TABLE public."zone2ikeepers"
SELECT res.* 
INTO Zone2iKeepers
FROM public."Zone2i" AS z2i, public."AllResidential2019" AS res
WHERE st_intersects(z2i.geom, res.geom)
	AND res."PARVAL" > 700000;
	
DROP TABLE public."zone2jkeepers"
SELECT res.* 
INTO Zone2jKeepers
FROM public."Zone2j" AS z2j, public."AllResidential2019" AS res
WHERE st_intersects(z2j.geom, res.geom)
	AND res."PARVAL" > 700000;
	
DROP TABLE public."zone3akeepers"
SELECT res.* 
INTO Zone3aKeepers
FROM public."Zone3a" AS z3a, public."AllResidential2019" AS res
WHERE st_intersects(z3a.geom, res.geom)
	AND res."PARVAL" > 150000;
	
DROP TABLE public."zone3bkeepers"
SELECT res.* 
INTO Zone3bKeepers
FROM public."Zone3b" AS z3b, public."AllResidential2019" AS res
WHERE st_intersects(z3b.geom, res.geom)
	AND res."PARVAL" > 150000;
	
DROP TABLE public."zone3ckeepers"
SELECT res.* 
INTO Zone3cKeepers
FROM public."Zone3c" AS z3c, public."AllResidential2019" AS res
WHERE st_intersects(z3c.geom, res.geom)
	AND res."PARVAL" > 200000;
	
DROP TABLE public."zone3dkeepers"
SELECT res.* 
INTO Zone3dKeepers
FROM public."Zone3d" AS z3d, public."AllResidential2019" AS res
WHERE st_intersects(z3d.geom, res.geom)
	AND res."PARVAL" > 200000;
	
DROP TABLE public."zone3ekeepers"
SELECT res.* 
INTO Zone3eKeepers
FROM public."Zone3e" AS z3e, public."AllResidential2019" AS res
WHERE st_intersects(z3e.geom, res.geom)
	AND res."PARVAL" > 300000;
	
DROP TABLE public."zone3fkeepers"
SELECT res.* 
INTO Zone3fKeepers
FROM public."Zone3f" AS z3f, public."AllResidential2019" AS res
WHERE st_intersects(z3f.geom, res.geom)
	AND res."PARVAL" > 400000;
	
DROP TABLE public."zone3gkeepers"
SELECT res.* 
INTO Zone3gKeepers
FROM public."Zone3g" AS z3g, public."AllResidential2019" AS res
WHERE st_intersects(z3g.geom, res.geom)
	AND res."PARVAL" > 400000;
	
DROP TABLE public."zone4akeepers"
SELECT res.* 
INTO Zone4aKeepers
FROM public."Zone4a" AS z4a, public."AllResidential2019" AS res
WHERE st_intersects(z4a.geom, res.geom)
	AND res."PARVAL" > 150000;
	
DROP TABLE public."zone4bkeepers"
SELECT res.* 
INTO Zone4bKeepers
FROM public."Zone4b" AS z4b, public."AllResidential2019" AS res
WHERE st_intersects(z4b.geom, res.geom)
	AND res."PARVAL" > 0;
	
DROP TABLE public."zone4ckeepers"
SELECT res.* 
INTO Zone4cKeepers
FROM public."Zone4c" AS z4c, public."AllResidential2019" AS res
WHERE st_intersects(z4c.geom, res.geom)
	AND res."PARVAL" > 200000;
	
DROP TABLE public."zone4dkeepers"
SELECT res.* 
INTO Zone4dKeepers
FROM public."Zone4d" AS z4d, public."AllResidential2019" AS res
WHERE st_intersects(z4d.geom, res.geom)
	AND res."PARVAL" > 250000;
	
DROP TABLE public."zone4ekeepers"
SELECT res.* 
INTO Zone4eKeepers
FROM public."Zone4e" AS z4e, public."AllResidential2019" AS res
WHERE st_intersects(z4e.geom, res.geom)
	AND res."PARVAL" > 150000;
	
DROP TABLE public."zone4fkeepers"
SELECT res.* 
INTO Zone4fKeepers
FROM public."Zone4f" AS z4f, public."AllResidential2019" AS res
WHERE st_intersects(z4f.geom, res.geom)
	AND res."PARVAL" > 350000;
	
DROP TABLE public."zone4gkeepers"
SELECT res.* 
INTO Zone4gKeepers
FROM public."Zone4g" AS z4g, public."AllResidential2019" AS res
WHERE st_intersects(z4g.geom, res.geom)
	AND res."PARVAL" > 350000;
	
DROP TABLE public."zone4hkeepers"
SELECT res.* 
INTO Zone4hKeepers
FROM public."Zone4h" AS z4h, public."AllResidential2019" AS res
WHERE st_intersects(z4h.geom, res.geom)
	AND res."PARVAL" > 300000;
	
DROP TABLE public."zone5akeepers"
SELECT res.* 
INTO Zone5aKeepers
FROM public."Zone5a" AS z5a, public."AllResidential2019" AS res
WHERE st_intersects(z5a.geom, res.geom)
	AND res."PARVAL" > 150000;
	
DROP TABLE public."zone5bkeepers"
SELECT res.* 
INTO Zone5bKeepers
FROM public."Zone5b" AS z5b, public."AllResidential2019" AS res
WHERE st_intersects(z5b.geom, res.geom)
	AND res."PARVAL" > 200000;
	
DROP TABLE public."zone5ckeepers"
SELECT res.* 
INTO Zone5cKeepers
FROM public."Zone5c" AS z5c, public."AllResidential2019" AS res
WHERE st_intersects(z5c.geom, res.geom)
	AND res."PARVAL" > 250000;
	
DROP TABLE public."zone5dkeepers"
SELECT res.* 
INTO Zone5dKeepers
FROM public."Zone5d" AS z5d, public."AllResidential2019" AS res
WHERE st_intersects(z5d.geom, res.geom)
	AND res."PARVAL" > 200000;
	
DROP TABLE public."zone5ekeepers"
SELECT res.* 
INTO Zone5eKeepers
FROM public."Zone5e" AS z5e, public."AllResidential2019" AS res
WHERE st_intersects(z5e.geom, res.geom)
	AND res."PARVAL" > 200000;
	
DROP TABLE public."zone5fkeepers"
SELECT res.* 
INTO Zone5fKeepers
FROM public."Zone5f" AS z5f, public."AllResidential2019" AS res
WHERE st_intersects(z5f.geom, res.geom)
	AND res."PARVAL" > 300000;
	
DROP TABLE public."zone5gkeepers"
SELECT res.* 
INTO Zone5gKeepers
FROM public."Zone5g" AS z5g, public."AllResidential2019" AS res
WHERE st_intersects(z5g.geom, res.geom)
	AND res."PARVAL" > 300000;
	
DROP TABLE public."zone5hkeepers"
SELECT res.* 
INTO Zone5hKeepers
FROM public."Zone5h" AS z5h, public."AllResidential2019" AS res
WHERE st_intersects(z5h.geom, res.geom)
	AND res."PARVAL" > 300000;
	
DROP TABLE public."zone5ikeepers"
SELECT res.* 
INTO Zone5iKeepers
FROM public."Zone5i" AS z5i, public."AllResidential2019" AS res
WHERE st_intersects(z5i.geom, res.geom)
	AND res."PARVAL" > 400000;
	
DROP TABLE public."zone5jkeepers"
SELECT res.* 
INTO Zone5jKeepers
FROM public."Zone5j" AS z5j, public."AllResidential2019" AS res
WHERE st_intersects(z5j.geom, res.geom)
	AND res."PARVAL" > 700000;
	
DROP TABLE public."zone5kkeepers"
SELECT res.* 
INTO Zone5kKeepers
FROM public."Zone5k" AS z5k, public."AllResidential2019" AS res
WHERE st_intersects(z5k.geom, res.geom)
	AND res."PARVAL" > 250000;
	
DROP TABLE public."zone5lkeepers"
SELECT res.* 
INTO Zone5lKeepers
FROM public."Zone5l" AS z5l, public."AllResidential2019" AS res
WHERE st_intersects(z5l.geom, res.geom)
	AND res."PARVAL" > 400000;
	
DROP TABLE public."zone5mkeepers"
SELECT res.* 
INTO Zone5mKeepers
FROM public."Zone5m" AS z5m, public."AllResidential2019" AS res
WHERE st_intersects(z5m.geom, res.geom)
	AND res."PARVAL" > 500000;
	
DROP TABLE public."zone5nkeepers"
SELECT res.* 
INTO Zone5nKeepers
FROM public."Zone5n" AS z5n, public."AllResidential2019" AS res
WHERE st_intersects(z5n.geom, res.geom)
	AND res."PARVAL" > 700000;
	
