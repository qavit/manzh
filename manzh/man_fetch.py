import subprocess

def fetch_man(command: str) -> str:
    """Fetches the raw text of a man page for a given command."""
    try:
        # Fetch the original man page
        man_process = subprocess.Popen(
            ["man", command],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        
        # Clean the output by removing backspaces with col -b
        col_process = subprocess.Popen(
            ["col", "-b"],
            stdin=man_process.stdout,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        
        # Allow man_process to receive a SIGPIPE if col_process exits
        if man_process.stdout:
            man_process.stdout.close()
            
        stdout, stderr = col_process.communicate()
        
        if col_process.returncode != 0:
            raise RuntimeError(f"Error fetching man page for {command}: {stderr}")
            
        # Also check man process error
        # Note: man might return non-zero if col terminates early, 
        # but if stdout is completely empty, it likely means the command wasn't found.
        if not stdout.strip():
             return ""
             
        return stdout
    except Exception as e:
        raise RuntimeError(f"Failed to execute man command: {e}")
