# CSS batch training

Allow to add trainings defined in the csv file for the members of the csstodulky to the web [https://csstodulky.cz](https://csstodulky.cz)

## CSV file
The CSV file allows only ';' as the separator.  
The first line of the CSV file must contain the labels of the columns.  
At this moments are only the columns `date`, `type`, `time` and `length` supported. 
See the [trainings_example.csv](trainings_example.csv)

---
### Mandatory columns

#### [date]
Uses d.m.yyyy format (example `1.1.2025`)

#### [type]
Integer value defines the type of sport activity:  
1 - road bike  
2 - ergo  
3 - posilovna  
4 - others  
5 - swiming  
6 - ski  
7 - running  
8 - MTB  

#### [time]
Duration of the sport activity uses h:m:s format (example `1:35:47`)

#### [length]
Length of the training in km (example `137,4`)

---
###  Optional columns
#### [avg]
Average speed during the training in km/h (example `33,4`)

#### [heardrate_avg]
Average heard beat rate in beats/sec (example `137`)

#### [heardrate_max]
Maximal heard beat rate in beats/sec (example `186`)

#### [feeling]
Integer value of feeling during the training:  
1 - Awesome  
2 - Good  
3 - Average  
4 - Poor  
5 - Very bad  

#### [info]
Optional text to the training

---
TODO: check input data for validity or print result of each insertion of workout