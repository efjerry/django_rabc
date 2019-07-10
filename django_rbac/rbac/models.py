from django.db import models


class Permission(models.Model):
    """
    权限表
    """
    url = models.CharField(max_length=256, verbose_name='权限', unique=True)
    title = models.CharField(max_length=32, verbose_name='标题')

    def __str__(self):
        return self.title


class Role(models.Model):
    """
    角色表
    """
    name = models.CharField(max_length=32, verbose_name='角色名称')
    permissions = models.ManyToManyField('Permission', blank=True)  # blank=True 可为空

    def __str__(self):
        return self.name


class User(models.Model):
    """
    用户表
    """
    name = models.CharField(max_length=32, verbose_name='用户名')
    pwd = models.CharField(max_length=32, verbose_name='密码')
    roles = models.ManyToManyField('Role', blank=True)

    def __str__(self):
        return self.name

