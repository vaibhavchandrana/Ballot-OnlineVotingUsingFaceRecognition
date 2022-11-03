from django.db import models

# Create your models here.
class User(models.Model):
    name=models.CharField(max_length=200)
    email=models.EmailField()
    phone=models.CharField(max_length=15)
    age =models.IntegerField()
    password=models.CharField(max_length=500)
    voter_id=models.IntegerField()
    profile=models.ImageField(null=True,blank=True)
    flag=models.IntegerField()

    def register(self):
        self.save()

    def isExists(mail):
        if User.objects.filter(email=mail):
            return True
        else:
            return False


    @staticmethod
    def get_user_by_email(email):
        try:
            return User.objects.get(email=email) # return one object only
        except:
            return False
    
    @staticmethod
    def get_user_by_id(cnd_id):
        return User.objects.filter(id=cnd_id)

class Candidate(models.Model):
    name=models.CharField(max_length=20)
    party=models.CharField(max_length=100)
    votes=models.IntegerField(default=0)
     
    @staticmethod
    def get_all_candidates():
        return Candidate.objects.all()

    @staticmethod
    def get_candidate_by_cnd_id(cnd_id):
        return Candidate.objects.filter(id=cnd_id)