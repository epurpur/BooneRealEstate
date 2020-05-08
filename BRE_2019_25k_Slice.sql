--Zone pricing SQL statements
--FOLLOW THIS TEMPLATE FOR ALL ZONE + PRICING QUERIES	

--DROP TABLE public."Zone1a25kSlice";
SELECT res.* 
INTO Zone1a25kSlice
FROM public."Zone1a" AS z1a, public."homes_df" AS res
WHERE st_intersects(z1a.geom, res.geom)
	AND res.parval > 125000 AND res.parval < 150000;

SELECT res.* 
INTO Zone1b25kSlice
FROM public."Zone1b" AS z1b, public."homes_df" AS res
WHERE st_intersects(z1b.geom, res.geom)
	AND res.parval > 200000 AND res.parval < 225000;
	
SELECT res.* 
INTO Zone1c25kSlice
FROM public."Zone1c" AS z1c, public."homes_df" AS res
WHERE st_intersects(z1c.geom, res.geom)
	AND res.parval > 225000 AND res.parval < 250000;
	
SELECT res.* 
INTO Zone1d25kSlice
FROM public."Zone1d" AS z1d, public."homes_df" AS res
WHERE st_intersects(z1d.geom, res.geom)
	AND res.parval > 225000 AND res.parval < 250000;
	
SELECT res.* 
INTO Zone1e25kSlice
FROM public."Zone1e" AS z1e, public."homes_df" AS res
WHERE st_intersects(z1e.geom, res.geom)
	AND res.parval > 375000 AND res.parval < 400000;
	
SELECT res.* 
INTO Zone1f25kSlice
FROM public."Zone1f" AS z1f, public."homes_df" AS res
WHERE st_intersects(z1f.geom, res.geom)
	AND res.parval > 375000 AND res.parval < 400000;
	
SELECT res.* 
INTO Zone1g25kSlice
FROM public."Zone1g" AS z1g, public."homes_df" AS res
WHERE st_intersects(z1g.geom, res.geom)
	AND res.parval > 225000 AND res.parval < 250000;
	
SELECT res.* 
INTO Zone1h25kSlice
FROM public."Zone1h" AS z1h, public."homes_df" AS res
WHERE st_intersects(z1h.geom, res.geom)
	AND res.parval > 475000 AND res.parval < 500000;
	
SELECT res.* 
INTO Zone1i25kSlice
FROM public."Zone1i" AS z1i, public."homes_df" AS res
WHERE st_intersects(z1i.geom, res.geom)
	AND res.parval > 325000 AND res.parval < 350000;
	
SELECT res.* 
INTO Zone1j25kSlice
FROM public."Zone1j" AS z1j, public."homes_df" AS res
WHERE st_intersects(z1j.geom, res.geom)
	AND res.parval > 475000 AND res.parval < 500000;
	
SELECT res.* 
INTO Zone2a25kSlice
FROM public."Zone2a" AS z2a, public."homes_df" AS res
WHERE st_intersects(z2a.geom, res.geom)
	AND res.parval > 125000 AND res.parval < 150000;
	
SELECT res.* 
INTO Zone2b25kSlice
FROM public."Zone2b" AS z2b, public."homes_df" AS res
WHERE st_intersects(z2b.geom, res.geom)
	AND res.parval > 200000 AND res.parval < 225000;
	
SELECT res.* 
INTO Zone2c25kSlice
FROM public."Zone2c" AS z2c, public."homes_df" AS res
WHERE st_intersects(z2c.geom, res.geom)
	AND res.parval > 250000 AND res.parval < 275000;
	
SELECT res.* 
INTO Zone2d25kSlice
FROM public."Zone2d" AS z2d, public."homes_df" AS res
WHERE st_intersects(z2d.geom, res.geom)
	AND res.parval > 275000 AND res.parval < 300000;
	
SELECT res.* 
INTO Zone2e25kSlice
FROM public."Zone2e" AS z2e, public."homes_df" AS res
WHERE st_intersects(z2e.geom, res.geom)
	AND res.parval > 325000 AND res.parval < 350000;
	
