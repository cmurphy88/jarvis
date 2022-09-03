
INSERT INTO routine (name, room_id, user_id, start_time, end_time)
    VALUES ('Wake me up', 1, 1, '09:00', '12:00');
INSERT INTO routine (name, room_id, user_id, start_time, end_time)
    VALUES ('Lunchtime Madness', 1, 1, '12:00', '15:00');
INSERT INTO routine (name, room_id, user_id, start_time, end_time)
    VALUES ('Winding Down', 1, 1, '15:00', '18:00');
INSERT INTO routine (name, room_id, user_id, start_time, end_time)
    VALUES ('Evening Gaming', 1, 1, '18:00', '21:00');
INSERT INTO routine (name, room_id, user_id, start_time, end_time)
    VALUES ('Bed Time', 1, 1, '21:00', '23:00');

-- light routine setting --
INSERT INTO light_routine_setting (light_id, routine_id, brightness, is_active)
    VALUES (1, 22, 100, TRUE);
INSERT INTO light_routine_setting (light_id, routine_id, brightness, is_active)
    VALUES (1, 23, 80, TRUE);
INSERT INTO light_routine_setting (light_id, routine_id, brightness, is_active)
    VALUES (1, 24, 75, TRUE);
INSERT INTO light_routine_setting (light_id, routine_id, brightness, is_active)
    VALUES (1, 25, 50, TRUE);
INSERT INTO light_routine_setting (light_id, routine_id, brightness, is_active)
    VALUES (1, 26, 40, TRUE);