# Mini Challenge 4

## Status and permissions

### Acceptance Criteria
1. Create an "archived post list view", together with any necessary urlpatterns.
1.1. The archived post list view should only allow logged in users to view the list of "archived" posts.
1.2. Posts displayed in the archived post list view should be ordered such that the newest post is at the top.
1.3. Make sure the title variable is set to "Archived" for this view.
2. Make sure that PostDetailView respects the rules we've established with our list views, such that:
2.1. A published post can be accessed by anyone without any limitations
2.2. A draft post can only be accessed by the author
2.3. An archived post can only be accessed by a logged in user (or an "authenticated" user -- hint)
3. Finally, redeploy your project to heroku and test, ensuring that the new functionality is available online.

### Bonus
Add additional custom CSS, JS or images (static files) as needed