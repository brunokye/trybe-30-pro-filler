from pro_filer.actions.main_actions import show_preview


def test_show_preview_empty_context(capsys):
    context = {
        "all_files": [],
        "all_dirs": []
    }

    show_preview(context)
    captured = capsys.readouterr()

    assert captured.out == 'Found 0 files and 0 directories\n'


def test_show_preview_normal_context(capsys):
    context = {
        "all_files": [
            'file1.txt', 'file2.txt', 'file3.txt',
            'file4.txt', 'file5.txt', 'file6.txt'
        ],
        "all_dirs": [
            'dir1', 'dir2', 'dir3',
            'dir4', 'dir5', 'dir6'
        ]
    }

    show_preview(context)
    captured = capsys.readouterr()

    assert captured.out == (
        f'Found 6 files and 6 directories\n'
        f'First 5 files: {context["all_files"][:5]}\n'
        f'First 5 directories: {context["all_dirs"][:5]}\n'
    )
