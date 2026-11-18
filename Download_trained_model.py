from google.colab import files
import os

# Available model options
paths_to_check = [
    "/content/ppo-LunarLander-v2.zip",
    "/content/ppo-LunarLander-v3.zip",
    "/content/drive/MyDrive/Colab_RL_Models/ppo-LunarLander-v3.zip",
    "/content/drive/MyDrive/Colab_RL_Models/ppo-LunarLander-v2.zip",
    "ppo-LunarLander-v3.zip",
    "ppo-LunarLander-v2.zip"
]

downloaded = False
for path in paths_to_check:
    if os.path.exists(path):
        print(f"Found model at {path}. Downloading to your computer...")
        files.download(path)
        downloaded = True
        break

if not downloaded:
    print("❌ Could not find any saved ppo-LunarLander model (.zip) on your local path or Google Drive. Please run your training cells first.")
