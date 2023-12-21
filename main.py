import subprocess

print("""
██████╗░██╗███╗░░██╗██╗░░██╗░░░░░░██╗░░░░░░█████╗░██████╗░
██╔══██╗██║████╗░██║██║░██╔╝░░░░░░██║░░░░░██╔══██╗██╔══██╗
██████╦╝██║██╔██╗██║█████═╝░█████╗██║░░░░░███████║██████╦╝
██╔══██╗██║██║╚████║██╔═██╗░╚════╝██║░░░░░██╔══██║██╔══██╗
██████╦╝██║██║░╚███║██║░╚██╗░░░░░░███████╗██║░░██║██████╦╝
╚═════╝░╚═╝╚═╝░░╚══╝╚═╝░░╚═╝░░░░░░╚══════╝╚═╝░░╚═╝╚═════╝░
      
Made with Python 3.11.4 by Sidney
      """)

def download_file(url, output_file):
    try:
        # Use subprocess to run PowerShell command to download a file
        result = subprocess.run(["powershell", "Invoke-WebRequest", url, "-OutFile", output_file], check=True)

        print(f"File downloaded and saved to {output_file}")

    except subprocess.CalledProcessError as e:
        # Handle errors if the PowerShell command fails
        print(f"Error: {e}")
        print(f"PowerShell stderr: {e.stderr}")

# Example usage
url_to_download = input("Link to file: ")
output_file_path = input("Output file name: ")
download_file(url_to_download, output_file_path)
