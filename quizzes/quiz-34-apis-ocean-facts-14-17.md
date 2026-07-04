# Week 34 Quiz — APIs — Fetching Ocean Facts — Ages 14–17

> *10 code-focused, CBE-aligned questions for Week 34: APIs — Fetching Ocean Facts.*

## Questions

1. Write Python code to fetch JSON from an API and print one field.
2. What is a REST API?
3. Explain the difference between JSON and XML.
4. How do you handle a failed API request in code?
5. What is an API key and why is it private?
6. Write code that retries an API call up to 3 times.
7. What is rate limiting?
8. How would you cache API responses to work offline?
9. What is pagination in an API?
10. Map APIs to CBE Networks/Data outcomes.

## Answer Key

1. import requests
data = requests.get(url).json()
print(data['fact'])
2. An API that uses HTTP methods like GET, POST, PUT, DELETE.
3. JSON is lighter and easier to read; XML uses tags.
4. Use try/except and check response.status_code.
5. A token that identifies the user; sharing it allows abuse.
6. for i in range(3):
    try:
        return requests.get(url)
    except:
        sleep(1)
7. A restriction on how many API requests you can make in a time period.
8. Save responses to local files and read them if offline.
9. Returning large results in chunks or pages.
10. Learners retrieve and process remote data programmatically.
