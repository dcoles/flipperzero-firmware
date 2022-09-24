#!/usr/bin/env python3

import logging
import sys
import subprocess
from flipper.utils.cdc import resolve_port


def main():
    logger = logging.getLogger()
    if not (port := resolve_port(logger, "auto")):
        return 1

    subprocess.call([sys.executable, "-m", "serial.tools.miniterm", "--raw", port, "230400"])


if __name__ == "__main__":
    main()
