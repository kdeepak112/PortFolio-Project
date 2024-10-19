from django.db import models
import uuid 
# Create your models here.
class contactRequest(models.Model):
    request_id = models.UUIDField(default=uuid.uuid4, primary_key=True)  # Use uuid.uuid4 for automatic generation
    requested_on = models.DateTimeField(auto_now_add=True,null=True)
    name = models.CharField(max_length=20)
    email = models.EmailField()
    subject = models.TextField()
    message = models.TextField()

    def __str__(self) -> str:
        return super().__str__()