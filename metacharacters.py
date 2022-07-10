#!/usr/bin/env python
"""Regexes in python"""
import re

# Basic string manipulation
s = "foo123bar"

# Matching is pretty straight forward in the above
print(f"{'123' in s}")
print(s.find("123"))
print(s.index("123"))

match = re.search("123", s)
print(match)

# Python Regex Metacharacters
# Problem: Determine whether a string contains any 3 consecutive decimal digital characters
s1 = "foo456bar"
match = re.search("[0-9][0-9][0-9]", s1)
print(match)

# Metacharacters supported by the re module
# Metacharacters that match a single character
# Characters contained in square brackets ([]) represent a character class
# An enumerated set of characters to match from. A character class metacharacter sequence will match any single character contained in the class.
print(f"{re.search('ba[artz]','foobarqux')}")
print(f"{re.search('ba[artz]','foobazqux')}")
# character class with a range of characters
# Example: [a-z] matches any lowercase alphabetic character between 'a' and 'z', inclusive.
print(f"{re.search('[a-z]','FOObar')}")
# [0-9] matches any digit character:
print(f"{re.search('[0-9][0-9]','foo123bar')}")

# Match any hexadecimal number
print(f"{re.search('[0-9a-fA-f]','0x3H')}")

# In the above examples, the return value is always the leftmost possible match.
# re.search() scans the search string from left to right, and as soon as it locates a match for <regex>, it stops scanning and returns the match.


# complementing a character class
print(re.search("[^0-9]", "12345foo"))
# if the ^ character appears in a character class but not as the first character in the string then it has no special meaning and matches a literal `^` character
print(re.search("[#:^]", "foo^bar:baz#qux"))
# Hyphen as a literal in a character class
# You can place it as the first or last character or escape it with a backslash (\)
print(
    re.search("[-abc]", "123-456"),
    re.search("[abc-]", "123-456"),
    re.search("[ab\-c]", "123-456"),
)
# Likewise to use `]` as a literal in a character class place it as the first character or escape it with backslash:
print(re.search("[]]", "foo[1]"), re.search("[ab\]cd]", "foo[0]"))

# Other regex metacharacters lose their special meaning inside a character class:
print(re.search("[)*+|]", "123*456"), re.search("[)*+|]", "123+456"))

# The dot(.) metacharacter
# The . metacharacter matches any single character except a newline:
print(re.search("foo.bar", "foozbar"), re.search("foo.bar", "foo\nbar"))

# Special character classes
# \w and \W
# \w matches any alphanumeric word characters ie:
# uppercase and lowercase letters, digits, and the underscore (_) character
# so \w is essentially shorthand for [a-zA-Z0-9_]:
print(re.search("\w", "@#$2a&"))

# \W matches any non-word character and is equivalent to [^a-zA-Z0-9_]:
print(re.search("\W", "213das#"))


# \d and \D
# \d matches any decimal digit character.
print(re.search("\d", "fdsfgdsd4"))
# \D matches any character that is not a decimal digit
print(re.search("\D", "324234D43"))

# \s and \S
#  \s and \S consider a newline to be whitespace
# \s matches any whitespace character
print(re.search("\s", "hello regex"))
# \S matches any character that isn’t whitespace
print(re.search("\S", "\n\n\n hello regex\n"))

# The character class sequences \w, \W, \d, \D, \s, and \S
# can appear inside a square bracket character class as well:
print(
    re.search(
        "[\d\w\s]", "---3---"
    ),  # matches any digit, word, or whitespace character.
    re.search("[\d\w\s]", "---a---"),
    re.search("[\d\w\s]", "--- ---"),
)

# Escaping Metacharacters
# The backslash (\):
# 1. Introduce special character classes as seen above
# 2. Some special metacharacter sequences called anchors that begin with a backslash <to be seen later>
# When it’s not serving either of these purposes, the backslash escapes metacharacters.
print(re.search(".", "foo.bar"), re.search("\.", "foo.bar"))

