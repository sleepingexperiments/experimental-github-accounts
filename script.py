
import os
import sys
import datetime

# Formatted Git command to change the current repository user name
GIT_DEFINE_LOCAL_USER_NAME_FORMATTED="git config --local user.name \"{}\""

# Formatted Git command to change the current repository user email
GIT_DEFINE_LOCAL_USER_EMAIL_FORMATTED="git config --local user.email \"{}\""

# Formatted Git command to commit changes
GIT_COMMIT_CHANGES_FORMATTED="git commit -a -m \"{}\""

# Fake commit command format
FAKE_COMMIT_COMMAND_FORMAT="{}|{}|{}>>{}|{}"


"""
Script startup function
"""
def main(argv):
    if(len(argv)!=2):
        print("Please provide emails list file via parameters")
        # Parameters error here
    else:
        emails=extract_emails(argv[1])
        start_contribution_script(emails)


"""
Starts the contribution script
"""
def start_contribution_script(emails):
    random_file=create_random_file()
    commit_initial_file(random_file)
    for email in emails:
        fake_commit(email,email,random_file)
    push_changes()


"""
Commits initial fake file for allowing changes merge
"""
def commit_initial_file(file):
    os.system("git add {}|git commit -a -m \"{}\"".format(file,file))

"""
Creates a random file for dumping fake commit changes
"""
def create_random_file():
    random_file=str(datetime.datetime.now()).replace(" ","T")
    os.system("touch {}".format(random_file))
    return random_file


"""
Fakes a commit
"""
def fake_commit(email,commit_description,commit_file):
    user_name_command=GIT_DEFINE_LOCAL_USER_NAME_FORMATTED.format(email)
    user_email_command=GIT_DEFINE_LOCAL_USER_EMAIL_FORMATTED.format(email)
    echo_command="echo {}".format(str(datetime.datetime.now()))
    commit_command=GIT_COMMIT_CHANGES_FORMATTED.format(commit_description)
    os.system(FAKE_COMMIT_COMMAND_FORMAT.format(user_name_command,user_email_command,echo_command,commit_file,commit_command))


"""
Pushes changes to repository
"""
def push_changes():
    os.system("git push")

"""
Extrats emails from a certain file
"""

def extract_emails(file):
    lines=read_file(file)
    if(len(lines)==0):
        raise Exception("{} contains no emails!".format(file))
    return lines


"""
Reads a file and returns it content
"""
def read_file(file):
    print(file)
    return open(file,"r").readlines()


if __name__=="__main__":
    main(sys.argv)
