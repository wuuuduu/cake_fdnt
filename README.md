# Local development:

```bash
sudo apt install libmysqlclient-dev python3-dev
```

```mariadb
CREATE USER 'cake_fdnt'@'localhost' IDENTIFIED BY 'cake_fdnt';
create database cake_fdnt_local CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
create database test_cake_fdnt_local CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
GRANT ALL PRIVILEGES ON `cake_fdnt_local` . * TO 'cake_fdnt'@'localhost';
GRANT ALL PRIVILEGES ON `test_cake_fdnt_local` . * TO 'cake_fdnt'@'localhost';
```

#### virtualenv && virtualenvwrapper

```bash
sudo apt install python3-pip
sudo pip3 install virtualenv
mkdir ~/.virtualenvs
sudo pip3 install virtualenvwrapper
echo 'export WORKON_HOME=$HOME/.virtualenvs' >> ~/.bashrc
echo 'source /usr/local/bin/virtualenvwrapper.sh' >> ~/.bashrc
```

**Restart your terminal and:**
```bash
mkvirtualenv --python=/usr/bin/python3 cake_fdnt
echo 'export DJANGO_SETTINGS_MODULE=cake_fdnt.settings.local' >> ~/.virtualenvs/cake_fdnt/bin/postactivate
workon cake_fdnt
```

```bash
pip3 install -r installation/packages/develop.txt
```

```bash
./manage.py migrate
./manage.py createsuperuser
./manage.py collectstatic
./manage.py runserver
```

# Translations
## create new language
```bash
./manage.py makemessages -l lang_code
example for the ES language:
./manage.py makemessages -l es
```

## compile translations
```bash
./manage.py compilemessages
```

## regenerate translations
```bash
./manage.py makemessages
```

# Tests
```bash
coverage run --source='.' manage.py test
```