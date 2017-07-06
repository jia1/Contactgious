curl -X 'POST' 'http://contact-jiayee.rhcloud.com/connect' -H 'Content-Type:application/json' -d '
{
    "enquiry":"9",
    "name":"Jia Yee",
    "email":"jia10@u.nus.edu",
    "subject":"Need some help",
    "message":"Need more help"
}'

curl -X 'POST' 'http://contact-jiayee.rhcloud.com/connect' -H 'Content-Type:application/json' -d '
{
    "enquiry":"3",
    "name":"Jia Yee",
    "email":"jia10@u.nus.edu",
    "phone": "67773777",
    "subject":"Some sponsorship questions",
    "message":"More sponsorship questions"
}'
