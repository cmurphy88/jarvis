-- home
INSERT INTO home (name) VALUES ('Test Home 1');
INSERT INTO home (name) VALUES ('Test Home 2');

-- home user
INSERT INTO home_user (home_id, user_id, is_admin) VALUES (4, 1, true);
INSERT INTO home_user (home_id, user_id, is_admin) VALUES (5, 1, true);

-- room
-- ids: 6, 7, 8, 9
INSERT INTO room (name, home_id) VALUES ('Test Room 1', 4);
INSERT INTO room (name, home_id) VALUES ('Test Room 2', 4);
INSERT INTO room (name, home_id) VALUES ('Test Room 3', 5);
INSERT INTO room (name, home_id) VALUES ('Test Room 4', 5);

-- light
-- id starts 12
INSERT INTO light (name, ip_address) VALUES ('Test Light 1', '1111');
INSERT INTO light (name, ip_address) VALUES ('Test Light 2', '1112');
INSERT INTO light (name, ip_address) VALUES ('Test Light 3', '1113');
INSERT INTO light (name, ip_address) VALUES ('Test Light 4', '1114');
INSERT INTO light (name, ip_address) VALUES ('Test Light 5', '1115');
INSERT INTO light (name, ip_address) VALUES ('Test Light 6', '1116');
INSERT INTO light (name, ip_address) VALUES ('Test Light 7', '1117');
INSERT INTO light (name, ip_address) VALUES ('Test Light 8', '1118');
INSERT INTO light (name, ip_address) VALUES ('Test Light 9', '1119');
INSERT INTO light (name, ip_address) VALUES ('Test Light 10', '11110');

-- add light to room
-- room 1
INSERT INTO light_room (light_id, room_id) VALUES (3, 5);
INSERT INTO light_room (light_id, room_id) VALUES (4, 5);
INSERT INTO light_room (light_id, room_id) VALUES (5, 5);
-- room 2
INSERT INTO light_room (light_id, room_id) VALUES (6, 6);
INSERT INTO light_room (light_id, room_id) VALUES (7, 6);
INSERT INTO light_room (light_id, room_id) VALUES (8, 6);
-- room 3
INSERT INTO light_room (light_id, room_id) VALUES (9, 7);
INSERT INTO light_room (light_id, room_id) VALUES (10, 7);
INSERT INTO light_room (light_id, room_id) VALUES (11, 7);
--room 4
INSERT INTO light_room (light_id, room_id) VALUES (12, 8);

-- media
-- id starts 5
INSERT INTO media (name, is_playing, ip_address) VALUES ('Test Media 1', true, '2111');
INSERT INTO media (name, is_playing, ip_address) VALUES ('Test Media 2', true, '2112');
INSERT INTO media (name, is_playing, ip_address) VALUES ('Test Media 3', true, '2113');
INSERT INTO media (name, is_playing, ip_address) VALUES ('Test Media 4', true, '2114');
INSERT INTO media (name, is_playing, ip_address) VALUES ('Test Media 5', true, '2115');
INSERT INTO media (name, is_playing, ip_address) VALUES ('Test Media 6', true, '2116');

-- add media to room
-- room 1
INSERT INTO media_room (media_id, room_id) VALUES (3, 5);
INSERT INTO media_room (media_id, room_id) VALUES (4, 5);
--room 2
INSERT INTO media_room (media_id, room_id) VALUES (5, 6);
--room 3
INSERT INTO media_room (media_id, room_id) VALUES (6, 7);
INSERT INTO media_room (media_id, room_id) VALUES (7, 7);
-- room 4
INSERT INTO media_room (media_id, room_id) VALUES (8, 8);

-- trv
-- id starts at 4
INSERT INTO trv (ip_address, name) VALUES ('3111', 'Test Trv 1');
INSERT INTO trv (ip_address, name) VALUES ('3112', 'Test Trv 2');
INSERT INTO trv (ip_address, name) VALUES ('3113', 'Test Trv 3');
INSERT INTO trv (ip_address, name) VALUES ('3114', 'Test Trv 4');
INSERT INTO trv (ip_address, name) VALUES ('3115', 'Test Trv 5');

-- add trv to room
-- room 1
INSERT INTO trv_room (trv_id, room_id) VALUES (3, 5);
--room 2
INSERT INTO trv_room (trv_id, room_id) VALUES (4, 6);
INSERT INTO trv_room (trv_id, room_id) VALUES (5, 6);
-- room 3
INSERT INTO trv_room (trv_id, room_id) VALUES (6, 7);
-- room 4
INSERT INTO trv_room (trv_id, room_id) VALUES (7, 8);

