--FIRST, SELECT OUT RESIDENTIAL PARCELS FROM VARIOUS COUNTIES. NOT ALL
--COUNTIES CONTAIN FIELDS WHICH ALLOW ME TO DISTINGUISH RESIDENTIAL PARCELS
--ONLY WATAUGA AND WILKES HAVE THESE FIELDS
	
SELECT * 
INTO WilkesResidential
FROM public."nc_wilkes_parcels_poly"
WHERE parusecode = 'R1';

SELECT *
INTO WataugaResidential
FROM public."nc_watauga_parcels_poly"
WHERE parusedesc = 'RESIDENTIAL 1 FAMILY'
	OR parusedesc = 'RESIDENTIAL 2 FAMILY'
	OR parusedesc = 'RESIDENTIAL 3 FAMILY'
	OR parusedesc = 'RESIDENTIAL STRUCTURE ON COMMERCIAL LAND'
	OR parusedesc = 'RESIDENTIAL UNDER CONSTRUCTION'
	OR parusedesc = 'RESIDENTIAL UNDER CONSTRUCTION/LONG TERM'
	OR parusedesc = 'RESIDENTIAL VACANT';


--NOW, COMBINE ALL POTENTIAL RESIDENTIAL PARCELS INTO ONE TABLE

--DROP TABLE public."allresidential_2019"

CREATE TABLE AllResidential_2019
AS SELECT * FROM public."nc_alleghany_parcels_poly" UNION
	SELECT * FROM public."nc_ashe_parcels_poly_2019_03_28" UNION
	SELECT * FROM public."nc_avery_parcels_poly" UNION
	SELECT * FROM public."nc_caldwell_parcels_poly" UNION
	SELECT * FROM public."wataugaresidential" UNION
	SELECT * FROM public."wilkesresidential";







--START HERE *********

--Zone pricing SQL statements
--FOLLOW THIS TEMPLATE FOR ALL ZONE + PRICING QUERIES	
DROP TABLE public."Zone1aKeepers"
SELECT res.* 
INTO Zone1aKeepers
FROM public."Zone1a" AS z1a, public."AllResidential_2019" AS res
WHERE st_intersects(z1a.geom, res.the_geom)
	AND res.parval > 150000;

DROP TABLE public."Zone1bKeepers"
SELECT res.* 
INTO Zone1bKeepers
FROM public."Zone1b" AS z1b, public."AllKeepers2018Update" AS res
WHERE st_intersects(z1b.geom, res.the_geom)
	AND res.parval > 225000;
	
DROP TABLE public."Zone1cKeepers"
SELECT res.* 
INTO Zone1cKeepers
FROM public."Zone1c" AS z1c, public."AllKeepers2018Update" AS res
WHERE st_intersects(z1c.geom, res.the_geom)
	AND res.parval > 250000;
	
DROP TABLE public."Zone1dKeepers"
SELECT res.* 
INTO Zone1dKeepers
FROM public."Zone1d" AS z1d, public."AllKeepers2018Update" AS res
WHERE st_intersects(z1d.geom, res.the_geom)
	AND res.parval > 250000;	

DROP TABLE public."Zone1eKeepers"
SELECT res.* 
INTO Zone1eKeepers
FROM public."Zone1e" AS z1e, public."AllKeepers2018Update" AS res
WHERE st_intersects(z1e.geom, res.the_geom)
	AND res.parval > 400000;
	
DROP TABLE public."Zone1fKeepers"
SELECT res.* 
INTO Zone1fKeepers
FROM public."Zone1f" AS z1f, public."AllKeepers2018Update" AS res
WHERE st_intersects(z1f.geom, res.the_geom)
	AND res.parval > 400000;
	
DROP TABLE public."Zone1gKeepers"
SELECT res.* 
INTO Zone1gKeepers
FROM public."Zone1g" AS z1g, public."AllKeepers2018Update" AS res
WHERE st_intersects(z1g.geom, res.the_geom)
	AND res.parval > 250000;
	
