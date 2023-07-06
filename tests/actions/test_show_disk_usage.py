from pro_filer.actions.main_actions import show_disk_usage
from pro_filer.cli_helpers import _get_printable_file_path


def test_show_disk_usage_normal_paths(tmp_path, capsys):
    fake_file_01 = tmp_path / 'fake_01.json'
    fake_file_01.touch()
    fake_file_01.write_text('a')

    fake_file_02 = tmp_path / 'fake_02.json'
    fake_file_02.touch()

    context = {'all_files': [str(fake_file_01), str(fake_file_02)]}

    show_disk_usage(context)
    captured = capsys.readouterr()

    assert captured.out == (
        f"'{_get_printable_file_path(str(fake_file_01))}':        1 (100%)\n"
        f"'{_get_printable_file_path(str(fake_file_02))}':        0 (0%)\n"
        'Total size: 1\n'
    )
