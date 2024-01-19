# myapp/views.py
from django.shortcuts import render
from django.http import JsonResponse
import mysql.connector

def get_data(request):
    category = request.GET.get('category')

    # Replace the connection parameters with your correct MySQL details
    connection = mysql.connector.connect(
        host='localhost',
        database='customer',
        user='root',
        password='1234'
    )

    cursor = connection.cursor()

    # Example query
    query = f'SELECT * FROM {category}_table'  # Adjust table name based on category
    cursor.execute(query)

    # Fetch and return the results
    rows = cursor.fetchall()

    # Get column names from the cursor description
    columns = [column[0] for column in cursor.description]

    # Convert results to a list of dictionaries
    result = [dict(zip(columns, row)) for row in rows]

    # Close the cursor and connection
    cursor.close()
    connection.close()

    return JsonResponse(result, safe=False)

def dropdown(request):
    return render(request, 'dropdown.html')
