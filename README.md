# 🗃️ Task Manager

Simple API & Frontend to manage tasks

## 🛠 Tech Stack

### Backend

[![Backend](https://skillicons.dev/icons?i=py,js,django)](https://skillicons.dev)

### Frontend

[![Frontend](https://skillicons.dev/icons?i=html,css,django,vue)](https://skillicons.dev)


### Database

[![Backend](https://skillicons.dev/icons?i=sqlite)](https://skillicons.dev)

### Environment

[![Environment](https://skillicons.dev/icons?i=windows,vscode,powershell,npm,git,github,py)](https://skillicons.dev)

## 🧩 Features

-   Create tasks
-   Update tasks
-   Delete tasks
-   List tasks
-   List families

## 🚀 Get Started

Before running the project on Windows system you must have installed:

### 🔃 Git

> Recommended version:
>
> Git 2.47.1.windows.2
>

Check installation:

``` bash
git --version
```

### 🐍 Python

> Recommended version:
> 
> Python v3.13+
> 

Check installation:

``` bash
python --version
```

### 📚 Poetry

Poetry is used to manage dependencies and virtual environments.

> Recommended version:
> 
> Poetry v2.3.2+
>

Check installation:

``` bash
poetry --version
```

📦 Node.js / npm

> Recommended versions:
> 
> node v22.13.1+ / npm v10.9.2+
> 

Check installation:

``` bash
node --version
npm --version
```

> If commands to get versions dont work, please ensure they are added in system PATH

## ⚙ Proyect Setup

Clone the proyect, as usual:

``` bash
git clone https://github.com/Endermaiter/Task_Manager.git
```

This project includes an automatic setup script (setup.ps1). However Windows may block script execution by default. So, before running the script, ensure running scripts is disabled on your system by:

Run PowerShell **as Administrator** and execute:

``` powershell
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
```

When prompted:

`\[A\] Yes to All`



## ▶️ Run Setup Script

From the project root folder:

``` powershell
./setup.ps1
```

This script will:

- Install backend dependencies with Poetry
- Install frontend dependencies with NPM
- Start Django service in a terminal
- Start Vue service in other terminal

## 🌐 Endpoints

### Django

Django server usually will start at:

http://localhost:8000/

> The URL could be different in case the port 8000 is busy. Please, check the terminal to ensure, since Django will automatically select another available port if needed, and the URL will be displayed in the console when the server starts.

Django endpoints:

http://localhost:8000/api/

This is the base endpoint for the REST API. It provides access to the backend resources and acts as the entry point for all API-related routes.

http://localhost:8000/admin/

This is the Django administration panel. It allows managing users, permissions, and application data through a graphical interface. **For testing, the families were created here to be used in Frontend.**

The default credentials created for development purposes are:

- User: admin
- Password: admin

http://localhost:8000/api/tasks/

This endpoint provides access to task-related resources. It allows GET, POST, HEAD, OPTIONS tasks through standard REST operations.

### Vue

Vue server usually will start at:

http://localhost:5173/

> The URL could be different in case the port 5173 is busy. Please, check the terminal to ensure. The development server (usually powered by Vite) will display the active URL and port in the terminal when running.

http://localhost:5173/tasks

This route displays the frontend interface for managing tasks. It connects to the backend API to fetch, create, edit, and delete tasks through the user interface.

http://localhost:5173/families

This route displays the frontend interface related to family or grouping management. It allows users to visualize all the families created, interacting with the corresponding backend endpoints.