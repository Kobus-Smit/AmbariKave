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
from resource_management import *

config = Script.get_config()

install_topdir = default('configurations/archiva/install_topdir', '/opt/')

if len(install_topdir) < 4 or install_topdir.count('/') < 2 or not install_topdir.startswith('/'):
    raise ValueError('archiva/install_topdir must be a valid directory full path,'
                     ' with a length of at least 4 and two /')

if not install_topdir.endswith('/'):
    install_topdir = install_topdir + '/'

install_subdir = default('configurations/archiva/install_subdir', 'archiva')

if not len(install_subdir) or install_subdir.count('/'):
    raise ValueError('archiva/install_subdir must be a simple string, with no "/"')

archiva_jetty_port = default('configurations/archiva/archiva_jetty_port', '5050')
