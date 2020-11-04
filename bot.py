import tweepy
import pickle
import sys
from keys import *

# below username and id is my twitter account , change it to the user you want to send message.

username = '0x1h0b'
my_userId = '3335776572'


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth, wait_on_rate_limit=True)


def main():

    followers_id = api.followers_ids(username)
    
    print('\nCurrent Followers : '+ str(len(followers_id))+'\n\n')
    
    try:
        data = pickle.load(open("local_db.p","rb"))
        unfollowers = [ i for i in data['followers_id'] if i not in followers_id]
        if len(unfollowers) > 0:
            print('\n{} People unfollowed you : \n'.format(len(unfollowers)))
            for i in unfollowers :
                try:
                    msg = ' {0} with username : @{1} unfollowed you !'.format(api.get_user(i).name,api.get_user(i).screen_name)
                except Exception as e:
                    msg = ' Error for User ID: {} '.format(i)+str(e)
                dm = api.send_direct_message(my_userId, msg)
                print( '** Check your Inbox **\n')
        else:
            print('\n ALL GOOD ! \n')
        ans = input("Save the current state of your twitter account ? (y/n) ")
        if ans.lower()=='y':
            data = {'followers_id': followers_id}
            pickle.dump(data,open("local_db.p","wb"))
        else:
            print('\n')
            sys.exit()
    except (IOError, pickle.PickleError, pickle.UnpicklingError):
        ans = input('No local file found !! Would you like to Save the Current state of your twitter account ? (y/n) ')
        if ans.lower()=='y':
            data = {'followers_id': followers_id}
            pickle.dump(data,open("local_db.p","wb"))
        else:
            print('\n')
            sys.exit()
    except Exception as e:
        msg = str(e)
        m = api.send_direct_message(my_userId, msg)
        print( '** Check your Inbox **')
        print('\n')
        sys.exit()


    

if __name__ == "__main__" :
    main()
