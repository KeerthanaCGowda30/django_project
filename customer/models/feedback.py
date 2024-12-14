from django.db import models
from .customer import Customer

class Feedback(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)  # Customer giving feedback
    message = models.TextField()  # Feedback content
    rating = models.PositiveIntegerField(choices=[(i, f"{i} Stars") for i in range(1, 6)])  # Rating (1 to 5 stars)
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp when feedback was created

    def __str__(self):
        return f"{self.customer.name} - {self.rating} Stars"
