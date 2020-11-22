# twittermarket

#back end done with python using

__init__.py
#initializes data base connetion, twitters api authorization and creates app

app.py
#has all the routes where it servers as an api for the front end to get info/data to use in the web app front end

@app.route('/register_account')
#routes that deals with registring suppliers account and saving the supplier info do the database in the 'Users Table'
#also saves the product to the Products table

@app.route('/get_analyze')
#search most revelant tweets about the requested product, send it to the sentiment analyze and give it back to the front end the porcentage of people saying positive, negative
#and neutral things about that product

@app.route('/new_request')
#everytime someone tweets ! followed by a product that is in our database ('Products Table'), it receives a post request and save that request to a data base 'Table Requests'

@app.route('/allproducts')
#send back all the products that are in our database 'Products Table'

@app.route('/get_requests')
#send back all the requests (!<product> tweets) based on the requested location and product
  
streamer.apy
#a separate program that runs infinitely and keeps track (real time) if someone tweets any "!" followed by a word that is a product in our data base and send a post request with 
#that tweets information to app.py (@app.new_request)

test.py
#ignore it lol

Procfie
#failed attempts to deploy this web app

#sentiments.py and ml folder
abnu stuff
