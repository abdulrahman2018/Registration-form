# Project Documentation

## Overview

This documentation provides an overview of the project, detailing the technologies used, project setup, and important configurations. The project involves a React frontend and a .NET Core backend, with database management handled through MySQL Workbench.

## Technologies Used

- **Frontend**: React.js with Bootstrap
- **Backend**: ASP.NET Core
- **Database**: MySQL Workbench

## Project Structure

- **Frontend**: 
  - React.js application for user registration
  - Bootstrap for styling
  - API calls to the backend for data operations

- **Backend**: 
  - ASP.NET Core Web API
  - Entity Framework Core for ORM
  - MySQL for database operations

## Setup Instructions

### Frontend Setup

1. **Install Dependencies**: Navigate to the frontend directory and run the following command:
   ```bash
   npm install
   ```

2. **Start the Development Server**: 
   ```bash
   npm start
   ```

3. **Access the Application**: Open a web browser and go to `http://localhost:3000` to view the application.

### Backend Setup

1. **Install Dependencies**: Navigate to the backend directory and run:
   ```bash
   dotnet restore
   ```

2. **Apply Migrations**:
   ```bash
   dotnet ef database update
   ```

3. **Run the Application**: 
   ```bash
   dotnet run
   ```

4. **Access the API**: Open a web browser and go to `http://localhost:5146` to interact with the API.

## Database Configuration

### Using MySQL Workbench

For this project, **MySQL Workbench** was used for database management. Here are the details:

- **Database Name**: `BUERegistration`
- **Tables**: Created as per the Entity Framework migrations
- **Connection String**: 
  ```json
  "DefaultConnection": "Server=localhost;Database=BUERegistration;User=root;Password=YourPasswordHere"
  ```

### Important Note

For this project, I utilized **MySQL Workbench** for database management instead of **MS SQL Server**. This choice was due to the availability of MySQL Workbench on my Mac, which facilitated a smoother development process. All database operations, including schema creation, data insertion, and query execution, were performed using MySQL Workbench. The project remains fully functional and integrates seamlessly with the React frontend and .NET Core backend, ensuring consistent and reliable performance.

If you have any questions or need further clarification on the use of MySQL Workbench, please feel free to reach out.

## API Endpoints

### Registration

- **URL**: `/api/Registration`
- **Method**: POST
- **Description**: Adds a new registration to the database.

### Retrieve Registrations

- **URL**: `/api/Registration`
- **Method**: GET
- **Description**: Retrieves all registrations from the database.

## Troubleshooting

- **Issue**: Data is not saving to the database.
  - **Solution**: Ensure that the backend is running and properly connected to the database. Verify that the API endpoint is correctly configured in the frontend.

- **Issue**: Cannot access the API from the frontend.
  - **Solution**: Check CORS settings in the backend configuration to ensure requests from the frontend are allowed.

## Conclusion

This documentation provides a comprehensive overview of the project setup, technology stack, and database management. The use of MySQL Workbench instead of MS SQL Server was a strategic decision to align with the development environment on my Mac. The application is designed to be fully functional, integrating both frontend and backend components seamlessly.

For further information or assistance, please contact me.
