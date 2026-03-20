def test_get_activities_returns_activity_dictionary(client):
    response = client.get("/activities")

    assert response.status_code == 200

    payload = response.json()

    assert isinstance(payload, dict)
    assert "Chess Club" in payload


def test_each_activity_includes_expected_fields(client):
    response = client.get("/activities")

    assert response.status_code == 200

    payload = response.json()

    for details in payload.values():
        assert set(details) == {
            "description",
            "schedule",
            "max_participants",
            "participants",
        }
        assert isinstance(details["participants"], list)