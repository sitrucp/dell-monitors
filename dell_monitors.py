#-*- coding: utf-8 -*-
import urllib2
import urllib
from cookielib import CookieJar
from bs4 import BeautifulSoup
import csv
import re
from datetime import datetime

countries={
    'AC':'Ascension Island',
    'AD':'Andorra',
    'AE':'United Arab Emirates',
    'AF':'Afghanistan',
    'AG':'Antigua and Barbuda',
    'AI':'Anguilla',
    'AL':'Albania',
    'AM':'Armenia',
    'AN':'Netherlands Antilles',
    'AO':'Angola',
    'AQ':'Antarctica',
    'AR':'Argentina',
    'AS':'American Samoa',
    'AT':'Austria',
    'AU':'Australia',
    'AW':'Aruba',
    'AX':'Aland',
    'AZ':'Azerbaijan',
    'BA':'Bosnia and Herzegovina',
    'BB':'Barbados',
    'BD':'Bangladesh',
    'BE':'Belgium',
    'BF':'Burkina Faso',
    'BG':'Bulgaria',
    'BH':'Bahrain',
    'BI':'Burundi',
    'BJ':'Benin',
    'BL':'Saint Barthelemy',
    'BM':'Bermuda',
    'BN':'Brunei Darussalam',
    'BO':'Bolivia Plurinational State of',
    'BR':'Brazil',
    'BS':'Bahamas',
    'BT':'Bhutan',
    'BU':'Burma',
    'BV':'Bouvet Island',
    'BW':'Botswana',
    'BY':'Belarus',
    'BZ':'Belize',
    'CA':'Canada',
    'CC':'Cocos (Keeling) Islands',
    'CD':'Congo the Democratic Republic of the',
    'CF':'Central African Republic',
    'CG':'Congo',
    'CH':'Switzerland',
    'CI':'Cote dIvoire',
    'CK':'Cook Islands',
    'CL':'Chile',
    'CM':'Cameroon',
    'CN':'China',
    'CO':'Colombia',
    'CP':'Clipperton Island',
    'CR':'Costa Rica',
    'CS':'Czechoslovakia',
    'CT':'Canton and Enderbury Islands',
    'CU':'Cuba',
    'CV':'Cabo Verde',
    'CW':'Curacao',
    'CX':'Christmas Island',
    'CY':'Cyprus',
    'CZ':'Czech Republic',
    'DE':'Germany',
    'DG':'Diego Garcia',
    'DJ':'Djibouti',
    'DK':'Denmark',
    'DM':'Dominica',
    'DO':'Dominican Republic',
    'DY':'Benin',
    'DZ':'Algeria',
    'EC':'Ecuador',
    'EE':'Estonia',
    'EG':'Egypt',
    'EH':'Western Sahara',
    'ER':'Eritrea',
    'ES':'Spain',
    'ET':'Ethiopia',
    'EW':'Estonia',
    'EZ':'Eurozone',
    'FI':'Finland',
    'FJ':'Fiji',
    'FK':'Falkland Islands (Malvinas)',
    'FL':'Liechtenstein',
    'FM':'Micronesia Federated States of',
    'FO':'Faroe Islands',
    'FQ':'French Southern and Antarctic Territories',
    'FR':'France',
    'GA':'Gabon',
    'GB':'United Kingdom of Great Britain and Northern Ireland',
    'GD':'Grenada',
    'GE':'Georgia',
    'GF':'French Guiana',
    'GH':'Ghana',
    'GI':'Gibraltar',
    'GL':'Greenland',
    'GM':'Gambia',
    'GN':'Guinea',
    'GP':'Guadeloupe',
    'GQ':'Equatorial Guinea',
    'GR':'Greece',
    'GS':'South Georgia and the South Sandwich Islands',
    'GT':'Guatemala',
    'GU':'Guam',
    'GW':'Guinea-Bissau',
    'GY':'Guyana',
    'HK':'Hong Kong',
    'HM':'Heard Island and McDonald Islands',
    'HN':'Honduras',
    'HR':'Croatia',
    'HT':'Haiti',
    'HU':'Hungary',
    'HV':'Upper Volta',
    'IC':'Canary Islands',
    'ID':'Indonesia',
    'IE':'Ireland',
    'IL':'Israel',
    'IM':'Isle of Man',
    'IN':'India',
    'IQ':'Iraq',
    'IR':'Iran Islamic Republic of',
    'IS':'Iceland',
    'IT':'Italy',
    'JA':'Jamaica',
    'JE':'Jersey',
    'JM':'Jamaica',
    'JO':'Jordan',
    'JP':'Japan',
    'JT':'Johnston Island',
    'KE':'Kenya',
    'KG':'Kyrgyzstan',
    'KH':'Cambodia',
    'KI':'Kiribati',
    'KM':'Comoros',
    'KN':'Saint Kitts and Nevis',
    'KP':'Korea Democratic Peoples Republic of',
    'KR':'Korea Republic of',
    'KW':'Kuwait',
    'KY':'Cayman Islands',
    'KZ':'Kazakhstan',
    'LA':'Lao Peoples Democratic Republic',
    'LB':'Lebanon',
    'LC':'Saint Lucia',
    'LF':'Libya Fezzan',
    'LI':'Liechtenstein',
    'LK':'Sri Lanka',
    'LR':'Liberia',
    'LS':'Lesotho',
    'LT':'Libya Tripoli',
    'LU':'Luxembourg',
    'LV':'Latvia',
    'LY':'Libya',
    'MA':'Morocco',
    'MC':'Monaco',
    'MD':'Moldova, Republic of',
    'ME':'Montenegro',
    'MF':'Saint Martin (French part)',
    'MG':'Madagascar',
    'MH':'Marshall Islands',
    'MI':'Midway Islands',
    'MK':'Macedonia the former Yugoslav Republic of',
    'ML':'Mali',
    'MM':'Myanmar',
    'MN':'Mongolia',
    'MO':'Macao',
    'MP':'Northern Mariana Islands',
    'MQ':'Martinique',
    'MR':'Mauritania',
    'MS':'Montserrat',
    'MT':'Malta',
    'MU':'Mauritius',
    'MV':'Maldives',
    'MW':'Malawi',
    'MX':'Mexico',
    'MY':'Malaysia',
    'MZ':'Mozambique',
    'NA':'Namibia',
    'NC':'New Caledonia',
    'NE':'Niger',
    'NF':'Norfolk Island',
    'NG':'Nigeria',
    'NH':'New Hebrides',
    'NI':'Nicaragua',
    'NL':'Netherlands',
    'NO':'Norway',
    'NP':'Nepal',
    'NQ':'Dronning Maud Land',
    'NR':'Nauru',
    'NT':'Neutral Zone',
    'NU':'Niue',
    'NZ':'New Zealand',
    'OM':'Oman',
    'PA':'Panama',
    'PE':'Peru',
    'PF':'French Polynesia',
    'PG':'Papua New Guinea',
    'PH':'Philippines',
    'PI':'Philippines',
    'PK':'Pakistan',
    'PL':'Poland',
    'PM':'Saint Pierre and Miquelon',
    'PN':'Pitcairn',
    'PR':'Puerto Rico',
    'PS':'Palestine State of',
    'PT':'Portugal',
    'PW':'Palau',
    'PY':'Paraguay',
    'PZ':'Panama Canal Zone',
    'QA':'Qatar',
    'RA':'Argentina',
    'RB':'Bolivia',
    'RC':'China',
    'RE':'Reunion',
    'RH':'Haiti',
    'RI':'Indonesia',
    'RL':'Lebanon',
    'RM':'Madagascar',
    'RN':'Niger',
    'RO':'Romania',
    'RP':'Philippines',
    'RS':'Serbia',
    'RU':'Russian Federation',
    'RW':'Rwanda',
    'SA':'Saudi Arabia',
    'SB':'Solomon Islands',
    'SC':'Seychelles',
    'SD':'Sudan',
    'SE':'Sweden',
    'SF':'Finland',
    'SG':'Singapore',
    'SH':'Saint Helen Ascension and Tristan da Cunha',
    'SI':'Slovenia',
    'SJ':'Svalbard and Jan Mayen',
    'SK':'Slovakia',
    'SL':'Sierra Leone',
    'SM':'San Marino',
    'SN':'Senegal',
    'SO':'Somalia',
    'SR':'Suriname',
    'SS':'South Sudan',
    'ST':'Sao Tome and Principe',
    'SU':'USSR',
    'SV':'El Salvador',
    'SX':'Sint Maarten (Dutch part)',
    'SY':'Syrian Arab Republic',
    'SZ':'Swaziland',
    'TA':'Tristan da Cunha',
    'TC':'Turks and Caicos Islands',
    'TD':'Chad',
    'TG':'Togo',
    'TH':'Thailand',
    'TJ':'Tajikistan',
    'TK':'Tokelau',
    'TL':'Timor-Leste',
    'TM':'Turkmenistan',
    'TN':'Tunisia',
    'TO':'Tonga',
    'TP':'East Timor',
    'TR':'Turkey',
    'TT':'Trinidad and Tobago',
    'TV':'Tuvalu',
    'TW':'Taiwan Province of China',
    'TZ':'Tanzania United Republic of',
    'UA':'Ukraine',
    'UG':'Uganda',
    'UK':'United Kingdom',
    'UN':'United Nations',
    'US':'United States of America',
    'UY':'Uruguay',
    'UZ':'Uzbekistan',
    'VA':'Holy See',
    'VC':'Saint Vincent and the Grenadines',
    'VD':'Vietnam Democratic Republic of',
    'VE':'Venezuela Bolivarian Republic of',
    'VG':'Virgin Islands British',
    'VI':'Virgin Islands U.S.',
    'VN':'Vietnam',
    'VU':'Vanuatu',
    'WF':'Wallis and Futuna',
    'WG':'Grenada',
    'WK':'Wake Island',
    'WL':'Saint Lucia',
    'WS':'Samoa',
    'WV':'Saint Vincent',
    'YD':'Yemen Democratic',
    'YE':'Yemen',
    'YT':'Mayotte',
    'YU':'Yugoslavia',
    'YV':'Venezuela',
    'ZA':'South Africa',
    'ZM':'Zambia',
    'ZR':'Zaire',
    'ZW':'Zimbabwe'
}

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass
 
    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass
 
    return False

