def test_get_student(test_client, admin_auth_headers):
    response = test_client.get("/api/students", headers=admin_auth_headers)
    assert response.status_code == 200
    assert response.json == []

def test_create_student(test_client, admin_auth_headers):
    data = {"name": "John","last_name": "Doe","age": 20, "email": "john@example.com","school_year": "1er semestre", "subjects":"['inf-111','inf-112']"}
    response = test_client.post("/api/students", json=data, headers=admin_auth_headers)
    assert response.status_code == 201
    assert response.json["name"] == "John"

def test_get_id_student(test_client, admin_auth_headers):
    data = {"name": "Hola","last_name": "Mundo","age": 10, "email": "john@example.com","school_year": "1er semestre", "subjects":"['inf-111','inf-112']"}
    response = test_client.post("/api/students", json=data, headers=admin_auth_headers)
    assert response.status_code == 201
    student_id = response.json["id"]

    response = test_client.get(f"/api/students/{student_id}", headers=admin_auth_headers)
    assert response.status_code == 200
    assert response.json["name"] == "Hola"

def test_update_student(test_client, admin_auth_headers):
    update_data = {"name":"dalas", "last_name": "review", "age": 5}
    response = test_client.put(f"/api/students/1", json=update_data, headers=admin_auth_headers)
    assert response.status_code == 200
    assert response.json["name"] == "dalas"
    assert response.json["age"] == 5

def test_delete_studen(test_client, admin_auth_headers):
    response = test_client.delete("/api/students/1", headers=admin_auth_headers)
    assert response.status_code == 204

    response = test_client.get("/api/students/1", headers=admin_auth_headers)
    assert response.status_code == 404