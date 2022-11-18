~~~bash
mkdir wsstore
cd wsstore
~~~

~~~bash
sudo service docker start
git init
~~~

~~~bash
git init
touch gitignore
touch README.md
~~~

~~~bash
git add .
git commit -m 'Criado diretório raiz e arquivos gitignore e README.md'
~~~

~~~bash
touch docker-compose.yml
git add .
git commit -m 'Criado arquivo docker-compose.yml e o Serviço do PostgreSQL'
~~~

~~~bash
mkdir script
touch script/init.sql
touch script/check.sql
~~~

~~~bash
sudo docker-compose up -d
sudo docker-compose exec s-database psql -U wsstore -c '\l'
sudo docker-compose exec s-database psql -U wsstore -f /script/check.sql
~~~

~~~bash
git add .
git commit -m 'Criado o diretório script e os arquivos init.sql e check.sql'
~~~

~~~bash
mkdir backend
mkdir backend/app
touch backend/app/__init__.py
touch backend/app/config.py
touch backend/app/database.py
mkdir backend/app/model
touch backend/app/model/__init__.py
touch backend/app/model/user.py
touch backend/app/api.py
touch backend/app/cli.py
touch backend/requirements.txt
touch backend/app.sh
~~~

~~~bash
sudo docker-compose ps
sudo docker-compose down
sudo docker-compose up -d
~~~

~~~bash
git add .
git commit -m 'Criado diretório backend, sub-diretórios e arquivos Python'
~~~

~~~bash
git add .
git commit -m 'Adicionado Serviço do Python ao arquivo docker-compose.yml'
~~~

~~~bash
~~~