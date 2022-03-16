from helper import open_json_file, execute_sql_commands
import config

class Parser:
    def __init__(self, db_cursor) -> None:
        self.db_cursor = db_cursor
        self.sql_dir = config.SQL_FILES_DIRECTORY
        self.input_dir = config.INPUT_DATA_DIRECTORY

    def create_schemas(self):
        execute_sql_commands(self.sql_dir + "/create_schemas.sql", self.db_cursor)

    def parse_and_save_all(self):
        self.create_schemas()
        self.load_users()
        self.load_post_comments()
        self.load_saved_posts()
        self.load_liked_posts()
        self.load_liked_comments()
        self.load_account_searches()
        self.load_phrase_searches()
        self.load_suggested_accounts_viewed()
        self.load_viewed_posts()
        self.load_authors()
        self.load_ads_viewed()

    def create_user_profile(self):
        pass
        # either create new json based on following and following
        # or build array of user information to use

    def load_users(self):
        # insert following
        full_path = self.input_dir + "/followers_and_following/following.json"
        following_list = open_json_file(full_path)
        for user in following_list["relationships_following"]:
            user_data = user["string_list_data"][0]
            user_insert_command = f"""
                INSERT INTO users
                (username, link, following, timestamp)
                VALUES
                ('{user_data["value"]}', '{user_data["href"]}', 1, {user_data["timestamp"]});
            """
            self.db_cursor.execute(user_insert_command)

        # insert followers
        full_path = self.input_dir + "/followers_and_following/followers.json"
        follower_list = open_json_file(full_path)
        for user in follower_list["relationships_followers"]:
            user_data = user["string_list_data"][0]
            # hacky idea: query user -> w python, if already exists (u are following) update to following too
            # if not: insert
            user_insert_command = f"""
                INSERT OR REPLACE INTO users
                (username, link, follower, following, timestamp)
                VALUES
                ('{user_data["value"]}', '{user_data["href"]}', 1, 1, {user_data["timestamp"]});
            """
            # this assumes I follow everyone back
            self.db_cursor.execute(user_insert_command)

    # load post comments
    def load_post_comments(self):
        full_path = self.input_dir + "/comments/post_comments.json"
        post_comments_list = open_json_file(full_path)
        for comment in post_comments_list["comments_media_comments"]:
            username = comment["title"]
            content = comment["string_list_data"][0]["value"]
            timestamp = comment["string_list_data"][0]["timestamp"]
            post_comment_insert_command = f"""
                INSERT INTO post_comments
                (username, content, timestamp)
                VALUES
                ('{username}', '{content}', {timestamp});
            """
            self.db_cursor.execute(post_comment_insert_command)

        # load posts I saved

    def load_saved_posts(self):
        file_path = "/saved/saved_posts.json"
        full_path = self.input_dir + file_path
        saved_posts_list = open_json_file(full_path)

        for saved_post in saved_posts_list["saved_saved_media"]:
            username = saved_post["string_map_data"]["Shared by"]["value"]
            link = saved_post["string_map_data"]["Shared by"]["href"]
            timestamp = saved_post["string_map_data"]["Shared by"]["timestamp"]

            saved_posts_insert_command = f"""
                INSERT INTO saved_posts
                (username, link, timestamp)
                VALUES
                ('{username}', '{link}', {timestamp});
            """
            self.db_cursor.execute(saved_posts_insert_command)

    # load posts I viewed
    def load_viewed_posts(self):
        file_path = "/ads_and_content/posts_viewed.json"
        full_path = self.input_dir + file_path
        viewed_posts_list = open_json_file(full_path)

        for viewed_post in viewed_posts_list["impressions_history_posts_seen"]:
            username = viewed_post["string_map_data"]["Author"]["value"]
            timestamp = viewed_post["string_map_data"]["Time"]["timestamp"]

            viewed_posts_insert_command = f"""
                INSERT INTO viewed_posts
                (username, timestamp)
                VALUES
                ('{username}', {timestamp});
            """
            self.db_cursor.execute(viewed_posts_insert_command)

    # load posts I liked
    def load_liked_posts(self):
        file_path = "/likes/liked_posts.json"
        full_path = self.input_dir + file_path
        liked_posts_list = open_json_file(full_path)
        for liked_post in liked_posts_list["likes_media_likes"]:
            username = liked_post["title"]
            link = liked_post["string_list_data"][0]["href"]
            value = liked_post["string_list_data"][0]["value"]
            timestamp = liked_post["string_list_data"][0]["timestamp"]
            liked_posts_insert_command = f"""
                INSERT INTO liked_posts
                (username, link, value, timestamp)
                VALUES
                ('{username}', '{link}', '{value}', {timestamp});
            """
            self.db_cursor.execute(liked_posts_insert_command)

    # load comments I liked
    def load_liked_comments(self):
        file_path = "/likes/liked_comments.json"
        full_path = self.input_dir + file_path
        liked_comments_list = open_json_file(full_path)
        for liked_post in liked_comments_list["likes_comment_likes"]:
            username = liked_post["title"]
            link = liked_post["string_list_data"][0]["href"]
            value = liked_post["string_list_data"][0]["value"]
            timestamp = liked_post["string_list_data"][0]["timestamp"]
            liked_comments_insert_command = f"""
                INSERT INTO liked_comments
                (username, link, value, timestamp)
                VALUES
                ('{username}', '{link}', '{value}', {timestamp});
            """
            self.db_cursor.execute(liked_comments_insert_command)

    # accounts I have searched for recently
    def load_account_searches(self):
        file_path = "/recent_searches/account_searches.json"
        full_path = self.input_dir + file_path
        recent_account_searches_list = open_json_file(full_path)
        for recent_search in recent_account_searches_list["searches_user"]:
            username = recent_search["string_map_data"]["Search"]["value"]
            timestamp = recent_search["string_map_data"]["Time"]["timestamp"]
            recent_acc_searches_insert_command = f"""
                INSERT INTO account_searches
                (username, timestamp)
                VALUES
                ('{username}', {timestamp});
            """
            self.db_cursor.execute(recent_acc_searches_insert_command)

    # phrases I have searched for recently
    def load_phrase_searches(self):
        file_path = "/recent_searches/word_or_phrase_searches.json"
        full_path = self.input_dir + file_path
        recent_phrase_searches_list = open_json_file(full_path)
        for recent_search in recent_phrase_searches_list["searches_keyword"]:
            username = recent_search["string_map_data"]["Search"]["value"]
            timestamp = recent_search["string_map_data"]["Time"]["timestamp"]
            recent_acc_searches_insert_command = f"""
                INSERT INTO phrase_searches
                (username, timestamp)
                VALUES
                ('{username}', {timestamp});
            """
            self.db_cursor.execute(recent_acc_searches_insert_command)

    # suggested accounts I have viewed
    def load_suggested_accounts_viewed(self):
        file_path = "/ads_and_content/suggested_accounts_viewed.json"
        full_path = self.input_dir + file_path
        suggested_accounts_viewed_list = open_json_file(full_path)
        for sug_account in suggested_accounts_viewed_list[
            "impressions_history_chaining_seen"
        ]:
            username = sug_account["string_map_data"]["Username"]["value"]
            timestamp = sug_account["string_map_data"]["Time"]["timestamp"]
            recent_acc_searches_insert_command = f"""
                INSERT INTO suggested_accounts_viewed
                (username, timestamp)
                VALUES
                ('{username}', {timestamp});
            """
            self.db_cursor.execute(recent_acc_searches_insert_command)

    # Based on ads viewed: Create ad authors (unique) and ads_viewed referring to authors
    # load ad authors
    def load_authors(self):
        # primary key attribute should keep it unique
        # IDEA: Load information about author from some api
        file_path = "/ads_and_content/ads_viewed.json"
        full_path = self.input_dir + file_path
        ads_viewed_list = open_json_file(full_path)
        for ad in ads_viewed_list["impressions_history_ads_seen"]:
            author_name = ad["string_map_data"]["Author"]["value"]
            timestamp = ad["string_map_data"]["Time"]["timestamp"]
            author_insert_command = f"""
                INSERT OR IGNORE INTO authors
                (author_name, timestamp)
                VALUES
                ('{author_name}', '{timestamp}')
            """
            self.db_cursor.execute(author_insert_command)

    # load advertisements I have viewed
    def load_ads_viewed(self):
        # primary key attribute should keep it unique
        file_path = "/ads_and_content/ads_viewed.json"
        full_path = self.input_dir + file_path
        ads_viewed_list = open_json_file(full_path)
        for ad in ads_viewed_list["impressions_history_ads_seen"]:
            author_name = ad["string_map_data"]["Author"]["value"]
            timestamp = ad["string_map_data"]["Time"]["timestamp"]
            author_insert_command = f"""
                INSERT INTO ads_viewed
                (author_name, timestamp)
                VALUES
                ('{author_name}', '{timestamp}')
            """
            self.db_cursor.execute(author_insert_command)