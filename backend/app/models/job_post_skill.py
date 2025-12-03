from app.database import db

job_post_skills = db.Table(
    "job_post_skills",
    db.Column("job_post_id", db.Integer, db.ForeignKey(
        "job_posts.id"), primary_key=True),
    db.Column("skill_id", db.Integer, db.ForeignKey(
        "skills.id"), primary_key=True)
)
