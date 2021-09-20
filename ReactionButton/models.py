from django.conf import settings
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
from home.models import *

# Create your models here.
class ReactionType(models.Model):
    name = models.TextField(_('name'))
    number = models.IntegerField(_('number')) # for Mr. Maegawa
    description = models.TextField(_('description'), null=True)

    def __str__(self):
        return "(%d) %s" % (self.number, self.name)

class Reaction(models.Model):
    count = models.IntegerField(_('count'))
    reaction_type = models.ForeignKey(
        ReactionType, on_delete=models.CASCADE
    )
    dest_user = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE
    )
    conference = models.ForeignKey(
        Conference, on_delete=models.CASCADE
    )

    def __str__(self):
        return "%s -> %s : %d" % (str(self.reaction_type), str(self.dest_user), self.count)

    @classmethod
    def getReactionsByEachPresenter(cls, conf):
        result = []
        pres = Presenter.objects.filter(conference=conf).order_by('user')
        for pre in pres:
            reacs = []
            reac_raw = cls.objects.filter(dest_user=pre.user, conference=conf)
            sum = 0
            for rt in ReactionType.objects.all().order_by("number"):
                r = reac_raw.filter(reaction_type=rt).first()
                reacs.append(r)
                if r != None:
                    sum += r.count
            result.append({
                'presenter' : pre,
                'reactions' : reacs,
                'sum' : sum
            })
        result.sort(key=lambda x: x['sum'], reverse=True)
        return result
