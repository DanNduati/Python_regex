<h1 align="center"><b>Regex</b></h1>

## <b>Language analogy</b>
Full regular expressions are composed of two types of characters. The special characters (like *) are called `metacharacters`, while the rest are called `literal`, or normal text characters.
Consider regular expressions as their own language, with literal text acting as the words and metacharacters as the grammar. The words are combined with grammar according to a set of rules to create an expression that communicates an idea.

## <b>The re module</b>
Regex functionality in Python resides in a module named `re`.

### <b>re.search([regex],[string])</b>
re.search([regex], [string]) scans [string] looking for the first location where the pattern [regex] matches. If a match is found, then re.search() returns a `match object`. Otherwise, it returns `None`.

### <b>Metacharacters supported by the re module</b>

| <b>Character</b> 	| <b>Meaning</b>                                                                                                                                                        	|
|------------------	|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------	|
| .                	| Matches any single character except newline                                                                                                                           	|
| ^                	| ∙ Anchors a match at the start of a string<br>∙ Complements a character class                                                                                         	|
| $                	| Anchors a match at the end of a string                                                                                                                                	|
| *                	| Matches zero or more repetitions                                                                                                                                      	|
| +                	| Matches one or more repetitions                                                                                                                                       	|
| ?                	| ∙ Matches zero or one repetition<br>∙ Specifies the non-greedy versions of *, +, and ?<br>∙ Introduces a lookahead or lookbehind assertion<br>∙ Creates a named group 	|
| {}               	| Matches an explicitly specified number of repetitions                                                                                                                 	|
| \                	| ∙ Escapes a metacharacter of its special meaning<br>∙ Introduces a special character class<br>∙ Introduces a grouping backreference                                   	|
| []               	| Specifies a character class                                                                                                                                           	|
| \|               	| Designates alternation                                                                                                                                                	|
| ()               	| Creates a group                                                                                                                                                       	|
| :<br>#<br>=<br>! 	| Designate a specialized group                                                                                                                                         	|
| <>               	| Creates a named group                                                                                                                                                 	|


The regex parser regards any character not listed above as an ordinary character that matches only itself.


