# 0x00. AirBnB clone - The console

---

## Description

This is a complete web application, integrating database storage,
a back-end API, and front-end interfacing in a clone of [AirBnB](https://www.airbnb.com/).

## Classes

The project has the following classes:

* [BaseModel](./models/base_model.py)
* [User](./models/user.py)
* [State](./models/state.py)
* [City](./models/city.py)
* [Place](./models/place.py)
* [Amenity](./models/amenity.py)
* [Review](./models/review.py)

## Storage

The above classes are handled by the abstracted storage engine defined in the
[FileStorage](./models/engine/file_storage.py) class.

Every time the backend is initialized, hbnb instantiates an instance of
`FileStorage` called `storage`. The `storage` object is loaded/re-loaded from
any class instances stored in the JSON file `file.json`. As class instances are
created, updated, or deleted, the `storage` object is used to register
corresponding changes in the `file.json`.

## Console

The console is a command line interpreter that permits management of the backend
of hbnbBnB. It can be used to handle and manipulate all classes utilized by
the application (achieved by calls on the `storage` object defined above).

### Using the Console

The hbnbBnB console can be run both interactively and non-interactively.
To run the console in non-interactive mode, pipe any command(s) into an execution
of the file `console.py` at the command line.

```html
$ echo "help" | ./console.py
(hbnb) 
Documented commands (type help <topic>):
========================================
EOF  all  count  create  destroy  help  quit  show  update

(hbnb) 
$
```html

Alternatively, to use the hbnb console in interactive mode, run the
file `console.py` by itself:

```html
./console.py
```

While running in interactive mode, the console displays a prompt for input:

```html
$ ./console.py
(hbnb) 
```

To quit the console, enter the command `quit`, or input an EOF signal
(`ctrl-D`).

```html
$ ./console.py
(hbnb) quit
$
```

```html
$ ./console.py
(hbnb) EOF
$
```

### Console Commands

The hbnb console supports the following commands:

* **create**
  * Usage: `create <class>`

Creates a new instance of a given class. The class' ID is printed and
the instance is saved to the file `file.json`.

```html
$ ./console.py
(hbnb) create BaseModel
5fe40558-76e4-4331-aac5-9ada7acd550d
(hbnb) quit
$ cat file.json ; echo ""
{"BaseModel.5fe40558-76e4-4331-aac5-9ada7acd550d": {"id": "5fe40558-76e4-4331-aac5-9ada7acd550d", "created_at": "2022-08-06T21:46:16.635887", "updated_at": "2022-08-06T21:46:16.635887", "__class__": "BaseModel"}}
```

* **show**
  * Usage: `show <class> <id>` or `<class>.show(<id>)`

Prints the string representation of a class instance based on a given id.

```html
$ ./console.py
(hbnb) create User
d27f7b98-7245-4242-8134-3510f2f411ad
(hbnb)
(hbnb) show User d27f7b98-7245-4242-8134-3510f2f411ad
['type'] d27f7b98-7245-4242-8134-3510f2f411ad {'id': 'd27f7b98-7245-4242-8134-3510f2f411ad', 'created_at': datetime.datetime(2022, 8, 6, 21, 48, 0, 796174), 'updated_at': datetime.datetime(2022, 8, 6, 21, 48, 0, 796174)}
(hbnb) 
(hbnb) User.show(d27f7b98-7245-4242-8134-3510f2f411ad)
['type'] d27f7b98-7245-4242-8134-3510f2f411ad {'id': 'd27f7b98-7245-4242-8134-3510f2f411ad', 'created_at': datetime.datetime(2022, 8, 6, 21, 48, 0, 796174), 'updated_at': datetime.datetime(2022, 8, 6, 21, 48, 0, 796174)}
(hbnb) 
```

* **destroy**
  * Usage: `destroy <class> <id>` or `<class>.destroy(<id>)`

Deletes a class instance based on a given id. The storage file `file.json`
is updated accordingly.

```html
$ ./console.py
(hbnb) create State
a83b9d85-fa65-4fab-895b-2f5cfc420e1f
(hbnb) create Place
8ae9fd6c-7fbc-4337-bcff-adfb8a228ba2
(hbnb)
(hbnb) destroy State 8ae9fd6c-7fbc-4337-bcff-adfb8a228ba2
(hbnb) Place.destroy(8ae9fd6c-7fbc-4337-bcff-adfb8a228ba2)
(hbnb) quit
$ cat file.json ; echo ""
{}
```

* **all**
  * Usage: `all` or `all <class>` or `<class>.all()`

Prints the string representations of all instances of a given class. If no
class name is provided, the command prints all instances of every class.

```html
$ ./console.py
(hbnb) create BaseModel
fce2124c-8537-489b-956e-22da455cbee8
(hbnb) create BaseModel
450490fd-344e-47cf-8342-126244c2ba99
(hbnb) create User
b742dbc3-f4bf-425e-b1d4-165f52c6ff81
(hbnb) create User
8f2d75c8-fb82-48e1-8ae5-2544c909a9fe
(hbnb)
(hbnb) all BaseModel
["[BaseModel] (450490fd-344e-47cf-8342-126244c2ba99) {'updated_at': datetime.da
tetime(2022, 8, 3 21, 45, 5, 963516), 'created_at': datetime.datetime(2022, 8
, 17, 21, 45, 5, 963516), 'id': '450490fd-344e-47cf-8342-126244c2ba99'}", "[Bas
eModel] (fce2124c-8537-489b-956e-22da455cbee8) {'updated_at': datetime.datetime
(2022, 8, 3 21, 43, 56, 899348), 'created_at': datetime.datetime(2022, 8, 3
21, 43, 56, 899348), 'id': 'fce2124c-8537-489b-956e-22da455cbee8'}"]
(hbnb)
(hbnb) User.all()
["[User] (8f2d75c8-fb82-48e1-8ae5-2544c909a9fe) {'updated_at': datetime.datetim
e(2022, 8, 3 21, 44, 44, 428413), 'created_at': datetime.datetime(2022, 8, 17
, 21, 44, 44, 428413), 'id': '8f2d75c8-fb82-48e1-8ae5-2544c909a9fe'}", "[User] 
(b742dbc3-f4bf-425e-b1d4-165f52c6ff81) {'updated_at': datetime.datetime(2022, 8
, 17, 21, 44, 15, 974608), 'created_at': datetime.datetime(2022, 8, 3 21, 44,
15, 974608), 'id': 'b742dbc3-f4bf-425e-b1d4-165f52c6ff81'}"]
(hbnb) 
(hbnb) all
["[User] (8f2d75c8-fb82-48e1-8ae5-2544c909a9fe) {'updated_at': datetime.datetime(2022, 8, 3 21, 44, 44, 428413), 'created_at': datetime.datetime(2022, 8, 17
, 21, 44, 44, 428413), 'id': '8f2d75c8-fb82-48e1-8ae5-2544c909a9fe'}", "[BaseMo
del] (450490fd-344e-47cf-8342-126244c2ba99) {'updated_at': datetime.datetime(20
19, 2, 17, 21, 45, 5, 963516), 'created_at': datetime.datetime(2022, 8, 3 21,
45, 5, 963516), 'id': '450490fd-344e-47cf-8342-126244c2ba99'}", "[User] (b742db
c3-f4bf-425e-b1d4-165f52c6ff81) {'updated_at': datetime.datetime(2022, 8, 3 2
1, 44, 15, 974608), 'created_at': datetime.datetime(2022, 8, 3 21, 44, 15, 97
4608), 'id': 'b742dbc3-f4bf-425e-b1d4-165f52c6ff81'}", "[BaseModel] (fce2124c-8
537-489b-956e-22da455cbee8) {'updated_at': datetime.datetime(2022, 8, 3 21, 4
3, 56, 899348), 'created_at': datetime.datetime(2022, 8, 3 21, 43, 56, 899348
), 'id': 'fce2124c-8537-489b-956e-22da455cbee8'}"]
(hbnb) 
```

* **count**
  * Usage: `count <class>` or `<class>.count()`

Retrieves the number of instances of a given class.

```html
$ ./console.py
(hbnb) create Place
8ae9fd6c-7fbc-4337-bcff-adfb8a228ba2
(hbnb) create Place
c7854150-d828-49bc-967a-eee37dfd0953
(hbnb) create City
1fa46dfc-c634-460a-ad9c-ce5a59829e1a
(hbnb) create City
ceb92f23-5164-4c48-8451-515975a7cf89
(hbnb) 
(hbnb) count Place
2
(hbnb) city.count()
2
(hbnb) 
```

* **update**
  * Usage: `update <class> <id> <attribute name> "<attribute value>"` or
`<class>.update(<id>, <attribute name>, <attribute value>)` or `<class>.update(
<id>, <attribute dictionary>)`.

Updates a class instance based on a given id with a given key/value attribute
pair or dictionary of attribute pairs. If `update` is called with a single
key/value attribute pair, only "simple" attributes can be updated (ie. not
`id`, `created_at`, and `updated_at`). However, any attribute can be updated by
providing a dictionary.

```html
$ ./console.py
(hbnb) create User
03c69f4e-f2c4-4e84-92b6-665d90cec0ba
(hbnb)
(hbnb) update User 03c69f4e-f2c4-4e84-92b6-665d90cec0ba last_name "Blaq"
(hbnb) show User ['type'] 03c69f4e-f2c4-4e84-92b6-665d90cec0ba {'id': '03c69f4e-f2c4-4e84-92b6-665d90cec0ba', 'created_at': datetime.datetime(2022, 8, 6, 22, 43, 24, 238977), 'updated_at': datetime.datetime(2022, 8, 6, 22, 43, 24, 238977), 'last_name': 'Blaq'}
(hbnb)
(hbnb) User.update(6f348019-0499-420f-8eec-ef0fdc863c02, address, "98 Mission S
t")
(hbnb) User.show(30d57c4d-bc9c-4542-8b7b-6e4da8364640)
['type'] 30d57c4d-bc9c-4542-8b7b-6e4da8364640 {'id': '30d57c4d-bc9c-4542-8b7b-6e4da8364640', 'created_at': datetime.datetime(2022, 8, 6, 21, 37, 9, 970882), 'updated_at': datetime.datetime(2022, 8, 6, 21, 37, 9, 970882)}
(hbnb)
(hbnb) (hbnb) User.update(03c69f4e-f2c4-4e84-92b6-665d90cec0ba, email "blaq@hackersploit.or")
(hbnb)User.show(03c69f4e-f2c4-4e84-92b6-665d90cec0ba)
['type'] 03c69f4e-f2c4-4e84-92b6-665d90cec0ba {'id': '03c69f4e-f2c4-4e84-92b6-665d90cec0ba', 'created_at': datetime.datetime(2022, 8, 6, 22, 43, 24, 238977), 'updated_at': datetime.datetime(2022, 8, 6, 22, 43, 24, 238977), 'last_name': 'Blaq', 'email': 'blaq@hackersploit.or'}
(hbnb) 
```

## Authors

The project has been authored by individuals in [AUTHORS](./AUTHORS)
