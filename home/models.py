from django.conf import settings
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model

class Conference(models.Model):
    generation = models.IntegerField(_('generation'))
    number = models.IntegerField(_('number'))
    subtitle = models.TextField(_('subtitle'))
    event_date = models.DateTimeField(_('event date'), default=timezone.now)
    description = models.TextField(_('description'), null=True)
    # auto_now_add はインスタンスの作成(DBにINSERT)する度に更新
    created_at = models.DateTimeField(_('created at'), auto_now_add=True)
    # # auto_now=Trueの場合はモデルインスタンスを保存する度に現在の時間で更新
    updated_at = models.DateTimeField(_('updated at'), auto_now=True)

    def __str__(self):
        return self.title()

    def title(self):
        return "シーズン%d 第%d回 遼平会" % (self.generation, self.number)

    @classmethod
    def getConferenceById(cls, conf_id):
        if conf_id == -1:
            return cls.getCurrentConference()
        return cls.objects.filter(id=conf_id).first()

    @classmethod
    def getCurrentConference(cls):
        conf = Variable.get().current_conference
        conf_id = conf.id
        return cls.objects.filter(id=conf_id).first()

class Presenter(models.Model):
    user = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE
    )
    conference = models.ForeignKey(
        Conference, on_delete=models.CASCADE
    )

    def __str__(self):
        return str(self.user) + " : " + str(self.conference)

class Variable(models.Model):
    current_conference = models.ForeignKey(
        Conference, on_delete=models.CASCADE
    )

    def __str__(self):
        return str(self.current_conference)

    @classmethod
    def get(self):
        return Variable.objects.first()
