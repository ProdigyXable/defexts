# Defexts
##### (version January 31st, 2019)

## Overview
DefeXts is a collection of bug datasets containing real bugs from real-world projects focused on modern JVM languages.DefeXts currently has two child datasets, one for Kotlin (called DefextsKotlin) and one for Groovy (called DefextsGroovy).
DefextsKotlin contains 225 bugs and patches from real-world Github projects.
DefextsGroovy contains 302 bugs and patches from real-world Github projects.
We include an installation script so Defexts users can download these datasets and use them in their software research. 
As its development continues, we intend for DeFexts to include more JVM languages, notably Scala.

## Installing / Downloading Defexts

Defexts users should download / clone this repository.

```bash
$ git clone https://github.com/defexts/defexts my-output-folder
```
### Linux Users / MacOS Users
Execute the installation bash script to download Defexts' datasets locally to your environment. 

```bash
$ ./install
```
<!--- ### Window Users
Window users should download / clone this repository. -->
## Defexts Usage

After download is complete, execute the "defexts" bash script contained within the '/bin' folder. Enable the 'h' switch to see a list of commands.

```bash
$ cd bin/
$ ./defexts -h
```
- Show the list of projects within a particular Defexts child dataset
```bash
$ ./defexts (-k | -g | --kotlin | --groovy) (-a | --all-projects)
```
- Show the list of bugs within the Kotlin dataset
```bash
$ ./defexts (-k | --kotlin) (-l | --list-bugs)
```
- Show the list of bugs within the Groovy dataset
```bash
$ ./defexts (-g | --groovy) (-l | --list-bugs)
```
- Checkout the buggy version (-b) of kog-1 from the Kotlin dataset into my current directory {(-o | --out-dir) .}
```bash
$ ./defexts (-k | --kotlin) -c kog-1 (-b | --buggy) (-o | --out-dir) .
```
- Checkout the fixed version (-f) of gradle-1 from the Kotlin dataset into my current directory {(-o | --out-dir) .}
```bash
$ ./defexts (-k | --kotlin) -c gradle-1 (-f | --fixed) (-o | --out-dir) .
```
- View the the modified source file(s) (-s | --source) 'diff' between a project's buggy version and its fixed version
```bash
$ ./defexts (-k | -g | --kotlin | --groovy) -d <projectname-bugId> (-s | --source)
```
- View the the modified test file(s) (-t | --test) 'diff' between a project's buggy version and its fixed version
```bash
$ ./defexts (-k | -g | --kotlin | --groovy) -d  <projectname-bugId> (-t | --test)
```

Further Sample Usage of DefeXts can be viewed here:

## Minimum System / Environment Requirements
- All projects are verified to work with
  - Maven (v. 3.3.9)
  - Gradle (v. 4.8)
  - JDK (v. 1.8)
  - Git (v. 2.7.4)
- Installation file requires Perl 5+
