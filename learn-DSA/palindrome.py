import string

def longestPalindrome(s):
    """
    :type s: str
    :rtype: int
    """
    co = [s.count(let) for let in string.ascii_lowercase]
    rec = []
    for _ in co :
        if _ % 2 != 0:
            _ = _ -1
        rec.append(_)
    if 1 in co:
        return sum(rec)+1
    else:
        return sum(rec)

if __name__ == '__main__':
    print (longestPalindrome(s='ccc'))
