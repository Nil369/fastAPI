import subprocess
import os
import sys
import shutil

# Define the paths to the API and client directories
api_dir = os.path.join(os.path.dirname(__file__), 'api')
client_dir = os.path.join(os.path.dirname(__file__), 'client')

# Define the paths to the individual scripts
api_script = os.path.join(api_dir, 'api.py')
app_script = os.path.join(client_dir, 'app.py')

# Check if the scripts exist before trying to run them
if not os.path.exists(api_script):
    print(f"Error: API script not found at {api_script}")
    sys.exit(1)

if not os.path.exists(app_script):
    print(f"Error: App script not found at {app_script}")
    sys.exit(1)

# List to hold the subprocesses so we can terminate them later
processes = []

try:
    print("Starting API server...")
    # Start the API script in its own directory
    api_process = subprocess.Popen([sys.executable, api_script], cwd=api_dir)
    processes.append(api_process)
    print("API server started.")

    print("Starting client application...")
    # Find the streamlit executable path
    streamlit_path = shutil.which('streamlit')
    if not streamlit_path:
        print("Error: 'streamlit' command not found. Please ensure Streamlit is installed and in your system's PATH.")
        sys.exit(1)

    # Start the client application using the streamlit run command
    app_process = subprocess.Popen([streamlit_path, 'run', app_script], cwd=client_dir)
    processes.append(app_process)
    print("Client application started.")

    print("\nPress Enter to stop the servers...")
    # Wait for user input to keep the main script alive and the servers running
    input()

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Terminate all started processes
    print("\nStopping all processes...")
    for p in processes:
        if p.poll() is None:  # Check if the process is still running
            p.terminate()
            p.wait()  # Wait for the process to fully terminate
    print("All processes stopped.")
