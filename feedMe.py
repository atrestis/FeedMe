import feedparser

# Feedparser is an python API to manipulate the RSS feed data into dictionary format with several key/value pairs


def showFeedSummary(feedInfo):
    # This method manipulates the general info about the RSS feed like its URL, Description, Version etc
    summary = ["title","description","link"]
    
    if "url" in feedInfo:
        print ("\nURL feed: \n%s\n" % (feedInfo["url"]))

    if "version" in feedInfo:
        print ("RSS version: \n%s\n" % (feedInfo["version"]))

    if "channel" in feedInfo:
        for arg in summary:
            if arg in feedInfo["channel"]:
                print ("Broadcasting from %s: \n%s" % (arg,feedInfo["channel"][arg]))
        print("\n")

    

def showFeedItems(feedInfo):
    # This method manipulates each item in the feed and displays each field(like title, summary, link)associated with the item
    items = feedInfo["items"]
    args = ["title","summary","link"]
    for item in items:
        print("########################################")
        for arg in args:
            if arg in item:
                print ("%s:\n%s" % (arg,item[arg]))
        print("\n")
    

def main():
    rssurl = input("enter the RSS feed url to parse: ")
    feedInfo = feedparser.parse(rssurl)
    #(bozo == 0)?Feed_legit:Feed_broken/invalid
    if feedInfo['bozo'] == 0:
        showFeedSummary(feedInfo)
        showFeedItems(feedInfo)
    else:
        print("invalid RSS feed URL")

if __name__=="__main__":
    main()
