from core.model import mission_model


def test_mission_model():
    keys = mission_model.Mission._fields.keys()
    keys = list(keys)
    keys.sort()
    keys_expected = ['_id', 'auto_id_0', 'classification', 'code_mission', 'created_at', 'description_mission',
                     'expiration_date',
                     'image_mission', 'name_mission', 'points', 'time_mission', 'type_mission', 'type_points',
                     'updated_at', 'url_mission']
    keys_expected.sort()
    assert keys == keys_expected
