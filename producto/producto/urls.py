from igs_app_base.utils.utils import create_view_urls

from .vw import Create
from .vw import Delete
from .vw import DeleteMany
from .vw import List
from .vw import Read
from .vw import Update

obj = 'producto'
app_label = 'producto'

urlpatterns = create_view_urls(
    app_label, obj,
    List, Create, Update, Read, DeleteMany, Delete)
