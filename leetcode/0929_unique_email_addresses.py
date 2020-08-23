"""
Every email consists of a local name and a domain name, separated by the @ sign. For example, in alice@leetcode.com, 
alice is the local name, and leetcode.com is the domain name. Besides lowercase letters, these emails may contain 
'.'s or '+'s. If you add periods ('.') between some characters in the local name part of an email address, mail sent 
there will be forwarded to the same address without dots in the local name. For example, "alice.z@leetcode.com" and 
"alicez@leetcode.com" forward to the same email address. (Note that this rule does not apply for domain names.) If you 
add a plus ('+') in the local name, everything after the first plus sign will be ignored. This allows certain emails to 
be filtered, for example m.y+name@email.com will be forwarded to my@email.com. (Again, this rule does not apply for 
domain names.) It is possible to use both of these rules at the same time. Given a list of emails, we send one email to 
each address in the list. How many different addresses actually receive mails? 

Example 1:

    Input: ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
    Output: 2
    Explanation: "testemail@leetcode.com" and "testemail@lee.tcode.com" actually receive mails

Note:
    1. 1 <= emails[i].length <= 100
    2. 1 <= emails.length <= 100
    3. Each emails[i] contains exactly one '@' character.
    4. All local and domain names are non-empty.
    5. Local names do not start with a '+' character.
"""


class Solution:
    def numUniqueEmails1(self, emails):
        def helper(email):
            res, i = [], 0
            while i < len(email):
                s = email[i]
                if s.isalnum():
                    res.append(s)
                elif s == '+':
                    while email[i+1] != '@':
                        i += 1
                elif s == '@':
                    res.append(email[i:])
                    break

                i += 1

            return ''.join(res)

        return len(set(helper(x) for x in emails))

    def numUniqueEmails2(self, emails):
        def helper(email):
            loc, dom = email.split('@')
            loc = loc.replace('.', '')
            if '+' in loc:
                return loc[:loc.index('+')] + '@' + dom
            else:
                return loc + '@' + dom
        
        return len(set(helper(x) for x in emails))