# Interesting backslash escaping backslash problem:
# Suppose you have a string that contains a single backslash:
s = r"foo\bar"
print(s)
# print(re.search("\\",s)) # This fails because the backslash escaping happens twice, first by the Python interpreter on the string literal and then again by the regex parser on the regex it receives.
# Solutions:
# 1. Escape both backslashes in the original string(messy)
print(re.search("\\\\", s))
# 2. Using a raw string:
print(re.search(r"\\", s))
# It’s good practice to use a raw string to specify a regex in Python whenever it contains backslashes.

# Anchors
# Anchors are zero-width matches.
# They dont match any actual characters in the search string, and they dont consume any of the search string during parsing
# An anchor dictates a particular location in the search string where a match must occur.

# ^
# \A
# When the regex parser encounters ^ or \A, the parser’s current position must be at the beginning of the search string for it to find a match.
# In other words, regex ^foo stipulates that 'foo' must be present not just any old place in the search string, but at the beginning:

print(re.search("^foo", "foobar"), re.search("^bar", "foobar"))

# \A functions similarly
print(re.search("\Afoo", "foobar"))
# ^ and \A behave slightly differently from each other in MULTILINE mode.

# $
# \Z
# Anchor a match to the end of <string>.
print(re.search("bar$", "foobar"), re.search("bar\Z", "foobar"))
# As a special case, $ (but not \Z) also matches just before a single newline at the end of the search string:
print(re.search("bar$", "foobar\n"))
# $ and \Z behave slightly differently from each other in MULTILINE mode.

# \b
# Anchors a match to a word boundary
# \b asserts that the regex parser’s current position must be at the beginning or end of a word.
print(re.search(r"\bbar", "foo bar"), re.search(r"\bbar", "foobar"))
# Using the \b anchor on both ends of the <regex> will cause it to match when it’s present in the search string as a whole word:
print(re.search(r"\bfoo\b", "bar foo bar"))

# \B
# Anchors a match to a location that isn’t a word boundary.
# Asserts that the regex parser's current position must not be at the start or end of a word
print(re.search(r"\Bbar\B", "foobarbaz"), re.search(r"\Bfoo\B", ".foo."))

# Quantifiers
# A quantifier metacharacter immediately follows a portion of a <regex> and indicates how many times that portion must occur for the match to succeed

# The asterisk (*)
# Matches zero or more repetitions of the preceding regex
print(
    # Zero dashes
    re.search(r"foo-*bar", "foobar"),
    # One dash
    re.search(r"foo-*bar", "foo-bar"),
    # Two dashes
    re.search(r"foo-*bar", "foo--bar"),
)

print(re.search(r"foo.*bar", "foo fwhf47$53&262 bar jkds"))

# The Plus (+)
# Matches one or more repetitions of the preceding regex.
# This is similar to * but the quantified regex must occur atleast once:
print(
    # Zero dashes
    re.search(r"foo-+bar", "foobar"),
    # One dash
    re.search(r"foo-+bar", "foo-bar"),
    # Two dashes
    re.search(r"foo-+bar", "foo--bar"),
)

# ?
# Matches zero or one repetitions of the preceding regex
print(
    # Zero dashes
    re.search(r"foo-?bar", "foobar"),
    # One dash
    re.search(r"foo-?bar", "foo-bar"),
    # Two dashes
    re.search(r"foo-?bar", "foo--bar"),
)

# More examples of using all 3 quantifier metacharacters
print(
    re.search(r"foo[1-9]*bar", "foobar foo12bar foo54bar"),
    re.match(r"foo[1-9]*bar", "foo69bar"),
    re.match(r"foo[1-9]+bar", "foobar"),
    re.match(r"foo[0-9]+bar", "foo420bar"),
    re.match(r"foo[1-9]?bar", "foo1bar"),
)

# *?
# +?
# ??
# The non greedy(or lazy) versions of the *,+ and ? quantifiers
# When used alone  the quantifier metacharacters *, +, and ? are all greedy, meaning they produce the longest possible match.
# Example: Lazy version of *
# Greedy metacharacter sequence
print(re.search(r"<.*>", "%<foo> <bar> <baz>%"))
# Non-greedy metacharacter sequence -> Returns the shortest possible match
print(re.search(r"<.*?>", "%<foo> <bar> <baz>%"))

# Lazy versions of + and ? quantifiers
print(re.search(r"<.+>", "<foo> <bar> <baz>"))
print(re.search(r"<.+?>", "<foo> <bar> <baz>"))

