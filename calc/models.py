from django.db import models

# Create your models here.
class Destination(models.Model):
    
    name=models.CharField(max_length=100)
    description=models.TextField()
    img=models.ImageField(upload_to='pics')
    price=models.IntegerField()
    offer=models.BooleanField(default=False)


# class employee(models.Model):
#     id:models.CharField(max_length=20)
#     name:models.CharField(max_length=20)

#     class Meta:
#         db_table="employee"


class Registration(models.Model):
    first_name=models.CharField(max_length=20)
    last_name=models.CharField(max_length=20)
    username=models.CharField(max_length=20)
    email=models.EmailField(max_length=20)
    password=models.CharField(max_length=20)
    password=models.CharField(max_length=20)




class Position(models.Model):
    title = models.CharField(max_length=20)

    def __str__(self):
        return self.title


class Employee(models.Model):
    ename=models.CharField(max_length=20)
    email=models.CharField(max_length=20)
    econtact= models.IntegerField()
    # position =models.ForeignKey(Position,on_delete=models.CASCADE)




class kaam(models.Model):
    ename=models.CharField(max_length=20)
    email = models.CharField(max_length=20)
    econtact = models.IntegerField()
    position = models.ForeignKey(Position,on_delete=models.CASCADE)



   


