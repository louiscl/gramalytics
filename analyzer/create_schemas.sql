DROP table IF EXISTS users;
DROP table IF EXISTS messages;
DROP table IF EXISTS post_comments;
DROP table IF EXISTS saved_posts;
DROP table IF EXISTS viewed_posts;
DROP table IF EXISTS liked_posts;
DROP table IF EXISTS liked_comments;
DROP table IF EXISTS account_searches;
DROP table IF EXISTS phrase_searches;
DROP table IF EXISTS suggested_accounts_viewed;
DROP table IF EXISTS authors;
DROP table IF EXISTS ads_viewed;


-- make name primary key?
CREATE TABLE users (
    -- ID integer primary key,
    username varchar,
    link varchar,
    age int DEFAULT 0,
    follower BIT DEFAULT 0,
    following BIT DEFAULT 0,
    timestamp int,
    primary key (username)
);

CREATE TABLE messages (
    sender_name varchar,
    receiver_name varchar,
    content varchar,
    timestamp int,
    foreign key (sender_name) references users,
    foreign key (receiver_name) references users
);

-- my comments on posts!
CREATE TABLE post_comments (
    username varchar,
    content varchar,
    timestamp int,
    foreign key (username) references users
);

-- posts I saved
CREATE TABLE saved_posts (
    username varchar,
    link varchar,
    timestamp int,
    foreign key (username) references users
);

-- posts I viewed
CREATE TABLE viewed_posts (
    username varchar,
    link varchar,
    content varchar DEFAULT "Post Content here",
    timestamp int,
    foreign key (username) references users
);

-- posts I liked
CREATE TABLE liked_posts (
    username varchar,
    link varchar,
    value varchar,
    content varchar DEFAULT "Post Content here",
    timestamp int,
    foreign key (username) references users
);

-- comments I liked
CREATE TABLE liked_comments (
    username varchar,
    link varchar,
    value varchar,
    content varchar DEFAULT "Comment content here",
    timestamp int,
    foreign key (username) references users
);

-- accounts I have searched for
CREATE TABLE account_searches (
    username varchar,
    timestamp int,
    foreign key (username) references users
);

-- phrases I have searched for
CREATE TABLE phrase_searches (
    username varchar,
    timestamp int,
    foreign key (username) references users
);

-- suggested accounts I viewed
CREATE TABLE suggested_accounts_viewed (
    username varchar,
    timestamp int,
    foreign key (username) references users
);

-- advertisement authors
CREATE TABLE authors (
    author_name varchar,
    timestamp int,
    primary key (author_name)
);

-- advertisements viewed
CREATE TABLE ads_viewed (
    author_name varchar,
    timestamp int,
    foreign key (author_name) references authors
);


