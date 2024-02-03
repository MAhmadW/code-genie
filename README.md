# code-genie
A ChatGPT wrapper that helps create code solutions for leetcode questions instantly.

The following languages are supported:

- Python
- JavaScript
- Java
- C
- C++
- C#
- Ruby
- PHP
- Swift
- Objective-C
- R
- Go
- Rust
- Kotlin
- Scala
- Perl
- Lua
- Haskell
- Elixir
- Erlang
- TypeScript
- Shell (Bash, Zsh, etc.)
- Dart
- Groovy
- Pascal
- Fortran
- Assembly
- Visual Basic
- MATLAB
- Julia
- Clojure
- F#

## Usage

Rename example.env.py to env.py. Add your OpenAI api key in the OPENAI_API_KEY variable. You may change the default of the solutions directory (./solutions) as needed.

To see the supported languages, type into the command line:
`python genie.py languages`


To generate scripts, simply use
`python genie.py <question_file> <language_name>`

Put your question in a file of your choosing, e.g. question.txt in the root directory.

if I want the code script to be python, 
`python genie.py question.txt python`
