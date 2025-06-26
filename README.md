### Blog API
This is a demonstration API designed for teaching integration and unit testing across various components, validating the behavior of an API that handles creating, reading, updating, and deleting blog posts.
#### Types of Testing
- **Unit Testing**: These tests are unit tests for the blog application's API endpoints, ensuring that individual components (like creating, listing, updating, and deleting a blog post) behave as expected
- **Integration Testing**: These tests ensure that different parts of the system work together seamlessly, such as the interaction between the database and API routes.

#### Tools
- **pytest**: This is the testing framework used for running the tests.
- **pytest-asyncio**: This is a plugin for pytest that supports asynchronous testing using async and await
- **client**: This is likely a test client that interacts with the API endpoints during testing

#### Run Locally
Create a Database
```bash
  CREATE DATABASE blog;
```
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
Create a .env file in the root directory
```bash
  DB_URL = "mysql+aiomysql://root:<your_password>@localhost:3306/blog"
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

## Testing the API Endpoints
To interact with and test the API endpoints, you can use **Postman** or **Thunder Client** extension.
### How to Test:
- Open your chosen tool (Postman or Thunder Client).
- Set the HTTP method (GET, POST, PATCH, DELETE) and URL to the corresponding endpoint from your API.
- Add request parameters or body data if needed.
- Send the request and check the response.
### HTTP Methods and Their Usage:
**1. Fetch all blogs (GET)**
   - Used to fetch all the blogs in the database.
   - This will retrieve a list of all books in the database.
   - Request:
     ```bash
     GET http://127.0.0.1:8000/blogs
     ```
---
**2. Fetch a specific blog (GET)**
   - Used to fetch a particular blog by its ID.
   - This will get the details of a specific blog
   - Request:
     ```bash
     GET http://127.0.0.1:8000/blogs/{blog_id}
     ```
 ---
 **3. Add a new blog (POST)**
   - Used to create a new book entry in the database.
   - Add the blog's details (e.g., title,content) in the request body.
   - Request:
     ```bash
     POST http://127.0.0.1:8000/blogs
     ```
---
  **4. Update an existing blog (PATCH)**
   - Used to update the details of an existing blog by its ID.
   - Add the ID of the blog you want to update.
   - Request:
     ```bash
     PATCH http://127.0.0.1:8000/blogs/{blog_id}
     ```
---
  **4. Delete a blog (DELETE)**
   - Used to remove a blog from the database by its ID.
   - Add the ID of the blog you want to delete.
   - Request:
     ```bash
     DELETE http://127.0.0.1:8000/blogs/{blog_id}
     ```

