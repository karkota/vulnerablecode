# Copyright (c) nexB Inc. and others. All rights reserved.
# VulnerableCode is a trademark of nexB Inc.
#
# SPDX-License-Identifier: Apache-2.0 AND CC-BY-4.0
#
# VulnerableCode software is licensed under the Apache License version 2.0.
# VulnerableCode data is licensed collectively under CC-BY-4.0.
#
# See https://www.apache.org/licenses/LICENSE-2.0 for the Apache-2.0 license text.
# See https://creativecommons.org/licenses/by/4.0/legalcode for the CC-BY-4.0 license text.
#
# See https://github.com/nexB/vulnerablecode for support or download.
# See https://aboutcode.org for more information about nexB OSS projectsfrom pathlib import Path

import os
import unittest
from collections import OrderedDict

from packageurl import PackageURL

from vulnerabilities.helpers import AffectedPackage
from vulnerabilities.importer import Advisory
from vulnerabilities.importer import Reference
from vulnerabilities.importers.openssl import OpenSSLImporter

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TEST_DATA = os.path.join(BASE_DIR, "test_data/", "openssl_xml_data.xml")


def load_test_data():
    with open(TEST_DATA) as f:
        return f.read()


class TestOpenSSL(unittest.TestCase):
    def test_to_advisory(self):
        data = load_test_data()
        expected_advisories = [
            Advisory(
                summary='Server or client applications that call the SSL_check_chain() function during or after a TLS 1.3 handshake may crash due to a NULL pointer dereference as a result of incorrect handling of the "signature_algorithms_cert" TLS extension. The crash occurs if an invalid or unrecognised signature algorithm is received from the peer. This could be exploited by a malicious peer in a Denial of Service attack. OpenSSL version 1.1.1d, 1.1.1e, and 1.1.1f are affected by this issue. This issue did not affect OpenSSL versions prior to 1.1.1d.',
                vulnerability_id="CVE-2020-1967",
                affected_packages=[
                    AffectedPackage(
                        vulnerable_package=PackageURL(
                            type="generic",
                            namespace=None,
                            name="openssl",
                            version="1.1.1d",
                        ),
                        patched_package=PackageURL(
                            type="generic",
                            namespace=None,
                            name="openssl",
                            version="1.1.1g",
                        ),
                    ),
                    AffectedPackage(
                        vulnerable_package=PackageURL(
                            type="generic",
                            namespace=None,
                            name="openssl",
                            version="1.1.1e",
                        ),
                        patched_package=PackageURL(
                            type="generic",
                            namespace=None,
                            name="openssl",
                            version="1.1.1g",
                        ),
                    ),
                    AffectedPackage(
                        vulnerable_package=PackageURL(
                            type="generic",
                            namespace=None,
                            name="openssl",
                            version="1.1.1f",
                        ),
                        patched_package=PackageURL(
                            type="generic",
                            namespace=None,
                            name="openssl",
                            version="1.1.1g",
                        ),
                    ),
                ],
                references=[
                    Reference(
                        reference_id="",
                        url="https://github.com/openssl/openssl/commit/eb563247aef3e83dda7679c43f9649270462e5b1",
                        severities=[],
                    )
                ],
            ),
            Advisory(
                summary="There is an overflow bug in the x64_64 Montgomery squaring procedure used in exponentiation with 512-bit moduli. No EC algorithms are affected. Analysis suggests that attacks against 2-prime RSA1024, 3-prime RSA1536, and DSA1024 as a result of this defect would be very difficult to perform and are not believed likely. Attacks against DH512 are considered just feasible. However, for an attack the target would have to re-use the DH512 private key, which is not recommended anyway. Also applications directly using the low level API BN_mod_exp may be affected if they use BN_FLG_CONSTTIME.",
                vulnerability_id="CVE-2019-1551",
                affected_packages=[
                    AffectedPackage(
                        vulnerable_package=PackageURL(
                            type="generic",
                            namespace=None,
                            name="openssl",
                            version="1.0.2",
                        ),
                        patched_package=PackageURL(
                            type="generic",
                            namespace=None,
                            name="openssl",
                            version="1.1.1e",
                        ),
                    ),
                    AffectedPackage(
                        vulnerable_package=PackageURL(
                            type="generic",
                            namespace=None,
                            name="openssl",
                            version="1.0.2a",
                        ),
                        patched_package=PackageURL(
                            type="generic",
                            namespace=None,
                            name="openssl",
                            version="1.0.2u",
                        ),
                    ),
                    AffectedPackage(
                        vulnerable_package=PackageURL(
                            type="generic",
                            namespace=None,
                            name="openssl",
                            version="1.0.2b",
                        ),
                        patched_package=PackageURL(
                            type="generic",
                            namespace=None,
                            name="openssl",
                            version="1.0.2u",
                        ),
                    ),
                    AffectedPackage(
                        vulnerable_package=PackageURL(
                            type="generic",
                            namespace=None,
                            name="openssl",
                            version="1.0.2c",
                        ),
                        patched_package=PackageURL(
                            type="generic",
                            namespace=None,
                            name="openssl",
                            version="1.0.2u",
                        ),
                    ),
                    AffectedPackage(
                        vulnerable_package=PackageURL(
                            type="generic",
                            namespace=None,
                            name="openssl",
                            version="1.0.2d",
                        ),
                        patched_package=PackageURL(
                            type="generic",
                            namespace=None,
                            name="openssl",
                            version="1.0.2u",
                        ),
                    ),
                    AffectedPackage(
                        vulnerable_package=PackageURL(
                            type="generic",
                            namespace=None,
                            name="openssl",
                            version="1.0.2e",
                        ),
                        patched_package=PackageURL(
                            type="generic",
                            namespace=None,
                            name="openssl",
                            version="1.0.2u",
                        ),
                    ),
                    AffectedPackage(
                        vulnerable_package=PackageURL(
                            type="generic",
                            namespace=None,
                            name="openssl",
                            version="1.0.2f",
                        ),
                        patched_package=PackageURL(
                            type="generic",
                            namespace=None,
                            name="openssl",
                            version="1.0.2u",
                        ),
                    ),
                    AffectedPackage(
                        vulnerable_package=PackageURL(
                            type="generic",
                            namespace=None,
                            name="openssl",
                            version="1.0.2g",
                        ),
                        patched_package=PackageURL(
                            type="generic",
                            namespace=None,
                            name="openssl",
                            version="1.0.2u",
                        ),
                    ),
                    AffectedPackage(
                        vulnerable_package=PackageURL(
                            type="generic",
                            namespace=None,
                            name="openssl",
                            version="1.0.2h",
                        ),
                        patched_package=PackageURL(
                            type="generic",
                            namespace=None,
                            name="openssl",
                            version="1.0.2u",
                        ),
                    ),
                    AffectedPackage(
                        vulnerable_package=PackageURL(
                            type="generic",
                            namespace=None,
                            name="openssl",
                            version="1.0.2i",
                        ),
                        patched_package=PackageURL(
                            type="generic",
                            namespace=None,
                            name="openssl",
                            version="1.0.2u",
                        ),
                    ),
                    AffectedPackage(
                        vulnerable_package=PackageURL(
                            type="generic",
                            namespace=None,
                            name="openssl",
                            version="1.0.2j",
                        ),
                        patched_package=PackageURL(
                            type="generic",
                            namespace=None,
                            name="openssl",
                            version="1.0.2u",
                        ),
                    ),
                    AffectedPackage(
                        vulnerable_package=PackageURL(
                            type="generic",
                            namespace=None,
                            name="openssl",
                            version="1.0.2k",
                        ),
                        patched_package=PackageURL(
                            type="generic",
                            namespace=None,
                            name="openssl",
                            version="1.0.2u",
                        ),
                    ),
                    AffectedPackage(
                        vulnerable_package=PackageURL(
                            type="generic",
                            namespace=None,
                            name="openssl",
                            version="1.0.2l",
                        ),
                        patched_package=PackageURL(
                            type="generic",
                            namespace=None,
                            name="openssl",
                            version="1.0.2u",
                        ),
                    ),
                    AffectedPackage(
                        vulnerable_package=PackageURL(
                            type="generic",
                            namespace=None,
                            name="openssl",
                            version="1.0.2m",
                        ),
                        patched_package=PackageURL(
                            type="generic",
                            namespace=None,
                            name="openssl",
                            version="1.0.2u",
                        ),
                    ),
                    AffectedPackage(
                        vulnerable_package=PackageURL(
                            type="generic",
                            namespace=None,
                            name="openssl",
                            version="1.0.2n",
                        ),
                        patched_package=PackageURL(
                            type="generic",
                            namespace=None,
                            name="openssl",
                            version="1.0.2u",
                        ),
                    ),
                    AffectedPackage(
                        vulnerable_package=PackageURL(
                            type="generic",
                            namespace=None,
                            name="openssl",
                            version="1.0.2o",
                        ),
                        patched_package=PackageURL(
                            type="generic",
                            namespace=None,
                            name="openssl",
                            version="1.0.2u",
                        ),
                    ),
                    AffectedPackage(
                        vulnerable_package=PackageURL(
                            type="generic",
                            namespace=None,
                            name="openssl",
                            version="1.0.2p",
                        ),
                        patched_package=PackageURL(
                            type="generic",
                            namespace=None,
                            name="openssl",
                            version="1.0.2u",
                        ),
                    ),
                    AffectedPackage(
                        vulnerable_package=PackageURL(
                            type="generic",
                            namespace=None,
                            name="openssl",
                            version="1.0.2q",
                        ),
                        patched_package=PackageURL(
                            type="generic",
                            namespace=None,
                            name="openssl",
                            version="1.0.2u",
                        ),
                    ),
                    AffectedPackage(
                        vulnerable_package=PackageURL(
                            type="generic",
                            namespace=None,
                            name="openssl",
                            version="1.0.2r",
                        ),
                        patched_package=PackageURL(
                            type="generic",
                            namespace=None,
                            name="openssl",
                            version="1.0.2u",
                        ),
                    ),
                    AffectedPackage(
                        vulnerable_package=PackageURL(
                            type="generic",
                            namespace=None,
                            name="openssl",
                            version="1.0.2s",
                        ),
                        patched_package=PackageURL(
                            type="generic",
                            namespace=None,
                            name="openssl",
                            version="1.0.2u",
                        ),
                    ),
                    AffectedPackage(
                        vulnerable_package=PackageURL(
                            type="generic",
                            namespace=None,
                            name="openssl",
                            version="1.0.2t",
                        ),
                        patched_package=PackageURL(
                            type="generic",
                            namespace=None,
                            name="openssl",
                            version="1.0.2u",
                        ),
                    ),
                    AffectedPackage(
                        vulnerable_package=PackageURL(
                            type="generic",
                            namespace=None,
                            name="openssl",
                            version="1.1.1",
                        ),
                        patched_package=None,
                    ),
                    AffectedPackage(
                        vulnerable_package=PackageURL(
                            type="generic",
                            namespace=None,
                            name="openssl",
                            version="1.1.1a",
                        ),
                        patched_package=PackageURL(
                            type="generic",
                            namespace=None,
                            name="openssl",
                            version="1.1.1e",
                        ),
                    ),
                    AffectedPackage(
                        vulnerable_package=PackageURL(
                            type="generic",
                            namespace=None,
                            name="openssl",
                            version="1.1.1b",
                        ),
                        patched_package=PackageURL(
                            type="generic",
                            namespace=None,
                            name="openssl",
                            version="1.1.1e",
                        ),
                    ),
                    AffectedPackage(
                        vulnerable_package=PackageURL(
                            type="generic",
                            namespace=None,
                            name="openssl",
                            version="1.1.1c",
                        ),
                        patched_package=PackageURL(
                            type="generic",
                            namespace=None,
                            name="openssl",
                            version="1.1.1e",
                        ),
                    ),
                    AffectedPackage(
                        vulnerable_package=PackageURL(
                            type="generic",
                            namespace=None,
                            name="openssl",
                            version="1.1.1d",
                        ),
                        patched_package=PackageURL(
                            type="generic",
                            namespace=None,
                            name="openssl",
                            version="1.1.1e",
                        ),
                    ),
                ],
                references=[
                    Reference(
                        reference_id="",
                        url="https://github.com/openssl/openssl/commit/419102400a2811582a7a3d4a4e317d72e5ce0a8f",
                        severities=[],
                    ),
                    Reference(
                        reference_id="",
                        url="https://github.com/openssl/openssl/commit/f1c5eea8a817075d31e43f5876993c6710238c98",
                        severities=[],
                    ),
                ],
            ),
        ]

        found_advisories = OpenSSLImporter.to_advisories(data)

        found_advisories = list(map(Advisory.normalized, found_advisories))
        expected_advisories = list(map(Advisory.normalized, expected_advisories))
        assert sorted(found_advisories) == sorted(expected_advisories)
