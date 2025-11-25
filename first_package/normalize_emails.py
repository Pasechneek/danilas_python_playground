def normalize(emails: list):
    for i in range(0, len(emails)):
        email = emails[i]
        normalized_email = email.lower()
        emails[i] = normalized_email
    return emails
