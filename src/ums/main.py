import sys
import os
from pathlib import Path

# Add src directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

from ums.core.cli import run
from ums.theme import print_error


def main():
    """Application entry point."""
    try:
        run()
    except KeyboardInterrupt:
        print("\n\n" + "-" * 60)
        print_error("   Program interrupted by user. Exiting...")
        print("-" * 60 + "\n\n")
        sys.exit(0)
    except Exception as e:
        print_error(f"\n\n❌ Fatal error: {str(e)}")
        sys.exit(1)


if __name__ == "__main__":
    main()
