from selenium.webdriver.common.by import By

from .base import AuthorsBaseTest


class AuthorsRegisterTest(AuthorsBaseTest):

    def fill_form_dummy_data(self, form):

        fields = form.find_elements(By.TAG_NAME, 'input')

        for field in fields:
            if field.is_displayed():
                field.send_keys(' ')

    def get_form(self):
        return self.browser.find_element(By.XPATH, '/html/body/div/main/div[2]/form')

    def test_empty_first_name_error_message(self):
        self.browser.get(self.live_server_url + '/authors/register/')
        form = self.get_form()

        first_name_field = self.get_by_placeholder(form, 'Ex.: Maria')
        first_name_field.send_keys(' ')
        self.fill_form_dummy_data(form)
        form.submit()

        form = self.get_form()
        self.assertIn('Digite seu nome', form.text)

    def test_empty_last_name_error_message(self):
        self.browser.get(self.live_server_url + '/authors/register/')
        form = self.get_form()

        last_name_field = self.get_by_placeholder(form, 'Ex.: Silva')
        last_name_field.send_keys(' ')
        self.fill_form_dummy_data(form)
        form.submit()

        form = self.get_form()
        self.assertIn('Digite seu sobrenome', form.text)

    def test_empty_username_error_message(self):
        self.browser.get(self.live_server_url + '/authors/register/')
        form = self.get_form()

        username_field = self.get_by_placeholder(form, 'Digite seu usuário')
        username_field.send_keys(' ')
        self.fill_form_dummy_data(form)
        form.submit()

        form = self.get_form()
        self.assertIn('Este campo não deve estar vazio', form.text)

    def test_invalid_email_error_message(self):
        self.browser.get(self.live_server_url + '/authors/register/')
        form = self.get_form()

        email_field = self.get_by_placeholder(form, 'Ex: email@email.com')
        email_field.send_keys('email@invalid')
        self.fill_form_dummy_data(form)
        form.submit()

        form = self.get_form()
        self.assertIn('O e-mail deve ser válido.', form.text)

    def test_passwords_do_not_match(self):
        self.browser.get(self.live_server_url + '/authors/register/')
        form = self.get_form()

        password1 = self.get_by_placeholder(form, 'Digite sua senha')
        password2 = self.get_by_placeholder(form, 'Repita sua senha')
        password1.send_keys('P@ssw0rd')
        password2.send_keys('P@ssw0rd_Different')
        self.fill_form_dummy_data(form)
        form.submit()

        form = self.get_form()

        self.assertIn('Password e Password2 precisam ser iguais', form.text)

    def test_user_valid_data_register_successfully(self):
        self.browser.get(self.live_server_url + '/authors/register/')
        form = self.get_form()

        self.get_by_placeholder(form, 'Ex.: Maria').send_keys('First Name')
        self.get_by_placeholder(form, 'Ex.: Silva').send_keys('Last Name')
        self.get_by_placeholder(
            form, 'Digite seu usuário').send_keys('my_username')
        self.get_by_placeholder(
            form, 'Ex: email@email.com').send_keys('email@valid.com')
        self.get_by_placeholder(
            form, 'Digite sua senha').send_keys('P@ssw0rd1')
        self.get_by_placeholder(
            form, 'Repita sua senha').send_keys('P@ssw0rd1')

        form.submit()

        self.assertIn(
            'Usuário criado com sucesso! Pro favor, faça seu login.',
            self.browser.find_element(By.TAG_NAME, 'body').text
        )
