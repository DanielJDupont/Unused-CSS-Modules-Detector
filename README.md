# Unused CSS Modules Detector


### What Does This Do?

- Checks all pairs of `.tsx` and `.module.css` files for any missing or unused CSS between them and tells you what exactly is missing or unused in a provided folder and all of its subfolders.
- Tells you if any `.tsx` file is missing its corresponding `.module.css` file.
- Informs you if there is any difference in the spelling of the `.tsx` and its corresponding `.module.css` file.

### Rational for Using Pairs of .module.css and .tsx Files for Components

I enjoy using a pattern of using pairs of `.module.css` and `.tsx` files in React. This approach separates styling from logic very clearly, especially as I enjoy writing and having control over all of my own CSS and keeping the use of styling libraries to an absolute minimum. 

I typically write relatively large amounts of CSS so I have found this system to be crucial for myself as placing my CSS into `.tsx` files would overwhelm them quickly. I always create a `.module.css` file for every `.tsx` file and I consider breaking down and rewriting components if they exceed ~120 lines. I never use a single `.module.css` file with multiple components as I strive to also keep my `.module.css` files as small as possible.

The cost of having pairs of files is neglibile in the file-folder structure as long as the files are named the same. It is important that groups of tightly coupled components are grouped together their own folders.

The pattern of `.tsx` components always being paired with a `.module.css` file also makes it far more clear when a `.ts` file is present.


### How to Use

Tested on Python 3.7.6 with VS Code.

1. In VS Code, simply right click the **folder** you want to check and copy the **full path**, not the relative path.

2. Paste the **full path** as your first argument into the terminal while running the **index.py** file with **python**.
`python index.py /home/dan/Desktop/Unused-CSS-Module-Detector/`

*Note that you will need to have Python installed and able to execute .py files from your terminal with this approach. Python environments can be easily changed using the bottom left of VS Code.*

### Other Notes

All `.tsx` and `.module.css` files will be automatically checked within the folder full path you provide, as well as inside all nested folders. This is achieved with Python's `os.walk`.

*Note that the `.module.css` file and the `.tsx` file must be named identically for the check between them to occur properly, for example:*
- `File.module.css File.tsx`
- `Profile.module.css Profile.tsx`
- `index.module.css index.tsx`


### More Examples of How to Use the Command

`python index.py /home/dan/Desktop/interview_py/components`

`python index.py components/codeEditor`

`python index.py /home/dan/Desktop/interview_py/components/navbar`

`python index.py /home/dan/Desktop/interview_py/components/home`