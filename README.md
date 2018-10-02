# DefeXts (version October 1st, 2018)

## Overview
DefeXts is a collection of bug datasets containing real bugs from real-world projects focused on modern JVM languages. As of October 1st, 2018, DefeXts currently has two child datasets, one for Kotlin (called DefeKts) and one for Groovy (called DefeGts). DefeKts contains 271 Github-based buggy projects and their respective repair patches. DefeGts contains 321 Github-based buggy projects and their respective repair patches. We include an installation script so DefeXts users can download these datasets and use them in their software research. As its development continues, we intend for DeFeXts to include more JVM languages, notably Scala.

## Installation

### Linux Users / MacOS Users
Linux users should download / clone this repository. Execute the installation bash script to download DefeXts' datasets locally to your environment. After download is complete, execute the "defexts" bash script contained within the '/bin' folder to

- Show the list of projects within a particular DefeXts child dataset
- Checkout an entry's buggy version
- Checkout an entry's fixed version
- View the diff between an entry's buggy version and fixed version

<!--- ### Window Users -->
<!--- window user process here -->

## Minimum System / Environment Requirements

- All projects are verified to work with
  - Maven (version 3.3.9)
  - Gradle (4.8)
- JDK 1.8+
- Installation file requires Perl 5+
- git
