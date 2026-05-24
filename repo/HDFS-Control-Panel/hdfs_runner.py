import subprocess

def run_command(command):
    if not command or command == "None":
        return "Waiting for command..."
    try:
      
        full_command = f"source ~/.bashrc && {command}"
        result = subprocess.run(
            full_command, 
            shell=True, 
            executable="/bin/bash", 
            capture_output=True, 
            text=True
        )
        
        output = ""
        if result.stdout:
            output += result.stdout
        if result.stderr:
            output += f"\n[System Log/Error]:\n{result.stderr}"
            
        return output if output.strip() else "✅ Command executed successfully (No output text)."
    except Exception as e:
        return f"❌ Execution Failed: {str(e)}"

