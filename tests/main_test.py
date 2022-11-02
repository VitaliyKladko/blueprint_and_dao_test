class TestMain:

    def test_root_status(self, test_client):
        """Проверяем, получается ли нужный статус-код у вьюшки"""
        response = test_client.get('/', follow_redirects=True)
        assert response.status_code == 200, 'Статус код всех постов неверный'

    def test_root_content(self, test_client):
        response = test_client.get('/', follow_redirects=True)
        assert 'Это главная страница' in response.data.decode('utf-8'), 'Контент страницы неверный'
