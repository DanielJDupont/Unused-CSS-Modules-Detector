# Unused SCSS Modules Detector

### Next Feature:

- I have found a love for nested pseudo-classes and @mixin with @include to cut down on duplicate css significantly and to improve its readability and maintainability. I don't really see a reason to use css without scss so all support for .css files has been removed and replaced with only supporting .scss files.


### What Does This Do?

- Checks all pairs of `.tsx` and `.module.scss` files for any missing or unused CSS between them and tells you what exactly is missing or unused.
- Checks the provided folder and all subfolders.
- Tells you if any `.tsx` file is missing its corresponding `.module.scss` file.
- Informs you if there is any difference in the spelling of the `.tsx` and its corresponding `.module.scss` file.

### Who Uses It?

This is primarily used by Interview Py to help enforce a specific file-folder structure and to check for any unused CSS.


### Opinion: Rationale for Using Pairs of .module.css and .tsx Files for Components for Interview Py

I enjoy using a pattern of using pairs of `.module.scss` and `.tsx` files in React. This approach separates styling from logic very clearly, especially as I enjoy writing and having control over all of my own CSS and keeping the use of styling libraries to an absolute minimum. I find the animations that styling libaries come with to be very useful as this is something I am weak at, but otherwise I find that they are far more pain than they are worth when trying to achieve a specific look, with a restrictive API you have to learn and difficult to access deeply nested tags.

I typically write relatively large amounts of CSS so I have found this system to be crucial for myself as placing my CSS into `.tsx` files would overwhelm them quickly, so I strongly disagree with the practice of combining CSS and JavaScript into the same file. The interelatedness of the two can be easily communicated through naming the two files correctly. I always create a `.module.scss` file for every `.tsx` file and I consider breaking down and rewriting components if they exceed ~100 lines.

The cost of having pairs of files is neglibile in the file-folder structure as long as the files are named the same. I strongly disagree with using a single CSS file for multiple `.tsx` files as this leads to massive and unmaintainable files and it is difficult to track exactly which CSS class belongs to which `.tsx` file. I never use a single `.module.css` file with multiple components as I strive to also keep my `.module.sss` files as small as possible.

It is important that groups of tightly coupled components are grouped together their folders. This tool enforces having a `.module.scss` file present even if there is no styling being used for a `.tsx` file, as all components are expected to appear as a pair of files at first visual glance. Empty `.module.scss` files occur rarely.

Writing all of your own CSS can quickly fall into an unmaintainable mess of duplicate CSS, or with small tweaks and experiments taking forever. When enough CSS is being repeated across components for relatively complex styling (same card designs being repeated or same button designs, or same table designs...) it is very important to move all of the duplicate CSS and JSX to their own component within a Shared folder. There may be many Shared folders for a project, each Shared folder resides with what components it is coupled with. Even if you do not have repeated CSS in your application, it is important to actually standardize and settle upon uniformity and consistently and to do this as soon as possible within your application. Ask yourself if you can refactor 10 different button styles into just 2 or 3 buttons you can reuse and maintain for a less bug prone user experience and a more consistent appearance with less code.

The pattern of `.tsx` components always being paired with a `.module.scss` file also makes it far more clear when a `.ts` file or some other file is present.


### How to Use

Tested on Python 3.7.6 with VS Code.

1. In VS Code, simply right click the **folder** you want to check and copy the **full path**, not the relative path.

2. Paste the **full path** as your first argument into the terminal while running the **index.py** file with **python**.
`python index.py /home/dan/Desktop/interview_py/components`

*Note that you will need to have Python installed and able to execute .py files from your terminal with this approach. Python environments can be easily changed using the bottom left of VS Code.*

### Other Notes

All `.tsx` and `.module.scss` files will be automatically checked within the folder full path you provide, as well as inside all nested folders. This is achieved with Python's `os.walk`.

*Note that the `.module.scss` file and the `.tsx` file must be named identically for the check between them to occur properly, for example:*
- `File.module.scss File.tsx`
- `Profile.module.scss Profile.tsx`
- `index.module.scss index.tsx`


### More Examples of How to Use the Command

`python index.py /home/dan/Desktop/interview_py/components`

`python index.py /home/dan/Desktop/interview_py/components/codeEditor`

`python index.py /home/dan/Desktop/interview_py/components/navbar`

`python index.py /home/dan/Desktop/interview_py/components/home`
