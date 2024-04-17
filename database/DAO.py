from database.DB_connect import DBConnect


class DAO():

    @staticmethod
    def get_anni():
        cnx = DBConnect.get_connection()
        if cnx==None:
            print("errore di connessione!")
            return None
        cursor = cnx.cursor()
        query = """SELECT DISTINCT YEAR(Date) as Year 
                    FROM go_daily_sales"""
        cursor.execute(query)
        anni=[]
        for row in cursor:
            anni.append(row)
        cursor.close()
        cnx.close()
        return anni

    @staticmethod
    def get_brands():
        cnx = DBConnect.get_connection()
        if cnx == None:
            print("errore di connessione!")
            return None
        cursor = cnx.cursor()
        query = """SELECT DISTINCT Product_brand 
                        FROM go_products"""
        cursor.execute(query)
        brands = []
        for row in cursor:
            brands.append(row)
        cursor.close()
        cnx.close()
        return brands

    @staticmethod
    def get_retailers():
        cnx = DBConnect.get_connection()
        if cnx == None:
            print("errore di connessione!")
            return None
        cursor = cnx.cursor(dictionary=True)
        query = """SELECT DISTINCT * 
                            FROM go_retailers"""
        cursor.execute(query)
        retailers = []
        for row in cursor:
            retailers.append(row)
        cursor.close()
        cnx.close()
        return retailers

    @staticmethod
    def top_vendite(anno, brand, retailer):
        cnx = DBConnect.get_connection()
        if cnx == None:
            print("errore di connessione!")
            return None
        cursor = cnx.cursor(dictionary=True)
        query = """SELECT * 
                    FROM go_daily_sales as gds, go_products as gp
                    WHERE YEAR(gds.Date)=COALESCE(%s, YEAR(gds.Date)) AND gds.Retailer_code=COALESCE(%s, gds.Retailer_code)
                     AND gp.Product_brand=COALESCE(%s, gp.Product_brand) AND gds.Product_number=gp.Product_number
                    ORDER BY Unit_sale_price*Quantity DESC"""
        cursor.execute(query, (anno, retailer, brand,))
        top = cursor.fetchmany(5)
        cursor.fetchall()
        cursor.close()
        cnx.close()
        return top

    @staticmethod
    def analizza_vendite(anno, brand, retailer):
        cnx = DBConnect.get_connection()
        if cnx == None:
            print("errore di connessione!")
            return None
        cursor = cnx.cursor(dictionary=True)
        query = """SELECT COUNT(distinct gds.Retailer_code) as venditori, COUNT(distinct gds.Product_number) as prodotti, SUM(gds.Quantity*gds.Unit_sale_price) as ricavi, COUNT(*) as vendite
                    FROM go_sales.go_daily_sales as gds, go_sales.go_products as gp
                    WHERE YEAR(gds.Date)=COALESCE(%s, YEAR(gds.Date)) AND gds.Retailer_code=COALESCE(%s, gds.Retailer_code) 
	                AND gp.Product_brand=COALESCE(%s, gp.Product_brand) AND gds.Product_number=gp.Product_number"""
        cursor.execute(query, (anno, retailer, brand,))
        analisi = []
        for row in cursor:
            analisi.append(row)
        cursor.close()
        cnx.close()
        return analisi


if __name__ == "__main__":
    res = DAO.top_vendite("2017",None,None)
    for row in res:
        print(row)