from first_package import normalize_emails


class TestNormalizeEmails:
    def test_normalize_emails(self):
        emails = ["test@example.com", "Test@Example.com", "TEST@EXAMPLE.COM"]
        expected = ["test@example.com", "test@example.com", "test@example.com"]
        assert normalize_emails.normalize(emails) == expected
