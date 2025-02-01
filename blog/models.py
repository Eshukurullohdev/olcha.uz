from django.db import models
from django.utils.crypto import get_random_string
from django.core.validators import RegexValidator
# Create your models here
class Tovar(models.Model):
    unique_id = models.CharField(
        max_length=90,
        validators=[
                RegexValidator(
                    regex=r"^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*])[^?&^]{-}$",
                    message='bunda $ @ ^ kiritib bolmaydi ',
                    code='hato_boldi'
                    
                )
            
        ],
        unique=True,
        null=True,
        blank=True,
        help_text="bu yerga hechnarsa kiritilmaydi",

    )
    img = models.CharField(max_length=200)
    name = models.CharField(max_length=250)
    cost = models.CharField(max_length=250, null=True)
    skitka = models.BooleanField(default=False)



    def bolib3tolash(self):
        return int(int(self.cost) / 3 )
    def bolib6tolash(self):
        return int(int(self.cost) / 6 )  
    def bolib12tolash(self):
        return int(int(self.cost) / 12 ) 
    def save(self, *args, **kwargs):
        if not self.unique_id:
            self.unique_id = get_random_string(
                length=90,
                allowed_chars="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
            )
        super().save(*args, **kwargs)

        


class Texnika(models.Model):
    unique_id = models.CharField(
        max_length=90,
        validators=[
                RegexValidator(
                    regex=r"^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*])[^?&^]{-}$",
                    message='bunda $ @ ^ ',
                    code='hato_boldi'
                    
                )
            
        ],
        unique=True,
        null=True,
        blank=True,
        help_text="bu yerga hechnarsa kiritilmaydi",

    )
    img = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    cost = models.CharField(max_length=200)
    skitka = models.BooleanField(default=False, null=True)
    def bolib3tolash(self):
        return int(int(self.cost) / 3 )
    def bolib6tolash(self):
        return int(int(self.cost) / 6 )  
    def bolib12tolash(self):
        return int(int(self.cost) / 12 ) 
    def save(self, *args, **kwargs):
        if not self.unique_id:
            self.unique_id = get_random_string(
                length=90,
                allowed_chars="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
            )
        super().save(*args, **kwargs)

class Kitob(models.Model):
    unique_id = models.CharField(
        max_length=90,
        validators=[
                RegexValidator(
                    regex=r"^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*])[^?&^]{-}$",
                    message='bunda $ @ ^ ',
                    code='hato_boldi'
                    
                )
            
        ],
        unique=True,
        null=True,
        blank=True,
        help_text="bu yerga hechnarsa kiritilmaydi",

    )
    img = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    cost = models.CharField(max_length=200)
    skitka = models.BooleanField(default=False, null=True)
    def bolib3tolash(self):
        return int(int(self.cost) / 3 )
    def bolib6tolash(self):
        return int(int(self.cost) / 6 )  
    def bolib12tolash(self):
        return int(int(self.cost) / 12 ) 
    def save(self, *args, **kwargs):
        if not self.unique_id:
            self.unique_id = get_random_string(
                length=90,
                allowed_chars="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
            )
        super().save(*args, **kwargs)

class Tv(models.Model):
    unique_id = models.CharField(
        max_length=90,
        validators=[
                RegexValidator(
                    regex=r"^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*])[^?&^]{-}$",
                    message='bunda $ @ ^ ',
                    code='hato_boldi'
                    
                )
            
        ],
        unique=True,
        null=True,
        blank=True,
        help_text="bu yerga hechnarsa kiritilmaydi",

    )
    img = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    cost = models.CharField(max_length=200)
    skitka = models.BooleanField(default=False, null=True)
    def bolib3tolash(self):
        return int(int(self.cost) / 3 )
    def bolib6tolash(self):
        return int(int(self.cost) / 6 )  
    def bolib12tolash(self):
        return int(int(self.cost) / 12 ) 
    def save(self, *args, **kwargs):
        if not self.unique_id:
            self.unique_id = get_random_string(
                length=90,
                allowed_chars="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
            )
        super().save(*args, **kwargs)

