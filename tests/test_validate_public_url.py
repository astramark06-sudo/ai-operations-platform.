"""Unit tests for public audit target validation."""

from __future__ import annotations

import socket
import unittest
from unittest.mock import patch

from scripts.validate_public_url import validate_public_https_url


def dns_record(address: str) -> tuple:
    family = socket.AF_INET6 if ":" in address else socket.AF_INET
    return (family, socket.SOCK_STREAM, 6, "", (address, 443))


class PublicUrlValidationTests(unittest.TestCase):
    @patch("scripts.validate_public_url.socket.getaddrinfo", return_value=[dns_record("93.184.216.34")])
    def test_accepts_public_https_hostname(self, _lookup: object) -> None:
        validate_public_https_url("https://example.com/path?view=full")

    def test_accepts_public_ip_literal(self) -> None:
        validate_public_https_url("https://1.1.1.1/audit")

    def test_rejects_http(self) -> None:
        with self.assertRaisesRegex(ValueError, "only HTTPS"):
            validate_public_https_url("http://example.com")

    def test_rejects_missing_hostname(self) -> None:
        with self.assertRaises(ValueError):
            validate_public_https_url("https:///missing-host")

    def test_rejects_embedded_credentials(self) -> None:
        with self.assertRaisesRegex(ValueError, "credentials"):
            validate_public_https_url("https://user:secret@example.com")

    def test_rejects_non_default_port(self) -> None:
        with self.assertRaisesRegex(ValueError, "port"):
            validate_public_https_url("https://example.com:8443")

    def test_rejects_local_hostname(self) -> None:
        with self.assertRaisesRegex(ValueError, "local"):
            validate_public_https_url("https://service.local")

    def test_rejects_private_ip_literal(self) -> None:
        with self.assertRaisesRegex(ValueError, "non-public"):
            validate_public_https_url("https://192.168.1.10")

    @patch("scripts.validate_public_url.socket.getaddrinfo", return_value=[dns_record("127.0.0.1")])
    def test_rejects_hostname_resolving_to_loopback(self, _lookup: object) -> None:
        with self.assertRaisesRegex(ValueError, "non-public"):
            validate_public_https_url("https://example.com")

    @patch(
        "scripts.validate_public_url.socket.getaddrinfo",
        return_value=[dns_record("93.184.216.34"), dns_record("10.0.0.8")],
    )
    def test_rejects_mixed_public_and_private_dns_answers(self, _lookup: object) -> None:
        with self.assertRaisesRegex(ValueError, "non-public"):
            validate_public_https_url("https://example.com")

    @patch("scripts.validate_public_url.socket.getaddrinfo", side_effect=socket.gaierror("no DNS"))
    def test_rejects_unresolvable_hostname(self, _lookup: object) -> None:
        with self.assertRaisesRegex(ValueError, "did not resolve"):
            validate_public_https_url("https://not-resolvable.example")

    def test_rejects_whitespace_and_backslashes(self) -> None:
        for value in (" https://example.com", "https://example.com/path with space", "https://example.com\\@127.0.0.1"):
            with self.subTest(value=value), self.assertRaises(ValueError):
                validate_public_https_url(value)


if __name__ == "__main__":
    unittest.main()
