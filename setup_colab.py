
# Save this as first cell in your notebook
import os
from google.colab import drive

# 1. Mount Drive
drive.mount('/content/drive')

# 2. Clone or pull from GitHub
github_url = "https://github.com/YOUR_USERNAME/telco-churn-analysis.git"
project_path = "/content/telco_churn_analysis"

if os.path.exists(project_path):
    %cd {project_path}
    !git pull origin main
    print("✅ Updated existing project")
else:
    !git clone {github_url} {project_path}
    %cd {project_path}
    print("✅ Cloned fresh from GitHub")

# 3. Create Drive backup folder
drive_backup = "/content/drive/MyDrive/Colab_Projects/telco_churn"
!mkdir -p {drive_backup}

print(f"📁 Working in: {project_path}")
print(f"💾 Backing up to: {drive_backup}")
