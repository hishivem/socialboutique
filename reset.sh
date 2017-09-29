psql -c "drop database socialboutique;" &&
psql -c "create database socialboutique;" &&
rm main/migrations/* &&
touch main/migrations/__init__.py &&
./manage.py makemigrations &&
./manage.py migrate &&
./manage.py init
