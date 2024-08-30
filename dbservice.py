import psycopg2
# connect to the database
conn = psycopg2.connect(
    host = "localhost",
    dbname = "myduka",
    password = "#iamAfrica",
    user = "postgres",
    port = 5432
)

# declaring a cursor to perform database operation
cur = conn.cursor()

def fetchproducts() :
    cur.execute('SELECT * FROM products')
    products = cur.fetchall()
    return products

# products = fetchproducts()
# print(products)

# def fetchsales() :
#     cur.execute('SELECT * FROM sales')
#     sales = cur.fetchall()
#     return sales

# sales = fetchsales()
# print(sales)

def fetcheddata(a) :
    cur.execute(f'SELECT * FROM {a}')
    all = cur.fetchall()
    return all

# sales = fetcheddata('sales')
# print(sales)

products = fetcheddata('products')
# print(products)

def insertproducts(values) :
    query = 'INSERT INTO products(name,buyingprice,sellingprice,stockquantity) VALUES(%s,%s,%s,%s) '
    cur.execute(query,values)
    conn.commit()

# values = ("paprika",2000,4500,27)
# insertproducts(values)
# products = fetcheddata('products')
# # print(products)

def insertsales(salesvalues) :
    query = 'INSERT INTO sales(productid,quantity,createdat) VALUES(%s,%s,now())'
    cur.execute(query,salesvalues)
    conn.commit()

# salesvalues = (17,68)
# insertsales(salesvalues)
# sales = fetcheddata('sales')
# print(sales)

def profits() :
    query = 'SELECT sum((sellingprice - buyingprice)*quantity) AS Profits,name from products INNER JOIN sales on sales.productid = products.productid group by name;'
    cur.execute(query)
    profits = cur.fetchall()
    return profits

profits = profits()
# print(profits)

def salesperproduct() :
    query = 'SELECT sum(sellingprice*quantity) as totalsales,name from sales inner join products on sales.productid = products.productid group by name order by totalsales DESC'
    cur.execute(query)
    data = cur.fetchall()
    return data

# salesperproduct = salesperproduct()
# print(salesperproduct)

# Query and function per day for sales
def salesperday() :
    query = 'SELECT sum(sellingprice*quantity) as totalsales,DATE(createdat) from sales inner join products on sales.productid = products.productid group by createdat order by totalsales;'
    cur.execute(query)
    data = cur.fetchall()
    return data

# salesperday = salesperday()
# print(salesperday)

def profitsperday() :
    query = 'SELECT sum((sellingprice - buyingprice)*quantity) as profitsperday,DATE(createdat) from sales inner join products on products.productid = sales.productid group by createdat order by profitsperday;'
    cur.execute(query)
    data = cur.fetchall()
    return data

# profitsinaday = profitsperday()
# print(profitsinaday)
# Query and function for profits per day

# Profitsperproduct
def profitsperproduct() :
    query = "SELECT sum((sellingprice - buyingprice) * quantity) as profitsperproduct,name from sales inner join products on products.productid = sales.productid group by name order by profitsperproduct desc"
    cur.execute(query)
    data = cur.fetchall()
    return data

# sales = fetcheddata('sales')
# print(sales)
# print(products)  
# def salesproducts() :
#     cur.execute('Select name,sellingprice,quantity from products inner join sales on sales.productid = products.productid')
#     combined = cur.fetchall()
#     return combined

# combined = salesproducts()
# print(combined)

def insertusers(users) :
    query = "INSERT INTO users(fullname,email,password) values(%s,%s,%s)"
    cur.execute(query,users)
    conn.commit()

#query to checkm if email exists in database 

def checkemail(email) :
    query = "select * from users where email = %s"
    cur.execute(query,(email,))
    data = cur.fetchone()
    if data :
        return data

# def userdata (email,password) :
#     query = "select * from users where email = %s and password = %s"
#     cur.execute(query,(email,password,))
#     data = cur.fetchone()
#     if data :
#         print (data)

# def employees () :
#     cur.execute('SELECT COUNT(gender),language from employees group by language;')
#     employees = cur.fetchall()
#     return employees
# employees = employees()
# print(employees)