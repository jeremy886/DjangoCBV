Use this learning repo:
#######################

* Account is listed below.
* I named this app Courses but most of the work was about "Study Group" so it's not intuitive.


v0.01
=====

    superuser: jeremy
    password: AiFee2oo

v0.02
=====

* see home page

v0.03
=====

* see study group list and details

v0.04
=====

* edit models in admin

v0.05
=====

* start using base template to organise the feel and look

v0.06
=====

* use a form to create a study group
* remap web URLs
* add a Foreign Key User to Study Group (host)

v0.07
=====

* allow updating a study group
* add links to base and detail templates


v0.08
=====

* Delete a study group (using a URL)


v0.09
=====

* New staffer: james password: AiFee2oo
* Only allow to delete a study group if the user is the host or a superuser
* Allow editing and deleting listed study groups
* Test it: http://localhost:8000/courses/groups


v0.10
=====

* host of the study group is set to the logged-in user by default
* Test it: http://localhost:8000/courses/groups/create/