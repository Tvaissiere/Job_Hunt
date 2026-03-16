import webbrowser

# TODO: List most popular employers
companies = ["Monzo", "Lloyds",]
job_role = ""
job_type_optns = ["Full Time", "Part Time", "Temporary", "Graduate", "Placement", "Entry Level"]
job_type = ""

def main(companies, job_role, job_type_optns, job_type):
    for a in range(len(job_type_optns)):
        print(str(a+1) + ".   " + job_type_optns[a])
    job_type = int(input("\nPlease enter the corresponding number to your desired Job Type: ")) -1
    while job_type not in range(6):
        if job_type == 0:
            job_type = int(input("Sorry you need to select a valid option: ")) -1
        else:
            job_type = int(input("Sorry you need to select a valid option: ")) -1
    job_type = job_type_optns[job_type]
    job_role = input("\nWhat job role are you searching for? ")
    for i in range(len(companies)):
        webbrowser.open_new_tab("https://www.google.com/search?q="+job_type + " " +job_role+ " " +companies[i])

main(companies, job_role, job_type_optns, job_type)
