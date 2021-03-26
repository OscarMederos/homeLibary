# home library
A python + sqlite app to keep track of my stuff & a flask driven API for interacting with the databse

### CLI
```
username@workstation:~/homedir/$ python3 api.py
username@workstation:~/homedir/$ python3 homelib.py

Select a console from the following options:
('psp',)
('ds',)
('ps3',)
('switch',)
('3ds',)
('gba',)

What console would you like to see? 
```
### API
```
username@workstation:~/homedir/$ python3 api.py

http://127.0.0.1:5000/api/v1/resources/videogames/all
http://127.0.0.1:5000/api/v1/resources/videogames?platform=<platform>
http://127.0.0.1:5000/api/v1/resources/videogames?tittle=<tittle>
http://127.0.0.1:5000/api/v1/resources/videogames?publisher=<publisher>
```