print(re.search(r"ba?", "baa"))
print(re.search(r"ba??", "baaaa"))


# {m}
# Matches exactly m repetitions of the preceding regex
# Similar to * or +, but it specifies exactly how many times the preceding regex must occur for a match to succeed

print(re.search(r"x-{3}x", "x--x"), re.search(r"x-{3}x", "x---x"))

# {m,n}
# Matches any number of repetitions of the preceeding regex form m to n inclusive.
for i in range(1, 6):
    s = f"x{'-'*i}x"
    print(re.search(r"x-{1,4}x", s))

# Omitting m implies a lower bound of 0, and omitting n implies an unlimited upper bound
# If you omit all of m, n, and the comma, then the curly braces no longer function as metacharacters. {} matches just the literal string '{}'

# Non-greedy (lazy) version of {m,n}
# {m,n} will match as many characters as possible, and {m,n}? will match as few as possible

print(
    re.search(r"a{3,5}", "aaaaaaaa"),
    re.search(r"a{3,5}?", "aaaaaaaa"),
)


# Grouping Constructs and Backreferences
# Grouping constructs break up a regex in Python into subexpressions or groups.
# This serves 2 purposes:
#   1. Grouping -> A group represents a single syntactic entity. Additional metacharacters apply to the entire group as a unit.
#   2. Capturing ->  Some grouping constructs also capture the portion of the search string that matches the subexpression in the group. You can retrieve captured matches later through several different mechanisms.
# (<regex>)
# Defines a subexpression or group
# This is the most basic grouping construct this just matches the contents of the parentheses
print(re.search(r"(bar)", "foo bar baz"))
# This is the same as the regex bar would without the parentheses


# Treating a group as a unit
# A quantifier metacharacter that follows a group operates on the entire subexpression specified in the group as a single unit.
print(re.search(r"(bar)+", "foo bar baz"))
print(re.search(r"(bar)+", "foo barbarbar baz"))
# More complicated examples
print(
    re.search(r"(ba[rz]){2,4}(quz)?", "barbarzquz"),
    re.search(r"(ba[rz]){2,4}(quz)?", "barbaz"),
)

# Nest grouping parentheses
print(
    re.search(r"(foo(bar)?)+(\d\d\d)?", "foofoobar"),
    re.search(r"(foo(bar)?)+(\d\d\d)?", "foofoobar123"),
    re.search(r"(foo(bar)?)+(\d\d\d)?", "foofoo420"),
)

# Capturing groups
m = re.search(r"(\w+),(\w+),(\w+)", "foo,bar,baz")
print(m)
# Access the captured matches
print(m.groups())
# Access the nth captured match
print(m.group(1))
print(m.group(1, 2, 3))

# Backreferences
# You can match a previously captured group later within the same regex using a special metacharacter sequence called a backreference.
#
# \<n>
# Matches the contents of a previously captured group.
# Within a regex in python the sequence \<n> where <n> is an integer from 1 to 99, matches the contents of the <n>th captured group.

regex = r"(\w+),\1"
m = re.search(regex, "foo,foo")
print(m, m.group(1))


m = re.search(regex, "quz,quz")
print(m, m.group(1))

m = re.search(regex, "foo,quz")
print(m)

# Other Grouping Constructs
# (?P<name><regex>)
# Creates a named captured group

# basic grouping
m = re.search(r"(\w+),(\w+),(\w+)", "foo,bar,baz")
print(m)
print(m.group(1, 2, 3))
# Give the groups symbolic name
m = re.search(r"(?P<w1>\w+),(?P<w2>\w+),(?P<w3>\w+)", "foo,bar,baz")
print(m.groups())
print(m.group("w1"))

# Backreference a captured named group
m = re.search(r"(?P<word>\w+),(?P=word)", "foo,foo")
print(m)
m = re.search(r"(?P<num>\d+)\.(?P=num)", "69.69")
print(m)

