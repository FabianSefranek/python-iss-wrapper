# 🌌 Python Open Notify Iss Wrapper

An easy to use [Open-Notify](http://open-notify.org) Wrapper, written in Python

These instructions will get you a copy of the project up and running on your local machine for development purposes.

###  Prerequisites

What things you need to install the software and how to install them

```
python>=3.8
requests>=2.24.0
datetime>=4.3
```
###  Usage

A step by step series of examples that tells you how to get use this wrapper

1. Import the wrapper

```
from pyIss import Iss
```

2. Call a function like so
```
Iss.function()
```

### Functions
Get the current location from the Iss station
```
Iss.get_location()
  > {'latitude': '-2.0531', 'longitude': '-68.3810'}
```

Get the next time, the Iss passes a specific location
> Arguments: latitude, longitude, altitude
```
Iss.get_next_pass_time(lat, lon, alt)
  > "2020-12-22 03:49:18"
```

Get a number of times, the Iss passes a specific location
> Arguments: latitude, longitude, altitude & number of return values
```
Iss.get_next_pass_time(lat, lon, alt, num)
  > ['2020-12-22 03:49:18', '2020-12-22 05:28:34', '2020-12-22 13:51:19']
```

Get the number of astronauts, that are currently on the Iss station
```
Iss.get_number_of_astronauts()
  > 3
```

Get the astronauts names
```
Iss.get_astronauts()
  > ['Sergey Ryzhikov', 'Kate Rubins', 'Sergey Kud-Sverchkov']
```

## Meta

Fabian Sefranek

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details
