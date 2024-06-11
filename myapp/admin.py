from django.contrib import admin
from .models import PublicationStatu
from .models import Administrative
from .models import User
from .models import Editor
from .models import Presenter
from .models import ElementPresenter
from .models import ElementVideo
from .models import Element
from .models import Project
from .models import News
from .models import Fechas



# Register your models here.
admin.site.register(PublicationStatu)
admin.site.register(Administrative)
admin.site.register(User)
admin.site.register(Editor)
admin.site.register(Presenter)
admin.site.register(ElementPresenter)
admin.site.register(ElementVideo)
admin.site.register(Element)
admin.site.register(Project)
admin.site.register(News)
admin.site.register(Fechas)
