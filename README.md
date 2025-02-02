# Chat Assistant for SQLite Database
## Overview
This is a Python-based chat assistant that interacts with an SQLite database to answer user queries in natural language. The assistant converts user queries into SQL commands, fetches data from the database, and provides clear, formatted responses.

The project is designed to evaluate the ability to design, implement, and deploy a functional chat assistant that works seamlessly with an SQLite database.

# Features
The chat assistant supports the following types of queries:

-- "Show me all employees in the [department] department."
-- "Who is the manager of the [department] department?"
-- "List all employees hired after [date]."
-- "What is the total salary expense for the [department] department?"
Additionally, the assistant:

Gracefully handles invalid queries.
Returns meaningful messages when no results are found.
Handles incorrect department names or invalid input formats.

# Technologies Used
Python : Core programming language.
Flask : Web framework for building the API.
SQLite : Lightweight database for storing employee and department data.
Render : Hosting platform for deployment.

# Deployment
The chat assistant is deployed and accessible via the following public URL:

### Public URL : https://chatassistant-l79p.onrender.com
To deploy the app yourself:

Push the code to a GitHub repository.
Use a hosting platform like Render or Heroku to deploy the app.
Follow the platform's instructions to set up the environment and start the app.

# Example Queries and Responses
## Query 1: Show All Employees in a Department
### Request :

{
  "query": "Show me all employees in the Sales department."
}
