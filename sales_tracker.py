class SalesPerson:
    def __init__(self, id_number, name, quantity_sold=0, total_revenue=0.0):
        self._id_number = id_number
        self._name = name
        self._quantity_sold = quantity_sold
        self._total_revenue = total_revenue

    # Getter methods
    @property
    def id_number(self):
        return self._id_number

    @property
    def name(self):
        return self._name

    @property
    def quantity_sold(self):
        return self._quantity_sold

    @property
    def total_revenue(self):
        return self._total_revenue

    # Setter methods
    @id_number.setter
    def id_number(self, id_number):
        self._id_number = id_number

    @name.setter
    def name(self, name):
        self._name = name

    # Method to add to the quantity sold and update total revenue
    def sell_widgets(self, quantity):
        self._quantity_sold += quantity
        self._total_revenue += quantity * 9.99

greg = SalesPerson(1001, "Greg")
greg.sell_widgets(42)
greg.sell_widgets(78)
print(greg.id_number)
print(greg.quantity_sold)
print(greg.total_revenue)
