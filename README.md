# Walt Disney Application (Flask)

Flask application 

Technologies used: Python, pip, Flask, Bootstrap, CSS, Jquery



FUNCTIONALITIES:

1. Displays three different pages
      #HOME
      #MOVIES
      #UPCOMING_MOVIES
      
2. Page Routing done through python
   
3. #HOME_PAGE
   * Displays some walt-disney movies in carousel 
   * Displays corresponding trailer of the movies in modal
   
4. #MOVIES_PAGE
   * Displays n number of walt-disney movies in cards with details  
   * Cards datas from Object file "data.py"
   * Once click any card of the movie, it directs to the corresponding wikipedia page of the movie
   
4. #UPCOMING_MOVIES_PAGE
   * Displays n number of upcoming walt-disney movies in cards with details
   * Cards datas from Object file "upcomingData.py"
   * Once click any card of the movie, it directs to the corresponding wikipedia page of the movie
 


CONFIGURATION:

1. Download & Install python from official site (https://www.python.org/downloads/windows/)

2. Set environment variable Path -> (Python)

3. Install "pip" for Flask framework("sudo apt -get install python3-pip")

3. Type "pip install flask" -> It creates Flask application in the specified path
     
4. Inside the path create a root file "app.py" & import flask 


EXECUTION:

1. Type "python app.py" in root directory

2. Flask application opens in the localhost port "5000"


