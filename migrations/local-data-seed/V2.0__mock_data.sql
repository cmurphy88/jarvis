-- home --
INSERT INTO home (name) VALUES ('My First Home');
INSERT INTO home (name) VALUES ('My Belfast Home');
INSERT INTO home (name) VALUES ('My Fermanagh House');

-- user --
INSERT INTO "users" (first_name, last_name, email, password)
    VALUES ('Conor', 'Murphy', 'conor@g.com', 'password');
INSERT INTO "users" (first_name, last_name, email, password)
    VALUES ('Niamh', 'Doherty', 'niamh@g.com', 'password123');

-- home user --
INSERT INTO home_user (home_id, user_id, is_admin)
    VALUES (1, 1, TRUE);
INSERT INTO home_user (home_id, user_id, is_admin)
    VALUES (3, 2, FALSE);


-- room --
INSERT INTO room (name, home_id)
    VALUES ('Living Room', 1);
INSERT INTO room (name, home_id)
    VALUES ('Kitchen', 1);
INSERT INTO room (name, home_id)
    VALUES ('Living Room', 3);
INSERT INTO room (name, home_id)
    VALUES ('Dining Room', 3);

-- room user entry --
INSERT INTO room_user_entry (room_id, user_id)
    VALUES (1, 1);
INSERT INTO room_user_entry (room_id, user_id)
    VALUES (3, 2);

-- room alert --
INSERT INTO room_alert (message, room_id)
    VALUES ('Unrecognised face in the Living Room', 1);
INSERT INTO room_alert (message, room_id)
    VALUES ('Unrecognised face in the Dining Room', 4);

-- room user hierarchy --
INSERT INTO room_user_hierarchy (room_id, user_id, user_order)
    VALUES (1, 1, 1);
INSERT INTO room_user_hierarchy (room_id, user_id, user_order)
    VALUES (1, 2, 2);

-- camera --
INSERT INTO camera (ip_address) VALUES ('123:234:345');
INSERT INTO camera (ip_address) VALUES ('345:765:231');
INSERT INTO camera (ip_address) VALUES ('999:888:777');

-- room camera --
INSERT INTO room_camera (room_id, camera_id)
    VALUES (1, 1);
INSERT INTO room_camera (room_id, camera_id)
    VALUES (2, 3);
INSERT INTO room_camera (room_id, camera_id)
    VALUES (3, 2);

-- routine --
INSERT INTO routine (room_id, user_id, start_time, end_time)
    VALUES (1, 1, '10:00', '10:59');
INSERT INTO routine (room_id, user_id, start_time, end_time)
    VALUES (3, 2, '12:00', '12:59');

-- routine time entries --
INSERT INTO routine_time_entries (routine_id, time_entry)
    VALUES (1, '2022-06-24 19:10:25-07');
INSERT INTO routine_time_entries (routine_id, time_entry)
    VALUES (1, '2022-06-24 10:55:21-07');
INSERT INTO routine_time_entries (routine_id, time_entry)
    VALUES (2, '2022-06-19 08:57:25-07');

-- media --
INSERT INTO media (ip_address, is_playing)
    VALUES ('222:333:444', TRUE);
INSERT INTO media (ip_address, is_playing)
    VALUES ('555:444:888', FALSE);

-- media routine setting --
INSERT INTO media_routine_setting (media_id, routine_id, media_url, is_active)
    VALUES (1, 1, 'youtube.com/despacito', TRUE);
INSERT INTO media_routine_setting (media_id, routine_id, media_url, is_active)
    VALUES (1, 2, 'youtube.com/drake_playlist', TRUE);

-- trv --
INSERT INTO trv (ip_address) VALUES ('454:545:454');
INSERT INTO trv (ip_address) VALUES ('777:898:100');

-- trv routine setting --
INSERT INTO trv_routine_setting (trv_id, routine_id, temperature, is_active)
    VALUES (1, 1, 24, TRUE);
iNSERT INTO trv_routine_setting (trv_id, routine_id, temperature, is_active)
    VALUES (1, 2, 26, TRUE);

-- light --
INSERT INTO light (ip_address) VALUES ('345:543:345');
INSERT INTO light (ip_address) VALUES ('111:000:180');

-- light routine setting --
INSERT INTO light_routine_setting (light_id, routine_id, brightness, is_active)
    VALUES (1, 1, 80, TRUE);
INSERT INTO light_routine_setting (light_id, routine_id, brightness, is_active)
    VALUES (2, 2, 90, TRUE);

-- media room --
INSERT INTO media_room (media_id, room_id) VALUES (1, 1);
INSERT INTO media_room (media_id, room_id) VALUES (2, 2);

-- trv room --
INSERT INTO trv_room (trv_id, room_id) VALUES (1, 1);
INSERT INTO trv_room (trv_id, room_id) VALUES (2, 2);

-- light room --
INSERT INTO light_room (light_id, room_id) VALUES (1, 1);
INSERT INTO light_room (light_id, room_id) VALUES (2, 2);


