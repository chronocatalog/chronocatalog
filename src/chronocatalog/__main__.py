"""Allow running as ``python -m chronocatalog``."""

import sys

from chronocatalog.cli import main

if __name__ == "__main__":
    sys.exit(main())