-- creating routines
-- id starts at 29
-- room 1
INSERT INTO routine (name, room_id, user_id, start_time, end_time)
    VALUES ('Test Routine 1', 5, 1, '12:00', '14:00');
INSERT INTO routine (name, room_id, user_id, start_time, end_time)
    VALUES ('Test Routine 2', 5, 1, '18:00', '19:00');
-- room 2
INSERT INTO routine (name, room_id, user_id, start_time, end_time)
    VALUES ('Test Routine 3', 6, 1, '13:00', '15:00');
INSERT INTO routine (name, room_id, user_id, start_time, end_time)
    VALUES ('Test Routine 4', 6, 1, '19:00', '20:00');
-- room 3
INSERT INTO routine (name, room_id, user_id, start_time, end_time)
    VALUES ('Test Routine 5', 7, 1, '13:00', '15:00');
INSERT INTO routine (name, room_id, user_id, start_time, end_time)
    VALUES ('Test Routine 6', 7, 1, '20:00', '21:00');
-- room 4
INSERT INTO routine (name, room_id, user_id, start_time, end_time)
    VALUES ('Test Routine 7', 8, 1, '13:00', '15:00');

-- light routine settings
-- routine 1
INSERT INTO light_routine_setting (light_id, routine_id, brightness, is_active)
    VALUES (3, 3, 100, true);
INSERT INTO light_routine_setting (light_id, routine_id, brightness, is_active)
    VALUES (4, 3, 95, true);
-- routine 2
INSERT INTO light_routine_setting (light_id, routine_id, brightness, is_active)
    VALUES (5, 4, 90, true);
-- routine 3
INSERT INTO light_routine_setting (light_id, routine_id, brightness, is_active)
    VALUES (6, 5, 85, true);
INSERT INTO light_routine_setting (light_id, routine_id, brightness, is_active)
    VALUES (7, 5, 80, true);
-- routine 4
INSERT INTO light_routine_setting (light_id, routine_id, brightness, is_active)
    VALUES (8, 6, 75, true);
-- routine 5
INSERT INTO light_routine_setting (light_id, routine_id, brightness, is_active)
    VALUES (9, 7, 70, true);
INSERT INTO light_routine_setting (light_id, routine_id, brightness, is_active)
    VALUES (10, 7, 65, true);
-- routine 6
INSERT INTO light_routine_setting (light_id, routine_id, brightness, is_active)
    VALUES (11, 8, 60, true);
-- routine 7
INSERT INTO light_routine_setting (light_id, routine_id, brightness, is_active)
    VALUES (12, 9, 55, true);

-- media routine settings
--routine 1
INSERT INTO media_routine_setting (media_id, routine_id, media_url, is_active)
    VALUES (3, 3, 'test.com/1', true);
-- routine 2
INSERT INTO media_routine_setting (media_id, routine_id, media_url, is_active)
    VALUES (3, 4, 'test.com/2', true);
-- routine 3
INSERT INTO media_routine_setting (media_id, routine_id, media_url, is_active)
    VALUES (4, 5, 'test.com/3', true);
-- routine 4
-- routine 5
INSERT INTO media_routine_setting (media_id, routine_id, media_url, is_active)
    VALUES (6, 7, 'test.com/5', true);
-- routine 6
INSERT INTO media_routine_setting (media_id, routine_id, media_url, is_active)
    VALUES (6, 8, 'test.com/6', true);
-- routine 7
INSERT INTO media_routine_setting (media_id, routine_id, media_url, is_active)
    VALUES (7, 9, 'test.com/7', true);

-- trv routine settings
-- routine 1
INSERT INTO trv_routine_setting (trv_id, routine_id, temperature, is_active)
    VALUES (3, 3, 28, true);
-- routine 2
-- routine 3
INSERT INTO trv_routine_setting (trv_id, routine_id, temperature, is_active)
    VALUES (4, 5, 27, true);
-- routine 4
INSERT INTO trv_routine_setting (trv_id, routine_id, temperature, is_active)
    VALUES (4, 6, 26, true);
-- routine 5
INSERT INTO trv_routine_setting (trv_id, routine_id, temperature, is_active)
    VALUES (5, 7, 25, true);
-- routine 6
-- routine 7
INSERT INTO trv_routine_setting (trv_id, routine_id, temperature, is_active)
    VALUES (6, 9, 24, true);
