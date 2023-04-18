from django.test import TestCase
from django.urls import reverse


class MypageViewTests(TestCase):
  """MypageViewのテストクラス"""

  def test_get(self):
    """GET メソッドでアクセスしてステータスコード200を返されることを確認"""
    response = self.client.get(reverse('mypage'))
    self.assertEqual(response.status_code, 302)