class Konditsioner(models.Model):
    unique_id = models.CharField(
        max_length=90,
        validators=[
                RegexValidator(
                    regex=r"^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*])[^?&^]{-}$",
                    message='bunda $ @ ^ ',
                    code='hato_boldi'
                    
                )
            
        ],
        unique=True,
        null=True,
        blank=True,
        help_text="bu yerga hechnarsa kiritilmaydi",

    )
    img = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    cost = models.CharField(max_length=200)
    skitka = models.BooleanField(default=False, null=True)
    def bolib3tolash(self):
        return int(int(self.cost) / 3 )
    def bolib6tolash(self):
        return int(int(self.cost) / 6 )  
    def bolib12tolash(self):
        return int(int(self.cost) / 12 ) 
    def save(self, *args, **kwargs):
        if not self.unique_id:
            self.unique_id = get_random_string(
                length=90,
                allowed_chars="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
            )
        super().save(*args, **kwargs)

class Notebook(models.Model):
    unique_id = models.CharField(
        max_length=90,
        validators=[
                RegexValidator(
                    regex=r"^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*])[^?&^]{-}$",
                    message='bunda $ @ ^ ',
                    code='hato_boldi'
                    
                )
            
        ],
        unique=True,
        null=True,
        blank=True,
        help_text="bu yerga hechnarsa kiritilmaydi",

    )
    img = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    cost = models.CharField(max_length=200)
    def bolib3tolash(self):
        return int(int(self.cost) / 3 )
    def bolib6tolash(self):
        return int(int(self.cost) / 6 )  
    def bolib12tolash(self):
        return int(int(self.cost) / 12 ) 
    def save(self, *args, **kwargs):
        if not self.unique_id:
            self.unique_id = get_random_string(
                length=90,
                allowed_chars="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
            )
        super().save(*args, **kwargs)
    


class Gadjet(models.Model):
    unique_id = models.CharField(
        max_length=90,
        validators=[
                RegexValidator(
                    regex=r"^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*])[^?&^]{-}$",
                    message='bunda $ @ ^ ',
                    code='hato_boldi'
                    
                )
            
        ],
        unique=True,
        null=True,
        blank=True,
        help_text="bu yerga hechnarsa kiritilmaydi",

    )
    img = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    cost = models.CharField(max_length=200)
    skitka = models.BooleanField(default=False, null=True)
    def bolib3tolash(self):
        return int(int(self.cost) / 3 )
    def bolib6tolash(self):
        return int(int(self.cost) / 6 )  
    def bolib12tolash(self):
        return int(int(self.cost) / 12 ) 
    def save(self, *args, **kwargs):
        if not self.unique_id:
            self.unique_id = get_random_string(
                length=90,
                allowed_chars="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
            )
        super().save(*args, **kwargs)

class Cart(models.Model):
    tovar = models.ForeignKey(Tovar, on_delete=models.SET_NULL, null=True, blank=True)
    gadjet = models.ForeignKey(Gadjet, on_delete=models.SET_NULL, null=True, blank=True)
    notebook = models.ForeignKey(Notebook, on_delete=models.SET_NULL, null=True, blank=True)
    expensiv = models.ForeignKey(Konditsioner, on_delete=models.SET_NULL, null=True, blank=True)
    tv = models.ForeignKey(Tv, on_delete=models.SET_NULL, null=True, blank=True)
    kitob = models.ForeignKey(Kitob, on_delete=models.SET_NULL, null=True, blank=True)
    texnika = models.ForeignKey(Texnika, on_delete=models.SET_NULL, null=True, blank=True)


    time_added = models.DateTimeField(auto_now_add=True)



class Like(models.Model):
    tovar = models.ForeignKey(Tovar, on_delete=models.SET_NULL, null=True, blank=True)
    gadjet = models.ForeignKey(Gadjet, on_delete=models.SET_NULL, null=True, blank=True)
    notebook = models.ForeignKey(Notebook, on_delete=models.SET_NULL, null=True, blank=True)
    expensiv = models.ForeignKey(Konditsioner, on_delete=models.SET_NULL, null=True, blank=True)
    tv = models.ForeignKey(Tv, on_delete=models.SET_NULL, null=True, blank=True)
    kitob = models.ForeignKey(Kitob, on_delete=models.SET_NULL, null=True, blank=True)
    texnika = models.ForeignKey(Texnika, on_delete=models.SET_NULL, null=True, blank=True)

