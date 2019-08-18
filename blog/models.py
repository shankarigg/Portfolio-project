from django.db import models

class BlogPage(models.Model):
    title = models.CharField(max_length=20)
    pub_date = models.DateTimeField('date published')
    msg_content = models.TextField()
    blog_img = models.ImageField(upload_to='blogimages/')

    def __str__(self):
        return self.title
        
    def mod_date(self):
        return self.pub_date.strftime('%b %e %Y')

    def summary(self):
        return self.msg_content[:100]
