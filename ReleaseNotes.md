# The ReleaseNotes file

Contains a list of the released versions with a summary of the main changes in each version.


# Beta Releases

# v2.1-Beta
- June 2016

Minor release with significant bugfixes, new services and explorations of centos7

New services:
* We have added a new implementation of Ganglia to our stack, separate from the old
  HDP implementation. This is optional and can be used in the interim period while
  Ambari Metrics grows in maturity.

Minor improvements:
* Update to Ambari 2.2.2, bringing Grafana and other minor fixes
* Further code style fixes and additional unit tests
* Improvements in deployment libraries for stability

Minor improvements in services:
* Move forward to Java 1.8 consistently across all services
* HUE allow configuration of service username
* Move up to KaveToolbox v 2.1-Beta (described elsewhere)

Bugfixes in services:
* epel repo seems not very stable recently, yum clean all seems to solve most issues
* FreeIPA:
    - says install was successful in the client even when it failed actually
    - FreeIPA now supports domain names up to 61 characters (experimental patch)
    - resolv.conf overwriting now only occurs on successful client install
* KaveLanding:
    - KaveLanding now supports modified ambari password correctly
* Archiva:
	- Re-installation is now possible with limited cleanup, small changes in properties

Bugfixes in installer:
* No longer breaks with local directory in /etc/kave/mirror file
* New methods to check pdsh version compatibility
* Checkout/wget into temporary directory for cleanliness

Centos7:
* We have begun to test KAVE on the Centos7 operating system.
  In version 2.1 Centos6 is still the only supported os,
  but several of the basic services already deploy on Centos7.
  In the near future we intend to supply a version which also
  supports Centos7.
* We have already fixed several issues in
  the installer, Apache, deployment library, Sonar, FreeIPA
* At the moment there are major issues in
  FreeIPA, SonarQube and HUE specific to Centos7.

# v2.0-Beta
- May 2016

* MAJOR release to migrate to the latest Ambari version 2.2.1
* KAVE stack now on top of HDP 2.4 (2.4.KAVE)
* HOTFIX: gitlabs CVE-2016-4340 necessitated a quick hotfix on this version,
  updating gitlabs from 8.6.3 -> 8.7.1 (3rd May)

Major modifications in services:

* MongoDB,
    version increase to MongoDB 3. MongoDB 3 is not 100% backwards compatible
* FreeIPA
    Major modifications to how we handle keytabs for kerberos.
    During the kerberization of your cluster with Ambari, you can download a
    kerberos.csv containing the list of all keytabs to be created
    With this list, on the ambari node, as the root user:
    - kinit admin
    - createketabs.py kerberos.csv
    Then continue with the wizard through the web interface
    See the wiki and readme for details
    In the new Ambari version we need to distribute the Java Cryptographic Extensions
    into the correct directories before enabling kerberos on the cluster.
    This is now take into account by the FreeIPA client install
* KaveToolbox
    Version update to 2.0-Beta, many changes described separately in the KTB readme
    Most major change: creation of versioned directories
* StormSD
    Added the Storm Logviewer service, an optional service for each node, providing a web
    interface for the storm logs

General improvements:

* Example blueprints and diagrams modified to respect new services
* Tests modified to reduce fragility
* Modifications to installer to improve pdsh and Ambari install with new Ambari version
* Workarounds only necessary for old Ambari versions reviewed and removed
* Check pdsh version and group names during restart\_all\_services.sh script
* addition of resource\_wizard.py script, which naively guesses cluster size requirements

Minor modifications in services:

* MongoDB
    Conf file and repo file now configurable with an InlineTeplate through the web interface
* JBOSS
    In previous versions JBOSS would overwrite the standalone.xml with defaults on restart
    Now the standalone.xml is an InlineTemplate and configurable
* StormSD
    Updated version of Supervisord to v3.X. This new version of supervisord respects import statements
    which makes it a lot easier to configure and does not invoke duplication of code
* SonarQube
    Updated to version 5.4 of the server, only a minor update
* Jenkins: updated to version 1.642
* Gitlabs: updated to version 8.7.1


