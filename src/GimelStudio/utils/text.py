## ----------------------------------------------------------------------------
## Gimel Studio Copyright 2020 Noah Rahm, Correct Syntax. All rights reserved.
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
## FILE: text.py
## AUTHOR(S): Noah Rahm
## PURPOSE: Provides utility text manipulation functions
## ----------------------------------------------------------------------------


def TruncateText(text_string, str_length=18):
    """ Truncate the text string after a certain
    number of characters.
    """
    chars = []
    for char in text_string:
        chars.append(char)

    if len(chars) > str_length:
        words = chars[:str_length-1]
        text = ''.join(words)
        return '{}...'.format(text)
    else:
        return text_string