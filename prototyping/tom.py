import ConfigParser
import StringIO
import os

# Given a properties file (property=value format), Read every line into a StringIO memory-based object
# have the SafeConfigParser parse it into a dictionary and return it to the caller
def read_properties_file(file_path):
    with open(file_path) as f:
        config = StringIO.StringIO()
        config.write('[dummy_section]\n')
        config.write(f.read().replace('%', '%%'))
        config.seek(0, os.SEEK_SET)

        cp = ConfigParser.SafeConfigParser()
        cp.readfp(config)

        return dict(cp.items('dummy_section'))
    
# props = read_properties_file('tom.properties')
props = read_properties_file('C:/Applications/MyEclipse2015CI/Workspaces/VCHS_HomeworkCrawler/resources/config.properties')
# It will raise if `name` is not in the properties file
# name = props['name']
worksheet_caption = props.get('worksheet_caption')
# And if you deal with optional settings, use:
google_keyfile = props.get('google_keyfile')
google_spreadsheet_sharing = props.get('google_spreadsheet_sharing')

print ("worksheet_caption: " + worksheet_caption)
print( "google_keyfile: " + google_keyfile)
print( "google_spreadsheet_sharing: " +  google_spreadsheet_sharing)

