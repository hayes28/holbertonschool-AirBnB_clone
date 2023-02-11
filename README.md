![hbnb](https://user-images.githubusercontent.com/107968573/216862342-3bd995bb-a40c-4fcd-a66b-d0473af89352.png)

# Holberton AirBnB Clone - The Console
This is the first part of a six part series of making a simple copy of the AirBnB website. This project will be completed over four months as part of our second trimester for Holberton Tulsa. Below we will have more of a description of the project and examples of how to use our console.
![consoleairbnb](https://user-images.githubusercontent.com/107968573/216862622-98157f58-fed6-49ad-8ca9-d475dd3d2483.png)
![projectconsole](https://user-images.githubusercontent.com/107968573/216862867-53d9fc30-ba3a-4380-ae28-873428023d80.png)

## How to open our console
The console can be use in interactive or non-interactive mode. 
By entering `./console.py` in the terminal a prompt will open up where the user can enter various commands to be executed. 
### Interactive Mode:
![Screenshot 2023-02-05 195845](https://user-images.githubusercontent.com/107968573/216865079-bae04d78-5162-496e-be7d-9f55719873ff.png)
### Non-Interactive Mode:
![Screenshot 2023-02-05 200301](https://user-images.githubusercontent.com/107968573/216865604-01de94ad-1c7c-4e6c-ac06-caef81c48166.png)<br />
Exiting the console is as easy as Ctrl+D or the `EOF` command.

## Authors
[Heather Hayes](https://github.com/hayes28)<br />
![Screenshot_20230205_081038](https://user-images.githubusercontent.com/107968573/216867015-7086ad53-2d97-4739-95d4-494cef5288f2.png)

[Chris Stamper](https://github.com/ZeroDayPoke)<br />
![Screenshot_20230205_081012](https://user-images.githubusercontent.com/107968573/216867070-beffb327-9caa-448f-8a25-b41b889e8a6d.png)

<h3>Class Info:</h3>
<p>

|            | BaseModel | User | State | City | Place | Review | Amenity | FileStorage |
| ---------- | --------- | ---- | ----- | ---- | ----- | ------ | ------- | ----------- |
| Defined In | models/base_model.py | models/user.py | models/state.py | models/city.py | models/place.py | models/review.py | models/amenity.py | models/engine/file_storage.py |
| Inherits From | N/A | BaseModel | BaseModel | BaseModel | BaseModel | BaseModel | BaseModel | N/A |
| Methods (Pub / Pri) | __str__(), save(), to_dict() Pub | Inh | Inh | Inh | Inh | Inh | Inh | all(), new(obj), save(), reload() Pub |

</p>

<h3>Console.py do_{{command}} descriptions & usage:</h3>
<p>

| **Command / Usage**                                     | **Descriptions**                                  |
| ------------------------------------------------------- | ------------------------------------------------- |
| quit                                                    | returns true, breaking cmdloop                    |
| EOF (Ctrl+D)                                            | prints goodbye msg to SO, then breaks loop        |
| create {{class name}}                                   | creates an instance of specified class            |
| show {{class name}} {{instance}}                        | prints str rep of class instance given class & id |
| destroy {{class name}} {{instance}}                     | destroy specified instance of class               |
| all {{class name}}                                      | prints str rep of all class instances in mem      |
| update {{class name}} {{instance}} {{attribute}} "{{value}}" | updates value of instance attribute in mem        |

</p>
<h3>Console.py examples:</h3>
<p>

First run the console from the repo's base directory with:
```
./console.py
```
After this a (hbnb) prompt should be printed to standard out, and the command loop started.

Now you can use the built-in console functionality! To show all instances of State for example, you could use:
```
all State
```
but alas, there might not be any states prepopulated, but that's okay since youc an make one with...
```
create State
```
after which the instance ID of your newly created State should be printed to standard out. repeating this 
a few times then re-running the
```all State``` command should produce a list of all the state instances!

Now try updating the name of a state instance with... update!
```
update State 16360b87-6657-45dc-acbd-d3628c322493 name "Oklahoma"
```
and let's also give the other example states names...
```
update State f8377c68-8c8e-4a8d-887e-c575639f7cba name "Texas"
update State bd4d4249-b710-4d6a-b197-4919f77c4145 name "Colorado"
```
but what if we one day decide Texas sucks? well we can delete it like this:
```
destroy State f8377c68-8c8e-4a8d-887e-c575639f7cba
```
now if we try
```
show State f8377c68-8c8e-4a8d-887e-c575639f7cba
```
we'll see the "** no instance found **" error message!
we can confirm the good states still exist with a quick
```
all State
```
then exit the console with the built in quit:
```
quit
```
![](https://github.com/ZeroDayPoke/holbertonschool-AirBnB_clone/blob/master/console_tutorial.png)
</p>

<h3>Console.py Interactive Exit Conditions</h3>
<ul>
<li>1. It receives a SIGTERM (Ctrl + D) EOF signal, causing a controlled shutdown</li>
<li>2. It receives a SIGKILL signal, whereafter undefined behavior may transpire</li>
<li>3. The built-in exit method 'quit' is used, also causing a controlled exit</li>
<li>4. A fatal program error occurs, and is most likely printed to stderr</li>
</ul>

