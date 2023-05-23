# To run this PowerShell script remotely, open Windows Terminal and paste the following line (without the #):
# Invoke-Expression $(Invoke-WebRequest https://raw.githubusercontent.com/guygregory/ChatToolkit/main/Automated%20Install.ps1)

# Set the local folder path
$LocalFolder = "C:\Chat Toolkit\"

# Create a new directory at the local folder path
New-Item -Path $LocalFolder -ItemType Directory

# Download the ChatToolkit repository from GitHub and save it as a zip file in the local folder path
Invoke-WebRequest -Uri "https://github.com/guygregory/ChatToolkit/archive/refs/heads/main.zip" -OutFile $LocalFolder"ChatTk.zip"

# Extract the contents of the zip file to the local folder path
Expand-Archive -Path $LocalFolder"ChatTk.zip" -DestinationPath $LocalFolder

# Move the contents of the extracted folder to the local folder path
gci -Path $LocalFolder"ChatToolkit-main" -Recurse | Move-Item -Destination $LocalFolder -Force

# Remove the extracted folder
Remove-Item -Path $LocalFolder"ChatToolkit-main" -Recurse

# Install Python 3.11 from the Microsoft Store using the Windows Package Manager (winget)
Invoke-Command -ScriptBlock {winget install "Python 3.11" --source msstore}

# Install the OpenAI Python package using pip
Invoke-Command -ScriptBlock {pip install openai --quiet}

# Change the current directory to the local folder path
Set-Location -Path $LocalFolder

# Start the ChatTk.py script using Python, with no new window
Start-Process -FilePath "python.exe" -ArgumentList '"C:\Chat Toolkit\ChatTk.py"' -NoNewWindow
