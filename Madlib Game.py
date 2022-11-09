
#Game code

def mad_lib():
       
   """ Popular 
   Mad lib game"""
       
   space,inputs,pos=" ",[], ['A random last name','A noun','The time of day','An adjective','A verb present, that ends in ing',\
      'A body part','A number ', 'A noun','A verb base form','A liquid','A number', \
         'A period of time- day, month, year, etc','A noun plural', 'An animal','A noun plural','Your name']
   
   for part in pos:
          inputs.append(input(f"give me {part}{space}"))
          
   print("""Dear Dr. {0},
I cannot not make it to {1} this {2}. I am very {3} and cannot stop {4} my {5}. I have a fever of {6} degrees and the doctor ordered me to stay in {7} and {8} lots of {9}. Also. Can I have a {10} {11} extension on the essay about {12}? My {13} ate it now I have to start all over!
Best {14}
{15}""".format(*inputs))

          
      
mad_lib() 
print(mad_lib.__doc__)