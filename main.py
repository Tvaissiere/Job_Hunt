# TODO: Make it open new tab instead of window
import webbrowser

# TODO: List most popular employers
companies = ["Monzo",]
job_role = ""


def main(companies, job_role):
    job_role = input("What job role are you searching for? ")
    for i in range(len(companies)):
        webbrowser.open("https://www.google.com/search?q="+job_role+" "+companies[i])

main(companies, job_role)