
# Write-up Template

  

### Analyze, choose, and justify the appropriate resource option for deploying the app.

  

*For **both** a VM or App Service solution for the CMS app:*

-  *Analyze costs, scalability, availability, and workflow*

-  *Choose the appropriate solution (VM or App Service) for deploying the app*

-  *Justify your choice*


**Use App Service instead of virtual machines?**

App Service  is a PaaS (Platform as a Service), so I decided to use   App Service to deploy my app. This means that it specializes in    HTTP-based services for hosting web applications (for this project).    App Service also supports the Python language and Github,  dependencies used in this project. Because App Service is a PaaS,    developers can focus on developing their apps without worrying about     infrastructure such as  deployment pipelines, hosting servers, and    underlying operating systems. Finally, App Service is more cost    effective than Virtual Machine as you only have to pay to use it.

 **Not use Virtual Machines**
Since it's infrastructure as a service (IaaS), I didn't choose to deploy virtual machines (VMs). Since this project is a web application, there is no need to create and use a virtual machine in the cloud. There is no need to access and control VMs or other infrastructure such as storage, CPU, RAM, storage. Also, a VM would be expensive and time-consuming to develop for this project.

In virtual machine, we need to create project setup from scratch. so we use app service for our project. it is simple and easy to use.

**How would you change your apps or other requirements to change your decision to use a virtual machine?**
If your app is large and you need to  control  infrastructure such as  operating system and CPU capacity, you should choose (Azure) Virtual Machine as your deployment method.  (Azure) Virtual Machine is an IaaS (Infrastructure as a Service), so it supports developers to have full access and control over the virtual machine, controlling the deployment and operating system, and assigning memory for CPU and RAM. can be increased. Or storage. In this case, using (Azure) App Service for large apps is inappropriate.