SELECT res.* 
INTO Zone2f25kSlice
FROM public."Zone2f" AS z2f, public."homes_df" AS res
WHERE st_intersects(z2f.geom, res.geom)
	AND res.parval > 325000 AND res.parval < 350000;
	
SELECT res.* 
INTO Zone2g25kSlice
FROM public."Zone2g" AS z2g, public."homes_df" AS res
WHERE st_intersects(z2g.geom, res.geom)
	AND res.parval > 375000 AND res.parval < 400000;
	
SELECT res.* 
INTO Zone2h25kSlice
FROM public."Zone2h" AS z2h, public."homes_df" AS res
WHERE st_intersects(z2h.geom, res.geom)
	AND res.parval > 475000 AND res.parval < 500000;
	
SELECT res.* 
INTO Zone2i25kSlice
FROM public."Zone2i" AS z2i, public."homes_df" AS res
WHERE st_intersects(z2i.geom, res.geom)
	AND res.parval > 675000 AND res.parval < 700000;
	
SELECT res.* 
INTO Zone2j25kSlice
FROM public."Zone2j" AS z2j, public."homes_df" AS res
WHERE st_intersects(z2j.geom, res.geom)
	AND res.parval > 675000 AND res.parval < 700000;
	
SELECT res.* 
INTO Zone3a25kSlice
FROM public."Zone3a" AS z3a, public."homes_df" AS res
WHERE st_intersects(z3a.geom, res.geom)
	AND res.parval > 125000 AND res.parval < 150000;
	
SELECT res.* 
INTO Zone3b25kSlice
FROM public."Zone3b" AS z3b, public."homes_df" AS res
WHERE st_intersects(z3b.geom, res.geom)
	AND res.parval > 125000 AND res.parval < 150000;
	
SELECT res.* 
INTO Zone3c25kSlice
FROM public."Zone3c" AS z3c, public."homes_df" AS res
WHERE st_intersects(z3c.geom, res.geom)
	AND res.parval > 175000 AND res.parval < 200000;
	
SELECT res.* 
INTO Zone3d25kSlice
FROM public."Zone3d" AS z3d, public."homes_df" AS res
WHERE st_intersects(z3d.geom, res.geom)
	AND res.parval > 175000 AND res.parval < 200000;
	
SELECT res.* 
INTO Zone3e25kSlice
FROM public."Zone3e" AS z3e, public."homes_df" AS res
WHERE st_intersects(z3e.geom, res.geom)
	AND res.parval > 275000 AND res.parval < 300000;
	
SELECT res.* 
INTO Zone3f25kSlice
FROM public."Zone3f" AS z3f, public."homes_df" AS res
WHERE st_intersects(z3f.geom, res.geom)
	AND res.parval > 375000 AND res.parval < 400000;
	
SELECT res.* 
INTO Zone3g25kSlice
FROM public."Zone3g" AS z3g, public."homes_df" AS res
WHERE st_intersects(z3g.geom, res.geom)
	AND res.parval > 375000 AND res.parval < 400000;
	
SELECT res.* 
INTO Zone4a25kSlice
FROM public."Zone4a" AS z4a, public."homes_df" AS res
WHERE st_intersects(z4a.geom, res.geom)
	AND res.parval > 125000 AND res.parval < 150000;

--Skip 4b (includes all houses already)

SELECT res.* 
INTO Zone4c25kSlice
FROM public."Zone4c" AS z4c, public."homes_df" AS res
WHERE st_intersects(z4c.geom, res.geom)
	AND res.parval > 175000 AND res.parval < 200000;
	
SELECT res.* 
INTO Zone4d25kSlice
FROM public."Zone4d" AS z4d, public."homes_df" AS res
WHERE st_intersects(z4d.geom, res.geom)
	AND res.parval > 225000 AND res.parval < 250000;
	
SELECT res.* 
INTO Zone4e25kSlice
FROM public."Zone4e" AS z4e, public."homes_df" AS res
WHERE st_intersects(z4e.geom, res.geom)
	AND res.parval > 125000 AND res.parval < 150000;
	
