[![Build Status](https://travis-ci.org/rnantume/StackOverflow-liteApi.svg?branch=develop)](https://travis-ci.org/rnantume/StackOverflow-liteApi)
[![Coverage Status](https://coveralls.io/repos/github/rnantume/StackOverflow-liteApi/badge.svg?branch=develop)](https://coveralls.io/github/rnantume/StackOverflow-liteApi?branch=develop)
[![Maintainability](https://api.codeclimate.com/v1/badges/d38815d4d6998ac2ad88/maintainability)](https://codeclimate.com/github/rnantume/StackOverflow-liteApi/maintainability)

# StackOverflow-lite
StackOverflow-lite is a platform where people can ask questions and provide answers.

### Screenshot

![alt](./UI/assets/screenshot/shot1.png)

Preview UI template here[ UI Template](https://rnantume.github.io/StackOverflow-liteApi/UI/index.html)

# Motivation

This Application is a challenge that will contritube greatly to my journey of becoming a
world class software developer


### Features

- User should be able to create account and login
- User should be able to view all questions on the platform
- User should be able to post a question to the platform and people can respond to it
- User should be able to see the details of a question and post an answer to it
- user should be able to view and accept accept(prefer) answers to a question he/she has posted
- user should be able to post answers to other people's questions
- user should be able to view all answers to a given question and be able to upvote, downvote or
  leave a comment to an answer

## Installing

#### Prerequisites

Ensure you have **Python** installed by entering `python --version` on your terminal
If you don't have **Python** installed go to the [Python Website](http://python.org), and follow the download instructions

To install this app

```
git clone repo here (https://github.com/rnantume/StackOverflow-liteApi.git)
```
change directory to StackOverflow-liteApi
```
cd StackOverflow-liteApi
```
Create a virtual environment from commandline
```
python -m venv venv
```
The last 'venv' can be changed to prefered name but conventionally venv is better

Then activate the created virtual environment from commandline(for windows)
```
source venv/scripts/activate
```

And install the required dependencies - specified in requirements.txt

```
pip install -r requirements.txt
```

Running server

Setup  the environment variable
Run that command

```
export FLASK_APP=API/app.py
```
then run this

```
flask run 
```

Server runs on port ``5000``

## Running the tests

To run test cases

```
py.test <path-to-test-file>
```

### Working Routes

<table>
<thead>
<tr>
<th>Endpoint</th>
<th>Functionality</th>
</tr>
</thead>
<tbody>
<tr>
<td>GET /questions</td>
<td>Retrieves all questions in the application memory</td>
</tr>
<tr>
<td>GET /questions/:questionId></td>
<td>Retrives the details of a specific question</td>
</tr>
<tr>
<td>POST /questions</td>
<td>Creates a new question</td>
</tr>
<tr>
<td>POST /questions/:questionId/answers</td>
<td>Adds an answer to an identified question</td>
</tr>
<tr>
<td>GET /questions/:questionId/answers</td>
<td>Retrieves all answers to an identified question</td>
</tr>
</tbody></table>

## License

MIT LICENSED

## Author

[Robinah Nantume](http://github.com/rnantume)

## Acknowledgments

- [Andela](http://andela.com)
- [StackoverFlow](stackoverflow.com)
- [Youtube](youtube.com)
