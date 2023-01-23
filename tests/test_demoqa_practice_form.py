from demoqa_tests.model.pages import practice_form


def test_filling_form():
    practice_form.open_page()

    # WHEN
    practice_form.input_info(name='Ksenia',
                             surname='Kapranova',
                             email='ksenya14039@mail.ru',
                             mobile='9973655228',
                             address='Moscow'
                             )

    practice_form.select_gender('Female')

    practice_form.select_birthday(day='9', month='9', year='1997')

    practice_form.input_subject('English')

    practice_form.select_hobbies('Reading')

    practice_form.upload_picture('resources/wepk.jpeg')

    practice_form.select_state('NCR')
    practice_form.select_city('Noida')

    practice_form.submit()

    # THEN

    practice_form.assert_of_registered_user(
        'Ksenia Kapranova',
        'ksenya14039@mail.ru',
        'Female',
        '9973655228',
        '9 October,1997',
        'English',
        'Reading',
        'wepk.jpeg',
        'Moscow',
        'NCR Noida'
    )