class Contact(models.Model):
    first_name = models.CharField(max_length=250)
    phone = models.IntegerField(null=True)
    email = models.EmailField()
    message = models.TextField()
    
    

    def __str__(self):
        return f'{self.first_name} xabar yozdi'


class Comment(models.Model):
    first_name = models.CharField(max_length=250, null=True)
    email = models.EmailField(null=True)
    message = models.TextField(null=True, )
    tovar = models.ForeignKey(Tovar, on_delete=models.SET_NULL, null=True, blank=True)
    gadjet = models.ForeignKey(Gadjet, on_delete=models.SET_NULL, null=True, blank=True)
    notebook = models.ForeignKey(Notebook, on_delete=models.SET_NULL, null=True, blank=True)
    expensiv = models.ForeignKey(Konditsioner, on_delete=models.SET_NULL, null=True, blank=True)
    tv = models.ForeignKey(Tv, on_delete=models.SET_NULL, null=True, blank=True)
    kitob = models.ForeignKey(Kitob, on_delete=models.SET_NULL, null=True, blank=True)
    texnika = models.ForeignKey(Texnika, on_delete=models.SET_NULL, null=True, blank=True)

    

class Buy(models.Model):

    SHAXAR = [
        ("Tanlang", "Tanlang"),
        ("Andijon", "Andijon"),
        ("Namangan", "Namangan"),
        ("Toshkent", "Toshkent"),
        ("Farg'ona", "Farg'ona"),
    ]
    Tuman = [
        ("Tanlang", "Tanlang"),
        ("Izboskan", "Izboskan"),
        ("Marhamat", "Marhamat"),
        ("Oltinko'l", "Oltinko'l"),
        ("Jalaquduq", "Jalaquduq"),
    ]
    Pochta = [
        ("Tanlang", "Tanlang"),
        ("Poytug Po'chtasi", "Poytug Po'chtasi"),
    ]


    phone = models.CharField(max_length=50, null=True)
    full_name = models.CharField(max_length=100, null=True)
    shahar = models.CharField(max_length=20, choices=SHAXAR, default=SHAXAR[0][0], null=True)
    tuman = models.CharField(max_length=20, choices=Tuman, default=Tuman[0][0], null=True)
    pochta = models.CharField(max_length=20, choices=Pochta, default=Pochta[0][0], null=True)
    address = models.CharField(max_length=100)
    orienter = models.CharField(max_length=100)
    working_adress = models.CharField(max_length=100)
    tovar = models.ForeignKey(Tovar, on_delete=models.SET_NULL, null=True, blank=True)
    gadjet = models.ForeignKey(Gadjet, on_delete=models.SET_NULL, null=True, blank=True)
    notebook = models.ForeignKey(Notebook, on_delete=models.SET_NULL, null=True, blank=True)
    expensiv = models.ForeignKey(Konditsioner, on_delete=models.SET_NULL, null=True, blank=True)
    tv = models.ForeignKey(Tv, on_delete=models.SET_NULL, null=True, blank=True)
    kitob = models.ForeignKey(Kitob, on_delete=models.SET_NULL, null=True, blank=True)
    texnika = models.ForeignKey(Texnika, on_delete=models.SET_NULL, null=True, blank=True)

    date_orderded = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{} telefon egasi tovari {} da rasmiylashtirildi tovar yetkazib berish punkiti {} {}".format(self.phone, self.date_orderded, self.address, self.working_adress)
    
class Reyting(models.Model):

    # BAXOLASH = [
    #   "1", "1",
    #   "2", "2",
    #   "3", "3",
    # ]
    baholash = models.CharField(max_length=10,    default=[0][0], null=True)
    tovar = models.ForeignKey(Tovar, on_delete=models.SET_NULL, null=True, blank=True)
    gadjet = models.ForeignKey(Gadjet, on_delete=models.SET_NULL, null=True, blank=True)
    notebook = models.ForeignKey(Notebook, on_delete=models.SET_NULL, null=True, blank=True)
    expensiv = models.ForeignKey(Konditsioner, on_delete=models.SET_NULL, null=True, blank=True)
    tv = models.ForeignKey(Tv, on_delete=models.SET_NULL, null=True, blank=True)
    kitob = models.ForeignKey(Kitob, on_delete=models.SET_NULL, null=True, blank=True)
    texnika = models.ForeignKey(Texnika, on_delete=models.SET_NULL, null=True, blank=True)
