from django.db import models
from django.conf import settings
from teacher.models import Course
from django.dispatch import receiver


User = settings.AUTH_USER_MODEL
# Create your models here.



class Message(models.Model) :
    user    = models.ForeignKey(User,related_name="messages",on_delete=models.CASCADE)
    timestamp  = models.DateTimeField(auto_now_add=True)
    content   =   models.TextField()
    # read_by=models.ManyToManyField(Contact,related_name='messages_read')

    def __str__(self) :
        return self.contact.user.username


class Chat(models.Model) :
    participants = models.ManyToManyField(User,related_name='chats')
    messages = models.ManyToManyField(Messages,blank=True,related_name='chat')
    course = models.OneToOneField(Course ,related_name = "general_chat",on_delete=model.CASCADE)



    def __str__(self) :

        return "{}".format(self.pk)


    def last_10_messages(self) :
        return self.messages.objects.all().order_by('-timestamp')[:10]




@receiver(post_save ,sender = Course)
def create_chat(sender,instance,created,**kwargs) :
    if created :
        Chat.objects.create(participants = instance.students.all(),course=instance) 

