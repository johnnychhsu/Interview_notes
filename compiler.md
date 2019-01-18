## Compiler
Translate a language into another language. For example, translate C++ to assembly code.

1. Preprocessor
2. Interpreter <br />
    Difference between compiler and interpreter : Compiler take whole code at once, then translate it to intermediate code. While interpreter take statements from source code, translate it, execute and then read next statement.
3. Assembler
4. Linker
5. Loader

### Analysis and Synthesis
![compiler stage](./compiler_stages.jpg) <br />

In analysis stage, compiler would check syntax, grammer of the source code, then generate intermediate code for synthsis stage.

### Phases of compiler
![Compiler Phases](./compiler_phases.jpg) <br />
**Lexical Analysis** <br />
Take source code as input stream of characters, then converts it into meaningful lexems. Then represent these lexemes as token `<token name, attribute value>`. <br />
**Syntax Analysis** <br />
It takes the tokens and generate a parse tree (syntax tree). Tokens arrangement are checked here whether it is syntactically correct. <br />
**Semantic Analysis** <br />
It checks whether the parse tree contructed follows the rule of language. For example, assignment of values is between compatible data types, or adding string to integer. <br />

### Finite Automata 
Can be used to verify the validity of a regular expression. When a regular expression string is fed into finite automata, it changes its state for each literal. If the input string is successfully processed and the automata reaches its final state, it is accepted, i.e., the string just fed was said to be a valid token of the language in hand.



### Reference
[Tutorials Points : Compiler](https://www.tutorialspoint.com/compiler_design/index.htm)
