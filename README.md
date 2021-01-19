# supdem

## Onetime setup (DB)
$ flask db init
$ flask db migrate -m " initial migration"
$ flask db upgrade

### Note:  Everytime a new column is added or removed from model.py and forms.py run

$ flask db migrate -m " {{inster your message here}}"
$ flask db upgrade

after that flask run 