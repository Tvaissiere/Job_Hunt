import webbrowser

# TODO: List most popular employers
companies = ["Monzo", "Lloyds",]
job_role = ""


def main(companies, job_role):
    job_role = input("What job role are you searching for? ")
    for i in range(len(companies)):
        webbrowser.open_new_tab("https://www.google.com/search?q="+job_role+" "+companies[i])

main(companies, job_role)
