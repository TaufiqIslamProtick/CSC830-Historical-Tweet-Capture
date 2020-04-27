# CSC830-Historical-Tweet-Capture

This repository collects historical tweets. I collected the Twets using Twitter Sandbox API (free version). To use the Sandbox API, you need to fulfill the followinhg requirements.

## Requirements (Assuming you are logged in to your Twitter user account)

  1. You must have a Twitter developer account. [This](https://www.youtube.com/watch?v=2o_qt9cXicM&t=26s) is a good video to follow how to create one.
  2. After you have a developer account, you will be able to create apps [here](https://developer.twitter.com/en/apps). Create an app at this point.
  3. Now create a development environment going in [this](https://developer.twitter.com/en/account/environments) page. Create a developer environment in the Section that says ```Search Tweets: Full ArchiveSandbox```.
  4. Add the app you created in Step 2 in this developer environment.
  5. You are done creating a Sandbox!

### Caution!
This is a free version that uses the Twitter Full Archive API. It has its limits. You can only collect at most 5000 tweets per month. And there is a limit to the number of requests that you can do per minute, which is 30. So if you plan to runa  script exceeding any of the limits (per month or per minute), your account will lose the privilege of using the API for that month. So in the script the looping part is strictly commented out so prevent one from running out of request while having some few trials to call the API.

## How to create a bearer token
Bearer token is required to use the Sandbox API. Although to capture live tweets, bearer tokes are not needed. As we are interested more in historical tweets, we are not using the twitter API for live tweets collection. To generate the bearer token, go to a bash terminal and type:
<br /> ```curl -u '<API key:>:<API Secret Key>'   --data 'grant_type=client_credentials'   'https://api.twitter.com/oauth2/token'```

```API Key``` and ```API Secret key``` are the keys for your app that you created in step 2 of "Requirements". You will get a response in the terminal (for a successfull request) as follows:
<br /> ```"token_type":"bearer","access_token":"Your LONG bearer token here"```

### How to use the code

  1. In ```appCredentials.py```, you will find two variables ```devEnvLabel``` and ```bearerToken```, they are currently assigned empty strings because they are sensitive information. Do not upload any of your tokens on GitHub. In your personal computer, clone the repository and fill up ```devEnvLabel``` with the environment name that you created in Step 3 of "Requirements". Fill up the ```bearerToken``` variable using the bearer token you just created in the terminal.
  2. At this point you are all set. 





