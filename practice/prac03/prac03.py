json_text = '''{
  "company": "Tech Corp",
  "headquarters": "Tokyo, Japan",
  "departments": ["Engineering", "Marketing", "Finance", "HR"],
  "employees": [
    {
      "id": 1,
      "name": "Alice",
      "department": "Engineering",
      "projects": [
        {"id": "p1", "name": "Project A", "status": "Completed"},
        {"id": "p2", "name": "Project B", "status": "In Progress"}
      ],
      "manager": {
        "name": "Bob",
        "id": 101
      }
    },
    {
      "id": 2,
      "name": "Charlie",
      "department": "Marketing",
      "projects": [
        {"id": "p3", "name": "Project C", "status": "Completed"},
        {"id": "p4", "name": "Project D", "status": "In Progress"}
      ],
      "manager": {
        "name": "Dana",
        "id": 102
      }
    },
    {
      "id": 3,
      "name": "Eve",
      "department": "Finance",
      "projects": [
        {"id": "p5", "name": "Project E", "status": "Pending"},
        {"id": "p6", "name": "Project F", "status": "Completed"}
      ],
      "manager": {
        "name": "Frank",
        "id": 103
      }
    },
    {
      "id": 4,
      "name": "Grace",
      "department": "HR",
      "projects": [
        {"id": "p7", "name": "Project G", "status": "In Progress"},
        {"id": "p8", "name": "Project H", "status": "Pending"}
      ],
      "manager": {
        "name": "Hank",
        "id": 104
      }
    }
  ]
}'''