def main():

    todaydate = datetime.today().strftime('%Y-%m-%d')
    
    with open('dell_monitors.csv', 'wb') as file:
        writer = csv.DictWriter(file, fieldnames = ['date', 'country_code', 'country', 'page', 'desc', 'prod_name', 'size','model', 'delivery', 'price', 'url'], delimiter = ',')
        writer.writeheader()
        
        for key in sorted(countries):
        #for country in countries:
            country_code = key.lower()
            country = countries[key]
            pagenum = 1      
            while pagenum < 6:
                url = "http://accessories.dell.com/sna/category.aspx?c="+country_code+"&category_id=6481&l=en&s=dhs&ref=3245_mh&cs=cadhs1&~ck=anav&p=" + str(pagenum)
                # HTTPCookieProcessor allows cookies to be accepted and avoid timeout waiting for prompt
                page = urllib2.build_opener(urllib2.HTTPCookieProcessor).open(url).read()
                soup = BeautifulSoup(page)
                print country_code + " - " + str(pagenum)
                if soup.find("div", {"class":"rgParentH"}):
                    tablediv = soup.find("div", {"class":"rgParentH"})
                    tables = tablediv.find_all('table')
                    data_table = tables[0] # outermost table parent =0 or no parent
                    rows = data_table.find_all("tr")
                    
                    for row in rows:
                        #if len(row.find_parents("tr")) == 0:
                        rgDescription = row.find("div", {"class":"rgDescription"})
                        rgMiscInfo = row.find("div", {"class":"rgMiscInfo"})
                        pricing_retail_nodiscount_price = row.find("span", {"class":"pricing_retail_nodiscount_price"})

                        if rgMiscInfo: 
                            delivery = rgMiscInfo.get_text().encode('utf-8')
                        else:
                            delivery = ''
                            
                        if pricing_retail_nodiscount_price:
                            price1 = pricing_retail_nodiscount_price.get_text().encode('utf-8')
                            #remove currency symbols
                            non_decimal_char = re.compile(r'[^\d.]+')
                            price = non_decimal_char.sub('', price1)
                        else:
                            price = ''
                            
                        if rgDescription:
                            # clean up description so it be better parsed
                            desc = (rgDescription.get_text().encode('utf-8')
                                .replace("–","-")
                                .replace("|","-")
                                .replace('Built-in','built in')
                                .replace("("," ")
                                .replace(")"," ")
                                .replace("'"," ")
                                .replace(","," ")
                                .replace('"'," ")
                                .replace('”'," ")
                                .replace("-pulgadas"," ")
                                .replace("-inch"," ")
                                .replace("-Inch"," ")
                                .replace("모니터"," ")
                                .replace("인치 곡선"," ")
                                .replace(":",""))
                            
                            prod_name = desc.split("-")[0].strip()
                            
                            try:
                                # loop through desc split to find size
                                # size is most often the first number in desc 
                                # is_number function used to get integer and float format sizes
                                size = [s for s in desc.split() if is_number(s)][0]
                            except:
                                size = 'unknown'
                                
                            try:
                                model = desc.split("-")[1].strip()
                            except:
                                model = desc
                            
                            #create row to write to csv
                            results = str(todaydate)+","+country_code+","+country+","+str(pagenum)+","+desc+","+prod_name+","+str(size)+","+model+","+delivery+","+str(price)+","+url                            
                            file.write(results + '\n')
                    
                    pagenum +=1
                else:
                    pagenum =6
                    continue
                
if __name__ == '__main__':
    main()
