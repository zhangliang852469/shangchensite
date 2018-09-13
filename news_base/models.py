from django.db import models
from django.utils.timezone import now

# Create your models here.

# 新闻
class News(models.Model):
    title = models.CharField('标题', max_length=100, blank=True, default='')
    image = models.ImageField('图片', upload_to="media/newspictures", blank=True)
    date = models.DateTimeField('日期', auto_now_add=True)
    create_time = models.DateField('创建日期', default=now)
    body = models.TextField('正文')


    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-create_time']
        verbose_name = '新闻'
        verbose_name_plural = verbose_name


#交易记录
class Events(models.Model):
    title = models.CharField('标题', max_length=100, default='')
    image = models.ImageField('上传交易记录', upload_to='media/evetsimages', blank=True)
    create_time = models.DateTimeField('上传时间', auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-create_time']
        verbose_name = '交易记录'
        verbose_name_plural = verbose_name


# 联系方式

class Imformation(models.Model):
    name = models.CharField('姓名', max_length=68, default='如张三')
    tel  = models.CharField('电话', max_length=100, default='', )
    sub = models.TextField('留言', default='如：求职/办理业务', blank=True, null=True)
    create_time = models.DateField('时间', default=now)


    def __str__(self):
        return self.name

    class Meta:
        ordering = ('-create_time',)
        verbose_name = '留言信息'
        verbose_name_plural = verbose_name


class About(models.Model):
    title = models.CharField('简要介绍', max_length=128)
    text = models.TextField('详细介绍')
    img = models.ImageField('配图', upload_to='media/about')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '尚辰保理介绍'
        verbose_name_plural = verbose_name

# 欢迎合作
class  Cooperation(models.Model):
    text = models.TextField('欢迎合作')
    date = models.DateField('填写日期', auto_now_add=now)

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = '合作邀请文案'
        verbose_name_plural = verbose_name


class Services(models.Model):
    title = models.CharField('业务名称', max_length=128)
    text = models.TextField('服务详细')
    img = models.ImageField('配图', upload_to='media/services')
    creat = models.DateTimeField('编写日期', auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '服务内容'
        verbose_name_plural = '服务内容'
        ordering = ('-creat',)