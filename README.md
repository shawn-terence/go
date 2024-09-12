


To run machine locally your machine, you'll need to install docker based on the OS your machine. Here is the guideline: `https://docs.docker.com/engine/install/`

To start the application first run: 
`docker compose down`
Then run start the docker containers by running:
`docker compose up --build`

Install within the docker environment:
`docker compose exec web pip freeze > requirements.txt`

Installing module you can use this:
`docker compose exec web pip install.... `

To make migrations:
`docker compose exec web python manage.py makemigrations`
`docker compose exec web python manage.py migrate`

We are using postgress. I think the reason I get `No active accounts is database not figured well.`
Because when I djangoshell I can log in and get access token