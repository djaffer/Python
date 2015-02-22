"""This program checks in a text file if there are any curse words via using the
the google website wdyl"""
import urllib.request
def read_text():
    quotes = open(".\movie_quotes.txt")
    content = quotes.read()
    print(content)
    quotes.close()
    check_profanity(content)

def check_profanity(txt_to_check):
    opener = urllib.request.FancyURLopener({})
    connection = opener.open("http://www.wdyl.com/profanity?q="+txt_to_check)
    output = connection.read()
    output = output.decode('utf-8')
    connection.close()
    if "true" in output.lower():
        print("Curse words detected!!")
    elif "falsE".lower() in output.lower():
        print("No curse words detected!!")
    else:
        print("Could not scan document properly")
            
    # print(output)
   


# main
read_text()
         
         

