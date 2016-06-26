'''get and put connection,create table scripts'''
from psycopg2 import pool

POOL=None

def get_connection():    
    global POOL
    try:
        if POOL is None:
            line="dbname='db1' host='db.ii.fmph.uniba.sk' user='achbergero12' password='db1achbergero12'"
            POOL = pool.SimpleConnectionPool(5, 10, line)
#             5xconnections,max 10
            print("u r connected")
            return POOL.getconn()
        else:
            return POOL.getconn()
    except OperationalError as e:
        raise DatabaseError("{} - this error occurred while getting"
                            " connection from connection pool.".format(e))

def put_connection(connection):   
    global POOL
    try:
        if POOL is None:
            raise DatabaseError("Tried putting connection back to the pool before getting any.")
        else:
            return POOL.putconn(connection)
    except OperationalError as e:
        raise DatabaseError("{} - this error occurred while putting"
                            " connection back to connection pool.".format(e))


def createTablePersons():
    try:
        cursor.execute('''CREATE TABLE Persons(id serial PRIMARY KEY,
        name varchar(140),
        rating integer);
        ''');
        print("OK tabulka Persons uspesne vytvorena")
#         conn.commit()
        return True
    except:
        print("ERROR pri vytvarani tabulky Persons nastal problem")
        return False
def createTablePL():
    try:
        cursor.execute('''CREATE TABLE Persons_languages(
        Persons_id integer references  Persons(id ),
        languages_id integer references languages( id),
        primary key(Persons_id,languages_id) );
        ''');
        print("OK tabulka Persons_languages uspesne vytvorena")
#         conn.commit()
        return True
    except:
        print("ERROR pri vytvarani tabulky Persons_languages nastal problem")
        return False


def createTableDirectors():
    try:
        cursor.execute('''CREATE TABLE Directors(
        id serial PRIMARY KEY, 
        Persons_id integer references persons( id),
        Movie_id integer references Movies( id),
        is_main_director boolean);
        ''');
        print("OK tabulka Directors uspesne vytvorena")
#         conn.commit()
        return True
    except:
        print("ERROR pri vytvarani tabulky Directors nastal problem")
        return False   
        
def createTableMovies():
    try:
        cursor.execute('''CREATE TABLE Movies(
        id serial PRIMARY KEY, 
        name varchar(100),
        year integer,
        languages_id integer references languages(id), 
        Format_id integer references Format(id),
        rating integer);
        ''');
#         conn.commit()
        print("OK tabulka Movies uspesne vytvorena")
        return True
    except:
        print("ERROR pri vytvarani tabulky Movies nastal problem")
        return False
def createTableFormat():
    try:
        cursor.execute('''CREATE TABLE Format( id serial PRIMARY KEY, format_name varchar(50));  ''')
        print("OK tabulka Format uspesne vytvorena")
#         conn.commit()
        return True
    except:
        print("ERROR pri vytvarani tabulky Format nastal problem")
        return False
def createTableCast():
    try:
        cursor.execute('''CREATE TABLE Act(
        Actor_id integer references Persons(id),
        Movies_id integer references  Movies(id));
        ''')
#         conn.commit()
        print("OK tabulka Cast uspesne vytvorena")
        return True
    except:
        print("ERROR pri vytvarani tabulky Cast nastal problem")
        return False
        
def createTableLang():
    try:
        cursor.execute('''CREATE TABLE Languages(
        id serial PRIMARY KEY,
        lang_name varchar(50));
        ''')
#         conn.commit()
        print("OK tabulka Languages uspesne vytvorena")
        return True
    except:
        print("ERROR pri vytvarani tabulky Languages nastal problem")
        return False

    cnx=get_connection()
    cursor=cnx.cursor()
    # createTableFormat();
    # createTableLang(); 
    # createTablePersons();
    # createTablePL();
    # createTableMovies();
    # createTableDirectors();
    # createTableCast();
    cnx.commit()
