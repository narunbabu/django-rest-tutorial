from snippets.models import Snippet
from snippets.serializers import SnippetSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

snippet = Snippet(code='foo = "bar"\n')
snippet.save()

snippet = Snippet(code='print "hello, world"\n')
snippet.save()


####################################################
from gnippets.models import Gnippet
from gnippets.serializers import GnippetSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

gnippet = Gnippet(code='foo = "bar"\n')
gnippet.save()

gnippet = Gnippet(code='print "hello, world"\n')
gnippet.save()