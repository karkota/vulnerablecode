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
from unittest import TestCase
from unittest.mock import patch

from packageurl import PackageURL

from vulnerabilities.helpers import AffectedPackage
from vulnerabilities.importer import Advisory
from vulnerabilities.importer import Reference
from vulnerabilities.importers.apache_tomcat import ApacheTomcatImporter
from vulnerabilities.package_managers import MavenVersionAPI
from vulnerabilities.package_managers import Version

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TEST_DATA = os.path.join(BASE_DIR, "test_data", "apache_tomcat", "security-9.html")


class TestApacheTomcatImporter(TestCase):
    @classmethod
    def setUpClass(cls):
        data_source_cfg = {"etags": {}}
        mock_api = MavenVersionAPI(
            cache={
                "org.apache.tomcat:tomcat": [
                    Version("9.0.0.M1"),
                    Version("9.0.0.M2"),
                    Version("8.0.0.M1"),
                    Version("6.0.0M2"),
                ]
            }
        )
        with patch("vulnerabilities.importers.apache_tomcat.MavenVersionAPI"):
            with patch("vulnerabilities.importers.apache_tomcat.asyncio"):
                cls.data_src = ApacheTomcatImporter(1, config=data_source_cfg)
        cls.data_src.version_api = mock_api

    def test_to_advisories(self):
        expected_advisories = [
            Advisory(
                summary="",
                vulnerability_id="CVE-2015-5351",
                affected_packages=[
                    AffectedPackage(
                        vulnerable_package=PackageURL(
                            type="maven",
                            namespace="apache",
                            name="tomcat",
                            version="8.0.0.M1",
                            qualifiers={},
                            subpath=None,
                        ),
                        patched_package=PackageURL(
                            type="maven",
                            namespace="apache",
                            name="tomcat",
                            version="9.0.0.M3",
                            qualifiers={},
                            subpath=None,
                        ),
                    ),
                    AffectedPackage(
                        vulnerable_package=PackageURL(
                            type="maven",
                            namespace="apache",
                            name="tomcat",
                            version="9.0.0.M1",
                        ),
                        patched_package=PackageURL(
                            type="maven",
                            namespace="apache",
                            name="tomcat",
                            version="9.0.0.M3",
                        ),
                    ),
                    AffectedPackage(
                        vulnerable_package=PackageURL(
                            type="maven",
                            namespace="apache",
                            name="tomcat",
                            version="9.0.0.M2",
                        ),
                        patched_package=PackageURL(
                            type="maven",
                            namespace="apache",
                            name="tomcat",
                            version="9.0.0.M3",
                        ),
                    ),
                ],
                references=[
                    Reference(
                        reference_id="",
                        url="http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2015-5351",
                        severities=[],
                    ),
                    Reference(
                        reference_id="",
                        url="https://svn.apache.org/viewvc?view=rev&rev=1720652",
                        severities=[],
                    ),
                    Reference(
                        reference_id="",
                        url="https://svn.apache.org/viewvc?view=rev&rev=1720655",
                        severities=[],
                    ),
                ],
            ),
            Advisory(
                summary="",
                vulnerability_id="CVE-2016-0706",
                affected_packages=[
                    AffectedPackage(
                        vulnerable_package=PackageURL(
                            type="maven",
                            namespace="apache",
                            name="tomcat",
                            version="9.0.0.M1",
                        ),
                        patched_package=PackageURL(
                            type="maven",
                            namespace="apache",
                            name="tomcat",
                            version="9.0.0.M3",
                        ),
                    )
                ],
                references=[
                    Reference(
                        reference_id="",
                        url="http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2016-0706",
                        severities=[],
                    ),
                    Reference(
                        reference_id="",
                        url="https://svn.apache.org/viewvc?view=rev&rev=1722799",
                        severities=[],
                    ),
                ],
            ),
            Advisory(
                summary="",
                vulnerability_id="CVE-2016-0714",
                affected_packages={},
                references=[
                    Reference(
                        reference_id="",
                        url="http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2016-0714",
                        severities=[],
                    ),
                    Reference(
                        reference_id="",
                        url="https://svn.apache.org/viewvc?view=rev&rev=1725263",
                        severities=[],
                    ),
                    Reference(
                        reference_id="",
                        url="https://svn.apache.org/viewvc?view=rev&rev=1725914",
                        severities=[],
                    ),
                ],
            ),
            Advisory(
                summary="",
                vulnerability_id="CVE-2016-0763",
                affected_packages=[
                    AffectedPackage(
                        vulnerable_package=PackageURL(
                            type="maven",
                            namespace="apache",
                            name="tomcat",
                            version="9.0.0.M1",
                        ),
                        patched_package=PackageURL(
                            type="maven",
                            namespace="apache",
                            name="tomcat",
                            version="9.0.0.M3",
                        ),
                    ),
                    AffectedPackage(
                        vulnerable_package=PackageURL(
                            type="maven",
                            namespace="apache",
                            name="tomcat",
                            version="9.0.0.M2",
                        ),
                        patched_package=PackageURL(
                            type="maven",
                            namespace="apache",
                            name="tomcat",
                            version="9.0.0.M3",
                        ),
                    ),
                ],
                references=[
                    Reference(
                        reference_id="",
                        url="http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2016-0763",
                        severities=[],
                    ),
                    Reference(
                        reference_id="",
                        url="https://svn.apache.org/viewvc?view=rev&rev=1725926",
                        severities=[],
                    ),
                ],
            ),
        ]

        with open(TEST_DATA) as f:
            found_advisories = self.data_src.to_advisories(f)

        found_advisories = list(map(Advisory.normalized, found_advisories))
        expected_advisories = list(map(Advisory.normalized, expected_advisories))
        assert sorted(found_advisories) == sorted(expected_advisories)
