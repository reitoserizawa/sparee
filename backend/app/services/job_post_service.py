from app.models.job_post import JobPost
from app.models.company import Company
from app.services.address_service import AddressService


class JobPostService:
    @staticmethod
    def get_from_company(company: Company) -> list[JobPost]:
        return JobPost.get_by_company(company)

    def create_job_post(self, company, data) -> JobPost:
        address_data = data.pop("address", None)
        address = None
        if address_data:
            address = AddressService().create_address(
                street=address_data["street"],
                city=address_data["city"],
                state=address_data["state"],
                postal_code=address_data["postal_code"],
                country=address_data.get("country", "USA")
            )
        else:
            address = company.address
        job_post = JobPost()
        job_post.title = data["title"]
        job_post.description = data["description"]
        job_post.salary = data["salary"]
        job_post.salary_type = data.get("salary_type", None)
        job_post.job_category_id = data["job_category_id"]
        job_post.company_id = company.id
        job_post.address_id = address.id
        job_post.save()

        return job_post
