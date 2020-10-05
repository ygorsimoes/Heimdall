#!/usr/bin/env python3

import sys


class Color:
    """
    Helper object for easily printing
    colored text to the terminal.
    """

    # Basic console colors
    colors = {
        'W': '\033[0m',  # white (normal)
        'R': '\033[31m',  # red
        'G': '\033[32m',  # green
        'O': '\033[33m',  # orange
        'B': '\033[34m',  # blue
        'P': '\033[35m',  # purple
        'C': '\033[36m',  # cyan
        'GR': '\033[37m',  # gray
        'D': '\033[2m'  # dims current color. {W} resets.
    }

    # Helper string replacements
    replacements = {
        '{+}': '{W}{D}[{W}{G}+{W}{D}]{W}',
        '{-}': '{W}{D}[{W}-{D}]{W}',
        '{!}': '{O}[{R}!{O}]{W}',
        '{?}': '{W}[{C}?{W}]'
    }

    last_sameline_length = 0

    @staticmethod
    def p(text):
        """
        Prints text using colored
        format on same line.

        Example:
            Color.p('{R}This text is red. {W} This text is white')
        """
        sys.stdout.write(Color.s(text))
        sys.stdout.flush()
        if '\r' in text:
            text = text[text.rfind('\r') + 1:]
            Color.last_sameline_length = len(text)
        else:
            Color.last_sameline_length += len(text)

    @staticmethod
    def pl(text):
        """
        Returns colored string
        """
        Color.p('%s\n' % text)
        Color.last_sameline_length = 0

    @staticmethod
    def s(text):
        """
        Returns colored string
        """
        output = text
        for (key, value) in Color.replacements.items():
            output = output.replace(key, value)
        for (key, value) in Color.colors.items():
            output = output.replace('{%s}' % key, value)
        return output


if __name__ == '__main__':
    Color.pl('{R}Testing {G}One {C}Two {P}Three {W}Done')
    print(Color.s('{C}Testing {P}String{W}'))
    Color.pl('{+} Good line')
    Color.pl('{!} Danger')
