import datetime
x = datetime.datetime.now()
print(x)

import datetime                   #  "%A"
x = datetime.datetime.now()
print(x.year)
print(x.strftime("%A"))

import datetime
x=datetime.datetime.now()
print(x.year)
print(x.strftime("%A"))

import datetime                    # "%a"
x=datetime.datetime.now()
print(x.year)
print(x.strftime("%a"))

import datetime
x=datetime.datetime(2020, 5, 17)
print(x)

import datetime
x=datetime.datetime(2012, 10, 12)
print(x)

import datetime                         # "%B"
x=datetime.datetime(2018, 6, 1)
print(x.strftime("%B"))


# %a    	Weekday,    short version     	Wed
import datetime
x = datetime.datetime.now()
print(x.strftime("%a"))


# %A    	Weekday,   full   version	 Wednesday
import datetime
x = datetime.datetime.now()
print(x.strftime("%A"))


# %w	Weekday as a number 0-6, 0 is Sunday	3
import datetime
x = datetime.datetime.now()
print(x.strftime("%w"))


# %d	Day of month 01-31	31
import datetime
x = datetime.datetime.now()
print(x.strftime("%d"))


# %b	Month name,  short version	  Dec
import datetime
x = datetime.datetime.now()
print(x.strftime("%b"))


# %B	Month name,   full version	  December	
import datetime
x = datetime.datetime.now()
print(x.strftime("%B"))


# %m  	Month as a number 01-12	      12
import datetime
x = datetime.datetime.now()
print(x.strftime("%m"))


# %y	Year, short version, without century	18
import datetime
x = datetime.datetime.now()
print(x.strftime("%y"))


# %Y	Year, full version	  2018
import datetime
x = datetime.datetime.now()
print(x.strftime("%Y"))


# %H	  Hour 00-23	   17
import datetime
x = datetime.datetime.now()
print(x.strftime("%H"))


# %I	  Hour 00-12	  05
import datetime
x = datetime.datetime.now()
print(x.strftime("%I"))


# %p	   AM/PM	 PM
import datetime
x = datetime.datetime.now()
print(x.strftime("%p"))


# %M	Minute 00-59	41
import datetime
x = datetime.datetime.now()
print(x.strftime("%M"))


# %S	Second 00-59	08
import datetime
x = datetime.datetime.now()
print(x.strftime("%S"))


# %f	Microsecond 000000-999999	548513
import datetime
x = datetime.datetime.now()
print(x.strftime("%f"))


# %j	Day number of year 001-366  	365
import datetime
x = datetime.datetime.now()
print(x.strftime("%j"))


# %U	Week number of year, Sunday as the first day of week, 00-53	    52
import datetime
x = datetime.datetime.now()
print(x.strftime("%U"))


# %W	Week number of year, Monday as the first day of week, 00-53 	52
import datetime
x = datetime.datetime(2018, 5, 31)
print(x.strftime("%W"))


# %c	Local version of date and time      	Mon Dec 31 17:41:00 2018
import datetime
x = datetime.datetime.now()
print(x.strftime("%c"))


# %C	Century	   20
import datetime
x = datetime.datetime.now()
print(x.strftime("%C"))


# %x	Local version of date   	12/31/18
import datetime
x = datetime.datetime.now()
print(x.strftime("%x"))


# %X	Local version of time   	17:41:00
import datetime
x = datetime.datetime.now()
print(x.strftime("%X"))


#%G	ISO 8601 year	2018
import datetime
x = datetime.datetime.now()
print(x.strftime("%G"))


# %u	ISO 8601 weekday (1-7)  	1
import datetime
x = datetime.datetime.now()
print(x.strftime("%u"))


# %V	ISO 8601 weeknumber (01-53)	   01
import datetime
x = datetime.datetime.now()
print(x.strftime("%V"))
