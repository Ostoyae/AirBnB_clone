# :house_with_garden: Airbnb Clone :wrench:
 [@Ostoyae](https://github.com/Ostoyae) and I are building an Airbnb clone. This first repo is the console for object management.

## High Level Overview: C.R.U.D.D Sandbox
:movie_camera: **Create** - Handles creating instances of objects such as Users, Places, Reviews, etc.

:dog: **Retrieve** - Handles reading data from a file or database such as finding users who staying in Toyko this week.

:wrench: **Update** - Handles changing data/features such as adding a user to a host's home.

:put_litter_in_its_place: **Destroy** - Handles removal of objects such as deleting an inappropriate review.

:running: **Do** - Handles general operations such as calculating average review, trip price, etc.

## :scroll: Table of Contents
* [Environment](#environment)
* [Installation](#installation)
* [Descriptions](#file-descriptions)
* [Usage](#usage)
* [Examples of Use](#examples-of-use)
* [Bugs](#bugs)
* [Authors](#authors)
* [License](#license)

## :earth_americas: Environment
* [Ubuntu 14.04 LTS](http://releases.ubuntu.com/14.04/) - OS
* [Python3.4.3](https://www.python.org/downloads/release/python-343/) - Language
* [pip3](https://pip.pypa.io/en/stable/) - Package Manager
* [PEP 8](https://www.python.org/dev/peps/pep-0008/) - Style Guide

## :arrow_down: Installation
* [Install Script](https://github.com/ConnorBrereton/AirBnB_clone/scripts) - Installation Script
* See examples of use for _interactive_ vs. _non-interactive_ mode

## :memo: Descriptions
Supported commands:
* `EOF` - exits console
* `quit` - exits console
* `<emptyline>` - overwrites default emptyline method and does nothing
* `create` - Creates a new instance of`BaseModel`, saves it (to the JSON file) and prints the id
* `destroy` - Deletes an instance based on the class name and id (save the change into the JSON file).
* `show` - Prints the string representation of an instance based on the class name and id.
* `all` - Prints all string representation of all instances based or not on the class name.
* `update` - Updates an instance based on the class name and id by adding or updating attribute (save the change into the JSON file).

## :school: Examples
```
➜  AirBnB_clone git:(master) ✗/console.py
(hbnb) helpDocumented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update(hbnb) all MyModel
** class doesn't exist **
(hbnb) create BaseModel
bf183ab2-3719-477f-87a7-22f0209b0653
(hbnb) all BaseModel
[[BaseModel] (bf183ab2-3719-477f-87a7-22f0209b0653) {'created_
at': datetime.datetime(2019, 2, 20, 16, 8, 57, 823535), 'update
d_at': datetime.datetime(2019, 2, 20, 16, 8, 57, 823535), 'id':
 'bf183ab2-3719-477f-87a7-22f0209b0653'}]
(hbnb) show BaseModel bf183ab2-3719-477f-87a7-22f0209b0653
[BaseModel] (bf183ab2-3719-477f-87a7-22f0209b0653) {'created_at
': datetime.datetime(2019, 2, 20, 16, 8, 57, 823535), 'updated_
at': datetime.datetime(2019, 2, 20, 16, 8, 57, 823535), 'id': '
bf183ab2-3719-477f-87a7-22f0209b0653'}
(hbnb) destroy BaseModel bf183ab2-3719-477f-87a7-22f0209b0653
(hbnb) show BaseModel d094af47-b450-4cef-92ae-84f3c975b183
** no instance found **
(hbnb) quit
```

## :bug: Bugs
None known at the this time. Please open a case should you find any.

## :octocat: Authors :octocat:
* **Connor Brereton** - [@ConnorBrereton](https://github.com/ConnorBrereton)

* **Martin Smith** - [@Ostoyae](https://github.com/Ostoyae)

## :mag: License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
