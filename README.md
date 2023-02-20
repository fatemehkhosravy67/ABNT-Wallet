# ABNT-Wallet





  <h3 align="center">Wallet</h3>

  <p align="center">
Get balance, Get Debit and Get Credit </p>   <br/>





<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

This project get a wallet address and return balance, credit and debit and save them in redis and db 

This project will do:
* Create a postgresql database
* create a super user 
* run project (python manage.py runserver)
* type in browser 127.0.0.1:8000/balance, 127.0.0.1:8000/debit, 127.0.0.1:8000/credit


### Built With

This section should list any major frameworks/libraries used to bootstrap your project. Leave any add-ons/plugins for the acknowledgements section. Here are a few examples.

* [Python](https://www.python.org)
* [Django](https://django.com)
* [Mysql DB](https://www.postgresql.com)
* [redis](https://www.redis.com)


<p align="right">(<a href="#top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

In this part, there is an instructions on setting up the project locally.
To get a local copy up and running follow these simple steps.

### Prerequisites

For this project, you need python v3.8 and mongodb v5[Install Postgresqldb](https://dev.to/sm0ke/how-to-use-mysql-with-django-for-beginners-2ni0/)

### Installation

After installing prerequisites, now you can install dependencies of this project:

1. Clone the repo
   ```sh
   git clone https://github.com/fatemehkhosravy67/ABNT-Wallet.git
   ```
2. Setup an environment
    ```sh
    sudo apt install python3-virtualenv
    virtualenv venv
    source venv/bin/activate
    ```
3. Install pip packages
   ```sh
   pip install -r requirements.txt
   ```
4. Create your mysql User and Database and set it in settings.py
   ```buildoutcfg
   DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'your db name',
        'USER': 'your user name',
        'PASSWORD': 'your password',
        'HOST': 'localhost',
        'PORT': '5433',
    }
   }
   ```
5. Migrate 
    ```sh
   python manage.py makemigrations
   python manage.py migrate
   ```


<p align="right">(<a href="#top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

To run the project, make sure that the mysqldb service is up locally and run this in the app directory
```sh
python manage.py runserver --noreload
```
To run project with docker
```sh
docker build -t python-django-app .
docker run -it -p 8000:8000 python-django-app
```
- You can visit [localhost:8000/balance/](http://localhost:8000/weather-api/city_name) for get wallet balance. 

<p align="right">(<a href="#top">back to top</a>)</p>











