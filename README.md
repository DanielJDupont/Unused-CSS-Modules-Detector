# Unused CSS Modules Detector

### Rational for Using Pairs of .module.css and .tsx Files for Components

I enjoy using a pattern of using pairs of `.module.css` and `.tsx` files in React. This approach separates styling from logic very clearly, especially as I enjoy writing and having control over all of my own CSS and keeping the use of styling libraries to an absolute minimum. 

I typically write relatively large amounts of CSS so I have found this system to be crucial for myself as placing my CSS into .tsx files would overwhelm them quickly. I always create a .module.css file for every `.tsx` file and I consider breaking down and rewriting components if they exceed ~120 lines. I never use a single `.module.css` file with multiple components as I strive to also keep my `.module.css` files as small as possible.



The cost of having pairs of files is neglibile in the file-folder structure as long as the files are named the same and as long as groups of tightly coupled components are placed within their own folders.

The pattern of `.tsx` components always being paired with a `.module.css` file also makes it far more clear when a `.ts` file is present.


### How to Use

Tested on Python 3.7.6 with VS Code.

1. In VS Code, simply right click the `.tsx` file you want to check and copy the** full path**, not the relative path.

2. Paste the full path as your first argument into the terminal while running this python file: 
`python index.py /home/dan/Desktop/Unused-CSS-Module-Detector/File.tsx`

*Note that you will need to have Python installed and able to execute .py files from your terminal with this approach. Python environments can be easily changed using the bottom left of VS Code.*

### Other Notes

The corresponding `.module.css ` file will be checked automatically.

*Note that the `.module.css` file and the `.tsx` file must be named identically, for example:*
`File.module.css` `File.tsx`
`Profile.module.css` `Profile.tsx`
`index.module.css` `index.tsx`

Note that you must only provide the full path of the `.tsx` file. 
Do not provide the full path of the `.module.css` file as this program only expects the `.tsx` file.

### More Examples of How to Use the Command
`python index.py /home/dan/Desktop/Unused-CSS-Module-Detector/Profile.tsx`
`python index.py /home/dan/Desktop/Unused-CSS-Module-Detector/index.tsx`
`python index.py /home/dan/Desktop/interview_py/components/navbar/MobileDrawer.tsx`
`python index.py /home/dan/Desktop/interview_py/components/codeEditor/Editor/index.tsx`