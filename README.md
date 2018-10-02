# DefeXts
##### (version October 1st, 2018)

## Overview
DefeXts is a collection of bug datasets containing real bugs from real-world projects focused on modern JVM languages. As of October 1st, 2018, DefeXts currently has two child datasets, one for Kotlin (called DefeKts) and one for Groovy (called DefeGts). DefeKts contains 271 Github-based buggy projects and their respective repair patches. DefeGts contains 321 Github-based buggy projects and their respective repair patches. We include an installation script so DefeXts users can download these datasets and use them in their software research. As its development continues, we intend for DeFeXts to include more JVM languages, notably Scala.

## DefeXts Usage

### Installation - Linux Users / MacOS Users
Linux users should download / clone this repository.

```bash
$ git clone https://github.com/ProdigyXable/defexts my-output-folder
```
### Installation - Window Users
...
### DefeXts Commands
Execute the installation bash script to download DefeXts' datasets locally to your environment. 

```bash
$ ./install
```
After download is complete, execute the "defexts" bash script contained within the '/bin' folder. Enable the 'h' switch to see a list of commands.

```bash
$ cd bin/
$ ./defexts -h
```
- Show the list of projects within a particular DefeXts child dataset
```bash
$ ./defexts (-k | -g | --kotlin | --groovy) (-a | --all-projects)
```
- Show the list of bugs within the Groovy dataset
```bash
$ ./defexts (-g | --groovy) (-l | --list-bugs)
```
- Checkout the buggy version (-b) of thrifty-4 from the Kotlin dataset into my current directory {(-o | --out-dir) .}
```bash
$ ./defexts (-k | --kotlin) -c thrifty-4 (-b | --buggy) (-o | --out-dir) .
```
- Checkout the fixed version (-f) of thrifty-4 from the Kotlin dataset into my current directory  {(-o | --out-dir) .}
```bash
$ ./defexts (-k | --kotlin) -c thrifty-4 (-f | --fixed) (-o | --out-dir) .
```
- View the the modified source file(s) (-s | --source) 'diff' between a project's buggy version and its fixed version
```bash
$ ./.defexts (-k | -g | --kotlin | --groovy) -d  <projectname-bugId> (-s | --source)
```
- View the the modified test file(s) (-t | --test) 'diff' between a project's buggy version and its fixed version
```bash
$ ./.defexts (-k | -g | --kotlin | --groovy) -d  <projectname-bugId> (-t | --test)
```

## Minimum System / Environment Requirements
- All projects are verified to work with
  - Maven (v. 3.3.9)
  - Gradle (v. 4.8)
  - JDK (v. 1.8)
  - Git (v. 2.7.4)
- Installation file requires Perl 5+
