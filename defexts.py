import argparse
import os
import csv
import subprocess
from prettytable import PrettyTable

def printProjectInfo(dict):
    table = PrettyTable(["BugID", "Commit URL"])
    
    table.align["BugID"] = 'r'
    table.align["Commit URL"] = 'l'
    
    for key in sorted(dict.keys()):
        row = dict[key]
        table.add_row([key, row["commit_url"]])
    
    print(table)
    
def printPrintBugs(new_dict, dict):
    columnProjectName = "Project Name"
    columnNumberBugs = "# of Bugs"
    columnProjectURL = "Project URL"
        
    table = PrettyTable([columnProjectName, columnNumberBugs, columnProjectURL])
    
    table.align[columnProjectName] = 'l'
    table.align[columnNumberBugs] = 'c'
    table.align[columnProjectURL] = 'r'

    temp_dict = {}

    for key in dict.keys():
        row = dict[key]
        if(row["url"] in new_dict.keys()):
            new_dict[row["url"]] = new_dict[row["url"]] + 1
        else:
            new_dict[row["url"]] = 1
            temp_dict[row["url"]] = row["project"]

    for key, value in sorted(new_dict.items()):
        table.add_row([temp_dict[key], value, key])
    
    table.sortby = "Project Name"
    print(table)

def printTableStatistics(new_dict, dict):

    table = PrettyTable(["Projects","#"])
    table.add_row(["Distinct Bugs / Patches", len(new_dict.keys())])
    table.add_row(["Total Bugs / Patches", len(dict.keys())])
    
    print(table)

def setupParser():

    parser = argparse.ArgumentParser(description="Python interface to Defexts. Defexts is a family of bug datasets (currently Kotlin, Groovy, and Scala) for use in software engineering research.")
    parser.add_argument("language", action="store", help="Specifies which dataset to act on. Acceptable values: kotlin, groovy, scala", type=str.lower)
    
    # Project information / statistics options ---------------------------------------- #
    parser.add_argument("-a", "--all-projects", help="Display brief project information for each project", default=False, action="store_true")
    parser.add_argument("-l", "--list-bugs", help="List all bugs + bugIDs in the specified dataset", default=False, action="store_true")
    
    # ---------------------------------------- #
    parser.add_argument("-c", "--checkout", metavar="bugID", help="Checkouts a given project based on its bugID",default=False, action="store")
    parser.add_argument("-d", "--diff", metavar="bugID", help="Performs a bug -> patch diff on a given project based on its bugID", default=False, action="store")
    
    # Bug / patch options ---------------------------------------- #
    parser.add_argument("-b", "--buggy", help="Specifies the buggy version for the --checkout command", default=False, action="store_true")
    parser.add_argument("-f", "--fixed", help="Specifies the fixed version for the --checkout command", default=False, action="store_true")
    
    # Source / test options ---------------------------------------- #
    parser.add_argument("-s", "--source", help="Specifies the source file(s) for the --diff command", default=False, action="store_true")
    parser.add_argument("-t", "--test", help="Specifies the test file(s) for the --diff command", default=False, action="store_true")
    
    # ---------------------------------------- #
    parser.add_argument("-p", "--path", help="Specifies the folder containing the dataset-<language> folder. Use if you wish to execute this script from another directory. ", default="./", action="store")
    
    result = parser.parse_args()
    if(not result.path.endswith("/")):
        result.path = result.path + "/"

    return result
    
def command_all_projects(r, dict):
    if(r.source or r.test or r.buggy or r.fixed):
        print("Extra options specified - these options (\"-s\", \"-t\", \"-b\" or \"-f\") will be ignored")

    print(" ".join(["Printing details for all", r.language, "projects:"])) 
    printProjectInfo(dict)
    print("Further project information can be found in " + r.path  + "dataset-<language>/references.csv")

def command_list_bugs(r, dict):
    if(r.source or r.test or r.buggy or r.fixed):
        print("Extra options specified - these options (\"-s\", \"-t\", \"-b\", or \"-f\") will be ignored")
    
    print(" ".join(["Printing bugs per project + other project statistics", r.language, "projects"]))

    new_dict = {}
    
    printPrintBugs(new_dict, dict)
    printTableStatistics(new_dict, dict)

