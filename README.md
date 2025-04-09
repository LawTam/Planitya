```
trainOS/
├── data.py         # fetch_whoop_data, save_to_db
├── suggest_workout.py        # suggest_workout
├── dashboard.py    # run_dashboard
├── trainOS.db     # SQLite database
└── main.py         # Entry point to tie it together
```

# Dev Log
### April 9, 2025
- I began validation of Whoop API authentication with Postman, using this tutorial: https://developer.whoop.com/docs/tutorials/access-token-postman/
- Note: To test the Whoop API with Postman, I needed to manually add a new Callback URL to my Whoop Developer Dashboard: https://oauth.pstmn.io/v1/browser-callback. This is thew new Callback URL that Postman uses, which is different from the callback URL provided in the tutorial above (https://oauth.pstmn.io/v1/callback). I suggest Whoop to update the tutorial to reflect this.

### April 8, 2025
- Created github repository
- Set up Whoop Developer account for access to Whoop API for access to cycle, sleep, recovery, workout, and user data
- Learning how to make an API request with Javascript and Postman