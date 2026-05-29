import argparse

from blacklistr.scanner import classify_target, parse_url
from blacklistr.scoring import calculate_risk
from blacklistr.indicators import extract_indicators
from blacklistr.storage import save_case
from blacklistr.reporter import generate_report


def main():
    parser = argparse.ArgumentParser(
        prog="blacklistr",
        description="CLI Threat Triage Toolkit"
    )

    subparsers = parser.add_subparsers(dest="command")

    scan_parser = subparsers.add_parser(
        "scan",
        help="Scan a URL, domain, or IP"
    )

    scan_parser.add_argument(
        "target",
        help="Target to analyze"
    )

    extract_parser = subparsers.add_parser(
        "extract",
        help="Extract indicators from a text file"
    )

    extract_parser.add_argument(
        "file",
        help="Text file to analyze"
    )

    args = parser.parse_args()

    if args.command == "scan":

        target_type = classify_target(args.target)

        print("\n=== BLACKLISTR REPORT ===\n")

        print(f"Target   : {args.target}")
        print(f"Type     : {target_type}")

        if target_type == "url":
            details = parse_url(args.target)

            print(f"Host     : {details['hostname']}")
            print(f"Path     : {details['path'] or '/'}")

        result = calculate_risk(args.target)

        print(f"\nRisk Score : {result['score']}/100")
        print(f"Severity   : {result['severity']}")

        print("\nReasons:")

        if result["reasons"]:
            for reason in result["reasons"]:
                print(f" - {reason}")
        else:
            print(" - No obvious risk indicators found")

        case_data = {
            "target": args.target,
            "type": target_type,
            "score": result["score"],
            "severity": result["severity"],
            "reasons": result["reasons"]
        }

        saved_case = save_case(case_data)
        report_file = generate_report(case_data)

        print(f"\nCase saved   : {saved_case}")
        print(f"Report saved : {report_file}")

    elif args.command == "extract":

        with open(args.file, "r", encoding="utf-8") as f:
            content = f.read()

        results = extract_indicators(content)

        print("\n=== INDICATOR EXTRACTION ===\n")

        for category, items in results.items():
            print(f"{category.upper()}:")

            if items:
                for item in items:
                    print(f" - {item}")
            else:
                print(" - None")

            print()

    else:
        parser.print_help()


if __name__ == "__main__":
    main()
