# ntz-py
* **Purpose**
    * To familiarize with how to manipulate persistent data through command line.
* **Objective**
    * `ntz.py` is intended to be a note taker that can be interacted with through the command line.
    * `ntz.py` is a python command line note tool that allows users to read and write notes to and from `SQLite3`, `YAML`, or `JSON`

Keeping track of a small list of things to remember or stuff that needs doing is a pain. 
Remembering its location, manually accessing it, formatting it and all of the clicking that entails, 
is something many find unpleasant.

Other command line note tools out there are...clunky. 
They require interacting with vim or nano, and manual formatting. 
Yuck

ntz takes command line arguments and builds tidy todo/remember lists using the inherent 
neatness of SQLite (or YAML) and a little python magic. 
The result is a notes system that is easily manipulated both in the command line 
using ntz' interface, or manually in the SQLite database (or YAML file).


## Installation (Once you have it written)
1. Execute the command below to prepend the python environment to the `ntz.py`
    * `echo "#!/usr/bin/env python3" | cat - ntz.py`
2. Execute the command below to add execution permissions to `ntz.py`
    * `chmod +x ntz.py`
3. Execute the command below to move the `ntz.py` file to your `/usr/local/bin` directory.
    * `cp ./ntz.py /usr/local/bin/ntz.py`
4. Execute the command below to append `ntz` alias to your `.bashrc`
    * `echo "alias ntz='./ntz.py'" >> ~/.bashrc`
5. Execute the command below to reread the `.bashrc` file
    * `source ~/.bashrc`  

* TLDR

```bash
echo "#!/usr/bin/env python3" | cat - ntz.py
chmod +x ntz.py
cp ./ntz.py /usr/local/bin/ntz.py
echo "alias ntz='./ntz.py'" >> ~/.bashrc
source ~/.bashrc
```

## Usage

### What's it look like?
* ntz has four commands.
    * [r]emember
    * [-c] creates or appends to a category
    * [f]orget a note
    * [e]dit a note
    * clear
    
### Showing notes.
Typing `ntz` with no arguments should display all your notes. (Can you figure out how to send them to `more` or 
`less` so you can see them one screen at a time?)

## cli - command line interface to ntz json file.

### Showing notes.
Typing `ntz` will display your notes.
So will `ntz -l Shopping`

### Saving notes
Use [-r] for remember. Using [-r] on its own will save to the default ToDo category, like so:

`$ ntz -r "my first note"`

Using `-r` is the same as `ntz -c ToDo "my first note"

Use the -c flag to create a new category or direct a note to an existing category, like this:

`$ ntz -c Shopping "while out, get eggs"`

### Removing notes
Use [-f] for forget. [-f] requires a category and note number.

To delete the note we made in the Shopping category (and also the category, because it will be empty) we can do:

`$ ntz -f Shopping 1`

### Editing notes
Use [-e] for edit. This is more of a replacement then an edit.

To replace our first note, we can do

`$ ntz -e General 1 'my first note, edited'`

### Clearing all notes

`$ ntz clear`

You will be prompted with a Y/N and given a chance to review your notes before they are deleted.



