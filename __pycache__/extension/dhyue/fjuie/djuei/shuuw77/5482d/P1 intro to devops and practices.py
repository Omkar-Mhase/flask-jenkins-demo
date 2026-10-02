Practical 1

Introduction to DevOps Tools and Practices.
a. Research and document the importance of DevOps in modern software development.
b. Install and explore one DevOps tool (e.g., Jenkins, Docker, or Ansible).
c. Create a diagram showing how CI/CD, monitoring, and Infrastructure as Code work
together
Introduction to DevOps Tools and Practices
A. Importance of DevOps in Modern Software Development
What is DevOps?
DevOps is a software development approach that combines Development (Dev) and Operations
(Ops) teams to improve collaboration, automate workflows, and deliver software faster and more
reliably.
Importance of DevOps
1. Faster Software Delivery
o Automates building, testing, and deployment processes.
o Reduces time-to-market for new features and updates.
2. Improved Collaboration
o Developers and operations teams work together throughout the software lifecycle.
o Reduces communication gaps and misunderstandings.
3. Higher Software Quality
o Continuous testing identifies bugs early.
o Automated quality checks improve reliability.
4. Increased Deployment Frequency
o Organizations can release updates multiple times a day instead of monthly or
quarterly.
5. Better System Reliability
o Continuous monitoring helps detect and fix issues quickly.
o Infrastructure automation reduces configuration errors.
6. Scalability and Flexibility
o Cloud platforms and Infrastructure as Code (IaC) make scaling easier.
Common DevOps Practices  Continuous Integration (CI)
 Continuous Delivery/Deployment (CD)  Infrastructure as Code (IaC)  Monitoring and Logging
 Automated Testing
 Version Control (Git)  Containerization
Popular DevOps Tools
Category Tools
Version Control Git, GitHub, GitLab
CI/CD Jenkins, GitHub Actions, GitLab
CI
Containers Docker, Podman
Container Orchestration Kubernetes
Configuration
Management Ansible, Puppet, Chef
Monitoring Prometheus, Grafana, Nagios
B. Installation and Exploration of Docker
Why Docker?
Docker is a containerization platform that packages applications and their dependencies into
lightweight containers, ensuring consistent behavior across environments.
Installation Steps (Windows)
1. Visit the official Docker website:
o Docker Desktop
2. Download Docker Desktop.
3. Run the installer and follow the setup wizard.
4. Restart the system if required.
5. Verify installation:
docker --version
Expected output:
Docker version XX.X.X
Basic Docker Commands
Check Docker Status
docker info
Pull an Image
docker pull nginx
View Images
docker images
Run a Container
docker run -d -p 8080:80 nginx
List Running Containers
docker ps
Stop a Container
docker stop <container-id>
Observations  Docker containers start quickly.  Applications run consistently across systems.  Resource usage is lower compared to virtual machines.  Simplifies deployment and scaling.
Advantages of Docker  Portability
 Isolation
 Faster deployments  Reduced infrastructure costs  Supports microservices architecture
C. Diagram: How CI/CD, Monitoring, and Infrastructure as Code Work Together

Explanation of the Diagram
1. Developers commit code to a Git repository.
2. The CI pipeline automatically builds and tests the code.
3. If tests pass, the CD pipeline deploys the application.
4. Infrastructure as Code tools provision and configure servers automatically.
5. The application runs in production.
6. Monitoring tools collect performance metrics and logs.
7. Alerts and feedback help teams identify issues and improve future releases.
Conclusion
DevOps enables organizations to deliver software faster, more reliably, and with higher quality.
Tools such as Docker, Jenkins, Ansible, Prometheus, and Grafana support automation throughout
the software lifecycle. By integrating CI/CD pipelines, Infrastructure as Code, and monitoring
systems, teams can achieve continuous improvement and efficient software delivery.
