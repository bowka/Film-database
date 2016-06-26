'''UI ,help,exampes,shortcuts'''
from triedy import *
print("Hello, welcome to my datbase IMDB application. \nit is simple to use. Firstly write 'help' to know how to write commads\nOr use EXAMPLES in the end of this file")
def addCast(personName,filmName):
    '''1. chceck if movie exists
    if not print error message 
    2.check is person exists
    if not then create
    else continue with insert person and his language
    '''
    
    findMovie=MovieFinder.findByName(filmName)
    if findMovie is None:
        print("film with this name doesnt exist, insert it with command :add movie/name/year/lang/format/rating")
        return False
    else:        
        findPerson=PersonFinder.findByName(personName)
        if (findPerson is None):        
            L=Person(personName,3)
            findPerson=PersonGateway(L)
            findPerson.insert()
            lang=PLGateway(PL(L.id,5))
            lang.insert()
        A=Act(findPerson.person.id, findMovie.movie.id)
        FA=ActGateway(A)
        FA.insert()
        
    
def addMovie(name,year,lang,form,rating):
    '''1.check if film with this name exists
    if not then continue and chceck if language wit this id exists
    if yes then create film
    '''
    findMovie=MovieFinder.findByName(name)
    if findMovie is not None:
        print(" this film already exists if u wanna update it then use command: update movie/name/year/lang/format/rating")
    else:   
        try:
            M=Movie(name,year,lang,form,rating)
            newM=MovieGateway(M)
            newM.insert()
        except:
            print("you may be trying to insert wrong language or format. Check u r correct")
            return False
        
def updateMovie(name,year,lang,form,rating):
    '''update movie, find film by name. Rest of data replace with new. If film doesnt exist return error message'''
    findMovie=MovieFinder.findByName(name)
    if findMovie is None:
        print("this film doesnt exist if u wanna insert it then use command: add movie/name/year/lang/format/rating")
        return
    else:   
        findMovie.movie.name,findMovie.movie.year,findMovie.movie.languages_id,findMovie.movie.format_id,findMovie.movie.rating=name,year,lang,form,rating
        findMovie.update()        
def deleteMovie(name):  
    '''delete movie, find film by name.If film doesnt exist return error message.
    only if theres no reference from other table to this data'''
    findMovie=MovieFinder.findByName(name)
    if findMovie is None:
        print("this film doesnt exist if u wanna insert it then use command: add movie/name/year/lang/format/rating\n there is no reason delete non existing movie:)")
        return
    else:   
        try:
            M=findMovie.movie
            newM=MovieGateway(M)   
            newM.delete()
        except:
            print("in others tables are references to this data.u have to firstly delete or update them. HINT- use command DEL")
def DELMovie(name):
    '''delete movie from all existing tables'''
    findMovie=MovieFinder.findByName(name)
    if findMovie is None:
        print("this film doesnt exist if u wanna insert it then use command: add movie/name/year/lang/format/rating\n there is no reason delete non existing movie:)")
        return
    else:
        '''delet from Act'''  
        M=findMovie.movie
        movie_id=M.id
        act=ActFinder.findByMovie(movie_id)
        while   act is not None:                               
            newActGw=ActGateway(act.Cast)
            newActGw.delete()
            act=ActFinder.findByMovie(movie_id)
        '''delet from directors'''        
        dir=DirectorsFinder.findByMovie(movie_id)
        while dir is not None:        
            newDirGw=DirectorGateway(dir.D)
            newDirGw.delete()
            dir=DirectorsFinder.findByMovie(movie_id)
        '''delet from Movies'''         
        newM=MovieGateway(M)   
        newM.delete()
                 
