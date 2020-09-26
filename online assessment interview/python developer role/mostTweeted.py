import sys

no_test_cases = sys.argv[1]
print(no_test_cases)

no_tweets = 0
all_user_tweets = {}

for test_case in range(1, int(no_test_cases) + 1):
    # taking each test case input
    # print("test case ", testcase)

    arg_val = int(test_case + (no_tweets * 2) + 1)
    no_tweets = sys.argv[arg_val]
    no_tweets = int(no_tweets)

    print(no_tweets)

    for tweet in range(no_tweets):
        arg_val = arg_val + 1
        username = sys.argv[arg_val]

        arg_val = arg_val + 1
        usertweetid = sys.argv[arg_val]

        print(username, usertweetid)

        if username not in all_user_tweets.keys():
            all_user_tweets[username] = [usertweetid]
        else:
            all_user_tweets[username].extend([usertweetid])
            # all_user_tweets[username] = all_user_tweets[username] + " " + usertweetid

print()
tweet_feeds_dic = {}
for username, tweet_count in all_user_tweets.items():
    # print(username, len(tweet_count))
    tweet_feeds_dic[username] = len(tweet_count)

print()
tweet_feeds_dic = dict(sorted(tweet_feeds_dic.items(), key=lambda x: x[0].lower()))
tweet_feeds_dic = dict(sorted(tweet_feeds_dic.items(), key=lambda x: x[1], reverse=True))

# removing item with tweet < 2
tweet_feeds_dic = {myuser: mycount for myuser, mycount in tweet_feeds_dic.items() if mycount >1}

for final_user, final_count in tweet_feeds_dic.items():
    print(final_user, final_count)


