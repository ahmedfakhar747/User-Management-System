import sys
from cli import run
from theme import print_header, print_error, print_success, print_info


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
