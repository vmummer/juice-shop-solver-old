#!/usr/bin/env python
#
# 8/21/22 Added option to change server via cli - vincem@checkpoint.com
import sys

#set default server to http://localhost:3000
if len(sys.argv) == 1: sys.argv[1:] = ["http://localhost:3000"]


from authentication import get_admin_session
from browser import solve_browser_challenges
from feedback import solve_feedback_challenges
from filehandling import solve_file_handling_challenges
from misc import solve_misc_challenges
from products import solve_product_challenges
from users import solve_user_challenges

#server = 'http://localhost:3000'
server = sys.argv[1]
print("Website: " +server)
session = get_admin_session(server)
solve_file_handling_challenges(server)
solve_user_challenges(server)
solve_feedback_challenges(server)
solve_product_challenges(server)
solve_misc_challenges(server)
# Selenium-based - comment out the below if you don't have the Chromedriver set up.
solve_browser_challenges(server)
