CREATE TABLE home
(
    id     INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    name   VARCHAR(30)
);


CREATE TABLE "users"
(
    id         INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    first_name      VARCHAR(30),
    last_name       VARCHAR(30),
    email           VARCHAR(50),
    password        VARCHAR(30)
);


CREATE TABLE "home_user"
(
    id        INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    home_id             INT,
    user_id             INT,
    is_admin            BOOLEAN,
    CONSTRAINT fk_home_user_home_id FOREIGN KEY (home_id)
        REFERENCES home(id),
    CONSTRAINT fk_home_user_user_id FOREIGN KEY (user_id)
        REFERENCES "users"(id)
);


CREATE TABLE "camera"
(
    id       INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    ip_address      VARCHAR(30)
);


CREATE TABLE "room"
(
    id     INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    name   VARCHAR(30),
    home_id     INT,

    CONSTRAINT fk_room_home_home_id FOREIGN KEY (home_id)
        REFERENCES home(id)
);

CREATE TABLE room_camera
(
    id          INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    room_id     INT,
    camera_id   INT,

    CONSTRAINT fk_room_camera_room_id FOREIGN KEY (room_id)
        REFERENCES room(id),
    CONSTRAINT fk_room_home_camera_id FOREIGN KEY (camera_id)
        REFERENCES camera(id)
);


CREATE TABLE "room_user_hierarchy"
(
    id                  INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    room_id             INT,
    user_id             INT,
    user_order          INT,

    CONSTRAINT fk_user_hierarchy_room_room_id FOREIGN KEY (room_id)
        REFERENCES room(id),
    CONSTRAINT fk_user_hierarchy_user_user_id FOREIGN KEY (user_id)
        REFERENCES "users"(id)
);


CREATE  TABLE "media"
(
    id              INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    ip_address      VARCHAR(30),
    is_playing      BOOLEAN
);


CREATE TABLE "trv"
(
    id      INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    ip_address  VARCHAR(30)
);

CREATE TABLE "light"
(
    id        INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    ip_address      VARCHAR(30)
);


CREATE TABLE "routine"
(
    id              INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    room_id         INT,
    user_id         INT,
    start_time      TIME,
    end_time        TIME,

    CONSTRAINT fk_routine_room_room_id FOREIGN KEY (room_id)
        REFERENCES room(id),
    CONSTRAINT fk_routine_user_user_id FOREIGN KEY (user_id)
        REFERENCES "users"(id)
);


CREATE TABLE "media_routine_setting"
(
    id        INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    media_id                INT,
    routine_id              INT,
    media_url               VARCHAR(100),
    is_active               BOOLEAN,

    CONSTRAINT fk_media_routine_setting_media_id FOREIGN KEY (media_id)
        REFERENCES media(id),
    CONSTRAINT fk_media_routine_setting_routine_id FOREIGN KEY (routine_id)
        REFERENCES routine(id)
);


CREATE TABLE "trv_routine_setting"
(
    id                      INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    trv_id                  INT,
    routine_id              INT,
    temperature             INT,
    is_active               BOOLEAN,

    CONSTRAINT fk_trv_routine_setting_trv_id FOREIGN KEY (trv_id)
        REFERENCES trv(id),
    CONSTRAINT fk_trv_routine_setting_routine_id FOREIGN KEY (routine_id)
        REFERENCES routine(id)
);


CREATE TABLE "light_routine_setting"
(
    id                      INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    light_id                INT,
    routine_id              INT,
    brightness              INT,
    is_active               BOOLEAN,

    CONSTRAINT fk_light_routine_setting_light_id FOREIGN KEY (light_id)
        REFERENCES light(id),
    CONSTRAINT fk_light_routine_setting_routine_id FOREIGN KEY (routine_id)
        REFERENCES routine(id)
);


CREATE TABLE "routine_time_entries"
(
    id           INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    routine_id                      INT,
    time_entry                      TIMESTAMP,

    CONSTRAINT fk_routine_time_entry_routine_id FOREIGN KEY (routine_id)
        REFERENCES routine(id)
);

CREATE TABLE "room_alert"
(
    id              INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    "message"       VARCHAR(225),
    room_id         INT,

    CONSTRAINT fk_routine_alert_routine_id FOREIGN KEY (room_id)
        REFERENCES room(id)
);


CREATE TABLE room_user_entry
(
    id          INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    room_id     INT,
    user_id     INT,

    CONSTRAINT fk_room_user_entry_room_id FOREIGN KEY (room_id)
        REFERENCES room(id),
    CONSTRAINT fk_room_user_entry_user_id FOREIGN KEY (user_id)
        REFERENCES "users"(id)
);


CREATE TABLE media_room
(
    id          INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    media_id    INT,
    room_id     INT,

    CONSTRAINT fk_media_room_media_id FOREIGN KEY (media_id)
        REFERENCES media(id),
    CONSTRAINT fk_media_room_room_id FOREIGN KEY (room_id)
        REFERENCES room(id)
);


CREATE TABLE trv_room
(
    id          INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    trv_id      INT,
    room_id     INT,

    CONSTRAINT fk_trv_room_trv_id FOREIGN KEY (trv_id)
        REFERENCES trv(id),
    CONSTRAINT fk_trv_room_room_id FOREIGN KEY (room_id)
        REFERENCES room(id)
);

CREATE TABLE light_room
(
    id          INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    light_id    INT,
    room_id     INT,

    CONSTRAINT fk_light_room_light_id FOREIGN KEY (light_id)
        REFERENCES light(id),
    CONSTRAINT fk_light_room_room_id FOREIGN KEY (room_id)
        REFERENCES room(id)
);

