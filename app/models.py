from django.db import models
def main():
    conn_string = "host='localhost' dbname='web' user='postgres' password='fulin0908B'"
    # Local database

# Create your models here.
class Greeting(models.Model):
    id = models.AutoField(primary_key=True)
    when = models.DateTimeField("date created", auto_now_add=True)
