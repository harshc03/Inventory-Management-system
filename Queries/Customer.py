class Query:
    ORDER_STATUS = """
                Select FoodDetails,FoodTotal 
                from FoodOrder
                where CustomerId=%s
                and IsComplete=0
                order by FoodOrderId
            """

    GET_FOOD_PRICE = """Select FoodName,FoodPrice
                                from FoodMenu
                                where FoodName in (%s)"""


    RECENT_ORDERS = """Select FoodDetails, FoodTotal,IsComplete,OrderDate
                from FoodOrder
                where CustomerId=%s
                order by FoodOrderId DESC"""

    GET_MENU_DETAILS = """Select FoodMenuId,FoodName,FoodPrice
                from FoodMenu
                where FoodType=%s
        """

    INSERT_ORDER = """
            Insert into FoodOrder(CustomerId,FoodDetails,FoodTotal,OrderDate)
            Values(%s,%s,%s,%s)"""

