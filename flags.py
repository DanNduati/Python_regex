import re

# Modified Regular expression matching with flags
#
# re.I
# re.IGNORECASE
# Makes matching case insensitive
print(re.search(r"a+", "aaaAAA"), re.search(r"a+", "aaaaAAA", re.IGNORECASE))
print(re.search(r"[a-z]+", "aBcDeF"), re.search(r"[a-z]+", "aBcDeF", re.IGNORECASE))
#
# re.M
# re.MULTILINE
s = "foo\nbar\nbaz"
print(re.search("^foo", s), re.search("^bar", s), re.search("^baz", s))
print(re.search(r"foo$", s), re.search(r"bar$", s), re.search(r"baz$", s))
# With the MULTILINE flag set the ^ and $ anchor metacharacters match internal lines as well
print(
    re.search("^foo", s, re.MULTILINE),
    re.search("^bar", s, re.MULTILINE),
    re.search("^baz", s, re.MULTILINE),
)
print(
    re.search("foo$", s, re.MULTILINE),
    re.search("bar$", s, re.MULTILINE),
    re.search("baz$", s, re.MULTILINE),
)
# The MULTILINE flag only modifies the ^ and $ anchors in this way. It doesn’t have any effect on the \A and \Z anchors
#
# re.S
# re.DOTALL
# Causes the dot(.) metacharacter to match a newline.
# By default the dot metacharacter match any character except the newline character. The DOTALL flag lifts this restriction
print(re.search(r"foo.bar", "foo\nbar"))
print(re.search(r"foo.bar", "foo\nbar", re.DOTALL))
#
# re.X
# re.VERBOSE
# Allows inclusion of whitespace unless its within a character class or escaped with a backlash and
# comments as long as its to the right of a # chracter and not contained within a character class within a regex
# Example : Parse Phone numbers with the format:
#    - Optional three digit area code in parentheses
#    - Optional whitespace
#    - Three-digit prefix
#    - Seperator (either - or .)
#    - Four digit line number

regex = r"^(\(\d{3}\))?\s?\d{3}[-.]\d{4}$"
print(re.search(regex, "414.9229"))
# More readable with the verbose flag
regex = r"""^               # Start of string
            (\(\d{3}\))?    # Optional area code
            \s?             # Optional whitespace
            \d{3}           # Three digit prefix
            [-.]            # Seperator character
            \d{4}           # Four digit line number
            $               # Anchor at the end of the string
            """
print(
    re.search(regex, "414.9229", re.VERBOSE),
    re.search(regex, "414-9229", re.VERBOSE),
    re.search(regex, "(712)414-9229", re.X),
    re.search(regex, "(712) 414-9229", re.X),
)

# Significant whitespace when using the VERBOSE flag
print(
    re.search(r"foo bar", "foo bar", re.VERBOSE),
    re.search(r"foo\ bar", "foo bar", re.VERBOSE),
)
#
# re.DEBUG
# Displays debugging information
# The DEBUG flag causes the regex parser in Python to display debugging information about the parsing process to the console
re.search(r"foo.bar", "foozbar", re.DEBUG)
# More complicated example
regex = r"^(\(\d{3}\))?\s?\d{3}[-.]\d{4}$"
print(re.search(regex, "414.9229", re.DEBUG))
#
# Combining <flags> Arguments in a regex function call
# Using the bitwise OR (|) operator.
print(re.search(r"^bar", "FOO\nBAR\nbaz", re.IGNORECASE | re.MULTILINE))
# Setting and Clearing Flags within a regular expression
# There are two regex metacharacter sequences that provide this capability.
# (?<flags>)
# Sets the flag value(s) for the duration of a regex
# Within a regex, the metacharacter sequence (?<flags>) sets the specified flags for the entire expression.
# The value of <flags> is one or more letters from the set a(re.ASCII), i(re.IGNORECASE), L(re.LOCALE), m(re.MULTILINE), s(re.DOTALL), u, and x(re.VERBOSE).
# The (?<flags>) metacharacter sequence as a whole matches the empty string. It always matches successfully and doesn’t consume any of the search string.
print(
    # Equivalent ways of setting the IGNORECASE and MULTILINE flags
    re.search(r"^bar", "FOO\nBAR\nbaz\n", re.IGNORECASE | re.MULTILINE),
    re.search(r"(?im)^bar", "FOO\nBAR\nbaz\n"),
)
# Note that a (?<flags>) metacharacter sequence sets the given flag(s) for the entire regex no matter where you place it in the expression:
print(
    re.search(r"foo.bar(?s).baz", "foo\nbar\nbaz"),
    re.search(r"foo.bar.baz(?s)", "foo\nbar\nbaz"),
)
# As of Python 3.7, it’s deprecated to specify (?<flags>) anywhere in a regex other than at the beginning
# It still produces the appropriate match, but you’ll get a warning message.
#
# (?<set_flags>-<remove_flags>:<regex>)
# Sets or removes flag value(s) for the duration of a group.
# This defines a non-capturing group that matches against <regex>. For the <regex> contained in the group,
# the regex parser sets any flags specified in <set_flags> and clears any flags specified in <remove_flags>.
# Values for <set_flags> and <remove_flags> are most commonly i, m, s or x.
# Example: set IGNORECASE for a specified group
print(re.search(r"(?i:foo)bar", "FOObar"), re.search("(?i:foo)bar", "FOOBAR"))
# Turn a flag off for a group
print(re.search(r"(?-i:foo)bar", "FOOBAR", re.IGNORECASE))
# Although re.IGNORECASE enables case-insensitive matching for the entire call, 
# the metacharacter sequence (?-i:foo) turns off IGNORECASE for the duration of that group, so the match against 'FOO' fails.
