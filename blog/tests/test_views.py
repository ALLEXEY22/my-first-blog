from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

# reverse('post_list')
# reverse('post_detail')
# reverse('post_new')
# reverse('post_edit')
from blog.models import Post


class ViewsTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        user = User.objects.create_user(username='testuser', password='12345')
        post = Post.objects.create(author=user, title='мой пост', text='мой текст')

    def test_empty_post(self):
        """The index page loads properly"""
        response = self.client.get(reverse('post_list'))
        self.assertEqual(response.status_code, 200)
        self.assertFalse(response.context['posts'])
