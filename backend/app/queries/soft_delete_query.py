from flask_sqlalchemy.query import Query


class SoftDeleteQuery(Query):
    _with_deleted = False

    # Usage: Model.query.with_deleted().all() to include soft-deleted records
    def with_deleted(self):
        q = self._clone()
        q._with_deleted = True
        return q

    def __iter__(self):
        if not self._with_deleted:
            model = self._only_full_mapper_zero("get").class_
            if hasattr(model, "deleted_at"):
                self = self.filter(model.deleted_at.is_(None))
        return super().__iter__()
