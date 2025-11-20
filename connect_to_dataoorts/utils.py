import re

def extract_public_ip(ssh_command: str) -> str:
    """
    Extracts the PUBLIC_IP from an SSH command of the format:
    ssh -i "path" ubuntu@IP -p 22
    """
    # Regex to capture anything after ubuntu@ and before space or colon
    match = re.search(r"ubuntu@([0-9]+\.[0-9]+\.[0-9]+\.[0-9]+)", ssh_command)
    
    if match:
        return match.group(1)
    else:
        raise ValueError("❌ Could not extract IP address from SSH command!")

def temporary(path_link: str) -> str:
    temp_file_path = (fr'{path_link}\temporary.pem')
    return temp_file_path

# --------------------------
# Example Usage
# --------------------------

ssh_cmd = r'ssh -i temporary.pem ubuntu@38.80.122.156 -p 22'
PUBLIC_IP = extract_public_ip(ssh_cmd)
print("Extracted PUBLIC_IP:", PUBLIC_IP)



temp_file_path = temporary(r"D:\code\Course\SLM\SLM - Copy")
print(temp_file_path)
