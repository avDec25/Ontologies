import xml.etree.ElementTree as et
import webbrowser

front = """<!doctype html>
<html lang="en">
  <head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">

    <title>XML Data</title>
  </head>
  <body>"""
middle = ""
rear = """<script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js" integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q" crossorigin="anonymous"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
  </body>
</html>"""

tree = et.parse('temp.xml')
news = tree.getroot()

data = ""
format_data_start = """<table class="table table-hover"><tbody>"""
format_data_end = """</tbody></table>"""

row_num = 1

field = input("Field name? ")
instance = input("Instance name? ")

middle = "<thead><tr><th scope='col'>Retrieving instances where " + field + " = " + instance + "</th></tr></thead>"
for article in news:
    author = article.find(field).text
    if author == instance:#'PTI':
        data = article.find('headline').text
        middle += "<tr><th scope='row'>" + str(row_num) + "</th><td>" + data + "</td></tr>"
        row_num += 1
        print(data)

f = open('temp.html','w')

f.write(front + format_data_start + middle + format_data_end + rear)
f.close()

filename = 'temp.html'
webbrowser.open_new_tab(filename)
