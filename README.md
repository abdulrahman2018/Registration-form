Certainly! Here's a detailed documentation for your project, covering both frontend and backend aspects:

---

# **Registration Form Application Documentation**

## **Overview**

This project consists of a registration form application with a frontend built using React.js and Bootstrap, and a backend built using ASP.NET Core and MySQL. The application allows users to register by submitting a form, and the data is stored in a MySQL database.

## **Table of Contents**

1. [**Project Setup**](#project-setup)
   - [Frontend Setup](#frontend-setup)
   - [Backend Setup](#backend-setup)
2. [**Frontend Documentation**](#frontend-documentation)
   - [React.js Setup](#reactjs-setup)
   - [Bootstrap Integration](#bootstrap-integration)
   - [Components](#components)
3. [**Backend Documentation**](#backend-documentation)
   - [ASP.NET Core Setup](#aspnet-core-setup)
   - [Database Integration](#database-integration)
   - [API Endpoints](#api-endpoints)
4. [**Testing**](#testing)
5. [**Troubleshooting**](#troubleshooting)

---

## **Project Setup**

### **Frontend Setup**

1. **Install Dependencies**
   
   Make sure you have Node.js installed. Navigate to the frontend directory and install dependencies:

   ```bash
   npm install
   ```

2. **Run the Development Server**
   
   Start the React development server:

   ```bash
   npm start
   ```

   This will run the application on `http://localhost:3000`.

### **Backend Setup**

1. **Install .NET SDK**

   Ensure you have .NET SDK installed. If not, download and install it from the [.NET website](https://dotnet.microsoft.com/download).

2. **Install Dependencies**

   Navigate to the backend directory and restore the required packages:

   ```bash
   dotnet restore
   ```

3. **Run the Application**

   Start the ASP.NET Core application:

   ```bash
   dotnet run
   ```

   This will run the application on `http://localhost:5146`.

## **Frontend Documentation**

### **React.js Setup**

1. **Create React App**

   Initialize a new React project if not already done:

   ```bash
   npx create-react-app registration-form-app
   ```

2. **Project Structure**

   Ensure your project structure looks like this:

   ```
   registration-form-app/
   ├── public/
   ├── src/
   │   ├── components/
   │   │   └── RegistrationForm.js
   │   ├── App.js
   │   └── index.js
   ├── package.json
   └── ...
   ```

### **Bootstrap Integration**

1. **Install Bootstrap**

   Install Bootstrap via npm:

   ```bash
   npm install bootstrap
   ```

2. **Import Bootstrap CSS**

   In `src/index.js`:

   ```javascript
   import 'bootstrap/dist/css/bootstrap.min.css';
   ```

### **Components**

#### **RegistrationForm Component**

```javascript
import React, { useState } from 'react';
import { Form, Button, Container } from 'react-bootstrap';

const RegistrationForm = () => {
    const [formData, setFormData] = useState({
        name: '',
        email: '',
        phone: '',
        age: ''
    });

    const handleChange = (e) => {
        const { name, value } = e.target;
        setFormData({ ...formData, [name]: value });
    };

    const handleSubmit = async (e) => {
        e.preventDefault();

        try {
            const response = await fetch('http://localhost:5146/api/Registration', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(formData)
            });

            if (!response.ok) {
                throw new Error('Network response was not ok');
            }

            const result = await response.json();
            console.log('Success:', result);
            alert('Registration successful!');
        } catch (error) {
            console.error('Error:', error);
            alert('Error occurred during registration.');
        }
    };

    return (
        <Container className="mt-5">
            <h2>Register</h2>
            <Form onSubmit={handleSubmit}>
                <Form.Group controlId="formName">
                    <Form.Label>Name</Form.Label>
                    <Form.Control
                        type="text"
                        placeholder="Enter your name"
                        name="name"
                        value={formData.name}
                        onChange={handleChange}
                        required
                    />
                </Form.Group>
                <Form.Group controlId="formEmail">
                    <Form.Label>Email</Form.Label>
                    <Form.Control
                        type="email"
                        placeholder="Enter your email"
                        name="email"
                        value={formData.email}
                        onChange={handleChange}
                        required
                    />
                </Form.Group>
                <Form.Group controlId="formPhone">
                    <Form.Label>Phone</Form.Label>
                    <Form.Control
                        type="text"
                        placeholder="Enter your phone number"
                        name="phone"
                        value={formData.phone}
                        onChange={handleChange}
                        required
                    />
                </Form.Group>
                <Form.Group controlId="formAge">
                    <Form.Label>Age</Form.Label>
                    <Form.Control
                        type="number"
                        placeholder="Enter your age"
                        name="age"
                        value={formData.age}
                        onChange={handleChange}
                        required
                    />
                </Form.Group>
                <Button variant="primary" type="submit">
                    Register
                </Button>
            </Form>
        </Container>
    );
};

export default RegistrationForm;
```

## **Backend Documentation**

### **ASP.NET Core Setup**

1. **Create ASP.NET Core Project**

   Create a new ASP.NET Core Web API project:

   ```bash
   dotnet new webapi -n RegistrationFormApp
   ```

2. **Project Structure**

   Ensure your project structure looks like this:

   ```
   RegistrationFormApp/
   ├── Controllers/
   │   └── RegistrationController.cs
   ├── Data/
   │   └── AppDbContext.cs
   ├── Models/
   │   └── User.cs
   ├── Program.cs
   ├── Startup.cs
   └── ...
   ```

### **Database Integration**

1. **Install MySQL NuGet Packages**

   Install the necessary NuGet packages:

   ```bash
   dotnet add package Pomelo.EntityFrameworkCore.MySql
   ```

2. **Configure DbContext**

   Update `Program.cs` to configure the database context:

   ```csharp
   builder.Services.AddDbContext<AppDbContext>(options =>
       options.UseMySql(builder.Configuration.GetConnectionString("DefaultConnection"),
       new MySqlServerVersion(new Version(8, 0, 26))));
   ```

3. **Create and Apply Migrations**

   Create a new migration and update the database:

   ```bash
   dotnet ef migrations add InitialMigration
   dotnet ef database update
   ```

### **API Endpoints**

#### **RegistrationController**

Create a `RegistrationController.cs` file in the `Controllers` folder:

```csharp
using Microsoft.AspNetCore.Mvc;
using RegistrationFormApp.Data;
using RegistrationFormApp.Models;

namespace RegistrationFormApp.Controllers
{
    [ApiController]
    [Route("api/[controller]")]
    public class RegistrationController : ControllerBase
    {
        private readonly AppDbContext _context;

        public RegistrationController(AppDbContext context)
        {
            _context = context;
        }

        [HttpPost]
        public async Task<IActionResult> Post([FromBody] User user)
        {
            if (!ModelState.IsValid)
                return BadRequest(ModelState);

            _context.Users.Add(user);
            await _context.SaveChangesAsync();

            return Ok(user);
        }
    }
}
```

#### **User Model**

Create a `User.cs` file in the `Models` folder:

```csharp
using System.ComponentModel.DataAnnotations;

namespace RegistrationFormApp.Models
{
    public class User
    {
        public int Id { get; set; }

        [Required]
        public string Name { get; set; }

        [Required]
        [EmailAddress]
        public string Email { get; set; }

        [Required]
        public string Phone { get; set; }

        [Required]
        [Range(0, 120)]
        public int Age { get; set; }
    }
}
```

### **Testing**

1. **Frontend Testing**

   Test the frontend by navigating to `http://localhost:3000` and using the registration form.

2. **Backend Testing**

   Test the backend API using tools like Postman:

   - **Endpoint**: `POST http://localhost:5146/api/Registration`
   - **Body** (JSON):
     ```json
     {
       "name": "John Doe",
       "email": "john.doe@example.com",
       "phone": "1234567890",
       "age": 30
     }
     ```

## **Troubleshooting**

1. **Frontend Errors**

   - Ensure all Bootstrap and React-Bootstrap components are correctly imported and used.
   - Verify that the React application is properly configured and dependencies are up-to-date.

2. **Backend Errors**

   - Check the connection string in `appsettings.json` for correct database connection.
   - Ensure that Entity Framework Core migrations are properly created and applied.
   - Verify the API endpoint and ensure it matches the expected URL.

3. **Common Issues**

   - **

CORS Issues**: Ensure that CORS is configured in `Startup.cs` to allow requests from your frontend origin.
   - **Version Mismatches**: Ensure that all libraries and frameworks are compatible and up-to-date.

---

Feel free to adjust any sections based on your specific setup and requirements!