m = re.search(r"(\w+),(?:\w+),(\w+)", "foo,bar,baz")
print(m.groups())
# (?(<n>)<yes-regex>|<no-regex>) -> Matches against <yes-regex> if a group numbered <n> exists. Otherwise, it matches against <no-regex>.
# (?(<name>)<yes-regex>|<no-regex>) -> Matches againsta <yes-regex> if a group named <name> exists. Otherwise, it matches against <no-regex>.
# Example:
regex = r"^(###)?foo(?(1)bar|baz)"
# Explanation:
# 1. ^(###)? -> Indicates that the search string optionally starts with '###' if it does this creates a group numbered 1
# 2. The group is followed by the literal 'foo'
# 3. (?(1)bar|baz) -> if the numbered group 1 exists matches against 'bar' and 'baz' if it doesnt.

print(
    re.search(regex, "###foobar"),
    re.search(regex, "###foobaz"),
    re.search(regex, "foobaz"),
)

regex = r"^(?P<ch>\W)?foo(?(ch)(?P=ch)|)$"
print(re.search(regex, "foo"), re.search(regex, "@foo@"), re.search(regex, "#foo@"))

# Lookahead and Lookbehind Assertions
# Determine the success or failure of a regex match based on whats just behind(to the left) or ahead(to the right) of the parser's current position in the search string
# Like anchors, Lookahead and lookbehind assertions are zero-width assertions, so they dont consume any of the search string.
# Also even though they contain parentheses and perform grouping they do not capture what they match
#
# (?=<lookahead-regex>)
# Creates a positive lookahead assertion.
print(re.search(r"foo(?=[a-z])", "foobar"), re.search(r"foo(?=[a-z])", "foo123"))
# What’s unique about a lookahead is that the portion of the search string that matches <lookahead_regex> isn’t consumed, and it isn’t part of the returned match object.
m = re.search(r"foo(?=[a-z])(?P<ch>.)", "foobar")
print(m)
print(m.group("ch"))
m = re.search(r"foo([a-z])(?P<ch>.)", "foobar")
print(m)
print(m.group("ch"))
#
# (?!<lookahead_regex>)
# Creates a negative lookahead assertion
# This asserts that what follows the regex parser's current position must not match <lookahead_regex>.
print(re.search(r"foo(?![a-z])", "foobar"), re.search(r"foo(?![a-z])", "foo123"))
#
# (?<=<lookbehind_regex>)
# Creates a positive look behind assertion
# This asserts that what precedes the regex parser's current position must match <lookbehind_regex>.
print(re.search(r"(?<=foo)bar", "foobar"), re.search(r"(?<=foo)bar", "barfoo"))
# Restriction with <lookbehind_regex> : in a lookbehind assertion the <lookbehind_regex> must specify a match of fixed length
# That is a regex such as r"(?<=a+)" is not valid because the string matched by a+ is indeterminate.
# An okay example:
print(re.search(r"(?<=a{3})foo", "aaafoo"))
#
# (?<!<lookbehind_regex>)
# Creates a negative lookbehind assertion
# This asserts that what precedes the regex parser’s current position must not match <lookbehind_regex>
print(re.search(r"(?<!foo)bar", "foobar"), re.search(r"(?<!foo)bar", "zoobar"))

# Miscellaneous Metacharacters
# These are stray metacharacters that don’t obviously fall into any of the categories already discussed.
#
# (?#...)
# Specifies a comment
print(re.search(r"bar(?#This is a comment) * baz", "foo bar baz"))
#
# Vertical bar, or pipe (|)
# Specifies a set of alernatives on which to match
# An expression of the form <regex_1>|<regex_2>|...|<regex_n> matches at most one of the specified <regex_i> expressions:
print(
    re.search(r"foo|bar|baz", "bar"),
    re.search(r"foo|bar|baz", "baz"),
    re.search(r"foo|bar|baz", "quz"),
)
# Alternation is non-greedy. The regex parser looks at the expressions separated by | in left-to-right order and returns the first match that it finds.
# The remaining expressions aren’t tested, even if one of them would produce a longer match:
print(re.search(r"foo|graull", "foograull"))

# You can combine alternation, grouping, and any other metacharacters to achieve whatever level of complexity you need.
print(
    re.search(r"(foo|bar|baz)+", "foofoofoo"),
    re.search(r"(foo|bar|baz)+", "barfoobarbaz"),
)

print(re.search(r"([0-9]+|[a-f]+)", "45"), re.search(r"([0-9]+|[a-f]+)", "dada"))
