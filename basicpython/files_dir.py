from pathlib import Path

path =Path("my_package")
print(path.exists())  # Check if the path exists


path = Path()
for file in path.glob('*.py'):
    print(file)  # Print all Python files in the current directory
    
