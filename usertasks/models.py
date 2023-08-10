from django.db import models

# Create your models here.

choices  = ( ('C', 'Completed'),
            ('O', 'Ongoing'),
             ('P', 'Pending') )

priority = (('L', 'Low'),
            ('M', 'Medium'),
            ('H', 'High'))

class Tasks(models.Model):
    title = models.CharField(max_length=225)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    # description = models.TextField()
    dueDate = models.DateTimeField()
    status = models.CharField(max_length=10,)
    priority = models.CharField( max_length=10)
    creator = models.ForeignKey('auth.User', on_delete=models.CASCADE)

    class Meta:
        ordering = ['createdAt']
    
