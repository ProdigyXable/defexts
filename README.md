###### (v. June 8th, 2019)

# Defexts

## Overview

Defexts is a collection of bug datasets containing real bugs from real-world projects, focused towards modern JVM languages.
Defexts currently has two child datasets, one for Kotlin (**called DefextsKotlin**), one for Groovy (**called DefextsGroovy**), and one for Scala (**called DefextsScala**).

* DefextsKotlin contains **225** bugs and patches from *152* real-world Github projects.
* DefextsGroovy contains **301** bugs and patches from *170* real-world Github projects.
* DefextsScala contains **128** bugs and patches from *91* real-world Github projects.

We include an installation script so Defexts users can easily download these datasets and use them in their software research.
As Defexts' development continues, we intend to include more JVM languages and expand the variety of included bugs.

## Installing / Downloading Defexts

Users should clone this repository and then execute the install script (**install** via Bash). This will download the dataset to your local machine. This dataset can be further accessed by Defexts' interface file (**defexts.py** via Python) or by manually extracting the compressed folder files within a **dataset-\*** folder.

### Linux Users / MacOS Users

Execute the installation bash script to download Defexts' datasets to your local machine. The datasets will be downloaded to the install script's current directory.

`$ ./install`

### Window Users

Defexts' install and interface scripts are currently compatible only with Linux-based systems.

## Defexts Usage

After download is complete, execute the "defexts.py" script.
This script needs Python 2 or Python 3 to be installed on the local machine.
Python dependencies will be automatically downloaded by the install script.
The interface should be executed in the same path as the **dataset-\*** folders created by the install file.
If the interface is executed from another directory, use the "-p | --path" option to specify the directory containing the **dataset-\*** folders

The following commands are possible within Defexts.

* Show interface help
  * `$ python3 defexts.py (-h | --help)`
* List every bug within a particular Defexts child dataset alongside supplemental information including bugId, patch url, and underlying build system.
  * `$ python3 defexts.py <language> (-a | --all-projects)`
* List every unique project and the number of bugs associated to each project within the Kotlin dataset
  * `$ python3 defexts.py kotlin (-l | --list-bugs)`
* Show the list of bugs within the Groovy dataset
  * `$ python3 defexts.py groovy (-l | --list-bugs)`
* Checkout the buggy version (-b | --buggy) of kog-1 from the Kotlin dataset. This command extracts the project into the current working directory.
  * `$ python3 defexts.py kotlin (-c | --checkout) kog-1 (-b | --buggy)`
* Checkout the fixed version (-f | --fixed) of thrifty-2 from the Kotlin dataset. This command extracts the project into the current working directory.
  * `$ python3 defexts.py kotlin (-c | --checkout) thrifty-2 (-f | --fixed)`
* View the diff of any modified source file(s) (-s | --source) between a bug and its fix.
  * `$ python3 defexts.py <language> (-d | --diff) <bugId> (-s | --source)`
* View the diff of any modified test file(s) (-t | --test) between a bug and its fix.
  * `$ python3 defexts.py <language> (-d | --diff) <bugId> (-t | --test)`

The above examples are executed via Python 3. If you are executing with Python 2, replace all instances of `python3` with `python`.
Further sample usage of Defexts can be viewed here: <https://youtu.be/lenYcVzRGGQ>

## Minimum System / Environment Requirements

* All projects are verified to be crash-reproducible with
  * Maven 3.3.9 / Gradle 4.8
  * Java Development Kit (JDK) 1.8
  * Git 2.7.4
* Installation file requires Perl 5
* Interface file requires Python 2 or Python 3

# Publication(s)
You may read / review the following resources to directly learn more about Defexts.

*International Conference of Software Engineering - 2019*
```
@inproceedings{Benton:2019:DCD:3339663.3339689,
 author = {Benton, Samuel and Ghanbari, Ali and Zhang, Lingming},
 title = {Defexts: A Curated Dataset of Reproducible Real-world Bugs for Modern JVM Languages},
 booktitle = {Proceedings of the 41st International Conference on Software Engineering: Companion Proceedings},
 series = {ICSE '19},
 year = {2019},
 location = {Montreal, Quebec, Canada},
 pages = {47--50},
 numpages = {4},
 url = {https://doi.org/10.1109/ICSE-Companion.2019.00035},
 doi = {10.1109/ICSE-Companion.2019.00035},
 acmid = {3339689},
 publisher = {IEEE Press},
 address = {Piscataway, NJ, USA},
} 
```
