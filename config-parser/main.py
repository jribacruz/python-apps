import ConfigParser
config = ConfigParser.RawConfigParser()
config.read('service.cfg')

for item in config.items('HttpService'):
    print item