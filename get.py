from bs4 import BeautifulSoup
import mechanize
import wget
import getpass

activityPageURI = "https://connect.garmin.com/activities"
loginFormURI = "https://sso.garmin.com/sso/login?service=https%3A%2F%2Fconnect.garmin.com%2Fpost-auth%2Flogin&webhost=olaxpw-connect00&source=https%3A%2F%2Fconnect.garmin.com%2Fen-US%2Fsignin&redirectAfterAccountLoginUrl=https%3A%2F%2Fconnect.garmin.com%2Fpost-auth%2Flogin&redirectAfterAccountCreationUrl=https%3A%2F%2Fconnect.garmin.com%2Fpost-auth%2Flogin&gauthHost=https%3A%2F%2Fsso.garmin.com%2Fsso&locale=en_US&id=gauth-widget&cssUrl=https%3A%2F%2Fstatic.garmincdn.com%2Fcom.garmin.connect%2Fui%2Fcss%2Fgauth-custom-v1.1-min.css&clientId=GarminConnect&rememberMeShown=true&rememberMeChecked=false&createAccountShown=true&openCreateAccount=false&usernameShown=false&displayNameShown=false&consumeServiceTicket=false&initialFocus=true&embedWidget=false&generateExtraServiceTicket=false"
activityServiceURI = "https://connect.garmin.com/proxy/activity-service-1.1/tcx/activity/{}?full=true"

username = raw_input('Garmin Connect Username: ')
password = getpass.getpass('Garmin Connect Password: ')

br = mechanize.Browser()
br.open(loginFormURI)
br.select_form(nr=0)
br['username'] = username
br['password']= password
br.submit()
br.open(activityPageURI)

soup = BeautifulSoup(br.response().read())
# get all activity ids on this page
activityLinks = soup.findAll("a", { "class" : "activityNameLink" })
ids = [str(a.get('href').rsplit('/',1)[1]) for a in activityLinks]
urls = [activityServiceURI.format(id) for id in ids]

# download all activities
map(wget.download, urls)

