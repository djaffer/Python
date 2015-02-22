"""This program converts text in a textfile to pirate's speech"""
import urllib.request
def read_text():
    quotes = open(".\movie_quotes.txt") #textfile is converted to pirate speech
    content = quotes.read()
    print("Regular Speech: \n"+content)
    quotes.close()
    conv_to_pirate(content)

def conv_to_pirate(txt_to_check):
    opener = urllib.request.FancyURLopener({})
    connection = opener.open("http://isithackday.com/arrpi.php?text="+txt_to_check)
    output = connection.read()
    output = output.decode('utf-8')
    connection.close()
    print("Pirate Speech: \n"+output)

# main
read_text()
         
         

