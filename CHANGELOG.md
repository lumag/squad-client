# 0.9.1

This 0.9.1 release fixes a small bug and changes tuxbuild submission
slightly.

Complete list of changes going in:

* Remove the arch from the test name when using tuxbuild json
* Gracefully handle some tuxbuild json config errors
* Do not show the hash for an empty kconfig

# 0.9

This 0.9 release adds support for TuxBuild input for submitting test results
to SQUAD.

Complete list of changes going in:

* Add an option to the submit command that allows the submission of tuxbuild json result files
* Fix a file extension check error message
* Allow the verbose flag to be used when running specific tests
* tests: fixtures: fix fixtures to work along with recent squad changes
* core: models: query tests in Suite class
* commands: fix submit command docs

# 0.8.1

This 0.8.1 release just turns the featured added in 0.8 into a command line.
It makes possible to create or update a project using command line arguments.

Complete list of changes going in:

* commands: add create_or_update_project command
* shortcuts: add create_or_update_project shortcut

# 0.8

This 0.8 release fixes the number of suites retrieved in build_report
and allow users to create projects using the client. A newer version
will come in quickly allowing all models to be created/deleted.

Complete list of changes going in:

core: models allow project creation
examples: fix suite retrieval in build_report.py

# 0.7

This 0.7 release adds a method in project to fetch its environments
among other minor bug fixes.

The release also changes the home of squad-client docker image to
squadproject/squad-client.

Complete list of changes below:

* add methods to fetch environments from a project
* change the attribute from complete to finished
* core: models: add nested endpoints to models
* examples: fix URL in build_report
* fix the example for filtering on finished builds
* manage: avoid configuring api when running tests
* release: change docker repo to squadproject


# 0.6

This 0.6 release adds basic caching for fetching data. It also adds
support for fetching metrics and a shortcut for comparing two builds
from the same project.

Complete list of changes below:

* core:
  * api: ignore netrc auth
  * models: add metrics
  * models: add suite do project model
  * models: fix metrics and testrun status endpoints
  * shortcuts: add shortcut to compare builds
* manage: add basic caching
* shortcuts: return exit code of submit operation
* tests: add test for submit_results return value

# 0.5

This release includes many new additions and bug fixes to
work in sync with SQUAD.

The example build report template has been improved and anonymized
for genereric use.

A new command `./manage.py submit` has been added to allow
users to submit results to SQUAD backend by simply passing
results files. It still missing on attachments but will be
added in near future.
work in sync with SQUAD.

The example build report template has been improved and anonymized
for genereric use.

A new command `./manage.py submit` has been added to allow
users to submit results to SQUAD backend by simply passing
results files. It still missing on attachments but will be
added in near future.

Better testing has been implemeted. There's a squad instance
running on the fly, meaning tests are run against a real
squad instance, instead of basic mocking.

Complete list of changes below:

* commands:
  * add submit results
  * shell: add missing import
  * submit: fix bugs
  * test: return test result code
* core:
  * api: add helpful message on 500 errors
  * api: improve credentials handling
  * models: fix small bugs and add helpful messages
  * models: update metricthreshold to use env
  * models: use testrun status endpoint
* examples:
  * build_report: add free text form from params
  * rename schneider report
  * schneider_template: add links to tests
  * schneider_template: anonymize template
  * schneider_template: fix tabs and tr tags
* manage:
  * configure basic logging
  * exit with proper exit code
  * handle credentials before subcommands
  * make squad-host mandatory in environment
* tests:
  * add flake8 check
  * add tests for submit command
  * remove configurarion of the api before running tests
  * remove test_squad_service.py to speed up testing
  * start local squad server to support testing
  * test_api: add auth test
* misc:
  * fix the import paths for some docs and examples
  * reports: improve generic reports
  * setup.py: make squad-client program name shorter
  * shortcuts: add submit_results shortcut
  * travis: add travis file

# 0.4

This release improves basic report generation for Schneider project

# 0.3

This release make changes Dockerfile to make it better to
run squad-client in docker.

# 0.2

This release automates build of squad-client docker image
and pushes it to docker hub.

Complete list of changes below:
* release: build and push docker image as well

# 0.1

Initial Squad-Client release
