#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
import time
import re
import json

config_file = os.path.join(os.path.join(os.path.dirname(os.path.abspath(__file__))), 'config.json')

load = {}
try:
    with open(config_file, 'rb') as data:
        load.update(json.load(data))
except ValueError:
    print 'Error with configuration file'
    sys.exit(-1)

# MySQL connection
import MySQLdb

db = MySQLdb.connect(host=load.get('db_host'),      # your host, usually localhost
                     user=load.get('db_user'),      # your username
                     passwd=load.get('db_pass'),    # your password
                     db=load.get('db_name'))        # name of the data base

# you must create a Cursor object. It will let
#  you execute all the queries you need
cur = db.cursor()

bot_id = sys.argv[1]
bot_login = ""
bot_pass = ""

# Get data from database
try:
    numrows = cur.execute("SELECT * FROM bots WHERE bot_id = %s", bot_id)
    rows = cur.fetchall()
except MySQLdb.Error, e:
    try:
        print "MySQL Error [%d]: %s" % (e.args[0], e.args[1])
    except IndexError:
        print "MySQL Error: %s" % str(e)


if numrows > 0:
    for row in rows:
        bot_login = row[2]
        bot_pass = row[3]
        bot_like_per_day = row[5]
        bot_comments_per_day = row[6]
        bot_tag_list = row[7]
        
        if bot_tag_list is not None:
            line = bot_tag_list.split(",")
            new_line = []
            for item in line:
                new_line.append(re.sub('[@#]', '', item))
            
            bot_tag_list = new_line
        else:
            bot_tag_list = []
        
        bot_tag_blacklist = row[8]
        if bot_tag_blacklist is not None:
            line = bot_tag_blacklist.split(",")
            new_line = []
            for item in line:
                new_line.append(re.sub('[@#]', '', item))
            
            bot_tag_blacklist = new_line
        else:
            bot_tag_blacklist = []
        
        bot_max_like_for_one_tag = row[9]
        bot_follow_per_day = row[10]
        bot_follow_time = row[11]
        bot_unfollow_per_day = row[12]
        bot_unfollow_break_min = row[13]
        bot_unfollow_break_max = row[14]
        bot_log_mod = row[15]
        bot_proxy = row[16]
        bot_comment_list = row[17]
        
        bot_user_blacklist = row[18]
        if bot_user_blacklist is not None:
            line = bot_user_blacklist.split(",")
            new_line = []
            for item in line:
                new_line.append(re.sub('[@#]', '', item))
            
            bot_user_blacklist = dict((key, '') for key in new_line)
        else:
            bot_user_blacklist = {}
        
        bot_unfollow_whitelist = row[19]

    
    sys.path.append(os.path.join(sys.path[0], 'src'))
    
    from check_status import check_status
    from feed_scanner import feed_scanner
    from follow_protocol import follow_protocol
    from instabot import InstaBot
    from unfollow_protocol import unfollow_protocol
    
    bot = InstaBot(
        login = bot_login,
        password = bot_pass,
        like_per_day = bot_like_per_day,
        comments_per_day = bot_comments_per_day,
        tag_list = bot_tag_list,
        tag_blacklist = bot_tag_blacklist,
        user_blacklist = bot_user_blacklist,
        max_like_for_one_tag = bot_max_like_for_one_tag,
        follow_per_day = bot_follow_per_day,
        follow_time = bot_follow_time,
        unfollow_per_day = bot_unfollow_per_day,
        unfollow_break_min = bot_unfollow_break_min,
        unfollow_break_max = bot_unfollow_break_max,
        log_mod = bot_log_mod,
        proxy = '',
        # List of list of words, each of which will be used to generate comment
        # For example: "This shot feels wow!"
        comment_list=[["this", "the", "your"],
                      ["photo", "picture", "pic", "shot", "snapshot"],
                      ["is", "looks", "feels", "is really"],
                      ["great", "super", "good", "very good", "good", "wow",
                       "WOW", "cool", "GREAT","magnificent", "magical",
                       "very cool", "stylish", "beautiful", "so beautiful",
                       "so stylish", "so professional", "lovely",
                       "so lovely", "very lovely", "glorious","so glorious",
                       "very glorious", "adorable", "excellent", "amazing"],
                      [".", "..", "...", "!", "!!", "!!!"]],
        # Use unwanted_username_list to block usernames containing a string
        ## Will do partial matches; i.e. 'mozart' will block 'legend_mozart'
        ### 'free_followers' will be blocked because it contains 'free'
        unwanted_username_list=[
            'second', 'stuff', 'art', 'project', 'love', 'life', 'food', 'blog',
            'free', 'keren', 'photo', 'graphy', 'indo', 'travel', 'art', 'shop',
            'store', 'sex', 'toko', 'jual', 'online', 'murah', 'jam', 'kaos',
            'case', 'baju', 'fashion', 'corp', 'tas', 'butik', 'grosir', 'karpet',
            'sosis', 'salon', 'skin', 'care', 'cloth', 'tech', 'rental', 'kamera',
            'beauty', 'express', 'kredit', 'collection', 'impor', 'preloved',
            'follow', 'follower', 'gain', '.id', '_id', 'bags'
        ],
        unfollow_whitelist=[])
    while True:
    
        #print("# MODE 0 = ORIGINAL MODE BY LEVPASHA")
        #print("## MODE 1 = MODIFIED MODE BY KEMONG")
        #print("### MODE 2 = ORIGINAL MODE + UNFOLLOW WHO DON'T FOLLOW BACK")
        #print("#### MODE 3 = MODIFIED MODE : UNFOLLOW USERS WHO DON'T FOLLOW YOU BASED ON RECENT FEED")
        #print("##### MODE 4 = MODIFIED MODE : FOLLOW USERS BASED ON RECENT FEED ONLY")
        #print("###### MODE 5 = MODIFIED MODE : JUST UNFOLLOW EVERYBODY, EITHER YOUR FOLLOWER OR NOT")
    
        ################################
        ##  WARNING   ###
        ################################
    
        # DON'T USE MODE 5 FOR A LONG PERIOD. YOU RISK YOUR ACCOUNT FROM GETTING BANNED
        ## USE MODE 5 IN BURST MODE, USE IT TO UNFOLLOW PEOPLE AS MANY AS YOU WANT IN SHORT TIME PERIOD
    
        mode = 0
    
        #print("You choose mode : %i" %(mode))
        #print("CTRL + C to cancel this operation or wait 30 seconds to start")
        #time.sleep(30)
    
        if mode == 0:
            bot.new_auto_mod()
    
        elif mode == 1:
            check_status(bot)
            while bot.self_following - bot.self_follower > 200:
                unfollow_protocol(bot)
                time.sleep(10 * 60)
                check_status(bot)
            while bot.self_following - bot.self_follower < 400:
                while len(bot.user_info_list) < 50:
                    feed_scanner(bot)
                    time.sleep(5 * 60)
                    follow_protocol(bot)
                    time.sleep(10 * 60)
                    check_status(bot)
    
        elif mode == 2:
            bot.bot_mode = 1
            bot.new_auto_mod()
    
        elif mode == 3:
            unfollow_protocol(bot)
            time.sleep(10 * 60)
    
        elif mode == 4:
            feed_scanner(bot)
            time.sleep(60)
            follow_protocol(bot)
            time.sleep(10 * 60)
    
        elif mode == 5:
            bot.bot_mode = 2
            unfollow_protocol(bot)
    
        else:
            print("Wrong mode!")

else:
    print "Bot ID '%s' NOT found." % bot_id

cur.close()
db.close()