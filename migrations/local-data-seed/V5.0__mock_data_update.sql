INSERT INTO home (name) VALUES ('Test Home');

INSERT INTO room (name, home_id) VALUES ('Test Kitchen', 4);

INSERT INTO routine (name, room_id, user_id, start_time, end_time)
    VALUES ('Test Room', 5, 1, '13:00', '15:00');

INSERT INTO light (ip_address, name) VALUES ('111:222:333', 'Test Light1');
INSERT INTO light (ip_address, name) VALUES ('567:2662:4567', 'Test Light2');

INSERT INTO light_routine_setting (light_id, routine_id, brightness, is_active)
    VALUES (10, 4, 50, true);
INSERT INTO light_routine_setting (light_id, routine_id, brightness, is_active)
    VALUES (11, 4, 88, true);

INSERT INTO media (ip_address, is_playing, name) VALUES ('234523452345', true, 'Test Media1');

INSERT INTO media_routine_setting (media_id, routine_id, media_url, is_active)
    VALUES (3, 4, 'test@test.com/test', true);

INSERT INTO trv (ip_address, name) VALUES ('234523453', 'Test Trv1');

INSERT INTO trv_routine_setting (trv_id, routine_id, temperature, is_active)
    VALUES (1, 4, 33, false);