DROP TABLE public."Zone1hKeepers"
SELECT res.* 
INTO Zone1hKeepers
FROM public."Zone1h" AS z1h, public."AllKeepers2018Update" AS res
WHERE st_intersects(z1h.geom, res.the_geom)
	AND res.parval > 500000;
	
DROP TABLE public."Zone1iKeepers"
SELECT res.* 
INTO Zone1iKeepers
FROM public."Zone1i" AS z1i, public."AllKeepers2018Update" AS res
WHERE st_intersects(z1i.geom, res.the_geom)
	AND res.parval > 350000;
	
DROP TABLE public."Zone1jKeepers"
SELECT res.* 
INTO Zone1jKeepers
FROM public."Zone1j" AS z1j, public."AllKeepers2018Update" AS res
WHERE st_intersects(z1j.geom, res.the_geom)
	AND res.parval > 500000;
	
DROP TABLE public."Zone2aKeepers"
SELECT res.* 
INTO Zone2aKeepers
FROM public."Zone2a" AS z2a, public."AllKeepers2018Update" AS res
WHERE st_intersects(z2a.geom, res.the_geom)
	AND res.parval > 150000;
	
DROP TABLE public."Zone2bKeepers"
SELECT res.* 
INTO Zone2bKeepers
FROM public."Zone2b" AS z2b, public."AllKeepers2018Update" AS res
WHERE st_intersects(z2b.geom, res.the_geom)
	AND res.parval > 225000;
	
DROP TABLE public."Zone2cKeepers"
SELECT res.* 
INTO Zone2cKeepers
FROM public."Zone2c" AS z2c, public."AllKeepers2018Update" AS res
WHERE st_intersects(z2c.geom, res.the_geom)
	AND res.parval > 275000;
	
DROP TABLE public."Zone2dKeepers"
SELECT res.* 
INTO Zone2dKeepers
FROM public."Zone2d" AS z2d, public."AllKeepers2018Update" AS res
WHERE st_intersects(z2d.geom, res.the_geom)
	AND res.parval > 300000;
	
DROP TABLE public."Zone2eKeepers"
SELECT res.* 
INTO Zone2eKeepers
FROM public."Zone2e" AS z2e, public."AllKeepers2018Update" AS res
WHERE st_intersects(z2e.geom, res.the_geom)
	AND res.parval > 350000;
	
DROP TABLE public."Zone2fKeepers"
SELECT res.* 
INTO Zone2fKeepers
FROM public."Zone2f" AS z2f, public."AllKeepers2018Update" AS res
WHERE st_intersects(z2f.geom, res.the_geom)
	AND res.parval > 350000;
	
DROP TABLE public."Zone2gKeepers"
SELECT res.* 
INTO Zone2gKeepers
FROM public."Zone2g" AS z2g, public."AllKeepers2018Update" AS res
WHERE st_intersects(z2g.geom, res.the_geom)
	AND res.parval > 400000;	
	
DROP TABLE public."Zone2hKeepers"
SELECT res.* 
INTO Zone2hKeepers
FROM public."Zone2h" AS z2h, public."AllKeepers2018Update" AS res
WHERE st_intersects(z2h.geom, res.the_geom)
	AND res.parval > 500000;
	
DROP TABLE public."Zone2iKeepers"
SELECT res.* 
INTO Zone2iKeepers
FROM public."Zone2i" AS z2i, public."AllKeepers2018Update" AS res
WHERE st_intersects(z2i.geom, res.the_geom)
	AND res.parval > 700000;
	
DROP TABLE public."Zone2jKeepers"
SELECT res.* 
INTO Zone2jKeepers
FROM public."Zone2j" AS z2j, public."AllKeepers2018Update" AS res
WHERE st_intersects(z2j.geom, res.the_geom)
	AND res.parval > 700000;
	
DROP TABLE public."Zone3aKeepers"
SELECT res.* 
INTO Zone3aKeepers
FROM public."Zone3a" AS z3a, public."AllKeepers2018Update" AS res
WHERE st_intersects(z3a.geom, res.the_geom)
	AND res.parval > 150000;
	
