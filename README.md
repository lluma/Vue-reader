# Vue-reader
- Open the virtual environment for backend to run on  
$ source venv/bin/activate

- On touch to run.py  
(venv) cd ..  
(venv) touch run.py  
  
- Let the backend run on local  
(venv) FLASK_APP=run.py FLASK_DEBUG=1 flask run  
  
Reminding:  
- if you kill the backend by ctrl+z then you must encounter the access problem definitely  
(venv) ps-fA | grep python  
and find out the process's id(pid) then force to kill it  
(venv) sudo kill -9 (pid)  
