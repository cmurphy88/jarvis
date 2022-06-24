
-- adding data to the home table --
INSERT INTO home (home_name) VALUES ('My First Home');
INSERT INTO home (home_name) VALUES ('My Belfast Home');
INSERT INTO home (home_name) VALUES ('My Fermanagh Home');

-- creating users for the table --
INSERT INTO "user" (first_name, last_name, email, password)
    VALUES ('Conor', 'Murphy', 'conormurphy9966@gmail.com', 'password');
INSERT INTO "user" (first_name, last_name, email, password)
    VALUES ('Niamh', 'Doherty', 'ndoherty@gmail.com', 'password123');

-- home_user table --
INSERT INTO home_user (home_id, user_id, is_admin)
    VALUES (2, 1, TRUE);
INSERT INTO home_user (home_id, user_id, is_admin)
    VALUES (3, 2, FALSE);

-- camera table --
INSERT INTO camera (ip_address) VALUES ('180.180.443');
INSERT INTO camera (ip_address) VALUES ('188.190.456');

-- room --
INSERT INTO room (room_name, home_id, camera_id)
    VALUES ('Living Room', 2, 1);
INSERT INTO room (room_name, home_id, camera_id)
    VALUES ('Kitchen', 2, 2);

-- user hierarchy --
INSERT INTO user_hierarchy (room_id, user_id, user_order)
    VALUES(1, 1, 1);
INSERT INTO user_hierarchy (room_id, user_id, user_order)
    VALUES(1, 2, 2);

-- routine --
INSERT INTO routine (room_id, user_id, start_time, end_time)
    VALUES (1, 1, '10:00', '10:59');
INSERT INTO routine (room_id, user_id, start_time, end_time)
    VALUES (1, 2, '11:00', '11:59');

-- media --
INSERT INTO media (ip_address) VALUES ('180:888:999');
INSERT INTO media (ip_address) VALUES ('167:344:900');

-- media routine setting --
INSERT INTO media_routine_setting (media_id, routine_id, media_url, is_active, is_playing)
    VALUES (1, 1, 'google.com', TRUE, FALSE);
INSERT INTO media_routine_setting (media_id, routine_id, media_url, is_active, is_playing)
    VALUES (1, 2, 'youtube.com', TRUE, TRUE);

-- trv --
INSERT INTO trv (ip_address) VALUES ('213:456:686');
INSERT INTO trv (ip_address) VALUES ('456:112:998');

-- trv routine settings --
INSERT INTO trv_routine_setting (trv_id, routine_id, temperature, is_active)
    VALUES (1, 1, 21, TRUE);
INSERT INTO trv_routine_setting (trv_id, routine_id, temperature, is_active)
    VALUES (1, 2, 25, FALSE);

-- light --
INSERT INTO light (ip_address) VALUES ('123:678:987');
INSERT INTO light (ip_address) VALUES ('321:678:789');

-- light routine settings --
INSERT INTO light_routine_setting (light_id, routine_id, brightness, is_active)
    VALUES (1, 1, 50, TRUE);
INSERT INTO light_routine_setting (light_id, routine_id, brightness, is_active)
    VALUES (1, 2, 80, FALSE);

-- routine time entries --
INSERT INTO routine_time_entries (routine_id, time_entry)
    VALUES (1, '2022-06-22 19:10:25-07');
INSERT INTO routine_time_entries (routine_id, time_entry)
    VALUES (1, '2022-06-26 11:10:25-07');
INSERT INTO routine_time_entries (routine_id, time_entry)
    VALUES (2, '2022-06-20 19:10:25-07');

-- routine alert --
INSERT INTO routine_alert (message, routine_id)
    VALUES ('unrecognised face in the living room', 1);
INSERT INTO routine_alert (message, routine_id)
    VALUES ('unrecognised face in the kitchen, would you like to add them to the house?', 2);




