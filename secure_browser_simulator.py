from stack import Stack


class SecureBrowserSimulator:
    def __init__(self):
        self.forward = Stack()
        self.backward = Stack()
        self.current_page = None
        self.security_alert = []
        self.malicious_domains = {"badsite.com",
                                  "phishing-login.net",
                                  "secure-update.xyz",
                                  "account-verify.ru",
                                  "free-prize.tk",
                                  "login-alert.cn",
                                  "banking-security-check.com"}
        self.malicious_keywords = {"login",
                                   "verify",
                                   "password",
                                   "account",
                                   "urgent",
                                   "free",
                                   "prize",
                                   "phishing"}

    # Visit a new URL and check it for malicious indicators
    def visit_url(self, url):
        # If there is a current page, push it to the back stack
        if self.current_page:
            self.backward.push(self.current_page)
        self.current_page = url   # Set the new URL as the current page
        self.forward = Stack()    # Clear the forward stack
        # Check if the visited URL is malicious
        if self.is_malicious(url):
            # Create an alert message that includes the malicious URL
            alert = f"WARNING: Malicious URL Detected {url}"
            # Store the alert in the security_alert list so it can be viewed later
            self.security_alert.append(alert)
            # Immediately notify the user that the URL is malicious
            print(alert)

    def is_malicious(self, url):
       # Changes the url to lowercase
       url = url.lower()
       # Loops through the set of malicious domains
       for domain in self.malicious_domains:
          # If the malicious domain is in the url
          if domain in url:
             # Return statement
             return True
       # Loops through the set of malicious keywords
       for keyword in self.malicious_keywords:
          # If the malicious keyword is in the url
          if keyword in url:
             # Return Statement
             return True
       # If none of the conditions are met, returns False
       return False

    def go_back(self):
        # To push current page to the foward stack
        if not self.backward.is_empty():
            self.forward.push(self.current_page)
            # To Pop from back stack and set current page
            self.current_page = self.backward.pop()
            print("current Page:", self.current_page)
            # To see if backstack is empty
        if self.backward.is_empty():
            print("No History")

    def forward_navigation(self):
        # Check if there is a page to navigate forward to
        if not self.forward.is_empty():
            # Move the current page to the backward stack and
            #  set the current page to the top of the forward stack
            self.backward.push(self.current_page)
            self.current_page = self.forward.pop()
            # Print the current page after navigating forward
            print(f"current page: {self.current_page}")
        else:
            # If there are no pages to navigate forward to, print a message
            print("No History.")

    def show_history(self):
        print("===Browser History===")

        print("Back Stack")
    # If the back stack is not empty, print it
        if not self.backward.is_empty():
            print(self.backward)
    # If the back stack is empty, print "No History"
        else:
            print("[No History]")

        print("Current Page")
    # Prints the current page if one exists
        if self.current_page:
            print(self.current_page)
    # If there is not a current page, print "None"
        else:
            print("[None]")

        print("Forward Stack")
    # Prints the forward stack if it is not empty
        if not self.forward.is_empty():
            print(self.forward)
    # If the forward stack is empty, print "None"
        else:
            print("[None]")

    def show_alerts(self):
        # Print title for the alerts section
        print("=== Security Alerts ===")

        # Check if no alerts have been stored
        if not self.security_alert:
            print("No alerts detected.")
        else:
            # Loop through each stored alert and print it
            for alert in self.security_alert:
                print(alert)


def main():
    browser = SecureBrowserSimulator()

    while True:
        command = input(
            "visit (Then type the url)\n"
            "back\n"
            "forward\n"
            "history\n"
            "alerts\n"
            "exit\n"
            "Enter command: "
        ).strip()

        if command == "exit":
            break

        elif command.startswith("visit "):
            url = command[6:]
            browser.visit_url(url)

        elif command == "back":
            browser.go_back()

        elif command == "forward":
            browser.forward_navigation()

        elif command == "history":
            browser.show_history()

        elif command == "alerts":
            browser.show_alerts()

        else:
            print("Invalid command")


if __name__ == "__main__":
    main()
