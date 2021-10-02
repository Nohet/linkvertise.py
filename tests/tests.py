from linkvertise.client.app import LinkvertiseClient

# Defining the client
client = LinkvertiseClient()

# Creating a linkvertise url, and printing it
# 25565 is your linkvertise account id, and,
# google.com is link to monetize.
link = client.linkvertise(25565, "google.com")
print(link)

# Returns https://link-to.net/25565/832.3652483894998/dynamic?r=Z29vZ2xlLmNvbQ==
