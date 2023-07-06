import datetime
from pro_filer.actions.main_actions import show_details


def test_show_details_empty_path(capsys):
    context = {'base_path': 'fake.json'}

    show_details(context)
    captured = capsys.readouterr()

    assert captured.out == "File 'fake.json' does not exist\n"


def test_show_details_no_extension(tmp_path, capsys):
    fake_file_path = tmp_path / 'fake'
    fake_file_path.touch()

    context = {'base_path': str(fake_file_path)}

    show_details(context)
    captured = capsys.readouterr()

    assert captured.out == (
        'File name: fake\n'
        'File size in bytes: 0\n'
        'File type: file\n'
        'File extension: [no extension]\n'
        f'Last modified date: {datetime.date.today()}\n'
    )


def test_show_details_normal_path(tmp_path, capsys):
    fake_file_path = tmp_path / 'fake.json'
    fake_file_path.touch()

    context = {'base_path': str(fake_file_path)}

    show_details(context)
    captured = capsys.readouterr()

    assert captured.out == (
        'File name: fake.json\n'
        'File size in bytes: 0\n'
        'File type: file\n'
        'File extension: .json\n'
        f'Last modified date: {datetime.date.today()}\n'
    )
