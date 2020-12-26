# Unused SCSS Modules Detector

### What Does This Do?

- Checks all pairs of `.tsx` and `.module.scss` files for any missing or unused CSS between them and tells you what exactly is missing by reporting a list for each the `.tsx` and the `.module.scss` on what should not be in each file.
- Checks the provided folder and all subfolders using the Python OS API.
- Tells you if any `.tsx` file doesn't have or is spelled incorrectly compared to its corresponding `.module.scss` file through FileNotFoundError messages.

### Who Uses It?

This is primarily used by Interview Py to help enforce a specific file-folder structure and to check for any unused CSS.

### How to Use:

Tested on Python 3.7.6 with VS Code.

1. In VS Code, simply right click the **folder** you want to investigate and copy the **full path**, not the relative path.

2. Paste the **full path** as your first argument into the terminal while running the **index.py** file with **python**. Below is an example of myself providing the **full path** to the location I want to investigate on my own file system while also having the current folder for this program open in the terminal. Your full path will almost certainly be different from mine.

`python index.py /home/dan/Desktop/Unused-CSS-Modules-Detector`

3. Run the command and check out the results of what happens when you investigate the ExampleCoffeeCard.



*Note that you will need to have Python installed and able to execute .py files from your terminal with this approach. Python environments can be easily changed using the bottom left of VS Code.*

### Other Notes:

All `.tsx` and `.module.scss` files will be automatically checked within the folder full path you provide, as well as inside all nested folders. This is achieved with Python's `os.walk`.

*Note that the `.module.scss` file and the `.tsx` file must be named identically for the check between them to occur properly, for example:*
- `File.module.scss File.tsx`
- `Profile.module.scss Profile.tsx`
- `index.module.scss index.tsx`


### More Examples of How to Use the Command:

`python index.py /home/dan/Desktop/interview_py/components`

`python index.py /home/dan/Desktop/interview_py/components/codeEditor`

`python index.py /home/dan/Desktop/interview_py/components/navbar`

`python index.py /home/dan/Desktop/interview_py/components/home`