Bugfixes:

* StormSD
    re-installation of partially completed install fixed.
    installation errors now with better error messages
    installation error when on top of FreeIPA fixed
* JBOSS
    fix removing of users during install
    fix re-installation of partially completed install
* FreeIPA: Installation without DNS fixed


Notes about the new ambari/HDP version:

* Ganglia and Nagios are replaced by AmbariMetrics
  The new HDP assumes the user will install Ganglia/Nagios themselves if needed
* The latest stack requires more RAM on the ambari (+500MB) node and more disk space to run HDP components (+2GB)
* Ranger, Atlas and Falcon, although they have been added are not installable in a simple way
  the installer must install and create specific databases before following the install wizard

# v1.4-Beta
- Jan 2016

* Bugfix release in preparation to migration to Ambari 2.X
* Over 50 independent fixes

General improvements:

* Use Ambari's protected strings feature to hide sensitive strings such as passwords from logs
* Modify test/deployment framework to avoid ever using the ambari password as plain text on the command line
* Review initial passwords across services
* Finalize integration of remaining services with FreeIPA
* Copy a lot of templates into the configuration files, so that the templates are also configurable

New features/improvements in services:

* StormSD:
    Moved to Storm 10.0
* FreeIPA:
    kadm.acl is now configurable through ambari to control the kerberos admin users
    resolv.conf now configurable
 * Gitlab:
    set initial gitlab root admin password based on configurable
 * Sonar:
    Integrate with Host-based access control to centralize user management with FreeIPA
 * MongoDB:
    Replication of datasets is now supported
 * Twiki:
    Integrate with Host-based access control and also LDAP to centralize user management with FreeIPA
* Jenkins:
    set initial jenkins root admin password based on configurable

Bugfixes:

* FreeIPA:
    initial_passwords does not need to be of password type.
    prepare for moving to version 2.X by coping with reading all hosts from all_hosts
* Apache:
    start/stop of Apache services now more reliable
* KaveLanding:
    no longer show false-negative or false-positive running status
* Twiki:
    Fix installation error where PhP is missing
* Packaging script:
    Fix packaging/installation script so that it copes with missing repositories in the mirrors file

Modifications to tests and deployment:

* Improved documentation
* Check for PDSH at start of scripts
* Respect git branches
* Modify example blueprints for latest changes
* New unit tests verify python completeness of files
* More prior checking of blueprints within tests
* Fix creating Centos7 clusters to avoid needing a tty terminal

# v1.3-Beta
- Sept 2015

* Bugfix release in preparation for migration to Ambari 2.X
* Over 50 independent fixes

New features in services:

* KaveToolbox:
    move to 1.3 - Beta(lots of minor improvements), e.g. the ProtectNotebooks.sh script
* KaveToolbox:
    Possibility to customize CustomInstall.py added as configuration parameter
* Hue:
    now integrated with HBAC(host - based access control) and thus also with FreeIPA
* Jenkins:
    Migration to latest stable version
* Jenkins:
    Installer and list of default plugins now cached on our repo server
* FreeIPA:
    you can now specify also a list of sudoers in the initial configuration
* FreeIPA:
    Full usernames(first and last) can now be added through the configuration
* KaveLanding:
    Links are now sorted
* KaveLanding:
    Custom links can be provided
* TWiki:
    HBAC and LDAP access supported, thus integrated with FreeIPA
* All services reviewed to ensure they can be restarted effectively without downloads after installation
* Ambari / clusterHostInfo / can be used to determine most server locations in the cluster

New features in test and deployment framework:

* restart\_all\_services.sh script:
    recovers from most aborted blueprints see the in-built help
* Add check for datetime(ntp) in deploy\_from\_blueprint.py to avoid unknown timing issues for ambari agents
* Default blueprints updated, several spurious parameters no longer need to be specified in current ambari versions
* Slight modification to host authentication in the gitwrap script used for testing
* FDisk part of mount command is now guessed per region, simplifying the test scripts
* In tests, threads now unlock if an exception is thrown
* Small bug in packaging script fixed

