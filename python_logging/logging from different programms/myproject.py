import logging

def testfunction(var1,var2):
    logger = logging.getLogger("loggerexample3.myproject.testfunction")    
    logger.info("added %s and %s to get %s" % (var1, var2, var1+var2))    
    return var1+var2