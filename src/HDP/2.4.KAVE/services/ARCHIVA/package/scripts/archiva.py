##############################################################################
#
# Copyright 2016 KPMG Advisory N.V. (unless otherwise stated)
#
# Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
#
##############################################################################
import kavecommon as kc
from resource_management import *
import os


class Archiva(Script):
    installer_cache_path = '/tmp/'
    package = 'apache-archiva-2.2.0-bin.zip'
    # archiva_mirror='http://www.us.apache.org/dist/archiva/2.2.0/binaries/apache-archiva-2.2.0-bin.zip'

    def install(self, env):
        import params

        env.set_params(params)
        self.install_packages(env)

        Execute('mkdir -p %s ' % params.install_topdir)
        kc.copy_cache_or_repo(self.package, arch="noarch")
        Execute('unzip -q %s' % (self.package))
        if os.path.exists(params.install_topdir + params.install_subdir):
            Execute('rm -rf %s' % (params.install_topdir + params.install_subdir))
        Execute('mv apache-archiva-2.2.0 %s' % (params.install_topdir + params.install_subdir))
        if os.path.exists(self.package):
            Execute('rm -f ' + self.package)
        if os.path.exists('/etc/init.d/archiva'):
            Execute('rm -f /etc/init.d/archiva')
        Execute('ln -s %s/bin/archiva /etc/init.d/archiva' % (params.install_topdir + params.install_subdir))

        self.configure(env)

    def start(self, env):
        self.configure(env)
        Execute('service archiva start > /dev/null')

    def stop(self, env):
        Execute('service archiva stop')

    def restart(self, env):
        self.configure(env)
        Execute('service archiva restart > /dev/null')

    def status(self, env):
        Execute('service archiva status')

    def configure(self, env):
        import params

        env.set_params(params)

        File(params.install_topdir + params.install_subdir + "/conf/jetty.xml",
             content=Template("jetty.xml.j2"),
             mode=0600
             )
        File(params.install_topdir + params.install_subdir + "/conf/security.properties",
             content=Template("security.properties.j2"),
             mode=0600
             )


if __name__ == "__main__":
    Archiva().execute()
