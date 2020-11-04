# TwitterBot
A simple bot that tells who unfollowed you on twitter !

## Requirements:-
 
   **Python3 -** 
      You can download and install it from it's [official website](https://www.python.org/downloads/).
      **Tweepy** is a python library that helps you interact with your account via twitter api . [read docs for installation](http://docs.tweepy.org/en/latest/install.html)      
      
  **access keys from twitter** you need to apply for a developer account. when you have it twitter will give you 4 access keys which can be used in script to 
  connect with twitter via api. for this purpose you can watch many youtube videos (there are tons of it with very clear explanation !)
  
 ## How to Use :-
 when you get connected with access keys you can monitor any twitter users followers  so i recommend using a secondary account 
 
 
 (create one -> apply for developer account -> create app -> get keys ) so that you can send a DM to your original account
 with a customiszed output like " this person with username: ---- unfollowed you ".
 
 Download the  project. 
 ```
    git clone https://github.com/0x1h0b/TwitterBot.git
 ```
 or simply download the zip file .
 
 go inside the project folder
 
 Inside the keys.py paste your keys accordingly (save it)
 
 open terminal and cd into the project folder and run
 ```
  python3 bot.py
 ```
 AT first, as there is no local file , it will create one. so that next time when you run the script it starts comparing data from local_file.

**NOTE :-**  make sure you cange the username as by default it's my username inside the script ... 
 
   and  ```api.send_direct_message('user_id', msg) ``` uses user_id of the person you want to send DM, so make sure you change that.
 
 
## How does It work ?
Approach is pretty straight forward. when you run the script for the very first time ,it saves the current state (followers_ids ) of your twitter account into
a pickle file in the same folder . now when you run the script again it compares the current followers ids to the exsisiting local file (pickle file) and which 
ever is missing it grabs the screen_name and name for that user ids and sends a direct message to the original account 
and simultaneously overwrites the existing local_file with the new list of followers ids. (Thats how the pickle file gets updated )

## Automating the script :-

if you use Linux ,there is a inbuilt tool called crontab (google it if you don't know) it helps is scheduling scripts. 
you can use it to run the script every 6 hrs ,so that you don't have to check it again.

for this you need to modify the code  and remove all the user-interaction part where it asks a y/n question to perform specific task. and remove some
print() statements which gives the status of script..and that's it your good to go