SELECT res.* 
INTO Zone4f25kSlice
FROM public."Zone4f" AS z4f, public."homes_df" AS res
WHERE st_intersects(z4f.geom, res.geom)
	AND res.parval > 325000 AND res.parval < 350000;
	
--Skip 4g (includes all houses already)
	
SELECT res.* 
INTO Zone4h25kSlice
FROM public."Zone4h" AS z4h, public."homes_df" AS res
WHERE st_intersects(z4h.geom, res.geom)
	AND res.parval > 275000 AND res.parval < 300000;
	
SELECT res.* 
INTO Zone5a25kSlice
FROM public."Zone5a" AS z5a, public."homes_df" AS res
WHERE st_intersects(z5a.geom, res.geom)
	AND res.parval > 125000 AND res.parval < 150000;
	
SELECT res.* 
INTO Zone5b25kSlice
FROM public."Zone5b" AS z5b, public."homes_df" AS res
WHERE st_intersects(z5b.geom, res.geom)
	AND res.parval > 225000 AND res.parval < 250000;
	
SELECT res.* 
INTO Zone5c25kSlice
FROM public."Zone5c" AS z5c, public."homes_df" AS res
WHERE st_intersects(z5c.geom, res.geom)
	AND res.parval > 225000 AND res.parval < 250000;
	
SELECT res.* 
INTO Zone5d25kSlice
FROM public."Zone5d" AS z5d, public."homes_df" AS res
WHERE st_intersects(z5d.geom, res.geom)
	AND res.parval > 175000 AND res.parval < 200000;
	
SELECT res.* 
INTO Zone5e25kSlice
FROM public."Zone5e" AS z5e, public."homes_df" AS res
WHERE st_intersects(z5e.geom, res.geom)
	AND res.parval > 175000 AND res.parval < 200000;
	
SELECT res.* 
INTO Zone5f25kSlice
FROM public."Zone5f" AS z5f, public."homes_df" AS res
WHERE st_intersects(z5f.geom, res.geom)
	AND res.parval > 275000 AND res.parval < 300000;
	
SELECT res.* 
INTO Zone5g25kSlice
FROM public."Zone5g" AS z5g, public."homes_df" AS res
WHERE st_intersects(z5g.geom, res.geom)
	AND res.parval > 275000 AND res.parval < 300000;
	
SELECT res.* 
INTO Zone5h25kSlice
FROM public."Zone5h" AS z5h, public."homes_df" AS res
WHERE st_intersects(z5h.geom, res.geom)
	AND res.parval > 275000 AND res.parval < 300000;
	
SELECT res.* 
INTO Zone5i25kSlice
FROM public."Zone5i" AS z5i, public."homes_df" AS res
WHERE st_intersects(z5i.geom, res.geom)
	AND res.parval > 375000 AND res.parval < 400000;
	
SELECT res.* 
INTO Zone5j25kSlice
FROM public."Zone5j" AS z5j, public."homes_df" AS res
WHERE st_intersects(z5j.geom, res.geom)
	AND res.parval > 675000 AND res.parval < 700000;
	
SELECT res.* 
INTO Zone5k25kSlice
FROM public."Zone5k" AS z5k, public."homes_df" AS res
WHERE st_intersects(z5f.geom, res.geom)
	AND res.parval > 225000 AND res.parval < 250000;
	
SELECT res.* 
INTO Zone5l25kSlice
FROM public."Zone5l" AS z5l, public."homes_df" AS res
WHERE st_intersects(z5l.geom, res.geom)
	AND res.parval > 375000 AND res.parval < 400000;
	
SELECT res.* 
INTO Zone5m25kSlice
FROM public."Zone5m" AS z5m, public."homes_df" AS res
WHERE st_intersects(z5m.geom, res.geom)
	AND res.parval > 475000 AND res.parval < 500000;
	
SELECT res.* 
INTO Zone5n25kSlice
FROM public."Zone5n" AS z5n, public."homes_df" AS res
WHERE st_intersects(z5n.geom, res.geom)
	AND res.parval > 675000 AND res.parval < 700000;