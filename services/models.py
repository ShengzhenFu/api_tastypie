from django.db import models
import uuid


class Product(models.Model):
    name = models.CharField(max_length=30)
    product_type = models.CharField(max_length=50)
    price = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Order(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    product = models.ForeignKey('Product', on_delete=models.PROTECT)

    def __str__(self):
        return self.id


class Team(models.Model):
    tid = models.CharField(max_length=30, primary_key=True)
    team_name = models.CharField(max_length=100)
    team_owner = models.CharField(max_length=100)
    team_owner_email = models.CharField(max_length=100)

    def __str__(self):
        return self.tid


class TechnicalService(models.Model):
    ts_id = models.CharField(primary_key=True, max_length=30)
    ts_name = models.CharField(max_length=100)
    tid = models.ForeignKey('Team', on_delete=models.PROTECT)
    # team_name = models.ForeignKey('Team', on_delete=models.PROTECT)
    ts_ops_mgr = models.CharField(max_length=100)
    ts_ops_mgr_email = models.CharField(max_length=100)
    ts_dev_mgr = models.CharField(max_length=100)
    ts_dev_mgr_email = models.CharField(max_length=100)
    ts_qa_mgr = models.CharField(max_length=100)
    ts_qa_mgr_email = models.CharField(max_length=100)

    def __str__(self):
        return self.ts_id


class Server(models.Model):
    server_name = models.CharField(max_length=50)
    server_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    tid = models.ForeignKey('Team', related_name='team_id', on_delete=models.PROTECT)
    # team_name = models.ForeignKey('Team', on_delete=models.PROTECT)
    ts_id = models.ForeignKey('TechnicalService', on_delete=models.PROTECT)
    # ts_name = models.ForeignKey('TechnicalService', on_delete=models.PROTECT)
    server_status = models.CharField(max_length=10)
    server_environment = models.CharField(max_length=10)
    server_function = models.CharField(max_length=20)
    server_location = models.CharField(max_length=20)
    ts_ops_mgr = models.CharField(max_length=50)
    ts_ops_mgr_email = models.CharField(max_length=50)

    def __str__(self):
        return self.server_name

