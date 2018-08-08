from django.conf import settings
from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager)
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver



# Create your models here.
class Role(models.Model):
  '''
  The Role entries are managed by the system,
  automatically created via a Django data migration.
  '''
  CLUBADMIN = 1
  CLUBMANAGER = 2
  CREWCAPTAIN = 3
  CREWMEMBER = 4
  DECKHAND = 5
  ROLE_CHOICES = (
      (CLUBADMIN, 'Club Administrator'),
      (CLUBMANAGER, 'Club Manager'),
      (CREWCAPTAIN, 'Crew Captain'),
      (CREWMEMBER, 'Crew Member'),
      (DECKHAND, 'Deck Hand'),
  )

  user_role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, primary_key=True)

  def __str__(self):
      return self.get_user_role_display()


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, is_active=True, is_staff=False, is_admin=False):
        if not email:
            raise ValueError("Users must have an email address")
        if not password:
            raise ValueError("User must have a password")
        # if not roles:
        #     raise ValueError("User must have a role")
        user_obj = self.model(
            email = self.normalize_email(email)
        )
        user_obj.set_password(password) #change user password
        user_obj.staff = is_staff
        user_obj.admin = is_admin
        user_obj.active = is_active
        user_obj.save(using=self._db)
        return user_obj

    def create_staffuser(self, email, password=None):
        user = self.create_user(
            email,
            password=password,
        )
        user.staff = True
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None):
        user = self.create_user(
            email,
            password=password,
        )
        user.admin = True
        user.staff = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    email       = models.EmailField(max_length=255, unique=True, blank=True, null=True)
    active      = models.BooleanField(default=True) #Can login
    staff       = models.BooleanField(default=False) #View and edit permissions
    admin       = models.BooleanField(default=False) #Superuser
    timestamp   = models.DateTimeField(auto_now_add=True)
    user_role   = models.ManyToManyField(Role)

    USERNAME_FIELD = 'email' #replaces username in the default User model.
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        return self.staff

    @property
    def is_admin(self):
        "Is the user a admin member?"
        return self.admin

    @property
    def is_active(self):
        "Is the user active?"
        return self.active

class Profile(models.Model):
	user = models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE)
	mobile = models.CharField(max_length=20, blank=True)
	def __str__(self):
		return self.mobile

		class Meta:
			ordering = ['-user']

class YachtClub(models.Model):
	#actual model items
	user = models.ForeignKey(
		settings.AUTH_USER_MODEL,
		default=1,
		related_name='%(class)s_requests_created',
		on_delete=models.CASCADE
		)
	name = models.CharField(max_length=200)
	address = models.CharField(max_length=200)
	phone = models.CharField(max_length=200)
	website = models.CharField(max_length=200)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.name

	class Meta:
		ordering = ['-id']

class Yacht(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,default=1,related_name='%(class)s_requests_created',on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    manufacturer = models.CharField(max_length=200)
    model = models.CharField(max_length=200)
    length = models.CharField(max_length=200)
    vessel_class = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-id']


from django.conf import settings
from django.db import models
