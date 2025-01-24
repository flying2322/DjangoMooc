### CMD

#### Django Shell 
```shell
python manage.py
python manage.py shell

# after join mysql and the command line start with <<<
s = Students.objects.filter(name__contains="李")
s
# query those whose score is greater and equal than --
s = Students.objects.filter(score__gte=80
for i in s:
    print(i.name)
    print(i.score)
    
s = Students.objects.exclude(score__gte=80)
s
# output are like: <QuerySet []>

s = Students.objects.all()

all_1 = Students.objects.all()
all = Students.objects.raw("select * from students;")

a = Students.objects.raw("select id, name from students where name like 't%%';")
for i in a:
    print(i.name)


s = Students.objects.raw("select * from students where name=%s and gender=%s", ["韩梅梅", "女"])
for i in s:
    print(i.name, "--", i.gender)

# generate migration script
python manage.py makemigrations

```


#### Python code in Course for recheck

```python
from django import models


class School(models.Model):
    name = models.CharField(max_length=32)
    address = models.CharField(max_length=64)
    history = models.TextField(null=True)


class Students(models.Model):
    name = models.CharField(max_length=32)
    gender = models.CharField(max_length=2)
    score = models.FloatField()
    join_date = models.DateField(null=True)
    school = models.ForeignKey(School, on_delete=models.CASCADE, null=True)

    class Meta:
        db_table = "students"

    @classmethod
    def get_all(cls):
        cls.objects.all()

    @classmethod
    def get_one(cls, pk):
        return cls.objects.get(pk=pk)


class MyManager(Manager):

    def create_one(self, name, price):
        model = self.model()  # 实例化与自定义的一项管理关联的模型
        model.name = name
        model.price = price
        model.save()
        return model

    def get_all(self):
        return super().all()


class Cake(models.Model):
    name = models.CharField(max_length=32)
    price = models.FloatField()
    manage = MyManager()


class Person(model.Model):
    name = models.CharField(max_length=32)
    age = models.IntegerField()
    gender = models.CharField(max_length=2)


class Card(models.Model):
    number = models.CharField(max_length=32)
    person = models.OneToOneField(Person, on_delete=models.CASCADE)


class Member(models.Model):
    name = models.CharField(max_length=32)
    age = models.IntegerField()
    gender = models.CharField(max_length=2)


class Commmunity(models.Model):
    name = models.CharField(max_length=32)
    create_date = models.DateField(null=True)
    members = models.ManyToManyField(Member, through="Relation")


class Relation(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    community = models.ForeignKey(Commmunity, on_delete=models.CASCADE())
    join_reason = models.CharField(max_length=64, null=True)

```

### add data
```python

class StudentsTestCase(TestCase):
    def setUp(selfself) -> None:
        self.start_time = time.time()

    # Add data
    def test_insert_data(self):
        # Method1: Object manager
        Students.objects.create(name="test", gender="Male", score=99.5)
        print(f"Time Cost: {time.time() - self.start_time}")

        # Method2: Objectify the object
        s = Students(name="test", gender="Male", score="44.1")
        s.save()

        print(f"Time Cost: {time.time() - self.start_time}")

    def tearDown(self) -> None:

```

#### MySql
data migration

Data Model: Add Delete Update Check
#### models.db里面关键的函数
`___contains`
`__startwith`
`__endswith, __gte __lte, __year, __month, __day`
`order_by` 排序
```mysql
select * from migration;
select * from student
desc django_migration
# Insert data
s = Students(name="test", gender="Female", score=56)
s.save()
    
# Filter
s_n = Students.objects.filter(gender='Male')
s_n[0].name

```
# 模型概念

```python
from model_app.models import Students
from django import Q

q1 = Q(score__gt=90)
q2 = Q(gender='Male')
s = Students.objects.filter(q1 & q2)
s
s[0].name
```

## Q查询
```
s_all = Students.objects.all()
[i.name for i in s_all]
# Query those score is > 80 and in start with "韩"
```

