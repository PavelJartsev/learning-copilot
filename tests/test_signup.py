def test_signup_adds_new_participant(client):
    response = client.post("/activities/Chess Club/signup?email=test@mergington.edu")

    assert response.status_code == 200
    assert response.json() == {
        "message": "Signed up test@mergington.edu for Chess Club"
    }

    activities_response = client.get("/activities")

    assert "test@mergington.edu" in activities_response.json()["Chess Club"]["participants"]


def test_signup_rejects_duplicate_participant(client):
    response = client.post("/activities/Chess Club/signup?email=michael@mergington.edu")

    assert response.status_code == 400
    assert response.json() == {
        "detail": "Student already signed up for this activity"
    }


def test_signup_returns_not_found_for_unknown_activity(client):
    response = client.post("/activities/Unknown Club/signup?email=test@mergington.edu")

    assert response.status_code == 404
    assert response.json() == {"detail": "Activity not found"}