#Basically, allows you to install all Python Packages/dependencies into DOCKER

FROM apache/airflow:2.7.1-python3.9 
    #FROM: This instruction SPECIFIES the BASE IMAGE for the Docker image you are building. In this case, it uses the apache/airflow:2.7.1-python3.9 image. This image includes Apache Airflow version 2.7.1 and Python 3.9 as the base environment.
        #Purpose: It provides a starting point with Airflow and Python pre-installed.
COPY requirements.txt /opt/airflow/
    #COPY: This instruction copies files and directories from your local file system into the Docker image.
        #requirements.txt: The file on your local machine.
        #/opt/airflow/: The destination directory inside the Docker image.
        #Purpose: It transfers the requirements.txt file, which typically lists Python packages needed by your application, into the image.
USER root
    #USER: This instruction sets the user to root. By default, Docker containers run as a non-root user (in this case, airflow). Changing to root is necessary to perform certain system-level operations, such as installing packages.
RUN apt-get update && apt-get install -y gcc python3-dev
    #RUN: This instruction executes commands in the image during the build process.
    #apt-get update: Updates the package lists for the apt package manager.
    #apt-get install -y gcc python3-dev: Installs the gcc compiler and python3-dev package. The -y flag automatically answers "yes" to any prompts.
    #Purpose: Installs necessary system packages that might be required for compiling Python packages or other dependencies.
USER airflow
    #USER: This instruction switches back to the non-root airflow user.
    #Purpose: For security reasons, it’s a good practice to run applications as a non-root user whenever possible.

RUN pip install --no-cache-dir -r /opt/airflow/requirements.txt 
        #'--no-cache-dir'prevent pip from using its cache directory.  
        #It ensures that packages are installed fresh, without using any 
        #previously cached versions. This is particularly useful to avoid installing 
        #outdated or corrupted packages from the cache.
        #'-r' This flag is used with pip install to specify a requirements file.
    #RUN: Executes build commands in the image during the build.
    #pip install --no-cache-dir -r /opt/airflow/requirements.txt: Installs Python packages listed in the requirements.txt file. The --no-cache-dir option prevents caching of the packages, reducing the image size.
    #Purpose: Installs the Python packages required for your application as defined in requirements.txt.

#SUMMARY
    #FROM: Sets the base image for the Docker image.
    #COPY: Transfers files from the local system to the Docker image.
    #USER: Switches between different users in the image.
    #RUN: Executes commands to modify the image, such as installing packages.    


#A Dockerfile is a script containing a series of instructions on how to build a Docker image. 
#Each instruction creates a layer in the image, and the final image is composed of these layers. 
#The Dockerfile defines the base image, adds files, installs dependencies, and configures the environment 
#for the container.