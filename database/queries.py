########################################CREATE TABLE QUERIES########################################

create_users = '''
								CREATE TABLE USERS (
									USERID TEXT PRIMARY KEY NOT NULL,
								 	NAME TEXT NOT NULL,
								 	SEX TEXT NOT NULL,
								 	PASSWORD TEXT NOT NULL
								 );'''

create_posts = '''
								CREATE TABLE POSTS (
									TIMESTAMP TEXT NOT NULL,
									USERID TEXT NOT NULL,
									POSTID INTEGER PRIMARY KEY AUTOINCREMENT,
									CONTENT TEXT NOT NULL
									);'''

create_subscriptions = '''
								CREATE TABLE SUBSCRIPTIONS (
									USERID TEXT NOT NULL,
									SUBSID TEXT NOT NULL
									);'''

create_pings = '''
								CREATE TABLE PINGS (
									FROMID TEXT NOT NULL,
									TOID TEXT NOT NULL,
									TIMESTAMP TEXT NOT NULL
									);'''

create_ups = '''
								CREATE TABLE UPS (
									POSTID TEXT NOT NULL,
									USERID TEXT NOT NULL,
									TIMESTAMP TEXT NOT NULL
									);'''

########################################INSERT QUERIES########################################

insert_user = '''INSERT INTO USERS
									(USERID, NAME, SEX, PASSWORD) \
									VALUES (:userid, :name, :sex, :password) '''

insert_post = '''INSERT INTO POSTS
									(TIMESTAMP, USERID, CONTENT) \
									VALUES (:timestamp,:userid,:content) '''

insert_subscription = '''INSERT INTO SUBSCRIPTIONS
													(USERID, SUBSID) \
													VALUES (:userid,:subsid) '''

insert_ping = '''INSERT INTO PINGS
									(FROMID, TOID, TIMESTAMP) \
									VALUES (:fromid,:toid,:timestamp) '''

insert_up = '''INSERT INTO UPS
									(POSTID, USERID,TIMESTAMP) \
									VALUES (:postid,:userid,:timestamp) '''

########################################QUERIES########################################

all_users = '''SELECT USERID, NAME, SEX 
								FROM USERS'''

all_posts = '''SELECT POSTID, CONTENT, USERID, TIMESTAMP
								FROM POSTS
								ORDER BY TIMESTAMP DESC'''

all_posts_by_user = '''SELECT POSTID, CONTENT, USERID, TIMESTAMP
												FROM POSTS
												WHERE USERID = :userid
												ORDER BY TIMESTAMP DESC'''

all_subscriptions_of_user = '''SELECT USERID, SUBSID
																FROM SUBSCRIPTIONS
																WHERE USERID = :userid'''

all_subscribers_of_user = '''SELECT USERID
															FROM SUBSCRIPTIONS
															WHERE SUBSID = :subsid'''																

all_pings_by_user = '''SELECT TOID
												FROM PINGS
												WHERE FROMID = :userid
												ORDER BY TIMESTAMP DESC'''

all_pings_to_user = '''SELECT FROMID
												FROM PINGS
												WHERE TOID = :userid
												ORDER BY TIMESTAMP DESC'''

all_pings = '''SELECT FROMID, TOID
								FROM PINGS
								ORDER BY TIMESTAMP DESC'''
																
all_ups_to_post = '''SELECT USERID
											FROM UPS
											WHERE POSTID = :postid
											ORDER BY TIMESTAMP DESC'''

all_ups_of_user = '''SELECT USERID, POSTID
											FROM UPS
											WHERE USERID = :userid
											ORDER BY TIMESTAMP DESC'''															

find_user = '''SELECT USERID, NAME, SEX, PASSWORD
								FROM USERS
								WHERE USERID = :userid'''

find_post = '''SELECT POSTID, CONTENT, USERID, TIMESTAMP
								FROM POSTS
								WHERE POSTID = :postid'''

#Function to fetch create table queries
def getCreateTable():
	return [create_users,create_ups,create_pings,create_subscriptions,create_posts]

#Functions to fetch insert element queries
def getInsertUser():
	return insert_user 

def getInsertPost():
	return insert_post

def getInsertSubscription():
	return insert_subscription

def getInsertPing():
	return insert_ping

def getInsertUp():
	return insert_up

#Functions to fetch query request queries :/ 
def getAllUsers():
	return all_users

def getAllPosts():
	return all_posts

def getPostsByUser():
	return all_posts_by_user

def getSubscriptionsOfUser():
	return all_subscriptions_of_user

def getSubscribersOfUser():
	return all_subscribers_of_user

def getPingsByUser():
	return all_pings_by_user

def getPingsToUser():
	return all_pings_to_user

def getPings():
	return all_pings

def getUpsToPost():
	return all_ups_to_post

def getUpsOfUser():
	return all_ups_of_user

def getFindUser():
	return find_user

def getFindPost():
	return find_post
