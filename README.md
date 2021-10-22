# Hasegawa-Django

## setup
```
# ターミナルで
# 仮想環境を作る
pipenv shell
pipenv install
```

```
# DBを作成してmigrateする
createdb hasegawa
python manage.py makemigrations
python manage.py migrate
```

```
# runserverする
python manage.py runserver
# 終了したいならcontrole + c
```
