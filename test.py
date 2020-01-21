#!/usr/bin/env python3

import unittest


from api import SquadApi
from models import Squad, Group, Project, Build, TestJob, TestRun, Test, Suite, Environment, Backend, EmailTemplate, KnownIssue, SuiteMetadata, Annotation, MetricThreshold, Report

SquadApi.configure(url='http://localhost:8000')


class SquadTest(unittest.TestCase):

    def setUp(self):
        self.squad = Squad()

    def test_groups(self):
        groups = self.squad.groups()
        self.assertTrue(True, len(groups))

    def test_groups_with_count(self):
        four_groups = self.squad.groups(count=4)
        self.assertEqual(4, len(four_groups))

    def test_group(self):
        lkft_group = self.squad.group('lkft')
        self.assertTrue(lkft_group is not None)

    def test_projects(self):
        projects = self.squad.projects()
        self.assertTrue(True, len(projects))

    def test_builds(self):
        builds = self.squad.builds()
        self.assertTrue(True, len(builds))

    def test_testjobs(self):
        testjobs = self.squad.testjobs()
        self.assertTrue(True, len(testjobs))

    def test_testruns(self):
        testruns = self.squad.testruns()
        self.assertTrue(True, len(testruns))

    def test_tests(self):
        tests = self.squad.tests()
        self.assertTrue(True, len(tests))

    def test_suites(self):
        suites = self.squad.suites()
        self.assertTrue(True, len(suites))

    def test_environments(self):
        environments = self.squad.environments()
        self.assertTrue(True, len(environments))

    def test_backends(self):
        backends = self.squad.backends()
        self.assertTrue(True, len(backends))

    def test_emailtemplates(self):
        emailtemplates = self.squad.emailtemplates()
        self.assertTrue(True, len(emailtemplates))

    def test_knownissues(self):
        knownissues = self.squad.knownissues()
        self.assertTrue(True, len(knownissues))

    def test_suitemetadata(self):
        suitemetadata = self.squad.suitemetadata()
        self.assertTrue(True, len(suitemetadata))

    def test_annotations(self):
        annotations = self.squad.annotations()
        self.assertTrue(True, len(annotations))

    def test_metricthresholds(self):
        metricthresholds = self.squad.metricthresholds()
        self.assertTrue(True, len(metricthresholds))

    def test_reports(self):
        reports = self.squad.reports()
        self.assertTrue(True, len(reports))


if __name__ == '__main__':
    unittest.main()
