# from https://pynative.com/python/regex/
import re


def re_finall():
    target_str = "My roll number is 25"
    # regex pattern \d to match any digit between 0 to 9.
    res = re.findall(r"\d", target_str)
    # extract mathing value
    print(res)


def re_search():
    
    # path_to_search = "c:\example\task\new"
    target_string = r"c:\example\task\new\exercises\session404"

    # regex pattern
   
    # \n and \t has a special meaning in Python
    # Python will treat them differently

    print("with raw string:")
    pattern = r"^c:\\example\\task\\new"
    res = re.search(pattern, target_string)
    print(res.group())

    print("without raw string:")
    pattern = "^c:\\example\\task\\new"
    res = re.search(pattern, target_string)
    print(res.group())
    


if __name__ == "__main__":
    #re_finall()
    re_search()
