import os
import yaml

DATA_DIR = os.path.join(os.path.dirname(__file__), "..", "data")

MONTHS = [
    "", "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December",
]


def format_date(date_str):
    if not date_str or date_str == "present":
        return date_str
    parts = date_str.split("-")
    if len(parts) == 2:
        year, month = parts
        return f"{MONTHS[int(month)]} {year}"
    return date_str


def format_experience_dates(roles):
    for r in roles:
        roles_list = r if isinstance(r, list) else [r]
        for role in roles_list:
            if "start" in role:
                role["start"] = format_date(role["start"])
            if "end" in role:
                role["end"] = format_date(role["end"])


def load_yaml(path):
    with open(path, "r") as f:
        return yaml.safe_load(f)


def load_profile():
    return load_yaml(os.path.join(DATA_DIR, "profile.yml"))


def load_skills():
    return load_yaml(os.path.join(DATA_DIR, "skills.yml"))


def format_item_dates(items):
    for item in items:
        if "start" in item:
            item["start"] = format_date(item["start"])
        if "end" in item:
            item["end"] = format_date(item["end"])


def load_education():
    data = load_yaml(os.path.join(DATA_DIR, "education.yml"))
    if "education" in data:
        format_item_dates(data["education"])
    return data


def load_certifications():
    return load_yaml(os.path.join(DATA_DIR, "certifications.yml"))


def load_experience():
    exp_dir = os.path.join(DATA_DIR, "experience")
    roles = []
    for fname in sorted(os.listdir(exp_dir)):
        if fname.endswith(".yml"):
            data = load_yaml(os.path.join(exp_dir, fname))
            if isinstance(data, list):
                roles.extend(data)
            else:
                roles.append(data)
    roles.sort(key=lambda r: r.get("start", ""), reverse=True)
    format_experience_dates(roles)
    return roles


def load_projects():
    proj_dir = os.path.join(DATA_DIR, "projects")
    projects = []
    for fname in sorted(os.listdir(proj_dir)):
        if fname.endswith(".yml"):
            projects.append(load_yaml(os.path.join(proj_dir, fname)))
    return projects


def load_all():
    return {
        "profile": load_profile(),
        "skills": load_skills(),
        "education": load_education(),
        "certifications": load_certifications(),
        "experience": load_experience(),
        "projects": load_projects(),
    }
