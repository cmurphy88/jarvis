CREATE TABLE home
(
    home_id     INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    home_name   VARCHAR(30)
);


CREATE TABLE "user"
(
    user_id         INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    first_name      VARCHAR(30),
    last_name       VARCHAR(30),
    email           VARCHAR(50),
    password        VARCHAR(30)
);


CREATE TABLE "home_user"
(
    home_user_id        INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    home_id             INT,
    user_id             INT,
    is_admin            BOOLEAN,
    CONSTRAINT fk_home_user_home_id FOREIGN KEY (home_id)
        REFERENCES home(home_id),
    CONSTRAINT fk_home_user_user_id FOREIGN KEY (user_id)
        REFERENCES "user"(user_id)
);


CREATE TABLE "camera"
(
    camera_id       INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    ip_address      VARCHAR(30)
);


CREATE TABLE "room"
(
    room_id     INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    room_name   VARCHAR(30),
    home_id     INT,
    camera_id   INT,

    CONSTRAINT fk_room_camera_camera_id FOREIGN KEY (camera_id)
        REFERENCES camera(camera_id),
    CONSTRAINT fk_room_home_home_id FOREIGN KEY (home_id)
        REFERENCES home(home_id)
);


CREATE TABLE "user_hierarchy"
(
    user_hierarchy_id       INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    room_id                 INT,
    user_id                 INT,
    user_order              INT,

    CONSTRAINT fk_user_hierarchy_room_room_id FOREIGN KEY (room_id)
        REFERENCES room(room_id),
    CONSTRAINT fk_user_hierarchy_user_user_id FOREIGN KEY (user_id)
        REFERENCES "user"(user_id)
);


CREATE  TABLE "media"
(
    media_id        INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    ip_address      VARCHAR(30)
);


CREATE TABLE "trv"
(
    trv_id      INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    ip_address  VARCHAR(30)
);

CREATE TABLE "light"
(
    light_id        INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    ip_address      VARCHAR(30)
);


CREATE TABLE "routine"
(
    routine_id      INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    room_id         INT,
    user_id         INT,
    start_time      TIME,
    end_time        TIME,

    CONSTRAINT fk_routine_room_room_id FOREIGN KEY (room_id)
        REFERENCES room(room_id),
    CONSTRAINT fk_routine_user_user_id FOREIGN KEY (user_id)
        REFERENCES "user"(user_id)
);


CREATE TABLE "media_routine_setting"
(
    media_routine_id        INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    media_id                INT,
    routine_id              INT,
    media_url               VARCHAR(100),
    is_active               BOOLEAN,
    is_playing              BOOLEAN,

    CONSTRAINT fk_media_routine_setting_media_id FOREIGN KEY (media_id)
        REFERENCES media(media_id),
    CONSTRAINT fk_media_routine_setting_routine_id FOREIGN KEY (routine_id)
        REFERENCES routine(routine_id)
);


CREATE TABLE "trv_routine_setting"
(
    trv_routine_id          INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    trv_id                  INT,
    routine_id              INT,
    temperature             INT,
    is_active               BOOLEAN,

    CONSTRAINT fk_trv_routine_setting_trv_id FOREIGN KEY (trv_id)
        REFERENCES trv(trv_id),
    CONSTRAINT fk_trv_routine_setting_routine_id FOREIGN KEY (routine_id)
        REFERENCES routine(routine_id)
);


CREATE TABLE "light_routine_setting"
(
    light_routine_id        INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    light_id                INT,
    routine_id              INT,
    brightness              INT,
    is_active               BOOLEAN,

    CONSTRAINT fk_light_routine_setting_light_id FOREIGN KEY (light_id)
        REFERENCES light(light_id),
    CONSTRAINT fk_light_routine_setting_routine_id FOREIGN KEY (routine_id)
        REFERENCES routine(routine_id)
);


CREATE TABLE "routine_time_entries"
(
    routine_time_entry_id           INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    routine_id                      INT,
    time_entry                      TIMESTAMP,

    CONSTRAINT fk_routine_time_entry_routine_id FOREIGN KEY (routine_id)
        REFERENCES routine(routine_id)
);

CREATE TABLE "routine_alert"
(
    alert_id        INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    "message"         VARCHAR(225),
    routine_id      INT,

    CONSTRAINT fk_routine_alert_routine_id FOREIGN KEY (routine_id)
        REFERENCES routine(routine_id)
);

