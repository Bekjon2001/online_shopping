# Task by "OnlineShopping"

## 1. Clone the Repository
```bash
git clone https://github.com/jahongiranorboyev/online_shopping.git
```
## 2. Change Directory
```bash
cd online_shopping
```
## 3. Create .env file using .env.example
```bash
cp .env.example .env
```
## 4. Create a virtual environment using Python 3.10 
```bash
python3 -m venv venv 
```
## 5. Activate the Virtual Environment On Linux/MacOS
```bash
source venv/bin/activate
```
## 5. Activate the Virtual Environment On Windows
```bash
venv\Scripts\activate
```
## 6. Install Packages from requirements.txt Inside the Virtual Environment:
```bash
pip install -r requirements.txt
```

## 7. Run the makemigrations and apply the changes to the database:
```bash
./manage.py makemigrations
./manage.py migrate
```
## 8. To start the server, run the following command inside your Django project directory:
```bash
./manage.py runserver
```
# Available APIs

1.**API **
   [http://127.0.0.1:8000](http://127.0.0.1:8000)

2.**Login API**
   [http://127.0.0.1:8000/en/auth/login_page/](http://127.0.0.1:8000/en/auth/login_page/)

3.**Register API**
   [http://127.0.0.1:8000/en/auth/register_page/](http://127.0.0.1:8000/en/auth/register_page/)

4.**Shop page**
   [http://127.0.0.1:8000/en/products/](http://127.0.0.1:8000/en/products/)

5**Contact page**
   [http://127.0.0.1:8000/en/contact/](http://127.0.0.1:8000/en/contact/)

6.**About page**
   [http://127.0.0.1:8000/en/about/(http://127.0.0.1:8000/en/about/)

