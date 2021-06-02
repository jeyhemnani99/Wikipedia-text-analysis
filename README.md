# Wikipedia-text-analysis
a Web Application that takes Wikipedia URL as input via simple Frontend form. On the backend, scrap the data from that Wikipedia page, and identify the most frequent words. Show top 10 frequent words with their counts, on the Frontend page in simple table format.

Web application using flask/pyhton.

Frontend: form.html & style.css
Backend: app.py

before compiling the code, 
Import following libraries:
                           Flask                
                           bs4        

Example:

Url:https://en.wikipedia.org/wiki/Sachin_Tendulkar

output: | Words       |  Count  |
        | the 	      |  1338   |
        | in 	        |  593    |
        | on	        |  476    |
        | of 	        |  427    |
        | from 	      |  424    |
        | retrieved   |	 422    |
        | tendulkar   |  399    |
        | archived    |  374    |
        | original    |  370    |
        | and         |  335    |
  
