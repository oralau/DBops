import ConfigParser
import logging
import sys
import datetime

class getParameter():

    def getStrParameter(self,paraFile,section,parameter):

        try:
            config = ConfigParser.RawConfigParser()
            config.read(paraFile)
            return config.get(section,parameter)

        except Exception as e:

           logging.error('errorCode' + str(e.returncode) + ':' + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + ':' + e.output)
           raise


    def getIntParameter(self, paraFile, section, parameter):


        try:
            config = ConfigParser.RawConfigParser()
            config.read(paraFile)
            return config.getint(section,parameter)

        except Exception as e:

            logging.error(
                'errorCode' + str(e.returncode) + ':' + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + ':' + e.output)
            raise




    def getFloatParameter(self, paraFile, section, parameter):

        try:
            config = ConfigParser.RawConfigParser()
            config.read(paraFile)
            return config.getfloat(section, parameter)

        except Exception as e:

            logging.error('errorCode' + str(e.returncode) + ':' + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + ':' + e.output)
            raise


    def getBooleanParameter(self, paraFile, section, parameter):

        try:
            config = ConfigParser.RawConfigParser()
            config.read(paraFile)
            return config.getboolean(section, parameter)

        except Exception as e:

            logging.error('errorCode' + str(e.returncode) + ':' + datetime.datetime.now().strftime(
               "%Y-%m-%d %H:%M:%S") + ':' + e.output)
            raise


    def getListParameter(self, paraFile, section, parameter):

        try:
            config = ConfigParser.RawConfigParser()
            config.read(paraFile)
            for  i  in str(config.get(section, parameter)).strip().split(','):
                yield i.strip()
                
        except Exception as e:

            logging.error('errorCode' + str(e.returncode) + ':' + datetime.datetime.now().strftime(
               "%Y-%m-%d %H:%M:%S") + ':' + e.output)
            raise