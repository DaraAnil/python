from mongoengine import Document, EmbeddedDocument, fields

# Create your models here.

class Employee(Document):
    empId = fields.StringField(max_length=10, required=True, null=False)
    empName = fields.StringField(max_length=100, required = True)
    workLocation = fields.StringField(max_length=100, required =False)
    projects = fields.EmbeddedDocumentListField(Project)
    skills = fields.EmbeddedDocumentListField(Skill)

class Project(EmbeddedDocument):
    projectId = fields.StringField(max_length=10, required=True, null=False)
    projectName = fields.StringField(max_length=100, required=True)
    startDate = fields.DateField()
    endDate = fields.DateField() 


class Skills(EmbeddedDocument):
    technology = fields.StringField(max_length=50, required=True)
    experience = fields.IntField(min_value=2,max_value=25,required=True)
    level = fields.StringField(max_length=27, required=True)

