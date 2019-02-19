from django.db import models


class roleper(models.Model):
    role = models.CharField(max_length=250)
    perr = models.TextField()

    def __int__(self):
        return self.id


class user(models.Model):
    empId = models.PositiveIntegerField(primary_key=True, serialize=False)
    password = models.CharField(max_length=20)
    FName = models.CharField(max_length=250)
    MName = models.CharField(max_length=250)
    LName = models.CharField(max_length=250)
    Email = models.EmailField(max_length=250)
    Phone = models.PositiveIntegerField()
    Address = models.TextField()
    MgName = models.CharField(max_length=250)
    Mg_email = models.CharField(max_length=250)
    Location = models.TextField()
    RId = models.ForeignKey(roleper, on_delete=models.CASCADE)

    def __str__(self):
        return self.FName + "-" + self.MName + "-" + self.LName + "^^^^^" + self.empId.__str__()


