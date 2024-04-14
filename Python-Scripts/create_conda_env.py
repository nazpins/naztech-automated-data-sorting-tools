import subprocess

def create_conda_env(env_name):
    subprocess.run(["conda", "create", "-n", env_name, "python=3.9", "-y"])
    subprocess.run(["conda", "activate", env_name])
    subprocess.run(["conda", "install", "numpy", "pandas", "scikit-learn", "-y"])
    print(f"Conda environment '{env_name}' created and activated.")

if __name__ == '__main__':
    env_name = input("Enter the name of the Conda environment: ")
    create_conda_env(env_name)