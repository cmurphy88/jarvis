-- light room --
INSERT INTO light_room (light_id, room_id) VALUES (8, 1);
INSERT INTO light_room (light_id, room_id) VALUES (9, 1);

-- creating new routines --
INSERT INTO trv_routine_setting (trv_id, routine_id, temperature, is_active)
VALUES (1, 1, 28, true);

INSERT INTO light_routine_setting (light_id, routine_id, brightness, is_active)
VALUES (8, 1, 78, true);

INSERT INTO light_routine_setting (light_id, routine_id, brightness, is_active)
VALUES (9, 1, 60, true);

INSERT INTO media_routine_setting (media_id, routine_id, media_url, is_active)
VALUES (1, 1, 'spotify.co.uk/conormurphy/morning-vibes', true);