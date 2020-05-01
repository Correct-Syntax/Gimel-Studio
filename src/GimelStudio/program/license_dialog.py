## ----------------------------------------------------------------------------
## Gimel Studio © 2020 Correct Syntax, Noah Rahm. All rights reserved.
##
## FILE: license_dialog.py
## AUTHOR(S): Noah Rahm
## PURPOSE: Defines the Gimel Studio license dialog
## ----------------------------------------------------------------------------

import wx
import wx.lib.dialogs

from GimelStudio.meta import (__NAME__, __AUTHOR__, __VERSION__,
                              __BUILD__, __RELEASE__, __TITLE__)

class GimelStudioLicenseDialog(object):
    def __init__(self, parent):
        self._parent = parent

    def ShowDialog(self):
        LICENSE = """
Gimel Studio © 2020 Correct Syntax, Noah Rahm. All rights reserved.

IMPORTANT - PLEASE READ BEFORE COPYING, INSTALLING OR USING GIMEL STUDIO VERSION {0}.{1}

Do not use or load this software and any associated materials (collectively,
the "Software") until you have carefully read the following terms and
conditions. By installing, loading or using the Software, you agree to all the
terms of this Agreement. If you do not wish to agree, do not install or use
the Software.

This copyright applies to all Software files, add-on modules/nodes, documentation,
graphics and auxiliary files, except those parts written by other people
(which usually will be under copyright by their authors). The license applies
to the whole Software.

This version (v{0}.{1}) of the Software may be used free of charge by any person or
organization to whom it is made available, provided that that person accepts the conditions
of this license.

THIS IS A BETA VERSION OF THE SOFTWARE RELEASED TO THE PUBLIC. THE SOFTWARE MAY BE
UNSTABLE AND CAUSE UNEXPECTED DAMAGE TO FILES, ETC. YOU ASSUME ALL
RESPONSIBILITY FOR ANY DAMAGE THAT MAY OCCUR.

You may copy the Software onto a single computer for personal, non-commercial or commercial use,
and you may make one back-up copy of the Software, subject to these conditions:

1. You may not copy, modify, rent, sell, distribute or transfer any part of the Software
except as provided in this Agreement, and you agree to prevent unauthorized copying
of the Software. Neither the Software, nor any associated files, may be sold or resold, distributed as
a part of any commercial package, or used or distributed to support any kind of profit-generating
activity, even if it is being distributed freely.

2. You may not reverse engineer, decompile, or disassemble the Software nor any of its
associated modules/nodes in any way.

3. You may not sublicense or permit simultaneous use of the Software by more than one user.

4. The Software may contain the software or other property of third party suppliers, some of
which may be identified in, and licensed in accordance with, any enclosed "license.txt" file
or other text or file.

THE SOFTWARE IS PROVIDED "AS IS" WITHOUT ANY EXPRESS OR IMPLIED WARRANTY OF ANY KIND INCLUDING
WARRANTIES OF MERCHANTABILITY, NONINFRINGEMENT, OR FITNESS FOR A PARTICULAR PURPOSE.

I, Noah Rahm do not warrant or assume responsibility for the accuracy
or completeness of any information, text, graphics, links or other items contained within the Software.

IN NO EVENT SHALL CORRECT SYNTAX OR THE COPYRIGHT HOLDERS BE LIABLE FOR ANY DAMAGES
WHATSOEVER (INCLUDING, WITHOUT LIMITATION, LOST PROFITS, BUSINESS INTERRUPTION, OR LOST INFORMATION)
ARISING OUT OF THE USE OF OR INABILITY TO USE THE SOFTWARE, EVEN IF CORRECT SYNTAX OR NOAH RAHM HAS
BEEN ADVISED OF THE POSSIBILITY OF SUCH DAMAGES. 

No warranty of any sort, expressed or implied, is provided in connection with the program, including,
but not limited to, implied warranties of merchantability or fitness for a particular purpose. Any cost, loss
or damage of any sort incurred owing to the malfunction or misuse of the program or the inaccuracy of the
documentation or connected with the program in any other way whatsoever is solely the responsibility of the
person who incurred the cost, loss or damage. Furthermore, any illegal use of the program is solely the
responsibility of the person committing the illegal act.

By using this program you accept these responsibilities, and give up any right to seek any damages against
Noah Rahm or Correct Syntax in connection with this program.

I, Noah Rahm, reserve the right to make exceptions to any of these conditions, or alter these conditions, at any time.

Visit https://correctsyntax.com/projects/gimel-studio/ for updates, support, documentation and more.

Thank you!
        """.format(__VERSION__, __RELEASE__)

        dlg = wx.lib.dialogs.ScrolledMessageDialog(
            self._parent, 
            LICENSE, 
            "Gimel Studio License",
            size=(600, 750)
            )
        dlg.ShowModal()
