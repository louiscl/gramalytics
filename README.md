---

## ReadMe For Assigment P8

To run the project simply install p8/requirements.txt and in the p8 directory run:
   python3 app.py

Further information:
This will parse the input json file, create tables, populate the db and start the webserver.

I set P8 up as an independent project. But it still uses all sql scripts necessary from p1-7.

The main relation used for the project is the 'users' relation. The complementary one is 'liked_posts'.

Hints for using: 

Since it's based on cleansed real data, not all users will have liked posts. To find some that do, search for users that 'you are following' but that 'don't follow you'. Alternatively, just hit the search button without any arguments or search for 'Thomas_Jefferson_Grover_Cleveland'.

The wildcard search works for the username.

Existing liked posts in the database will all have the same content. Can be distinguished by time! 

## GramalytiX - Instagram Analytics 4 U

Common analytics software obtains access to your personal data and uses it for their own monetarization. GramalytiX keeps your data on your own machine while providing you with deep insights into your online behaviour as well as the information Facebook is gathering about you.

Use the app in three simple steps:

1. Request to obtain your personal data from Instagram - Use this link to see how to

2. Save your data in the 'input' folder

3. Run GramalytiX on your own machine
   python3 web_server.py

Notes:

You can also test the software without requesting your data by using the existing dummy data.
