from app import db, models

record1 = models.income(name="May Salary", amount=1000)
record2 = models.income(name="June Salary", amount=800)

record3 = models.expense(name="Alsi shop", amount=10)
record4 = models.expense(name="phone bill", amount=20)


db.session.add(record1)
db.session.add(record2)
db.session.add(record3)
db.session.add(record4)
db.session.commit()
