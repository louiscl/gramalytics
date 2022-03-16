import sqlite3

database_path = "./data/local_database.db"
conn = sqlite3.connect(database_path)
cur = conn.cursor()


def test_account_searches_created():
    cur.execute("select count(*) from account_searches;")
    assert cur.fetchone()[0] > 0


def test_phrase_searches_created():
    cur.execute("select count(*) from phrase_searches;")
    assert cur.fetchone()[0] > 0


def test_ads_viewed_created():
    cur.execute("select count(*) from ads_viewed;")
    assert cur.fetchone()[0] > 0


def test_post_comments_created():
    cur.execute("select count(*) from post_comments;")
    assert cur.fetchone()[0] > 0


def test_authors_created():
    cur.execute("select count(*) from authors;")
    assert cur.fetchone()[0] > 0


def test_saved_posts_created():
    cur.execute("select count(*) from saved_posts;")
    assert cur.fetchone()[0] > 0


def test_liked_comments_created():
    cur.execute("select count(*) from liked_comments;")
    assert cur.fetchone()[0] > 0


def test_suggested_accounts_viewed_created():
    cur.execute("select count(*) from suggested_accounts_viewed;")
    assert cur.fetchone()[0] > 0


def test_liked_posts_created():
    cur.execute("select count(*) from liked_posts;")
    assert cur.fetchone()[0] > 0


def test_users_created():
    cur.execute("select count(*) from users;")
    assert cur.fetchone()[0] > 0


# def test_messages_created():
#     cur.execute("select count(*) from messages;")
#     assert cur.fetchone()[0] > 0


def test_viewed_posts_created():
    cur.execute("select count(*) from viewed_posts;")
    assert cur.fetchone()[0] > 0
