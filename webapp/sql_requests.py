class SqlRequest:
    @classmethod
    def new_user(cls, username, following, follower, link, timestamp, age=0):
        return f"""
            INSERT INTO users
            (username, following, follower, link, age, timestamp)
            VALUES ('{username}', {following}, {follower}, '{link}', {age}, {timestamp});
        """

    @classmethod
    def delete_user(cls, username):
        return f"DELETE FROM users WHERE username = '{username}';"

    @classmethod
    def update_user(cls, username, following, follower, age):
        command = f"""
        UPDATE users
        SET
        following = {following},
        follower = {follower},
        age = {age}
        WHERE
        username = '{username}';
        """
        return command

    @classmethod
    def add_liked_post(cls, username, content, value, link, timestamp):
        command = f"""
        INSERT INTO liked_posts
        (username, content, value, link, timestamp)
        VALUES
        ('{username}', '{content}', '{value}','{link}', '{timestamp}');
        """
        return command

    @classmethod
    def user_search(cls, username, following, follower):
        if username == "":
            username = False
        if following == "":
            following = False
        if follower == "":
            follower = False

        sql_head = "SELECT username, following, follower, link from users"
        sql_tail = " limit 20;"

        if username and following and follower:
            sql_head = (
                sql_head
                + f" WHERE username like '%{username}%' AND following = {following} AND follower = {follower}"
            )
        elif username and following:
            sql_head = (
                sql_head
                + f" WHERE username like '%{username}%' AND following = {following}"
            )
        elif username and follower:
            sql_head = (
                sql_head
                + f" WHERE username like '%{username}%' AND follower = {follower}"
            )
        elif following and follower:
            sql_head = (
                sql_head + f" WHERE following = {following} AND follower = {follower}"
            )
        elif username:
            sql_head = sql_head + f" WHERE username like '%{username}%'"

        elif following:
            sql_head = sql_head + f" WHERE following = {following}"
        elif following:
            sql_head = sql_head + f" WHERE follower = {follower}"

        return sql_head + sql_tail


sql_command = """
    SELECT users.username, COUNT(post_interaction.timestamp) AS total_interaction
    FROM users
    join post_interaction
    USING(username)
    GROUP BY users.username HAVING following = 1
    ORDER BY total_interaction DESC
    LIMIT 1;
    """
