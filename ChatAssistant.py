from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

# Function to execute SQL queries
def execute_query(query):
    conn = sqlite3.connect('assignment.db')
    cursor = conn.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    conn.close()
    return result

# Route to handle chat queries
@app.route('/chat', methods=['POST'])
def chat():
    user_query = request.json.get('query')
    print(f"User Query: {user_query}")
    
    # Example: Handle specific queries
    if "show me all employees in the" in user_query.lower():
        department = user_query.split("department")[0].split("in the")[-1].strip()
        query = f"SELECT * FROM Employees WHERE Department = '{department}'"
        result = execute_query(query)
        return jsonify({"response": result})

    elif "who is the manager of the" in user_query.lower():
        department = user_query.split("department")[0].split("of the")[-1].strip()
        query = f"SELECT Manager FROM Departments WHERE Name = '{department}'"
        result = execute_query(query)
        return jsonify({"response": result[0][0] if result else "No manager found"})

    elif "list all employees hired after" in user_query.lower():
        date = user_query.split("after")[-1].strip()
        query = f"SELECT * FROM Employees WHERE Hire_Date > '{date}'"
        result = execute_query(query)
        return jsonify({"response": result})

    elif "what is the total salary expense for the" in user_query.lower():
        department = user_query.split("department")[0].split("for the")[-1].strip()
        query = f"SELECT SUM(Salary) FROM Employees WHERE Department = '{department}'"
        result = execute_query(query)
        return jsonify({"response": result[0][0] if result[0][0] else "No data found"})

    # New Query 1: Show the highest-paid employee in a department
    elif "highest paid employee" in user_query.lower() and "department" in user_query.lower():
        department = user_query.split("department")[0].split("in the")[-1].strip()
        query = f"SELECT Name, MAX(Salary) FROM Employees WHERE Department = '{department}'"
        result = execute_query(query)
        return jsonify({"response": result[0] if result else "No data found"})

    # New Query 2: Show the average salary in a department
    elif "what is the average salary in the" in user_query.lower():
        department = user_query.split("department")[0].split("in the")[-1].strip()
        query = f"SELECT AVG(Salary) FROM Employees WHERE Department = '{department}'"
        result = execute_query(query)
        return jsonify({"response": round(result[0][0], 2) if result[0][0] else "No data found"})

    # New Query 3: Show all departments and their managers
    elif "list all departments and their managers" in user_query.lower():
        query = "SELECT Name, Manager FROM Departments"
        result = execute_query(query)
        return jsonify({"response": result})

    else:
        return jsonify({"response": "Sorry, I don't understand that query."})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
    
    
    
