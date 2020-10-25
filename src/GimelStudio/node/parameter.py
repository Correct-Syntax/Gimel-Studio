## ----------------------------------------------------------------------------
## Gimel Studio Copyright 2019-2020 by Noah Rahm and contributors
##
## Licensed under the Apache License, Version 2.0 (the "License");
## you may not use this file except in compliance with the License.
## You may obtain a copy of the License at
##
##    http://www.apache.org/licenses/LICENSE-2.0
##
## Unless required by applicable law or agreed to in writing, software
## distributed under the License is distributed on an "AS IS" BASIS,
## WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
## See the License for the specific language governing permissions and
## limitations under the License.
##
## FILE: parameter.py
## AUTHOR(S): Noah Rahm
## PURPOSE: Define the base node parameter class and specific parameter types
## ----------------------------------------------------------------------------

from GimelStudio.datatypes import RenderImage


class Parameter(object):
    def __init__(self, idname, default):
        self.idname = idname
        self.default = default
        self.binding = None

    @property
    def IdName(self):
        """ Gets the name identifier of the parameter.
        :return: the name of the parameter.
        """
        return self.idname

    def GetDefault(self):
        return self.default

    def SetBinding(self, binding):
        self.binding = binding


class RenderImageParam(Parameter):
    def __init__(self, idname, default=RenderImage()):
        Parameter.__init__(self, idname, default)
        self.value = default

    def GetValue(self):
        return self.value

    def SetValue(self, value):
        self.value = value
