import sys
import os

result = os.walk(str(sys.argv[1]))

print("Checking for all unused SCSS and styles in the folder: " + sys.argv[1])
# os.walk returns a list of tuples, with a tuple being an immutable list, a tuple represents the contents of a folder.
# This is essentially a comprehensive list of all folders and their contents within the selected folder.
# Each tuple has three indexes, the first index contains the full path of the current folder.
# The second argument is a list of all folders available within the folder, it is of no interest to us.
# The third argument contains all of the files present in the current folder.
found_tsx_files = []
for tuple_element in result:
    for file_item in tuple_element[2]:
        if ".tsx" in file_item:
            found_tsx_files.append(tuple_element[0] + "/" + file_item)


# For all of the walked .tsx files found.
for item in found_tsx_files:

    f_module_scss = open(item[0:-4] + ".module.scss", "r")
    f_tsx = open(item, "r")

    # Read in all SCSS class names from .module.css.
    # In the .module.scss file, add all ".className {" to a list between the "." and " {" so just record "className"
    module_scss_classes = []

    for line in f_module_scss:
        # Check if the header of the scss class contains anything that would mean it is not used in the .tsx file directly.
        if line[0] == '.' and ":" not in line and ">" not in line and 'iframe' not in line and "@mixin" not in line:
            className = line[1:-3]
            module_scss_classes.append(className)

    f_module_scss.close()

    # Read in all styles from .tsx.
    # In the .tsx file, add all "styles={className}" to a list between the "styles={" and "}" so just record "className"
    tsx_scss_classes = []

    for line in f_tsx:
        if "styles." in line:
            # Get the exact position on the line of where "styles={" is located.
            stylesIndex = line.index("styles.")
            # Get the exact position immediately to the right of the brace, which is where the CSS class name is located.
            classNameIndex = stylesIndex + len("styles.")

            # Iterate until we encounter a closing brace, which is where the end of the class name is.
            index = classNameIndex
            currentCharacter = line[classNameIndex]
            while currentCharacter not in ["}", ';', ' ', '\n']:
                index += 1
                try:
                    currentCharacter = line[index]
                except:
                    print("something is wrong")

            classNameIndexEnd = index

            className = line[classNameIndex: classNameIndexEnd]
            tsx_scss_classes.append(className)

    f_tsx.close()

    # Convert the list of class names and styles into sets, which are lists with no duplicates.
    module_scss_classes_set = set(module_scss_classes)
    tsx_scss_classes_set = set(tsx_scss_classes)

    # Logic that separately checks which classNames or styles are not used in the .module.css and .tsx files respectively.
    unused_module_scss = []
    for className in module_scss_classes_set:
        if className not in tsx_scss_classes_set:
            unused_module_scss.append(className)

    unused_tsx_styles = []
    for className in tsx_scss_classes_set:
        if className not in module_scss_classes_set:
            unused_tsx_styles.append(className)

    if len(unused_module_scss) != 0 or len(unused_tsx_styles) != 0:
        print("")
        print(item[len(sys.argv[1]):])
        print("Unused .module.scss:")
        print(unused_module_scss)
        print("Unused in .tsx:")
        print(unused_tsx_styles)


print("")
print("")
print("Check for unused CSS in .module.css and unused styles in .tsx complete.")
