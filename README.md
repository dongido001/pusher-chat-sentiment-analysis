# One-to-one private chat with sentiment analysis using Pusher Channels, Flask and Vue.js - Part 2

This is the part 2 of the tutorial series demonstrating how to build a chat app with sentiment analysis using Pusher Channels, Flask and Vue.js. You can read the tutorial on how it was built [here]()

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

This application uses the following:

- [Python 3.6+](https://www.python.org/)
- [Node.js](https://nodejs.org/) version 8.9 or above
- [Vue cli](https://cli.vuejs.org/guide/installation.html)

### Setting up the project

First, clone this repository to your local machine:

```sh
 $ git clone https://github.com/dongido001/pusher-chat-sentiment-analysis.git -b part-2
```

Next, update the following keys in the `.env` file with your correct Pusher keys:

```
PUSHER_APP_ID=app_id
PUSHER_KEY=key
PUSHER_SECRET=secret
PUSHER_CLUSTER=cluster
```

### Running the Apps

#### Run the Flask app

- CD to the Flask folder - api:

```
    $ cd api
```

- Create a virtual environment:

```
python3 -m venv env
```

- Activate the virtual environment:

```
  source env/bin/activate
```

On windows? Activate it with the below:

```
  source env/Scripts/activate
```

- Install the dependencies:

```
pip install -r requirements.txt
```

- Finally run the app:

```
 flask run
```

Check the URL where Flask is running - [http://localhost:5000](http://localhost:5000). You will get a text "Pong!".

#### Run the Vue app

Open a new terminal window, then cd into the projects root folder - `one-to-one chat`:
  
Then run the app:

```
    $ npm run serve
```

## Built With

- [Flask](http://flask.pocoo.org/) - A microframework for Python
- [Pusher](https://pusher.com/) - APIs to enable devs building realtime features
- [Vue.js](https://vuejs.org/) - A JavaScript Framework for building User Interfaces
