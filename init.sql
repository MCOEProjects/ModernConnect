create table users
(
    user_id       varchar(120)      not null
        constraint users_pkey
            primary key,
    user_name     varchar(255)      not null,
    user_gender   integer default 0 not null,
    user_email    varchar(255)      not null
        constraint alumni_email
            unique,
    user_contact  varchar(12)       not null
        constraint alumni_contact
            unique,
    user_bio      text,
    user_photo    bytea,
    user_password varchar(255)      not null,
    user_type     integer default 0 not null
);

create table social_links
(
    alumni_student_id varchar(255) not null
        primary key,
    linked_in         varchar(255) null,
    github            varchar(255) null,
    twitter           varchar(255) null,
    portfolio         varchar(255) null
);

create table skills
(
    skill_id int          not null
        primary key,
    title    varchar(200) not null
);

create table skill_details
(
    alumni_student_id varchar(255) not null,
    skill_id          int          not null
        primary key
);

create table organization_details
(
    alumni_id           varchar(255) not null
        primary key,
    alumni_location     varchar(255) not null,
    alumni_organization varchar(255) not null,
    alumni_position     varchar(255) not null
);

create table education_details
(
    alumni_student_id varchar(255) not null
        primary key,
    branch            int          null,
    graduation_year   int          null
);

