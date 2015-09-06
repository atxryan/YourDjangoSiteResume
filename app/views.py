"""
Definition of views.
"""

from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime

YOUR_INFO = {
    'name' : 'Ryan Joy',
    'bio' : 'Startup Evangelist @ Microsoft living in Austin, TX',
    'email' : '', # Leave blank if you'd prefer not to share your email with other conference attendees
    'twitter_username' : 'atxryan', # No @ symbol, just the handle.
    'github_username' : "atxryan", 
    'headshot_url' : 'https://pbs.twimg.com/profile_images/378800000096542701/16bc79cba82fe2a269063c2f5ef52ee6.jpeg', # Link to your GitHub, Twitter, or Gravatar profile image.
}
    
def home(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/base.html',
        context_instance = RequestContext(request,
            {
                'attendee' : YOUR_INFO,    
                'year': datetime.now().year,
            })
    )