Bugfixes:

* TWiki:
    LocalSiteCfg was broken through misapplication of a template
* TWiki:
    different default parameters being required through webUI vs blueprints fixed with defaults
* StormSD:
    Parameters renamed so that the install also works through the web interface
* StormSD:
    Partial fix for multiply writing the same configuration files into supervisord.conf, now less common
* StormSD:
    Start / Stop / Restart methods heavily modified to spawn background processes, otherwise they hung forever
* KaveLanding:
    bootstrap / bower not actually needed in most cases
* KaveLanding:
    removal of duplicate code
* KaveLanding:
    False positive status fixed(see status methods below)
* KaveToolbox:
    --ignore - missing - groups accidentally always applied, new logic added
* KaveToolbox:
    missing git install
* FreeIPA:
    did not declare it's forwarders configuration parameter
* Gitlab:
    Unicorn port(8080) was not configurable leading to port conflicts, fixed
* SonarQube:
    Unused parameters removed
* MongoDB:
    in the case a user - specified and IP address for a mongo server, it was not actually being applied
* Start and Install methods need to both call configure in most cases so that web interface reconfiguring is possible
* Status method needs to throw an exception when service not running
* Start / Stop / Restart methods reviewed especially for backgrounded - services

# v1.2-Beta
- June 2015

* Bugfix release of AmbariKave with over 40 independent fixes
* Thanks to the beta testing program for providing so much feedback

New features in services:

* storm added to the path for all users when storm is installed
* StormSD various parameters such as ports, zookeeper - servers, drpc servers, now allow for comma - separated - lists
* FreeIPA service now has a parameter to set groups, users, and initial user passwords
* FreeIPA now sets default user shell(bash as default, but it is configurable)
* new MONGODB_CLIENT adds mongo libraries for gateway machines
* MONGODB_CLIENT implements mongok script for simpler connectivity(mongok - -help)
* KaveLanding, small changes in website layout and better parsing of list of services

New features in test and deployment framework:

* current branch is now the default in tests
* deploy\_from\_blueprint.py now also creates pdsh groups for simpler local cluster management
* new restart\_all\_services.sh script to recover from aborted blueprint deploys
* New more fully tested blueprints which match better the examples on the twiki
* Cleaning script now also cleans content of the ambari - agent directory

Bugfixes:

* HUE integration with beeswax / hive minor fix in port number resolution
* add\_ebs\_volume script major fixes
* FreeIPA previously made a bind user with no password
* FreeIPA and SonarQube both had missing defaults in their configuration xml
* FreeIPA throwing a certain exception caused a different exception to be raised, confusingly
* FreeIPA now can be recovered from partial failures with a re - install
* tWiki installation was failing on jinja template resolution


# v1.1-Beta
- May 2015

* First version of the AmbariKave installer for public beta release(open source release)
* Stack 2.2.KAVE derived from HDP 2.2

Implemented 14 new services:

* FreeIPA as user - management component
* MongoDB and StormSD as key components in the complete lambda architecture
* Gitlabs, Jenkins, Twiki, SonarQube, Archiva, for the development line
* KaveToolbox installation in one of two modes for the analytical tools
* HUE on top of HDP for simplified hive access
* Apache and JBOSS webservers
* KaveLanding, a simple website of internal links within a KAVE
* Mail, postfix and dovecot for mail servers

Integrated services together:

* Integration of HUE into HDP
* Integration of FreeIPA with Twiki, Jenkins, Gitlabs, HDP(Kerberos, LDAP, DNS and unix users)

Implemented common libraries:

* src / shared / kavecommon is automatically distributed during patching

Automated deployment and testing:

* As part of our development cycle automated deployment and testing of deployed instances is done through aws or vagrant
* We extended the python unittests package for our testing purposes
* Implemented several developer scripts to speed up the development process
* We wrapped aws cli in a python suite to simplify these tests, but that's not really needed for most purposes
* We wrapped blueprint deployment into a simple script which is quite useful for easily deploying / redeploying clusters
