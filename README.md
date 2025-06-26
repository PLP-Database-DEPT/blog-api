### Blog API
This is a demostration api used for teaching intergration and unit testing for various components to validate the behavior of an API for creating, reading, updating, and deleting blog posts
#### Types of Testing
- **Unit Testing**: These tests are unit tests for the blog application's API endpoints, ensuring that individual components (like creating, listing, updating, and deleting a blog post) behave as expected
- **Integration Testing**: They test how different parts of the system work together, such as the database and the API routes.
#### Run Locally

Clone the project

```bash
  git clone https://github.com/PLP-Database-DEPT/blog-api.git
```

Go to the project directory

```bash
  cd blog-api
```
Create a virtual environment

```bash
  py -m venv .venv
```
Install dependencies

```bash
  pip install -r requirements.txt
```

Start the server

```bash
  fastapi dev main.py
```


#### Tech Stack

**Server:** Fastapi
