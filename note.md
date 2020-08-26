to update the heroku repo before you deploy, please follow below:
in the CLI: type:
pipenv shell
then, type:
heroku login
then, do a regular git updating routine:
git add .
git commit -m "comments"
git push

git push heroku pricer:master

uvicorn app.main:app --reload