## F查询
```
s_all = Students.objects.all()
[i.name for i in s_all]
# Query those score is > 80 and in start with "韩"
```
## 聚合查询

```python
from django import Sum, Avg, Max, Min, Count

avg_score = Students.objects.all().aggregate(Avg("score"))
avg_score
avg_score = Students.objects.aggregate(Avg("score"))


```
## 分组查询
```python
score_avg = Students.objects.values("gender").annotate(Agv("score"))
```

## 综合演练
```python
form django.shortcuts import render


def list_students(request):
    Students.get_all()
    return render(request, "", locals())


python manager.py makemigrations

from model_app.models import Cake
cake = Cake.my_manage.create_one('马卡龙', 34)

[i.name for i in cakes]

# 从多方查一方 集合小写+_set
students = beida.students_set.all()
[i.name for i in students]

# 从一方查多方

```
### 私教
```shell
from model_app.models import *
p1 = Person.object.create(name='张三', age=20, gender="男")
c = Card.objects.create(number='001', person=p1)

# 一对一

```

### 多对多
```python
from model_app.models import *

m1 = Member.objects.create(name="zhangsan", age=20, gender='Male')
m2 = Member.objects.create(name="zhaosi", age=20, gender='Male')
m3 = Member.objects.create(name="xiaoma", age=20, gender='Male')

from datetime import date
c1 = Community.objects.create(name="火花科技社", create_date=date(2008,9,1))
c2 = Community.objects.create(name="数学社", create_date=date(2008,9,1))
c3 = Community.objects.create(name="模型社", create_date=date(2008,9,1))

r1 = Relation.objects.create(member=m1, community=c1, join_reason='好玩')
r1 = Relation.objects.create(member_id=m2.id, community_id=c2.id, join_reason='好玩')

(r2.member, r2.community, r2.join_reason)
# 从主动维护关系的多方进行查询
c = Community.objects.all()
[i.name for i in c]
[(i.id, i.name) for i in c]

c1 = Community.objects.get(id =1)
r = Relation.Objects.filter(commnity = c1)
r
[i.member.name for i in r]

all_members = c1.members.all()
[i for i in all_members]
[i.name for i in all_members]

# 从不维护关系的多方进行查询
m = Member.objects.all()
[(i.id, i.name) for i in m]

c1 = Member.objects.get(id=1)
c1.name

all_community = c1.community_set.all()
[i.name for i in all_community]
```

## 模型关系--模型外键自关联
### 1.引用关系
方式一：“一对多”自引用--ForeignKey

方式二：“一对一”自应用--OneToOneField

```python

class Emp(models.Model):
    name = models.CharField(max_length=32)
    age = models.IntegerField()
    manager = models.ForeignKey("set", on_delete=models.CASCADE, null=True)

class Spy(models.Model):
    name = models.CharField(max_length=32)
    age = models.IntegerField()
    leader = models.OneToOneFiled("self", on_delete=models.CASCADE, null=True)
```
### 制作迁移脚本
```python
python manage.py makemigrations

from model_app.models import *
boss = Emp.objects.create(name='Zhangsan', age=55)
mp1 = Emp.objects.create(name='Xiaoli', age=45, manager=boss)
mp2 = Emp.objects.create(name='Xiaozhang', age=35, manager=boss)
e1 = Emp.objects.create(name='Xiaowang', age=25, manager=mp1)
e2 = Emp.objects.create(name='Xiaodai', age=26, manager=mp2)
e3 = Emp.objects.create(name='Xiaohong', age=27, manager_id=mp2.id)

e = mp2.emp_set.all()
[i.name for i in e]
mp2.manager.name

# Try to delete boss
boss
boss.delete()
Emp.objects.all()
exit()
```

### Case 2
```python
from model_app.models import *
boss = Spy.objects.create(name="戴笠", age=60)
s1 = Spy.objects.create(name="毛人凤", age=50, leader=boss)
s2 = Spy.objects.create(name="张三", age=30, leader=s1)
s2.leader.name
boss.spy.name # 不维护关系的一方查询
```

# URL技术
## Django URL反向解析
在子路由