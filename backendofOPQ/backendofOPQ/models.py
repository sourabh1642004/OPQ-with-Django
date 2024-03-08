Sure, here's a simple model for student registration in Django:

```python
# In your app's models.py file

from django.db import models

class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20)
    address = models.TextField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
```

In this model:

- We define a `Student` model with fields for first name, last name, date of birth, email, phone number, and address.
- `first_name` and `last_name` are CharFields with a maximum length of 100 characters.
- `date_of_birth` is a DateField.
- `email` is an EmailField with the unique constraint, ensuring each email address is unique in the database.
- `phone_number` is a CharField with a maximum length of 20 characters.
- `address` is a TextField, suitable for longer text entries.

You can further customize this model based on your specific requirements, such as adding more fields like gender, grade level, or any other relevant information for student registration. After defining the model, don't forget to run migrations (`python manage.py makemigrations` and `python manage.py migrate`) to apply the changes to your database schema.