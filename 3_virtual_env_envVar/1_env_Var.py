import os

# If the environment variable "MY_NAME" is not set, it will default to "World"
# To set it do the following steps in the bash: export MY_NAME="Akash Halder"
# To print it in terminal use this: echo "Hello $MY_NAME"

name = os.getenv("MY_NAME","World")
print(f"Hello {name} from python")