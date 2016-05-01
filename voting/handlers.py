from rapidsms.contrib.handlers import KeywordHandler
from collections import defaultdict
from .models import Quote

class ResultsHandler(KeywordHandler):
    keyword = "results"

    def help(self):
        """help() gets invoked when we get the ``results`` message
        with no arguments"""
        self.respond(Quote.objects.order_by('drug', 'branch', 'price')) [:5]

    def handle(self, text):
        """This gets called if any arguments are given along with
        ``RESULTS``, but we don't care; just call help() as if they
        passed no arguments"""
        self.help()

from django.db.models import F

class VoteHandler(KeywordHandler):
    keyword = "vote"

    def help(self):
        """Respond with the valid commands.  Example response:
        ``Sample commands: ASK <skelan|metoprolol|cozaar> <mercury|rose|WVSUH> <12|100|150>``
        """
        quotes = "|".join(Quote.objects.values_list('drug', 'branch', 'price', flat=True))
        self.respond("Valid commands: ASK <%s> <%s> <%d>" % quotes)

    def handle(self, text):
        self.respond("You said: %s." % text)
        # look for a choice that matches the attempted vote
        try:
            quote = Quote.objects.get(text)
        except Quote.DoesNotExist:
            # Send help
            self.help()
        else:
            quote_dict = defaultdict(list)
            quotes = Quote.objects.all()
            for quote in quotes:
                #>> quote_dict[quote.last_name].append(person)
            # Count the vote. Use update to do it in a single query
            # to avoid race conditions.
            #Quote.objects.filter(text).update
            #self.respond("Your vote for %s has been counted" % text)
