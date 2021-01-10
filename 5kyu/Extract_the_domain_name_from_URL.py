# https://www.codewars.com/kata/514a024011ea4fb54200004b/train/python

# Write a function that when given a URL as a string, 
# parses out just the domain name and returns it as a string. For example:

# domain_name("http://github.com/carbonfive/raygun") == "github" 
# domain_name("http://www.zombie-bites.com") == "zombie-bites"
# domain_name("https://www.cnet.com") == "cnet"


def domain_name(url):
    if "://" in url:
        if not "://www." in url:
            return url.split("://")[1].split(".")[0]
    elif len(url.split(".")) == 2:
        return url.split(".")[0]
    return url.split(".")[1]

print(domain_name("www.xakep.ru"))


# Test.assert_equals(domain_name("http://google.com"), "google")
# Test.assert_equals(domain_name("http://google.co.jp"), "google")
# Test.assert_equals(domain_name("www.xakep.ru"), "xakep")
# Test.assert_equals(domain_name("https://youtube.com"), "youtube")