DROP TABLE public."Zone3bKeepers"
SELECT res.* 
INTO Zone3bKeepers
FROM public."Zone3b" AS z3b, public."AllKeepers2018Update" AS res
WHERE st_intersects(z3b.geom, res.the_geom)
	AND res.parval > 150000;
	
DROP TABLE public."Zone3cKeepers"
SELECT res.* 
INTO Zone3cKeepers
FROM public."Zone3c" AS z3c, public."AllKeepers2018Update" AS res
WHERE st_intersects(z3c.geom, res.the_geom)
	AND res.parval > 200000;
	
DROP TABLE public."Zone3dKeepers"
SELECT res.* 
INTO Zone3dKeepers
FROM public."Zone3d" AS z3d, public."AllKeepers2018Update" AS res
WHERE st_intersects(z3d.geom, res.the_geom)
	AND res.parval > 200000;
	
DROP TABLE public."Zone3eKeepers"
SELECT res.* 
INTO Zone3eKeepers
FROM public."Zone3e" AS z3e, public."AllKeepers2018Update" AS res
WHERE st_intersects(z3e.geom, res.the_geom)
	AND res.parval > 300000;
	
DROP TABLE public."Zone3fKeepers"
SELECT res.* 
INTO Zone3fKeepers
FROM public."Zone3f" AS z3f, public."AllKeepers2018Update" AS res
WHERE st_intersects(z3f.geom, res.the_geom)
	AND res.parval > 400000;
	
DROP TABLE public."Zone3gKeepers"
SELECT res.* 
INTO Zone3gKeepers
FROM public."Zone3g" AS z3g, public."AllKeepers2018Update" AS res
WHERE st_intersects(z3g.geom, res.the_geom)
	AND res.parval > 400000;
	
DROP TABLE public."Zone4aKeepers"
SELECT res.* 
INTO Zone4aKeepers
FROM public."Zone4a" AS z4a, public."AllKeepers2018Update" AS res
WHERE st_intersects(z4a.geom, res.the_geom)
	AND res.parval > 150000;
	
DROP TABLE public."Zone4bKeepers"
SELECT res.* 
INTO Zone4bKeepers
FROM public."Zoneba" AS z4b, public."AllKeepers2018Update" AS res
WHERE st_intersects(z4b.geom, res.the_geom);
--Includes all properties.

DROP TABLE public."Zone4cKeepers"
SELECT res.* 
INTO Zone4cKeepers
FROM public."Zone4c" AS z4c, public."AllKeepers2018Update" AS res
WHERE st_intersects(z4c.geom, res.the_geom)
	AND res.parval > 200000;
	
DROP TABLE public."Zone4dKeepers"
SELECT res.* 
INTO Zone4dKeepers
FROM public."Zone4d" AS z4d, public."AllKeepers2018Update" AS res
WHERE st_intersects(z4d.geom, res.the_geom)
	AND res.parval > 250000;
	
DROP TABLE public."Zone4eKeepers"
SELECT res.* 
INTO Zone4eKeepers
FROM public."Zone4e" AS z4e, public."AllKeepers2018Update" AS res
WHERE st_intersects(z4e.geom, res.the_geom)
	AND res.parval > 150000;
	
DROP TABLE public."Zone4fKeepers"
SELECT res.* 
INTO Zone4fKeepers
FROM public."Zone4f" AS z4f, public."AllKeepers2018Update" AS res
WHERE st_intersects(z4f.geom, res.the_geom)
	AND res.parval > 350000;
	
DROP TABLE public."Zone4gKeepers"
SELECT res.* 
INTO Zone4gKeepers
FROM public."Zone4g" AS z4g, public."AllKeepers2018Update" AS res
WHERE st_intersects(z4g.geom, res.the_geom);
--Includes all parcels

DROP TABLE public."Zone4hKeepers"
SELECT res.* 
INTO Zone4hKeepers
FROM public."Zone4h" AS z4h, public."AllKeepers2018Update" AS res
WHERE st_intersects(z4h.geom, res.the_geom)
	AND res.parval > 300000;
	
