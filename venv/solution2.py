import os
import jsonParser as jp
import appCredentials as ac
import queryParams as qp
import time
import datetime


date = datetime.datetime(2018,5,17,0,0,0)
i = 106;
while i<127:
    filename = "tweets" + str(i) + ".json"
    date1 = date.strftime("%Y%m%d%H%M")
    date += datetime.timedelta(days=1)
    date2 = date.strftime("%Y%m%d%H%M")
    print(date1+"-"+date2)
    endPoint = "https://api.twitter.com/1.1/tweets/search/fullarchive/" + ac.devEnvLabel + ".json"
    command = "curl  \"" + endPoint + "?query=" + qp.query + "&maxResults=" + qp.maxResults + "&fromDate=" + date1 + "&toDate=" + date2 + "\" -H \"Authorization: Bearer " + ac.bearerToken + "\" >> " + filename
    #print(date.strftime("%Y%m%d%H%M"))
    os.system(command)
    i += 1

# i = 0
# filename = "tweets"+str(i)+".json"
# endPoint = "https://api.twitter.com/1.1/tweets/search/fullarchive/" + ac.devEnvLabel + ".json"
# command = "curl  \""+endPoint+"?query="+qp.query+"&maxResults="+qp.maxResults+"&fromDate="+qp.fromDate+"&toDate="+qp.toDate+"\" -H \"Authorization: Bearer "+ac.bearerToken+"\" >> "+filename
# os.system(command)
"""
The following loop, if run, will exhaust the rate limit within miuntes. 
When your query matches with tweets more than the maxResults parameter (maximum for sandbox is 100), the response json will have a next token in the key named "next" in the .json file.
This is like a chain. Every json response will continue to have a next token in its "next" key until the last set of tweets that matches the query. Query in a familiar topic has more tban a 1000
tweets per day. If one wants to use the sandbox facility for a longer period of time using the loop below, his rate limit will exhaust way before even a fraction of the tweets that matches
the specific keyword is collected. One is advised to have an enterprise account for searching tweets in huge amount. 
"""
# myObj = jp.getJSON(filename)
# nextToken = myObj.get("next", "")


# # while myObj.get("next", "") != "":
# while i < 1:
#     i += 1
#     filename = "tweets" + str(i) + ".json"
#     print(i)
#     command = "curl  \"" + endPoint + "?query=" + qp.query + "&maxResults=" + qp.maxResults + "&fromDate=" + qp.fromDate + "&toDate=" + qp.toDate + "&next=" + str(nextToken) + "\" -H \"Authorization: Bearer " + ac.bearerToken + "\" >> " + filename
#     os.system(command)
#     myObj = jp.getJSON(filename)
#     nextToken = myObj.get("next", "")
#     time.sleep(10)

