from django.test import TestCase
from product.models import Comment, Product, Category
from django.contrib.auth.models import User

class ProductTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Створюємо категорію для тестування
        category = Category.objects.create(name='Test Category')
        
        # Створюємо продукт для тестування
        product = Product.objects.create(
            category=category,
            title='Test Product',
            keywords='Test',
            description='Test Description',
            price=10,
            amount=5,
            minamount=3,
            variant='None',
            slug='test-product',
            status='True'
        )

        # Створюємо користувача для перевірки методу avaregereview
        user = User.objects.create(username='testuser')

        # Створюємо коментарі для продукту
        Comment.objects.create(
            product=product,
            user=user,
            content='Test comment 1',
            rate=4,
            status='True'
        )
        Comment.objects.create(
            product=product,
            user=user,
            content='Test comment 2',
            rate=5,
            status='True'
        )

    def test_model_fields(self):
        # Отримуємо створений продукт для перевірки полів моделі
        product = Product.objects.get(title='Test Product')

        self.assertEqual(product.category.name, 'Test Category')
        self.assertEqual(product.keywords, 'Test')
        self.assertEqual(product.description, 'Test Description')
        self.assertEqual(product.price, 10)
        self.assertEqual(product.amount, 5)
        self.assertEqual(product.minamount, 3)
        self.assertEqual(product.variant, 'None')
        self.assertEqual(product.slug, 'test-product')
        self.assertEqual(product.status, 'True')

    def test_image_tag(self):
        # Отримуємо створений продукт для перевірки методу image_tag
        product = Product.objects.get(title='Test Product')

        # Перевіряємо, чи метод повертає очікуваний HTML-код
        expected_html = '<img src="{}" height="50"/>'.format(product.image.url)
        self.assertEqual(product.image_tag(), expected_html)

    def test_get_absolute_url(self):
        # Отримуємо створений продукт для перевірки методу get_absolute_url
        product = Product.objects.get(title='Test Product')

        # Перевіряємо, чи метод повертає очікувану URL-адресу
        expected_url = '/category/test-product/'
        self.assertEqual(product.get_absolute_url(), expected_url)

    def test_avaregereview(self):
        # Отримуємо створений продукт для перевірки методу avaregereview
        product = Product.objects.get(title='Test Product')

        # Перевіряємо, чи метод повертає очікуваний середній рейтинг
        self.assertEqual(product.avaregereview(), 4.5)

    def test_countreview(self):
        # Отримуємо створений продукт для перевірки методу countreview
        product = Product.objects.get(title='Test Product')

        # Перевіряємо, чи метод повертає очікувану кількість коментарів
        self.assertEqual(product.countreview(), 2)