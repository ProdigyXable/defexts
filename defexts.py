import argparse
import os
import csv
import subprocess
from prettytable import PrettyTable

def printProjectInfo(dict):
    table = PrettyTable(['BugID', 'Hash', 'Build System', 'Android', 'Commit URL'])
    
    table.align["BugID"] = 'r'
    table.align["Hash"] = 'c'
    table.align["Build System"] = 'c'
    table.align["Android"] = 'c'
    table.align["Commit URL"] = 'l'
    
    for key in sorted(dict.keys()):
        row = dict[key]
        table.add_row([key, row['hash'], row['build_system'], row['android'], row['commit_url']])
    
    print(table)
    
def printPrintBugs(new_dict, dict):
    table = PrettyTable(['Project Name','Number of Projects', 'URL'])
    
    table.align["Project Name"] = 'r'
    table.align["URL"] = 'r'
    table.align["Number of Projects"] = 'c'

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
    table.add_row(["Distinct Projects", len(new_dict.keys())])
    table.add_row(["Total Projects", len(dict.keys())])
    
    print(table)

def setupParser():

    parser = argparse.ArgumentParser(description="Interface to Defexts")
    # parser.add_argument("-o", "--output", help="Set to show standard output of internal commands", default=False, action="store_true")
    parser.add_argument("language", action="store", type=str.lower)
    # ---------------------------------------- #
    parser.add_argument("-a", "--all-projects", default=False, action="store_true")
    parser.add_argument("-l", "--list-bugs", default=False, action="store_true")
    # ---------------------------------------- #
    parser.add_argument("-c", "--checkout", default=False, action="store")
    parser.add_argument("-d", "--diff", default=False, action="store")
    # ---------------------------------------- #
    parser.add_argument("-b", "--buggy", default=False, action="store_true")
    parser.add_argument("-f", "--fixed", default=False, action="store_true")
   
    # ---------------------------------------- #
    parser.add_argument("-s", "--source", default=False, action="store_true")
    parser.add_argument("-t", "--test", default=False, action="store_true")
    # ---------------------------------------- #
    parser.add_argument("-p", "--path", default="./", action="store")
    parser.add_argument("-v", "--version", default=False, action="store_true") # implement
    
    result = parser.parse_args()

    if(not result.path.endswith("/")):
        result.path = result.path + "/"

    return result
    
def all_projects(r, dict):
    if(r.source or r.test or r.buggy or r.fixed):
        print("Extra options specified - these options (\"-s\", \"-t\", \"-b\" or \"-f\") will be ignored")

    print(" ".join(["Printing details for all", r.language, "projects:"])) 
    
    printProjectInfo(dict)

def list_bugs(r, dict):
    if(r.source or r.test or r.buggy or r.fixed):
        print("Extra options specified - these options (\"-s\", \"-t\", \"-b\", or \"-f\") will be ignored")
    
    print(" ".join(["Printing bugs per project + other project statistics", r.language, "projects"]))

    new_dict = {}
    
    printPrintBugs(new_dict, dict)
    printTableStatistics(new_dict, dict)

def checkout(r, dict, path):
    if(not r.buggy and not r.fixed):
        print("Missing checkout options - specify exactly one option \"-b\" OR \"-f\"")
        exit(-9)
    
    elif(r.buggy and r.fixed):
        print("Too many checkout options - specify only one option: \"-b\" OR \"-f\"")
        exit(-10)
    
    elif(r.source or r.test):
        print("Extra options specified - these options (\"-s\" or \"-t\") will be ignored")
        
    if(not r.checkout in dict):
        print(r.checkout + " does not exist in the dataset! Use \"-a\" option to find valid bugIDs")
        exit(-11)

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

def diff(r, dict, path):
    if(not r.source and not r.test):
        print("Missing diff options - specify exactly one option \"-s\" OR \"-t\"")
        exit(-12)
    
    elif(r.source and r.test):
        print("Too many diff options - specify only one option: \"-s\" OR \"-t\"")
        exit(-13)

    elif(r.buggy or r.fixed):
        print("Extra option specified - these option (\"-b\", or \"-f\") will be ignored")
    
    if(not r.diff in dict):
        print(r.diff + " does not exist in the dataset! Use \"-a\" option to find valid bugIDs")
        exit(-14)
        
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
        return "database-kotlin"
    elif(r.language == "groovy"):
        return "database-groovy"

    raise Exception("invalid dataset language specified!")

def loadCSV(r, path):
    csvPath = path + "/references.csv"

    fields = ["id", "url", "project", "hash", "commit_url", "build_system", "android"]


    if (os.path.exists(r.path + csvPath)):
        with open(r.path + csvPath) as csvData:
            csvReader = csv.DictReader(csvData, fieldnames = fields)
            csvDict = {}

            for row in csvReader:
                csvDict[ row['project'].strip() + "-" + row["id"].strip()] = row            
    else:
        raise Exception("Failed to find references.csv file. Use the \"-p\" option to specify the directory containing the \"dataset-<language>\" folder(s)")

    return csvDict

def main():
    r = setupParser()

    if(not ( r.language == "kotlin" or r.language == "groovy")):
        print("Specify a specific langauge dataset - \"kotlin\" for Kotlin or \"groovy\" for Groovy")
        exit(-1)

    else:
        try:
            path = setDatasetPath(r)
            data = loadCSV(r, path)
        except Exception as e:
            print(e)
            exit(-2)

        if(r.all_projects and not r.list_bugs and not r.checkout and not r.diff):        
            all_projects(r, data)
            exit(-3)

        elif(not r.all_projects and r.list_bugs and not r.checkout and not r.diff):
            list_bugs(r, data)
            exit(-4)

        elif(not r.all_projects and not r.list_bugs and r.checkout and not r.diff):
            checkout(r, data, path)
            exit(-5)

        elif(not r.all_projects and not r.list_bugs and not r.checkout and r.diff):            
            diff(r, data, path)
            exit(-6)

        elif(not r.all_projects and not r.list_bugs and not r.checkout and not r.diff):
            print("Specify an action - \"-a\", \"-l\", \"c\", or \"-d\"")
            exit(-7)

        else:
            print("Invalid actions specified. Specify exactly one of these options: \"-a\", \"-l\", \"c\", or \"-d\"")
            exit(-8)

main()