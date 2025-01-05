# CSS batch trainig

Allow to add trainings defined in the csv file for the members of the csstodulky to the web [https://csstodulky.cz](https://csstodulky.cz)

## CSV file
The CSV file allows only ';' as the separator.  
The first line of the CSV file must contain the labels of the columns.  
At this moments are only the columns `date`, `type`, `time` and `length` supported. 
See the [trainings_example.csv](trainings_example.csv)

#### [date]
uses d.m.yyyy format (example `1.1.2025`)

#### [type]
ineger value defines the type of sport activity:  
 1 - road bike  
 2 - ergo  
 3 - posilovna  
 4 - others  
 5 - swiming  
 6 - ski  
 7 - running  
 8 - MTB  

 #### [time]
 duration of the sport activity uses h:m:s format (example `1:35:47`)

 #### [length]
 length of the training in km (example `33,4`)


# TODO

1) check source data for the validity
2) add  support for other parameters like mut, avrage speed, notes and the heard rate
