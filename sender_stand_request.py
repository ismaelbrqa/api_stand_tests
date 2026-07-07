import configuration
import requests
import data

def get_docs():
    return requests.get(configuration.URL_SERVICE + configuration.DOC_PATH)

def get_logs():
    return requests.get(configuration.URL_SERVICE + configuration.LOG_MAIN_PATH,
                        params={"count": 20})

def get_database():
    return requests.get(configuration.URL_SERVICE + configuration.DATABASE_PATH)

def get_all_kits():
    return requests.get(configuration.URL_SERVICE + configuration.KITS_PATH,
                        params={"cardId": 1})

def get_users_table():
    return requests.get(configuration.URL_SERVICE + configuration.USERS_TABLE_PATH)
response = get_users_table()
print(response.status_code)
print(response.text)

def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json=body,
                         headers=data.headers)

def post_products_kits(products_ids):
    return requests.post(configuration.URL_SERVICE + configuration.PRODUCTS_KITS_PATH,
                         json=products_ids,
                         headers=data.headers)
#response6 = post_products_kits(data.product_ids)
#print(f"Codigo de respuesta: {response6.status_code}")
#print(response6.json())
