from distutils.log import debug
from server.instace import server
from server.situacao import *
import os 


port = int(os.environ.get('PORT', 5000)) 
server.run(host='0.0.0.0', port=port)
#server.run()