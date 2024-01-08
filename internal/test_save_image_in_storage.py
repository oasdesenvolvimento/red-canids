from internal import save_image_in_storage


def test_upload_image_success():
    try:
        valid_image = open("./test/png.txt", "r").read()
    except FileNotFoundError:
        valid_image = open("../test/png.txt", "r").read()
    id_image = "test_id"

    url = save_image_in_storage.upload_image(valid_image, id_image)

    assert url is not None
    assert 'https' in url


def test_upload_image_success_png():
    try:
        valid_image = open("./test/png.txt", "r").read()
    except FileNotFoundError:
        valid_image = open("../test/png.txt", "r").read()
    id_image = "test_id"

    url = save_image_in_storage.upload_image(valid_image, id_image)

    assert url is not None
    assert 'https' in url


def test_upload_image_success_jpeg():
    try:
        valid_image = open("./test/jpeg.txt", "r").read()
    except FileNotFoundError:
        valid_image = open("../test/jpeg.txt", "r").read()

    id_image = "test_id"

    url = save_image_in_storage.upload_image(valid_image, id_image)

    assert url is not None
    assert 'https' in url


def test_upload_image_failure():
    invalid_image = "asd123"
    id_image = "test_id"

    url = save_image_in_storage.upload_image(invalid_image, id_image)
    assert url is None
