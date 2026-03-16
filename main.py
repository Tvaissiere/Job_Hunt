import webbrowser

companies = [
"Amazon","Amazon Web Services","Microsoft","Google","Meta","Apple","Oracle","IBM","Cisco","Nvidia","Intel","Salesforce","Adobe","SAP","ServiceNow","Atlassian","Snowflake","Databricks","MongoDB","Cloudflare","Fastly","Datadog","Elastic","HashiCorp","Palantir","GitHub","GitLab",
"BT Group","Openreach","EE","Sky","Virgin Media O2","Vodafone","Three UK","TalkTalk","Daisy Communications","CityFibre","Gamma Telecom","Hyperoptic","Colt Technology Services","KCOM","Telent","Nokia","Ericsson","Ciena",
"Lloyds Banking Group","Barclays","HSBC","NatWest Group","Santander UK","Nationwide Building Society","TSB Bank","Metro Bank","Virgin Money","Monzo","Starling Bank","Revolut","Wise","Zopa","OakNorth Bank","Atom Bank","Tandem Bank","ClearBank","Thought Machine","Checkout.com","TrueLayer","GoCardless","Worldpay","Visa","Mastercard","PayPal","Klarna","Adyen","Stripe","SumUp","Block","Currencycloud","Zilch",
"Accenture","Capgemini","Deloitte","PwC","EY","KPMG","Tata Consultancy Services","Infosys","Wipro","HCLTech","Cognizant","Thoughtworks","BJSS","Endava","EPAM Systems","Globant","Slalom","Kin + Carta","Valtech","SoftServe",
"Darktrace","Sophos","Snyk","Immersive Labs","CrowdStrike","Rapid7","SentinelOne","Palo Alto Networks","Fortinet","Check Point","Secureworks","Tenable","Arctic Wolf","Qualys","Trend Micro","Okta","CyberArk",
"BAE Systems","Rolls-Royce","Leonardo","Thales","QinetiQ","Babcock International","Raytheon UK","MBDA","Lockheed Martin UK","Northrop Grumman UK",
"Sage","ARM","AVEVA","Renishaw","Spectris","Micro Focus","Softcat","Computacenter","Bytes Technology","FD Technologies","Finastra","Auto Trader","Rightmove","Ocado Technology","Quantexa","Featurespace","Graphcore",
"DeepMind","Stability AI","Synthesia","Dataiku","Alteryx","Confluent","Grafana Labs","Sentry","Miro","Figma","Notion","HubSpot","Zendesk","Intercom","Asana","Canva","Squarespace","Wix","Shopify",
"King","Rockstar Games","Electronic Arts","Ubisoft","Epic Games","Unity","Improbable","Frontier Developments","Jagex","Sumo Digital","Codemasters","Rebellion",
"Tesco","Sainsbury's","ASDA","Co-op","Marks and Spencer","Unilever","Jaguar Land Rover","National Grid","British Airways","Shell","BP","Royal Mail","Deliveroo","ASOS","Boohoo","Farfetch","Gymshark","Zalando","Wayfair","eBay",
"BBC","Ofcom","HMRC","Government Digital Service","NHS England","Ministry of Justice","Home Office","National Crime Agency","Met Office","Ordnance Survey","Defence Digital","DVLA","Companies House","UK Parliament",
"Experian","Advanced","Iress","Open GI","Equiniti","GeoSLAM","Adzooma","Bloc Digital","Holovis","DeadHappy","VoxPopMe","Bluesky International","OneStream","Adapttech","Geospatial Insight"
]

job_role = ""
job_type_optns = ["Full Time", "Part Time", "Temporary", "Graduate", "Placement", "Entry Level"]
job_type = ""
count = 0
limiter = 20

def main(companies, job_role, job_type_optns, job_type, count, limiter):
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
        count += 1
        print(count)
        if count == limiter:
            input("\nPress Ctrl C to cancel or enter to load the next 20: ")
            limiter += 20
        webbrowser.open_new_tab("https://www.google.com/search?q=" + job_type + " " + job_role + " " + companies[i])

main(companies, job_role, job_type_optns, job_type, count, limiter)
