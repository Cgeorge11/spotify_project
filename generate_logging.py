# importing module
import logging
#from search_spotify import * 
# Create and configure logger
logging.basicConfig(filename="newfile.txt",
                    format='%(asctime)s %(message)s',
                    filemode='w')
 
# Creating an object
logger = logging.getLogger()
 
# Setting the threshold of logger to DEBUG
logger.setLevel(logging.DEBUG)
 
