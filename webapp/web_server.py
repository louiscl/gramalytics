from bottle import run, route, request, static_file, template
import time

# "."" bc launching from route
from .sql_requests import SqlRequest
import sqlite3
import config

def start():
    # Connect DB:
    conn = sqlite3.connect(config.DATABASE_PATH)
    cur = conn.cursor()

    @route("/webapp/css/<filename:re:.*\.css>")
    def css(filename):
        return static_file(filename, root="webapp/css")

    @route("/", method="GET")
    def index():
        my_data = []
        empty_msg = ""
        # Search request
        if request.GET.submit:
            sql_query = SqlRequest().user_search(
                request.GET.username, request.GET.following, request.GET.follower
            )
            cur.execute(sql_query)
            data = cur.fetchall()
            my_data = [list(ele) for ele in data]
            for ele in my_data:
                ele.append(f"http://localhost:8080/add_liked_posts/{ele[0]}")
                ele.append(f"http://localhost:8080/liked_posts/{ele[0]}")
                ele.append(f"http://localhost:8080/deleted_user/{ele[0]}")
                ele.append(f"http://localhost:8080/users/{ele[0]}")
            if my_data == []:
                empty_msg = "There are no such users"

        output = template(
            "webapp/templates/landing_page",
            my_data=my_data,
            empty_msg=empty_msg,
            root="/webapp/",
        )
        return output

    @route("/users/<param>", method="GET")
    def users(param):
        if request.GET.submit:
            if request.GET.age == "":
                age = False
            else:
                age = request.GET.age
            update_command = SqlRequest().update_user(
                param, request.GET.following, request.GET.follower, age
            )
            cur.execute(update_command)

        sql_command = f"select * from users where username = '{param}'"
        cur.execute(sql_command)
        user_data = cur.fetchone()
        output = template("webapp/templates/user_page", user_data=user_data)
        return output

    @route("/new_user", method="GET")
    # sorry for the horrible code below - last minute changes. But it works :)
    def new_user():
        response = False
        message = ""
        if request.GET.submit:
            age = 0
            if request.GET.age != "":
                try:
                    int(request.GET.age)
                except:
                    return template(
                        "webapp/templates/new_user",
                        response=True,
                        message="Age must be an integer between 0-100",
                    )
            if request.GET.age != "" and (
                int(request.GET.age) < 0 or int(request.GET.age) > 100
            ):
                return template(
                    "webapp/templates/new_user",
                    response=True,
                    message="Age must be an integer between 0-100",
                )
            if request.GET.age != "":
                age = int(request.GET.age)
            username = request.GET.username.replace(" ", "_")

            sql_query = SqlRequest().new_user(
                username,
                int(request.GET.following),
                int(request.GET.follower),
                f"https://www.instagram.com/{username}",
                int(time.time()),
                age,
            )
            try:
                cur.execute(sql_query)
                message = f"{username} has been added"
            except:
                message = f"This user already exists!"
            response = True

        output = template(
            "webapp/templates/new_user", response=response, message=message
        )
        return output

    @route("/deleted_user/<username>")
    def search_result(username):
        sql_command = SqlRequest().delete_user(username)
        cur.execute(sql_command)
        output = template("webapp/templates/deleted_user")
        return output

    @route("/liked_posts/<param>", method="GET")
    def liked_posts(param):

        add_link = f"http://localhost:8080/add_liked_posts/{param}"

        sql_command = f"select * from liked_posts where username = '{param}'"
        cur.execute(sql_command)
        liked_posts = cur.fetchall()
        output = template(
            "webapp/templates/liked_posts",
            username=param,
            liked_posts=liked_posts,
            add_link=add_link,
        )
        return output

    @route("/add_liked_posts/<param>", method="GET")
    def add_liked_posts(param):

        message = ""
        response = False
        if request.GET.submit:
            sql_query = SqlRequest().add_liked_post(
                param,
                request.GET.content,
                request.GET.value,
                "https://www.instagram.com/fake_post",
                int(time.time()),
            )
            cur.execute(sql_query)
            message = f"Post has been added to {param}"
            response = True

        output = template(
            "webapp/templates/add_liked_posts",
            username=param,
            message=message,
            response=response,
            back_link=f"http://localhost:8080/liked_posts/{param}",
        )
        return output

    run(
        host="localhost",
        port=8080,
        reloader=True,
        debug=True,
    )
