from flask_sqlalchemy import BaseQuery


class SoftDeleteQuery(BaseQuery):
    def __new__(cls, *args, **kwargs):
        return super(SoftDeleteQuery, cls).__new__(cls)

    def __init__(self, entities, *args, **kwargs):
        super().__init__(entities, *args, **kwargs)

        model = self._only_full_mapper_zero("get").class_
        if hasattr(model, "deleted_at"):
            self._soft_delete_filter_applied = True
            self = self.filter(model.deleted_at.is_(None))