def command_checkout(r, dict, path):
    if(not r.buggy and not r.fixed):
        print("Missing checkout options - specify exactly one option \"-b\" OR \"-f\"")
        exit(-5)
    
    elif(r.buggy and r.fixed):
        print("Too many checkout options - specify only one option: \"-b\" OR \"-f\"")
        exit(-6)
    
    elif(r.source or r.test):
        print("Extra options specified - these options (\"-s\" or \"-t\") will be ignored")
        
    if(not r.checkout in dict):
        print(r.checkout + " does not exist in the dataset! Use \"-a\" option to find valid bugIDs")
        exit(-7)

    else:
        print(" ".join(["Checking out project", r.checkout]))
        
        unzip_command = " ".join(["tar -xzf", r.path + path + "/repos/" + dict[r.checkout]["project"] + ".tar.gz"])
        subprocess.call(unzip_command, shell=True)

        if(r.buggy):
            checkout_command = " ".join(["git checkout -f", dict[r.checkout]["hash"] + "-b"])
        elif(r.fixed):
            checkout_command = " ".join(["git checkout -f", dict[r.checkout]["hash"] + "-f"])
        else:
            raise Exception("Missing checkout option!")

        subprocess.call(checkout_command, shell=True, cwd = dict[r.checkout]["project"])

def command_diff(r, dict, path):
    if(not r.source and not r.test):
        print("Missing diff options - specify exactly one option \"-s\" OR \"-t\"")
        exit(-8)
    
    elif(r.source and r.test):
        print("Too many diff options - specify only one option: \"-s\" OR \"-t\"")
        exit(-9)

    elif(r.buggy or r.fixed):
        print("Extra option specified - these option (\"-b\", or \"-f\") will be ignored")
    
    if(not r.diff in dict):
        print(r.diff + " does not exist in the dataset! Use \"-a\" option to find valid bugIDs")
        exit(-10)
        
    else:
        print(" ".join(["Printing diff information for", r.diff, ":\n"]))

        if(r.source):
            diff_command = " ".join(["cat", r.path + path + "/diffs/" + dict[r.diff]["project"] + "-" + dict[r.diff]["hash"] + ".src.patch"])
        elif(r.test):
            diff_command = " ".join(["cat", r.path + path + "/diffs/" + dict[r.diff]["project"] + "-" + dict[r.diff]["hash"] + ".test.patch"])
        else:
            raise Exception("Missing diff option!")

        subprocess.call(diff_command, shell=True)

def setDatasetPath(r):
    if(r.language == "kotlin"):
        return "dataset-kotlin"
    elif(r.language == "groovy"):
        return "dataset-groovy"
    elif(r.language == "scala"):
        return "dataset-scala"

    raise Exception("Invalid dataset language specified! Please use \"-h\" for acceptable languages")

def loadCSV(r, path):
    csvPath = path + "/references.csv"

    if (os.path.exists(r.path + csvPath)):
        with open(r.path + csvPath) as csvData:
            fields = ["id", "url", "project", "hash", "commit_url", "build_system", "android"] # Must be updated anytime the references.csv is updated
            csvReader = csv.DictReader(csvData, fieldnames = fields)
            csvDict = {}

            for row in csvReader:
                csvDict[row["id"].strip()] = row            
    else:
        print("Unable to locate file:", r.path + csvPath)
        raise Exception("Failed to find references.csv file. Use the \"-p\" (e.g \"python3 defexts.py <defexts-dataset> -p /my/directory/path/here\" option to specify the directory containing the \"dataset-<language>\" folder(s)")

    return csvDict

def main():
    r = setupParser()

    dataset_languages = []
    dataset_languages.append("kotlin")
    dataset_languages.append("groovy")
    dataset_languages.append("scala")

    if(not (r.language in dataset_languages)):
        print("Specify a valid langauge dataset: " + ", ".join(dataset_languages))
        exit(-1)

    else:
        try:
            path = setDatasetPath(r)
            data = loadCSV(r, path)
        except Exception as e:
            print(e)
            exit(-2)

        if(r.all_projects and not r.list_bugs and not r.checkout and not r.diff):        
            command_all_projects(r, data)
            exit(0)

        elif(not r.all_projects and r.list_bugs and not r.checkout and not r.diff):
            command_list_bugs(r, data)
            exit(0)

        elif(not r.all_projects and not r.list_bugs and r.checkout and not r.diff):
            command_checkout(r, data, path)
            exit(0)

        elif(not r.all_projects and not r.list_bugs and not r.checkout and r.diff):            
            command_diff(r, data, path)
            exit(0)

        elif(not r.all_projects and not r.list_bugs and not r.checkout and not r.diff):
            print("Specify an action: \"-a\", \"-l\", \"-c\", or \"-d\"")
            exit(-3)

        else:
            print("Invalid actions specified. Specify exactly one of these options: \"-a\", \"-l\", \"-c\", or \"-d\"")
            exit(-4)

main()