import sys

print("Number of arguments: ", len(sys.argv))
print("Argument List: ", str(sys.argv))


f_module_css = open("{}".format(sys.argv[1][0:-3] + "module.css"), "r")
f_tsx = open("{}".format(str(sys.argv[1])), "r")


# In the .module.css file, add all ".className {" to a list between the "." and " {" so just record "className"
module_css_classes = []
for line in f_module_css:
    if line[0] == '.' and ":" not in line:
        className = line[1:-3]
        module_css_classes.append(className)


# In the .tsx file, add all "styles={className}" to a list between the "styles={" and "}" so just record "className"
tsx_css_classes = []
for line in f_tsx:
    if "className={styles." in line:
        # Get the exact position on the line of where "styles={" is located.
        stylesIndex = line.index("className={styles.")
        # Get the exact position immediately to the right of the brace, which is where the CSS class name is located.
        classNameIndex = stylesIndex + len("className={styles.")

        # Iterate until we encounter a closing brace, which is where the end of the class name is.
        index = classNameIndex
        currentCharacter = line[classNameIndex]
        while currentCharacter is not "}":
            index += 1
            currentCharacter = line[index]
        classNameIndexEnd = index

        className = line[classNameIndex: classNameIndexEnd]
        tsx_css_classes.append(className)


module_css_classes_set = set(module_css_classes)
# print(module_css_classes_set)

tsx_css_classes_set = set(tsx_css_classes)
# print(tsx_css_classes_set)


# Logic that separately checks which classNames or styles are not used in the .module.css and .tsx files respectively.
unused_module_css = []
for className in module_css_classes_set:
    if className not in tsx_css_classes_set:
        unused_module_css.append(className)

print("")
print("Unused .classes in .module.css")
print(unused_module_css)


unused_tsx_styles = []
for className in tsx_css_classes_set:
    if className not in module_css_classes_set:
        unused_tsx_styles.append(className)

print("")
print("Unused className={styles. } in .tsx")
print(unused_tsx_styles)
