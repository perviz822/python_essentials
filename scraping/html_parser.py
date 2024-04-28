from html.parser import HTMLParser


# Enter your code here. Read input from STDIN. Print output to STDOUT


# create a subclass and override the handler methods
class Parser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print ("Start :", tag)
        self.print_attr(attrs)
    def handle_endtag(self, tag):
        print ("End   :", tag)
    def handle_startendtag(self, tag, attrs):
        print ("Empty :", tag)
        self.print_attr(attrs)
        
        
    def print_attr(self,attrs):
      for attr, value  in attrs:
          print("->{}>{}".format(attr,value))

# Creating an instance of our class.ll
parser = Parser()
# Poviding the input.
parser.feed('<html><title class = "t1">Satyam Blog</title><body><p>'
            'I love Tea.</p><'
            '/body><!--Just started--></html>')