DROP TABLE public."Zone5aKeepers"
SELECT res.* 
INTO Zone5aKeepers
FROM public."Zone5a" AS z5a, public."AllKeepers2018Update" AS res
WHERE st_intersects(z5a.geom, res.the_geom)
	AND res.parval > 150000;
	
DROP TABLE public."Zone5bKeepers"
SELECT res.* 
INTO Zone5bKeepers
FROM public."Zone5b" AS z5b, public."AllKeepers2018Update" AS res
WHERE st_intersects(z5b.geom, res.the_geom)
	AND res.parval > 200000;
	
DROP TABLE public."Zone5cKeepers"
SELECT res.* 
INTO Zone5cKeepers
FROM public."Zone5c" AS z5c, public."AllKeepers2018Update" AS res
WHERE st_intersects(z5c.geom, res.the_geom)
	AND res.parval > 250000;
	
DROP TABLE public."Zone5dKeepers"
SELECT res.* 
INTO Zone5dKeepers
FROM public."Zone5d" AS z5d, public."AllKeepers2018Update" AS res
WHERE st_intersects(z5d.geom, res.the_geom)
	AND res.parval > 200000;
	
DROP TABLE public."Zone5eKeepers"
SELECT res.* 
INTO Zone5eKeepers
FROM public."Zone5e" AS z5e, public."AllKeepers2018Update" AS res
WHERE st_intersects(z5e.geom, res.the_geom)
	AND res.parval > 200000;
	
DROP TABLE public."Zone5fKeepers"
SELECT res.* 
INTO Zone5fKeepers
FROM public."Zone5f" AS z5f, public."AllKeepers2018Update" AS res
WHERE st_intersects(z5f.geom, res.the_geom)
	AND res.parval > 300000;
	
DROP TABLE public."Zone5gKeepers"
SELECT res.* 
INTO Zone5gKeepers
FROM public."Zone5g" AS z5g, public."AllKeepers2018Update" AS res
WHERE st_intersects(z5g.geom, res.the_geom)
	AND res.parval > 300000;
	
DROP TABLE public."Zone5hKeepers"
SELECT res.* 
INTO Zone5hKeepers
FROM public."Zone5h" AS z5h, public."AllKeepers2018Update" AS res
WHERE st_intersects(z5h.geom, res.the_geom)
	AND res.parval > 300000;
	
DROP TABLE public."Zone5iKeepers"
SELECT res.* 
INTO Zone5iKeepers
FROM public."Zone5i" AS z5i, public."AllKeepers2018Update" AS res
WHERE st_intersects(z5i.geom, res.the_geom)
	AND res.parval > 400000;
	
DROP TABLE public."Zone5jKeepers"
SELECT res.* 
INTO Zone5jKeepers
FROM public."Zone5j" AS z5j, public."AllKeepers2018Update" AS res
WHERE st_intersects(z5j.geom, res.the_geom)
	AND res.parval > 700000;
	
DROP TABLE public."Zone5kKeepers"
SELECT res.* 
INTO Zone5kKeepers
FROM public."Zone5k" AS z5k, public."AllKeepers2018Update" AS res
WHERE st_intersects(z5k.geom, res.the_geom)
	AND res.parval > 250000;

DROP TABLE public."Zone5lKeepers"
SELECT res.* 
INTO Zone5lKeepers
FROM public."Zone5l" AS z5l, public."AllKeepers2018Update" AS res
WHERE st_intersects(z5l.geom, res.the_geom)
	AND res.parval > 400000;
	
DROP TABLE public."Zone5mKeepers"
SELECT res.* 
INTO Zone5mKeepers
FROM public."Zone5m" AS z5m, public."AllKeepers2018Update" AS res
WHERE st_intersects(z5m.geom, res.the_geom)
	AND res.parval > 500000;
	
DROP TABLE public."Zone5nKeepers"
SELECT res.* 
INTO Zone5nKeepers
FROM public."Zone5n" AS z5n, public."AllKeepers2018Update" AS res
WHERE st_intersects(z5n.geom, res.the_geom)
	AND res.parval > 700000;



