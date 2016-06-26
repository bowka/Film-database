'''fill tables with real data'''
from triedy import *
import random
def generatePersons():
    '''inserting Persons into database'''
#     arrayPerson=("Brad Pitt","James McAvoy","Daniel Bruhl","Jennifer Lawrence","Michael Fassbender","Nicholas Hoult","Oscar Isaac","Brian Singer","Hugh Jackman","Patrick Stewart","Ian McKellen","Famke Janssen","James Marseden","Quentin Tarantino","Halle Berry","Christofer Nollen","Tom Hardy","Johnny Deep")
    arrayPerson=("Adrianne Palicki","Alexa PenaVega","Alexandra Daddario","Jennifer Lawrence","Jennifer Aniston","Jared Leto","Jamie Dornan","Jake Gyllenhaal","Jaimie Alexander","Henry Cavill","Hayley Atwell","Hailee Steinfeld","Gal Gadot","Felicity Jones","Emilia Clarke","Emily Blunt","Emma Stone","Eddie Redmayne","Dylan O'Brien","Dwayne Johnson","Deborah Ann Woll","Dakota Johnson","Daisy Ridley","Chris Pratt","Chris Evans","Alicia Vikander","Alicia Vikander")
    for human in arrayPerson:
        r=random.randrange(5)
        L=Person(human,r)
        GWL=PersonGateway(L)
        GWL.insert()

def generateLang():
    '''inserting languages into database'''
    string="Abkhaz     Afar     Afrikaans  Albanian      Amharic     Arabic      Aragonese     Armenian     Assamese    Avaric     Avestan   Aymara Azerbaijani   Bambara   Bashkir   Basque    Belarusian   Bengali Bihari  Creole    Bislama   Bosnian  Breton    Bulgarian  Burmese    Catalan   Chamorro   Chechen   Chichewa   Chinese    Chuvash    Cornish      Corsican        Cree"    
    arrayLang=string.strip().split()
#     arrayLang=("slovak","czech","english","italian","spanish","german","franch")
    for lang in arrayLang:
        L=Language(lang)
        GWL=LanguageGateway(L)
        GWL.insert()
def generateMovies():
    arrayFilm=("X-men","Alice in wonderland","Great Gatsby","Disaster movie","Avengers","Spiderman","Batman","Deadpool","Inception","Untouchable","Alice Through the Looking Glass")    
    for film in arrayFilm:
        year=random.randint(2000,2016)
        lang=random.randint(2,7)
        f=random.randint(1,6)
        rating=random.randint(0,5)
        L=Movie(film,year,lang,f,rating)
        GWL=MovieGateway(L)
        GWL.insert()
def generateFromat():
    arrayFormats=("Drama","Horror","Thriller","Comedy","Sci-fi","Documentary","Action","Fantasy","Historical","Romance","Adventure","Crime","Saga","Urban","Cartoon","Mystery","Satire")
    for f in  arrayFormats:
        L=Format(f)
        GWL=FormatGateway(L)
        GWL.insert()
def generateAct():    
    for p in range(20):
        act_id=random.randint(1,19)
        movie_id=random.randint(2,12)
        L=Act(act_id,movie_id)
        GWL=ActGateway(L)
        GWL.insert()
def generatePL():
    for p in range(1000000):
        person_id=random.randint(24,77)
        lang_id=random.randint(2,43)
        L=PL(person_id,lang_id)
        GWL=PLGateway(L)
        GWL.insert()
def generateDir():
    for p in range(20):
        person_id=random.randint(1,19)
        movie_id=random.randint(2,9)
        main=random.choice([True,False])
        L=Director(person_id,movie_id,main)
        GWL=DirectorGateway(L)
        GWL.insert()
     
# generateLang()
# generateFromat()
# generatePersons()
# generateMovies()
# generateAct()
# generateDir()



