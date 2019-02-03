# Defexts
##### (version January 31st, 2019)

## Overview
Defexts is a collection of bug datasets containing real bugs from real-world projects focused on modern JVM languages.
Defexts currently has two child datasets, one for Kotlin (**called DefextsKotlin**) and one for Groovy (**called DefextsGroovy**).
DefextsKotlin contains 225 bugs and patches from real-world Github projects.
DefextsGroovy contains 302 bugs and patches from real-world Github projects.
We include an installation script so Defexts users can download these datasets and use them in their software research. 
As its development continues, we intend for DeFexts to include more JVM languages, notably Scala.

## Installing / Downloading Defexts

Defexts users should download the install script (install) and interface file (defexts.py) from this repository.

### Linux Users / MacOS Users
Execute the installation bash script to download Defexts' datasets to your local machine. The datasets will be downloaded to the directory of the install script

```bash
$ ./install
```

### Window Users
Defexts' install and iniiterface scripts are currently compatible only with Linux-based systems.

## Defexts Usage

After download is complete, execute the "defexts.py" script. This script needs Python 2 or Python 3 to be installed on the local machine. Include the 'h' switch to see a list of commands.

```bash
$ python3 defexts.py -h
```
- Show the list of projects within a particular Defexts child dataset
```bash
$ python3 defexts.py (kotlin | groovy) (-a | --all-projects)
```
- List every unique project and the number of bugs associatead to eahc project within the Kotlin dataset
```bash
$ python3 defexts.py kotlin (-l | --list-bugs)
```
- Show the list of bugs within the Groovy dataset
```bash
$ python3 defexts.py groovy (-l | --list-bugs)
```
- Checkout the buggy version (-b) of kog-1 from the Kotlin dataset. This command extracts the project into the current working directory.

```bash
$ python3 defexts.py kotlin -c kog-1 (-b | --buggy)
```
- Checkout the fixed version (-f) of thrifty-2 from the Kotlin dataset. This command extracts the project into the current working directory.
```bash
$ python3 defexts.py kotlin -c thrifty-2 (-f | --fixed)
```
- View the diff of any modified source file(s) (-s | --source) 'diff' between a bug and its fix.
```bash
$ python3 defexts.py (kotlin | groovy) -d <projectname-bugId> (-s | --source)
```
- View the diff of any modified test file(s) (-t | --test) 'diff' between a bug and its fix.
```bash
$ python3 defexts.py (kotlin | groovy) -d <projectname-bugId> (-t | --test)
```

Further sample usage of Defexts can be viewed here: https://youtu.be/lenYcVzRGGQ

## Minimum System / Environment Requirements
- All projects are verified to work with
  - Maven 3.3.9
  - Gradle 4.8
  - JDK 1.8
  - Git 2.7.4
- Installation file requires Perl 5+
- Interface file requires Python 2+ or Python 3+