def addMovieCast(actors,name,year,lang,form,rating):
    '''check all parameters if are correctly set  
    if every user speak by film language or speak by default language which is englinsh
    '''    
    arrayAct=actors.strip().split("#")
    if lang!=5 :    
        for act in arrayAct:        
            pers=PersonFinder.findByName(act)
            if pers is None:
                return False            
            arrayPL=PLFinder.findLanguagesForPerson(pers.person.id)
            knowsLang=False
            for lg in arrayPL:
                if lg[0]==lang:
                    knowsLang=True
            if knowsLang is False:
                print("one of persons dont know the language of film. please use command:add lang to Person/lang/person")
                return False
        
    if addMovie(name, year, lang, form, rating) is False:        
        return
    for act in arrayAct:        
        addCast(act, name)                    
def addLangPers(P_name,L_id):    
    '''if doesnt exist language or person id print error message
    else insert data into database'''        
    pers_id=PersonFinder.findByName(P_name).person.id 
    lang=LanguageFinder.find(L_id)   
    if pers_id is None:
        print("person doesnt exist.firstly please create it")
        return
    if lang is None:
        print("language doesnt exist.firstly please create it")
        return
    else:
        pl=PL(pers_id,L_id)
        newPL=PLGateway(pl)   
        newPL.insert()        
if __name__ == '__main__':   
    while True:
        IPT=input()
        I=IPT.strip().split("/")    
        if I[0]=="exit":
            break
        elif I[0]=="add cast":
            addCast(I[1],I[2])        
        elif I[0]=="add movie":
            addMovie(I[1],int(I[2]),int(I[3]),int(I[4]),int(I[5]))
        elif I[0]=="update movie":
            updateMovie(I[1],int(I[2]),int(I[3]),int(I[4]),int(I[5]))
        elif I[0]=="add lang person":
            addLangPers(I[1],int(I[2]))
        elif I[0]=="del movie":
            deleteMovie(I[1])
        elif I[0]=="DEL movie":
            DELMovie(I[1])
        elif I[0]=="add movie with cast":
            addMovieCast(I[1],I[2],int(I[3]),int(I[4]),int(I[5]),int(I[6]))
        elif I[0]=="help":
            print("DONT USE MORE SPACES THAN IS WRITEN IN HELP COMMANDS!")
            print()
            print("exit")
            print("     deatil = end applicaton\n")
            print("add cast/actor/film_name")
            print("     detail = insert actor into database with existing film.\n     if person doesnt exist,then it will create it\n")
            print("add movie/actor1#actor2#...#actorN/year/film_id/language/rating")
            print("     detail = insert movie and all of actors, \n     if one of actor doesnt speak language in which is film recorded \n     then nothing is gonna happend(no data inserted),\n     u have to set all attributes correctly\n")
            print("add movie/name/year/film_id/language_id/rating")
            print("     deatil = check if film with this name exists. \n     If not then continue and chceck if language with this id exists. \n     If yes then create film.\n")
            print("add lang person/persons_name/lang_id")
            print("     detail = if some actor speaks more languages \n     u can insert step by step all of  them into db") 
            print("     u need already existing person and language_id to insert this data\n")
            print("update movie/name/year/film_id/language_id/rating")
            print("     detail = if u used command add movie with wrong data and \n     u wanna change it use this command 'update movie'. ")
            print("     update movie, find film by name. Rest of data replace with new. \n     If film doesnt exist return error message\n")
            print("del movie/name")
            print("     detail = delete movie from table MOVIES by name \n     ONLY if in no other table reference to this Film\n")
            print("DEL movie/name")
            print("     detail = delete all information about this film.\n     From tables Act,Directors,Movies\n")
            
        
# EXAMPLES:
comma="add cast/Leonardo Dicaprio/Alice in wonderland"   
comma="add movie/Titanic/1998/5/2/4"       
comma="add movie with cast/Leonardo Dicaprio#Kate Winslet#Harison Ford/Titanic/1998/5/2/4"

comma="add lang person/Leonardo Dicaprio/2"
comma="add lang person/Leonardo Dicaprio/3"
comma="add lang person/Kate Winslet/2"
comma="add lang person/Kate Winslet/7"
comma="del movie/Alice in wonderland"
comma="DEL movie/Alice in wonderland"

    
