# Film-database
data gateway connection-PostgreSQL
My goal is to create a console application which comunicate with user as a classic command line(shell)
by typing help u will see manual:
DONT USE MORE SPACES THAN IS WRITEN IN HELP COMMANDS!

exit
     deatil = end applicaton

add cast/actor/film_name
     detail = insert actor into database with existing film.
     if person doesnt exist,then it will create it

add movie/actor1#actor2#...#actorN/year/film_id/language/rating
     detail = insert movie and all of actors,
     if one of actor doesnt speak language in which is film recorded
     then nothing is gonna happend(no data inserted),
     u have to set all attributes correctly

add movie/name/year/film_id/language_id/rating
     deatil = check if film with this name exists.
     If not then continue and chceck if language with this id exists.
     If yes then create film.

add lang person/persons_name/lang_id
     detail = if some actor speaks more languages
     u can insert step by step all of  them into db
     u need already existing person and language_id to insert this data

update movie/name/year/film_id/language_id/rating
     detail = if u used command add movie with wrong data and
     u wanna change it use this command 'update movie'.
     update movie, find film by name. Rest of data replace with new.
     If film doesnt exist return error message

del movie/name
     detail = delete movie from table MOVIES by name
     ONLY if in no other table reference to this Film

DEL movie/name
     detail = delete all information about this film.
     From tables Act,Directors,Movies

--------------------------------------
if u need some concrete exapmles,here u are
        
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
----------------------------------------
db.jpg is UML diagram of tables. I recomend firstly check this picture.
know the structure and relations of tables.
----------------------------------------


