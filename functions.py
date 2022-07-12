import re

# In addition to re.search(), the re module contains several other functions to help you perform regex-related tasks.
# The available regex functions in the Python re module fall into the following three categories:
#   1. Searching functions ->
#   2. Substitution functions -> re.sub() , re.subn()
#   3. Utility functions

# Utility
#
# re.split() -> Splits a string into substrings using a regex as a delimiter
# re.escape() -> Escapes characters in a regex
# Example: splits the specified string into substrings delimited by a comma (,), semicolon (;), or slash (/) character, surrounded by any amount of whitespace:
print(re.split(r"\s*[,;/]\s*", "foo,bar ; baz / qux"))
# If the <regex> contains capturing groups then the return list includes the mathching delimiter strings as well:
print(re.split(r"(\s*[\;,]\s*)", "foo,bar ; baz / qux"))


# Compiled Regex objects
# The re module supports the capability to precompile a regex in Python into a regular expression object that can be repeatedly used later.
# re.compile(<regex>, flags=0)
# Compiles a regex into a regular expression object.
# There are two ways to use a compiled regular expression object:
# 1. Specify it as the first argument to the re module functions in place of <regex>:
# re_obj = re.compile(<regex>, <flags>)
# result = re.search(re_obj, <string>)
# 2. Invoke a method directly from a regular expression object:
# re_obj = re.compile(<regex>, <flags>)
# result = re_obj.search(<string>)

re_obj = re.compile(r"\d+")
print(re.search(re_obj, "foo123bar"), re_obj.search("foo123bar"))
re_obj = re.compile(r"ba[rz]", flags=re.IGNORECASE)
print(re.search(re_obj, "FOOBARBAZ"), re_obj.search("FOOBAZBAR"))

# Why bother compiling a regex?
# If you use a particular regex in your Python code frequently, then precompiling allows you to separate out the regex definition from its uses.
# Enhancing modularity
s1, s2, s3, s4 = "foo.bar", "foo123bar", "baz99", "qux & grault"
re_obj = re.compile(r"\d+")
print(re_obj.search(s1), re_obj.search(s2), re_obj.search(s3), re_obj.search(s4))

