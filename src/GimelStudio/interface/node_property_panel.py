# ----------------------------------------------------------------------------
# Gimel Studio Copyright 2019-2021 by Noah Rahm and contributors
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# FILE: node_property_panel.py
# AUTHOR(S): Noah Rahm
# PURPOSE: Define the Node Property panel
# ----------------------------------------------------------------------------

import wx
import wx.lib.scrolledpanel as scrolledpanel

from GimelStudio.datafiles.icons import *


class NodePropertyPanel(wx.lib.scrolledpanel.ScrolledPanel):
    def __init__(self, parent, size=wx.DefaultSize):
        scrolledpanel.ScrolledPanel.__init__(self, parent, wx.ID_ANY, size=size)
        self._parent = parent
        self._selectedNode = None

        self._mainSizer = wx.BoxSizer(wx.VERTICAL)

        self.SetSizer(self._mainSizer)
        self._mainSizer.Fit(self)

        self.SetupScrolling(scroll_x=False)

        self.SetBackgroundColour(wx.Colour("#404040"))

    @property
    def Parent(self):
        return self._parent

    @property
    def AUIManager(self):
        return self._parent._mgr

    def UpdatePanelContents(self, selected_node):
        self.DestroyChildren()

        if selected_node != None:

            scrollbar_size = wx.SystemSettings.GetMetric(wx.SYS_VSCROLL_X)
            calc_size = wx.Size(self.Size[0] - scrollbar_size - 10, self.Size[1])

            self.panel_staticbox = wx.Panel(self, id=wx.ID_ANY,
                                            # label=selected_node.GetLabel(),
                                            size=calc_size)

            # This gets the recommended amount of border space to use for items
            # within in the static box for the current platform.
            #top_bd, other_bd = self.panel_staticbox.GetBordersForSizer()

            staticbox_sizer = wx.BoxSizer(wx.VERTICAL)
            staticbox_sizer.AddSpacer(8)

            inner_sizer = wx.BoxSizer(wx.VERTICAL)

            flagsExpand = wx.SizerFlags(1)
            flagsExpand.Expand().Border(wx.ALL, 18)
            staticbox_sizer.Add(inner_sizer, flagsExpand)

            self.panel_staticbox.SetSizer(staticbox_sizer)

            panel_sizer = wx.BoxSizer(wx.VERTICAL)
            panel_sizer.Add(self.panel_staticbox, 1, wx.EXPAND | wx.ALL, 8)

            # Node Properties UI
            selected_node.NodePanelUI(self.panel_staticbox, inner_sizer)

            self._mainSizer.Add(panel_sizer, wx.EXPAND | wx.ALL)

        else:
            # Delete the window if the node is not selected
            self._mainSizer.Clear(delete_windows=True)

        self.AUIManager.Update()
        self.Parent.Refresh()
        self.Parent.Update()
