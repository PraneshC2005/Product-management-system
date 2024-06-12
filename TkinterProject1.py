import sqlite3
import streamlit as st
import pandas as pd  # Make sure to import pandas

# Initialize the database connection
def init_db():
    with sqlite3.connect('database.db') as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS product (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                price INTEGER NOT NULL,
                model_name TEXT NOT NULL,
                year_of_launch INTEGER NOT NULL
            )
        ''')
        conn.commit()

# Function to execute database queries
def run_query(query, parameters=()):
    with sqlite3.connect('database.db') as conn:
        cursor = conn.cursor()
        result = cursor.execute(query, parameters)
        conn.commit()
    return result

# Function to get products from the database
def get_products():
    query = 'SELECT * FROM product ORDER BY name DESC'
    db_rows = run_query(query)
    return db_rows.fetchall()

# Function to validate user input
def validation(name, price, model_name, year_of_launch):
    try:
        int(year_of_launch)
        int(price)
        return len(name) != 0 and len(model_name) != 0
    except ValueError:
        st.error('Year of Launch and Price must be integers')
        return False

# Function to add a new product
def add_product(name, price, model_name, year_of_launch):
    if validation(name, price, model_name, year_of_launch):
        query = 'INSERT INTO product VALUES(NULL, ?, ?, ?, ?)'
        parameters = (name, int(price), model_name, int(year_of_launch))
        run_query(query, parameters)
        st.success(f'Product {name} added Successfully')
    else:
        st.error('All fields are required')

# Function to delete a product
def delete_product(product_id):
    query = 'DELETE FROM product WHERE id = ?'
    run_query(query, (product_id,))
    st.success(f'Record {product_id} deleted Successfully')

# Function to update a product
def edit_product(product_id, new_name, new_price, new_model_name, new_year_of_launch):
    query = 'UPDATE product SET name = ?, price = ?, model_name = ?, year_of_launch = ? WHERE id = ?'
    parameters = (new_name, int(new_price), new_model_name, int(new_year_of_launch), product_id)
    run_query(query, parameters)
    st.success(f'Record {product_id} updated Successfully')

# Streamlit UI
st.set_page_config(page_title='Products Application', layout='wide')
st.title('Products Application')
st.sidebar.header('Add New Product')

# Form to add a new product
with st.sidebar.form(key='add_product_form'):
    name = st.text_input('Name')
    price = st.text_input('Price')
    model_name = st.text_input('Model Name')
    year_of_launch = st.text_input('Year of Launch')
    submit_button = st.form_submit_button(label='Add Product')

    if submit_button:
        add_product(name, price, model_name, year_of_launch)

# Display the products
st.header('Product List')
products = get_products()

if products:
    product_df = pd.DataFrame(products, columns=['ID', 'Name', 'Price', 'Model Name', 'Year of Launch'])
    st.dataframe(product_df)

    selected_product_id = st.selectbox('Select a product to edit or delete', product_df['ID'])
    selected_product = product_df[product_df['ID'] == selected_product_id].iloc[0]

    # Edit product
    st.subheader('Edit Product')
    with st.form(key='edit_product_form'):
        new_name = st.text_input('New Name', value=selected_product['Name'])
        new_price = st.text_input('New Price', value=selected_product['Price'])
        new_model_name = st.text_input('New Model Name', value=selected_product['Model Name'])
        new_year_of_launch = st.text_input('New Year of Launch', value=selected_product['Year of Launch'])
        update_button = st.form_submit_button(label='Update Product')

        if update_button:
            edit_product(selected_product_id, new_name, new_price, new_model_name, new_year_of_launch)

    # Delete product
    if st.button('Delete Product'):
        delete_product(selected_product_id)
else:
    st.info('No products found')

# Initialize the database when the script runs
if __name__ == '__main__':
    init_db()
    st.experimental_rerun()
