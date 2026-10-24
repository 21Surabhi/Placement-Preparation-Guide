from pymongo import MongoClient
import gridfs

client = MongoClient("mongodb://localhost:27017/")

db = client["placement_portal"]

study_materials = db["study_materials"]

companies_collection = db["companies"]

print("Connected to MongoDB successfully")

fs = gridfs.GridFS(db)


def add_resource(company, title, uploaded_file):

    file_id = fs.put(
        uploaded_file.getvalue(),
        filename=uploaded_file.name
    )

    resource = {
        "company": company,
        "title": title,
        "resource_type": "PDF",
        "file_id": file_id
    }

    study_materials.insert_one(resource)

    print("Resource added successfully")


def get_resources(company):

    resources = study_materials.find({
        "$or": [
            {"company": company},
            {"companies": company}
        ]
    })

    return list(resources)


def add_company(name, arrival_date, vacancies, role, ctc):
    company = {
        "name": name,
        "arrival_date": arrival_date,
        "vacancies": vacancies,
        "role": role,
        "ctc": ctc
    }

    existing = companies_collection.find_one({
        "name": {"$regex": f"^{name}$", "$options": "i"}
    })

    if existing:
        return False

    companies_collection.insert_one(company)
    return True


def get_companies():
    return list(companies_collection.find().sort("name", 1))