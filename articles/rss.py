from django.contrib.syndication.views import Feed
from django.utils.feedgenerator import Atom1Feed

from articles.models import Post


class ArticleFeedPL(Feed):
	feed_type = Atom1Feed
	title = 'TyrantsThem: Artykuły'
	link = '/pl/artykuly/'
	description = 'Artykuły z TyrantsThem'

	def items(self):
		return Post.published.filter(is_active=True, language='PL')

	def item_title(self, item):
		return item.title

	def item_description(self, item):
		return item.content[:300] + '...'


class ArticleFeedEN(Feed):
	feed_type = Atom1Feed
	title = 'TyrantsThem: Articles'
	link = '/articles/'
	description = 'Articles from TyrantsThem'

	def items(self):
		return Post.published.filter(is_active=True, language='EN')

	def item_title(self, item):
		return item.title

	def item_description(self, item):
		return item.content[:300] + '...'