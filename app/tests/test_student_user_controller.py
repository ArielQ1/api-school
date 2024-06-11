def test_get_student(test_client, user_auth_headers):
    response = test_client.get("/api/students", headers=user_auth_headers)
    assert response.status_code == 200
    assert response.json == []

def test_create_student(test_client, user_auth_headers):
    data = {"name": "John","last_name": "Doe","age": 20, "email": "john@example.com","school_year": "1er semestre", "subjects":"['inf-111','inf-112']"}
    response = test_client.post("/api/students", json=data, headers=user_auth_headers)
    assert response.status_code == 403

def test_create_student(test_client, admin_auth_headers):
    data = {"name": "John","last_name": "Doe","age": 20, "email": "john@example.com","school_year": "1er semestre", "subjects":"['inf-111','inf-112']"}
    response = test_client.post("/api/students", json=data, headers=admin_auth_headers)
    assert response.status_code == 201
    assert response.json["name"] == "John"
    
def test_get_id_student(test_client, user_auth_headers):
    response = test_client.get(f"/api/students/1", headers=user_auth_headers)
    assert response.status_code == 200
    assert "name" in response.json

def test_update_student(test_client, user_auth_headers):
    update_data = {"name":"dalas", "last_name": "review", "age": 5}
    response = test_client.put(f"/api/students/1", json=update_data, headers=user_auth_headers)
    assert response.status_code == 403
def test_delete_studen(test_client, user_auth_headers):
    response = test_client.delete("/api/students/1", headers=user_auth_headers)
    assert response.status_code == 403