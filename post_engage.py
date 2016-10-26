import requests
import re
from bs4 import BeautifulSoup

def get_post(url):

    source_code = requests.get(url)
    plain_text = source_code.text
    my_soup = BeautifulSoup(plain_text)

    mylist = []
    int_list = []
    mylist_repost = []
    int_list_repost = []
    pinned = ""

    #   GETS "PINNED" TEXT IF PINNED
    for content in my_soup.findAll('span', {'class': 'js-pinned-text'}):
        pinned = str(content.string)
        #print(pinned)

    #   PUTS FAVORITE METRICS INTO LIST
    for content in my_soup.findAll('div', {'class': 'ProfileTweet-action ProfileTweet-action--favorite js-toggleState'}):
        fetch = content.contents[1]
        for tag in fetch.findAll('span', {'class': 'ProfileTweet-actionCountForPresentation'}):
            mylist.append(tag.string)
            if str(tag.string).isdigit():
                int_list.append(int(tag.string))

    #   PUTS RE-POST METRICS INTO LIST
    for content in my_soup.findAll('div', {'class': 'ProfileTweet-action ProfileTweet-action--retweet js-toggleState js-toggleRt'}):
        fetch = content.contents[1]
        for tag in fetch.findAll('span', {'class': 'ProfileTweet-actionCountForPresentation'}):
            mylist_repost.append(tag.string)
            if str(tag.string).isdigit():
                int_list_repost.append(int(tag.string))

    #   if pinned == 'Pinned Tweet':
    #   pinned_engagement = mylist[0]

    #   TESTS THAT THE DATA IS CORRECT

    print 'RAW LIST', mylist
    print 'the total items in list is', len(mylist)
    print 'RAW INT ONLY LIST', int_list
    print 'Out of', len(mylist), 'posts, the total amount of engaged posts is ', len(int_list)
    print 'the percent of first page utilization is', (len(int_list)/len(mylist))*100, '%'    

    like_page_utilization = str((len(int_list)/len(mylist))*100)+'%'

    print 'total amount of engagement is', sum(int_list)
    print '----------'
    print url
    print '----------'
    print 'repost list', mylist_repost
    print 'total items in repost list is', len(mylist_repost)
    print 'raw int only list', int_list_repost
    print 'out of', len(mylist_repost), 'posts, the total amount of retweeted is ', len(int_list_repost)
    print 'the percent of first page utilization is', (len(int_list_repost)/len(mylist_repost))*100, '%'

    repost_page_utilization = str((len(int_list_repost)/len(mylist_repost))*100)+'%'

    print 'total amount of retweets is', sum(int_list_repost)
    print '----------'

    #   TOTAL ENGAGEMENT METRICS
    largest_list = [len(int_list), len(int_list_repost)]
    largest_list_max = max(largest_list)
    total_engagements_overall = sum(int_list)+sum(int_list_repost)

    print 'posts with at least one engagement', largest_list_max
    print 'total engagements occurring', total_engagements_overall
    print 'overall utilization is', (largest_list_max/len(mylist))*100, '%'
    print '------------'

    overall_engagement_utilization = str((largest_list_max/len(mylist))*100)+'%'

    if pinned != 'Pinned Tweet':
        print pinned
        print "not pinned"
        print len(int_list), sum(int_list)
        return {'liked_posts': len(int_list), 'total_likes': sum(int_list),
                'pinned_likes': 0, 'pinned': 'F', 'like_page_utilization': like_page_utilization,
                'repost_page_utilization': repost_page_utilization,
                'overall_engagement_utilization': overall_engagement_utilization,
                'retweeted_posts': len(int_list_repost), 'pinned_retweets': 0,
                'total_retweets': sum(int_list_repost),
                'total_engagements_overall': total_engagements_overall}
    else:
        print pinned 
        print "is pinned"
        return {'liked_posts': len(int_list[1:]), 'total_likes': sum(int_list[1:]),
                'pinned_likes': int_list[0], 'pinned': 'T', 'like_page_utilization': like_page_utilization,
                'repost_page_utilization': repost_page_utilization,
                'overall_engagement_utilization': overall_engagement_utilization,
                'retweeted_posts': len(int_list_repost[1:]), 'pinned_retweets': int_list_repost[0],
                'total_retweets': sum(int_list_repost[1:]),
                'total_engagements_overall': total_engagements_overall}

get_post('https://twitter.com/annakoppad')
