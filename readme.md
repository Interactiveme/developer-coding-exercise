# Media Suite Coding Exercise


## Running the application
The project has been developed using Python 3.10.0
### Django
From the root directory run the following commands in a new terminal window
* `cd blog`
* `pip install -r requirements.txt`
* `cd ../`
* `sh run_django.sh`

### React
From the root directory run the following commands in a new terminal window
* `cd client/blog`
* `yarn install`
* `yarn start`

### Django Tests
After completing the requirements under Django, from the root directory run the following commands in a new terminal window
* `sh run_django_tests.sh`

### React Tests
After completing the requirements under React, from the root directory run the following commands in a new terminal window
* `cd client/blog`
* `yarn test a`

## Notes
With more time, I would expand on the test suite's in both applications.\
The Django application could benefit from testing the security of the file reading - ie could the slug allow access to the application's directory.\
The React application has very limited and basic tests. I would implement testing on all http requests with axios, adding mocks and further testing on the rendered data.

Thank you for the opportunity to interview with Media Suite.