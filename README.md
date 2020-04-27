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

## 





