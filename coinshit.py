from discord_webhook import webhook #line:1
import proxymanager #line:2
import requests #line:3
from bs4 import BeautifulSoup #line:4
import json #line:5
import cloudscraper #line:6
import time #line:7
import logging #line:8
import threading #line:9
from proxymanager import ProxyManager #line:10
proxy_manager =ProxyManager ('proxies.txt')#line:12
from discord_webhook import DiscordWebhook ,DiscordEmbed #line:14
from faker import Faker #line:16
fake =Faker ("en_US")#line:17
import random #line:18
from random import randint #line:19
import string #line:21
proxy_manager =ProxyManager ('proxies.txt')#line:23
import string #line:24
threads =input ("How many threads? ")#line:26
class getTHATBREADDDDDDDD :#line:27
    def __init__ (O00OOOOO0OO0O000O ,O000OO0000000O00O ):#line:36
        pass #line:37
    def start ():#line:40
        with open ('config.json')as O00O0000OO000O00O :#line:41
            O0O0OO0O0OO0O00O0 =json .load (O00O0000OO000O00O )#line:42
        OOOOOOO0OO0O000O0 ="unable to process your"#line:44
        O0OOOOOOO00OOO00O =random .choice (O0O0OO0O0OO0O00O0 )#line:45
        OO00O0O000O0000O0 =O0OOOOOOO00OOO00O ["addy"]#line:46
        OOO0O000OOOOO0O00 =O0OOOOOOO00OOO00O ["addy2"]#line:47
        O00OOO00O00OO0000 =O0OOOOOOO00OOO00O ["city"]#line:48
        OOOO0O0O0000000OO =O0OOOOOOO00OOO00O ["state"]#line:49
        O0OOO0OOOO0O0OO0O =O0OOOOOOO00OOO00O ["zip"]#line:50
        O0O00O0000O00O00O =O0OOOOOOO00OOO00O ["cc"]#line:51
        OOO0O00O0OOOO0O00 =O0OOOOOOO00OOO00O ["month"]#line:52
        OO0O0O0O00OOO00OO =O0OOOOOOO00OOO00O ["year"]#line:53
        OO0O0O00OO000OO0O =O0OOOOOOO00OOO00O ["cvv"]#line:54
        OO000O0O0OOO0OO00 =O0OOOOOOO00OOO00O ["cardtype"]#line:55
        O000000O0O0000O0O =O0OOOOOOO00OOO00O ["catchall"]#line:56
        O0OOO00OOOO0OOOO0 =O0OOOOOOO00OOO00O ["webhook"]#line:57
        O000000OO0OOOO00O =O0OOOOOOO00OOO00O ["pid"]#line:58
        O00O00000O000O000 ="************"#line:60
        O0OOOO0O000O0OO0O ="***"#line:61
        if OO000O0O0OOO0OO00 =="Amex":#line:63
            O00O00000O000O000 ="***********"#line:64
            O0OOOO0O000O0OO0O ="****"#line:65
        OO0OO00O0O0OOOOOO ={'authority':'catalog.usmint.gov','accept':'text/html, */*; q=0.01','accept-encoding':'gzip, deflate, br','accept-language':'en-US,en;q=0.9','origin':'https://catalog.usmint.gov','user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36','content-type':'application/x-www-form-urlencoded; charset=UTF-8','sec-fetch-site':'same-origin','sec-fetch-mode':'cors','x-requested-with':'XMLHttpRequest','referer':'https://catalog.usmint.gov/on/demandware.store/Sites-USM-Site/default/Cart-Show'}#line:78
        print ("Started Task")#line:79
        OO0OOO0OOO0O00OOO =requests .session ()#line:80
        O0OO0OOOOO0OO000O =cloudscraper .create_scraper (sess =OO0OOO0OOO0O00OOO )#line:81
        O0000OO0O0000O0O0 =proxy_manager .random_proxy ()#line:82
        OOO0000OO0O0O000O ={"https":O0000OO0O0000O0O0 .get_dict ()["https"]}#line:85
        O0OO0OOOOO0OO000O .proxies =OOO0000OO0O0O000O #line:86
        def OO00O0O0000O000OO ():#line:87
            O000O000O00O0O0O0 ="{}".format (O0OOO00OOOO0OOOO0 )#line:88
            O000O000O00O0O0O0 =DiscordWebhook (url =O000O000O00O0O0O0 )#line:89
            O00OOOOOOO0000OOO =DiscordEmbed (title ='US Mint Success!',description =f'Succesful Checkout!')#line:90
            O000O000O00O0O0O0 .add_embed (O00OOOOOOO0000OOO )#line:91
            O000O000O00O0O0O0 .execute ()#line:92
        def OOO0OOO0O0O0O0OOO ():#line:93
            O00OO0O00OO0OOO0O ={'pid':'{}'.format (O000000OO0OOOO00O ),'navid':'null','cartAction':'add','pid':'{}'.format (O000000OO0OOOO00O ),'cgid':'null','egc':'null'}#line:103
            O0O0O00000OO0O0O0 =O0OO0OOOOO0OO000O .post ("https://catalog.usmint.gov/on/demandware.store/Sites-USM-Site/default/Cart-AddProduct?format=ajax",data =O00OO0O00OO0OOO0O )#line:104
            print ("Adding to Cart")#line:105
            O0OO0OO0O00OOOOOO =O0OO0OOOOO0OO000O .get ("https://catalog.usmint.gov/on/demandware.store/Sites-USM-Site/default/Cart-ValidateBulkLimit")#line:106
        def OOOOO0OO00O0OO00O ():#line:109
            print ("Going to Checkout")#line:110
            OOO0O00O0O0000O0O =O0OO0OOOOO0OO000O .get ("https://catalog.usmint.gov/on/demandware.store/Sites-USM-Site/default/Cart-Show")#line:111
            O000O0OOOO000OO00 =OOO0O00O0O0000O0O .text #line:119
            OOO0000O000OO000O =BeautifulSoup (O000O0OOOO000OO00 ,"html.parser")#line:120
            O000OO0O0OO0OO0OO =OOO0000O000OO000O .find ("input",attrs ={"name":"dwfrm_singleshipping_securekey"})['value']#line:122
            OOOO000O0O0O0O000 =OOO0000O000OO000O .find ("input",attrs ={"name":"dwfrm_billing_securekey"})['value']#line:123
            O00OO0OO00000O000 =O000O0OOOO000OO00 .split ('form action="https://catalog.usmint.gov/on/demandware.store/Sites-USM-Site/default/Cart-Show/')[1 ]#line:124
            O0O0O00OOO0OO0OOO =O00OO0OO00000O000 .split ("\"")[0 ]#line:125
            OOO000OOOOOO0O00O ="https://catalog.usmint.gov/on/demandware.store/Sites-USM-Site/default/Cart-Show/"+O0O0O00OOO0OO0OOO #line:126
            OO000O00O0O0OOO0O =fake .first_name ()#line:127
            O0OOO0O0OOOOOOO00 =fake .last_name ()#line:128
            O0OO00000OO0O00O0 =fake .phone_number ()#line:129
            O000000OO000OOO00 =O0O00O0000O00O00O [-4 :]#line:130
            def O00OO0O0OOOOO0O0O ():#line:133
                O0000OO00O0O0O00O ={"dwfrm_singleshipping_shippingAddress_addressFields_selectedAddressID":"newaddress","dwfrm_singleshipping_shippingAddress_addressFields_firstName":OO000O00O0O0OOO0O ,"dwfrm_singleshipping_shippingAddress_addressFields_lastName":O0OOO0O0OOOOOOO00 ,"dwfrm_singleshipping_shippingAddress_addressFields_phone":O0OO00000OO0O00O0 ,"dwfrm_singleshipping_shippingAddress_email":"{}{}".format (OO000O00O0O0OOO0O +O0OOO0O0OOOOOOO00 ,O000000O0O0000O0O ),"dwfrm_billing_billingAddress_emailsource":"Website - Checkout","dwfrm_singleshipping_shippingAddress_addressFields_address1":"{}".format (OO00O0O000O0000O0 ),"dwfrm_singleshipping_shippingAddress_addressFields_address2":"{}".format (OOO0O000OOOOO0O00 ),"dwfrm_singleshipping_shippingAddress_addressFields_city":O00OOO00O00OO0000 ,'dwfrm_singleshipping_shippingAddress_addressFields_states_state':OOOO0O0O0000000OO ,'dwfrm_singleshipping_shippingAddress_addressFields_zip':O0OOO0OOOO0O0OO0O ,'dwfrm_singleshipping_shippingAddress_addressFields_country':"US","__avs_select":"1","dwfrm_singleshipping_shippingAddress_isCreateAccountSelected":"false","dwfrm_singleshipping_createAccount_password":"","dwfrm_singleshipping_createAccount_passwordconfirm":"","dwfrm_singleshipping_createAccount_question":"1","dwfrm_singleshipping_createAccount_answer":"","dwfrm_singleshipping_securekey":O000OO0O0OO0OO0OO ,"dwfrm_billing_securekey":OOOO000O0O0O0O000 ,"format":"ajax","refresh":"shipping","dwfrm_singleshipping_shippingAddress_applyShippingAddress":""}#line:158
                O00OOO0OO00000OO0 =O0OO0OOOOO0OO000O .post (OOO000OOOOOO0O00O ,headers =OO0OO00O0O0OOOOOO ,data =O0000OO00O0O0O00O )#line:160
            def O000000OO000O0000 ():#line:162
                O0000000OO00O00OO ='dwfrm_singleshipping_shippingAddress_useAsBillingAddress=true&dwfrm_billing_billingAddress_addressFields_selectedAddressID=&dwfrm_billing_billingAddress_addressFields_firstName={}&dwfrm_billing_billingAddress_addressFields_lastName={}&dwfrm_billing_billingAddress_addressFields_address1={}&dwfrm_billing_billingAddress_addressFields_address2={}&dwfrm_billing_billingAddress_addressFields_city={}&dwfrm_billing_billingAddress_addressFields_states_state={}&dwfrm_billing_billingAddress_addressFields_zip={}&dwfrm_billing_billingAddress_addressFields_country=US&dwfrm_billing_billingAddress_addressFields_phone={}&dwfrm_billing_billingAddress_email_emailAddress={}{}&dwfrm_billing_securekey={}&dwfrm_singleshipping_securekey={}&refresh=payment&format=ajax&dwfrm_billing_applyBillingAndPayment=&dwfrm_billing_paymentMethods_selectedPaymentMethodID=CREDIT_CARD&dwfrm_billing_paymentMethods_creditCard_type={}&dwfrm_billing_paymentMethods_creditCard_owner={}+{}&dwfrm_billing_paymentMethods_creditCard_number={}&dwfrm_billing_paymentMethods_creditCard_month={}&dwfrm_billing_paymentMethods_creditCard_year={}&dwfrm_billing_paymentMethods_creditCard_cvn={}&dwfrm_billing_securekey={}&dwfrm_emailsignup_phone='.format (OO000O00O0O0OOO0O ,O0OOO0O0OOOOOOO00 ,OO00O0O000O0000O0 ,OOO0O000OOOOO0O00 ,O00OOO00O00OO0000 ,OOOO0O0O0000000OO ,O0OOO0OOOO0O0OO0O ,O0OO00000OO0O00O0 ,OO000O00O0O0OOO0O ,O000000O0O0000O0O ,OOOO000O0O0O0O000 ,O000OO0O0OO0OO0OO ,OO000O0O0OOO0OO00 ,OO000O00O0O0OOO0O ,O0OOO0O0OOOOOOO00 ,O0O00O0000O00O00O ,OOO0O00O0OOOO0O00 ,OO0O0O0O00OOO00OO ,OO0O0O00OO000OO0O ,OOOO000O0O0O0O000 )#line:163
                O0O00OO0O0OO0OO00 =O0OO0OOOOO0OO000O .post (OOO000OOOOOO0O00O +'?'+O0000000OO00O00OO ,headers =OO0OO00O0O0OOOOOO )#line:164
                O000OOOOO000O000O ={'dwfrm_billing_paymentMethods_selectedPaymentMethodID':'CREDIT_CARD','dwfrm_billing_paymentMethods_creditCard_type':"{}".format (OO000O0O0OOO0OO00 ),'dwfrm_billing_paymentMethods_creditCard_owner':"{} {}".format (OO000O00O0O0OOO0O ,O0OOO0O0OOOOOOO00 ),'dwfrm_billing_paymentMethods_creditCard_number':"{}{}".format (O00O00000O000O000 ,O000000OO000OOO00 ),'dwfrm_billing_paymentMethods_creditCard_month':"{}".format (OOO0O00O0OOOO0O00 ),'dwfrm_billing_paymentMethods_creditCard_year':"{}".format (OO0O0O0O00OOO00OO ),'dwfrm_billing_paymentMethods_creditCard_cvn':'{}'.format (O0OOOO0O000O0OO0O ),'dwfrm_billing_securekey':OOOO000O0O0O0O000 ,'dwfrm_emailsignup_phone':''}#line:176
                O0O00OO0O0OO0OO00 =O0OO0OOOOO0OO000O .post ('https://catalog.usmint.gov/on/demandware.store/Sites-USM-Site/default/COSummary-Submit',headers =OO0OO00O0O0OOOOOO ,data =O000OOOOO000O000O )#line:178
                OOOO0OOOOO000OO0O =O0O00OO0O0OO0OO00 .text #line:179
                if "If you have questions about your order" in OOOO0OOOOO000OO0O:#line:180
                    OO00O0O0000O000OO ()#line:181
                elif "unable to process"in OOOO0OOOOO000OO0O :#line:182
                    print ("Payment Declined, Retyring")#line:183
                elif "properly"in OOOO0OOOOO000OO0O :#line:184

                    print ("request error")#line:185
                elif "Something went wrong"in OOOO0OOOOO000OO0O :#line:186
                    print ("site crashed")#line:187
            O00OO0O0OOOOO0O0O ()#line:193
            while "unable to process"or "Something went wrong"in OOOOOOO0OO0O000O0 :#line:198
                O000000OO000O0000 ()#line:199
        OOO0OOO0O0O0O0OOO ()#line:203
        OOOOO0OO00O0OO00O ()#line:204
    jobs =[]#line:212
    for i in range (0 ,int (threads )):#line:213
        jobs .append (threading .Thread (target =start ))#line:214
    for j in jobs :#line:217
        j .start ()#line:218
    for j in jobs :#line:221
        j .join ()
