import numpy as np
import pickle

import psycopg2 as pg
import pandas.io.sql as psql
import pandas as pd

from typing import Union, List, Tuple

connection = pg.connect(host='pgsql-196447.vipserv.org', port=5432, dbname='wbauer_adb', user='wbauer_adb', password='adb2020');

def film_in_category(category:Union[int,str])->pd.DataFrame:
    ''' Funkcja zwracająca wynik zapytania do bazy o tytuł filmu, język, oraz kategorię dla zadanego:
        - id: jeżeli categry jest int
        - name: jeżeli category jest str, dokładnie taki jak podana wartość
    Przykład wynikowej tabeli:
    |   |title          |languge    |category|
    |0	|Amadeus Holy	|English	|Action|
    
    Tabela wynikowa ma być posortowana po tylule filmu i języku.
    
    Jeżeli warunki wejściowe nie są spełnione to funkcja powinna zwracać wartość None.
    
    Parameters:
    category (int,str): wartość kategorii po id (jeżeli typ int) lub nazwie (jeżeli typ str)  dla którego wykonujemy zapytanie
    
    Returns:
    pd.DataFrame: DataFrame zawierający wyniki zapytania
    '''
    
    if isinstance(category, int):
        if category < 0:
            return None
        
        condition = f"category.category_id={category}"
        
    elif isinstance(category, str):
        condition = f"category.name LIKE '{category}'"
        
    else:
        return None
        
    
    
    sql = f'''SELECT
                  film.title title, language.name languge, category.name category
              FROM
                  category
              INNER JOIN film_category ON category.category_id=film_category.category_id
              INNER JOIN film ON film_category.film_id=film.film_id
              INNER JOIN language ON film.language_id=language.language_id
              WHERE
                  {condition}
              ORDER BY
                  title, languge;'''
    
    return pd.read_sql(sql, con=connection)
    
def film_in_category_case_insensitive(category:Union[int,str])->pd.DataFrame:
    ''' Funkcja zwracająca wynik zapytania do bazy o tytuł filmu, język, oraz kategorię dla zadanego:
        - id: jeżeli categry jest int
        - name: jeżeli category jest str
    Przykład wynikowej tabeli:
    |   |title          |languge    |category|
    |0	|Amadeus Holy	|English	|Action|
    
    Tabela wynikowa ma być posortowana po tylule filmu i języku.
    
    Jeżeli warunki wejściowe nie są spełnione to funkcja powinna zwracać wartość None.
    
    Parameters:
    category (int,str): wartość kategorii po id (jeżeli typ int) lub nazwie (jeżeli typ str)  dla którego wykonujemy zapytanie
    
    Returns:
    pd.DataFrame: DataFrame zawierający wyniki zapytania
    '''
    
    if isinstance(category, int):
        if category < 0:
            return None
        
        condition = f"category.category_id={category}"
        
    elif isinstance(category, str):
        condition = f"category.name ILIKE '{category}'"
        
    else:
        return None
        
    sql = f'''SELECT
                  film.title title, language.name languge, category.name category
              FROM
                  category
              INNER JOIN film_category ON category.category_id=film_category.category_id
              INNER JOIN film ON film_category.film_id=film.film_id
              INNER JOIN language ON film.language_id=language.language_id
              WHERE
                  {condition}
              ORDER BY
                  title, languge;'''
    
    return pd.read_sql(sql, con=connection)
    
def film_cast(title:str)->pd.DataFrame:
    ''' Funkcja zwracająca wynik zapytania do bazy o obsadę filmu o dokładnie zadanym tytule.
    Przykład wynikowej tabeli:
    |   |first_name |last_name  |
    |0	|Greg       |Chaplin    | 
    
    Tabela wynikowa ma być posortowana po nazwisku i imieniu klienta.
    Jeżeli warunki wejściowe nie są spełnione to funkcja powinna zwracać wartość None.
        
    Parameters:
    title (int): wartość id kategorii dla którego wykonujemy zapytanie
    
    Returns:
    pd.DataFrame: DataFrame zawierający wyniki zapytania
    '''
    
    if not isinstance(title, str):
        return None
    
    sql = f'''SELECT
                  actor.first_name, actor.last_name
              FROM
                  actor
              INNER JOIN film_actor ON actor.actor_id=film_actor.actor_id
              INNER JOIN film ON film_actor.film_id=film.film_id
              WHERE
                  film.title LIKE '{title}'
              ORDER BY
                  actor.last_name, actor.first_name;'''
    
    return pd.read_sql(sql, con=connection)
    

def film_title_case_insensitive(words:list) :
    ''' Funkcja zwracająca wynik zapytania do bazy o tytuły filmów zawierających conajmniej jedno z podanych słów z listy words.
    Przykład wynikowej tabeli:
    |   |title              |
    |0	|Crystal Breaking 	| 
    
    Tabela wynikowa ma być posortowana po nazwisku i imieniu klienta.

    Jeżeli warunki wejściowe nie są spełnione to funkcja powinna zwracać wartość None.
        
    Parameters:
    words(list): wartość minimalnej długości filmu
    
    Returns:
    pd.DataFrame: DataFrame zawierający wyniki zapytania
    '''
    
    if not isinstance(words, list) or not all([isinstance(w, str) for w in words]):
        return None
    
    regex = "(^| )(" + "|".join(words) + ")($| )"
    
    sql = f'''SELECT
                  title
              FROM
                  film
              WHERE
                  title ~* '{regex}'
              ORDER BY
                  title;'''
    
    return pd.read_sql(sql, con=connection)
    