# Docker and Airflow Setup Guide

This guide provides instructions on setting up Docker and Airflow for your project.

## Table of Contents

1. [Verify Docker is Running](#verify-docker-is-running)
2. [Docker Installation](#docker-installation)
3. [Docker Image Creation](#docker-image-creation)
4. [Docker Compose Setup](#docker-compose-setup)
5. [Airflow Setup](#airflow-setup)
6. [Running Containers](#running-containers)
7. [Debugging Containers](#debugging-containers)
8. [Accessing Airflow](#accessing-airflow)
9. [Triggering Airflow DAGs](#triggering-airflow-dags)

---

## Verify Docker is Running

### Step 1: Verify Docker is Running

Before using this script, ensure that Docker is properly installed and running on your system.

---

## Docker Installation

To use this script, Docker must be installed. First, I installed Docker using the `install.sh` file.


You need to make the file executable before running it.
    ```
    chmod +x install_docker.sh
    ```

---

## Docker Image Creation

1. **Create Docker Image**

   First, we create a Docker image by writing a `Dockerfile`. Once the `Dockerfile` is ready, we build the image using the chosen image name (`lnx` in this case).
    ```
    sudo docker build -t lnx:latest .
    ```
   

   - In the example code, I have chosen the image name `lnx`, which is also referenced in the `docker-compose.yml` file.
   - If you decide to use a different image name, you must update the `docker-compose.yml` file accordingly.

3. **Verify Docker Image**
     ```
     sudo docker images
     ```

   After creating the Docker image, you can verify the image by checking its details.

---

## Docker Compose Setup

Once the Docker image is created, the next step is to edit the `docker-compose.yml` file to ensure the container can run properly. 

---

## Airflow Setup

1. **Create Required Directories**

   In my case, before running Airflow, I needed to create the following directories manually due to permission issues. The following codes resolved the issue by creating the directories manually and setting permissions right.
   - `airflow/dags`
   - `airflow/logs`
   - `airflow/plugins`
     
  
    ```
      mkdir -p airflow/dags airflow/logs airflow/plugins
    ```
    

2. **Set Permissions**
   
   After creating these directories, update the permissions accordingly for proper access and functionality.
   ```
     sudo chown -R 50000:0 ./airflow
     sudo chmod -R 775 ./airflow
   ```

---

## Running Containers

Once the setup is complete, execute the necessary commands to run the Docker container using Docker Compose. You can run Docker Compose in either normal or detached mode, depending on your preference.

- **Detached Mode**: This allows the containers to run in the background.
  ```
     sudo docker compose up -d
   ```
  
- **Explicit File Specification**: If your Docker Compose file is not named `docker-compose.yml` or is located in a different directory, you can explicitly specify the file to use.

  ```
     sudo docker compose -f /path/to/your/docker-compose.yml up
   ```

---

## Debugging Containers

To debug Docker containers, you can use the following steps:

1. **Verify Running Containers**: Check which containers are running.
   ```
     sudo docker ps
   ```
2. **List All Containers**: See all containers, including stopped ones.
   ```
     sudo docker ps -a
   ```
3. **View Logs**: Access logs of a specific container.
   ```
     sudo docker logs <container_id>
   ```
4. **Access Container Shell**: Execute shell commands within a running container.
   ```
     sudo docker exec -it <container_name_or_id> bash
   ```

---

## Accessing Airflow

Once the container is successfully executed, you can access Airflow using the following URL: http://0.0.0.0:8080/

---

## Triggering Airflow DAGs

1. After starting Airflow, create a file named `welcome_dag.py` inside the `airflow/dags/` directory.
   
2. Wait for about 3-5 minutes for the DAG to appear in the Airflow browser interface.

3. Once visible, manually trigger the DAG and ensure that it runs correctly.

