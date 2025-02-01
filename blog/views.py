from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.db import IntegrityError
from django.utils.translation import gettext as _

def home_page(request):
    text = _("songi yangilikalr")
    tovar = Tovar.objects.all()
    cartCount = Cart.objects.count()
    likeCount = Like.objects.count()
    return render(request, "home.html", {"tovar": tovar, "cartcount": cartCount, "likeCount": likeCount, 'text': text})

def nav_page(request):
    return render(request, 'navigation.html')

def footer_page(request):
    return render(redirect,'footer.html' )

def sidebar_page(request):
    return render(request, 'sidebar.html')

def discount_page(request):
    tovar = Tovar.objects.all().filter(skitka=True)
    return render(request, 'discount.html', {"tovar": tovar})

def gadjet_page(request):
    tovar = Gadjet.objects.all()
    return render(request, 'gadjet.html', {"tovar": tovar})

def texnika_page(request):
    tovar = Texnika.objects.all()
    return render(request, 'texnika.html', {"tovar": tovar})

def kitob_page(request):
    tovar = Kitob.objects.all()
    return render(request, 'book.html', {"tovar": tovar})

def televizor_page(request):
    tovar = Tv.objects.all()
    return render(request, 'tv.html', {"tovar": tovar})

def expensive_page(request):
    tovar = Konditsioner.objects.all()
    return render(request, 'expensiv.html', {"tovar": tovar})

def notebook_page(request):
    tovar = Notebook.objects.all()
    return render(request, 'notebook.html', {"tovar": tovar})

def buy_page(request, tovar_id):

    if request.method == "POST":
        phone= request.POST.get("telefon", None)
        shaxar= request.POST.get("shaxar", None)
        full_name= request.POST.get("toliq ismi", None)
        phone= request.POST.get("telefon", None)
        pochta= request.POST.get("pochta", None)
        address= request.POST.get("manzil", None)
        working_address= request.POST.get("ish_manzil", None)
    tovar = Tovar.objects.filter(unique_id=tovar_id).exists()
    if tovar:
        tovar_m = Tovar.objects.get(unique_id=tovar_id)
        if request.method == "POST":
            Buy.objects.create(
               phone=phone,
               shaxar=shaxar,
               address=address,
               working_address=working_address,
               full_name=full_name,
               pochta=pochta,
               tovar = tovar_m,
            )
    else:
        tovar_m=False
    
    return render(request, 'tovar.html', {"tovar": tovar_m})

def tovar_page(request, tovar_id):
    
    tovar = Tovar.objects.filter(unique_id=tovar_id).exists()
    gadjet = Gadjet.objects.filter(unique_id=tovar_id).exists()
    kitob = Kitob.objects.filter(unique_id=tovar_id).exists()
    texnika = Texnika.objects.filter(unique_id=tovar_id).exists()
    notebook = Notebook.objects.filter(unique_id=tovar_id).exists()
    expensive = Konditsioner.objects.filter(unique_id=tovar_id).exists()
    tv = Tv.objects.filter(unique_id=tovar_id).exists()

    if tovar:                                     
        tovar_m = Tovar.objects.get(unique_id=tovar_id)
        commentlar = Comment.objects.filter(tovar=tovar_m)
        if request.method == "POST":
            first_name = request.POST.get("first_name")
            email = request.POST.get("email")
            message = request.POST.get("text")
            baholash = request.POST.get("baholash")
            Comment.objects.create(
            first_name = first_name,
            email = email,
            message = message,
            tovar=tovar_m,
            )
            Reyting.objects.create(
                baholash=baholash,
                tovar=tovar_m
            )
       
            return redirect("/tovar/" + tovar_id)
        

    elif gadjet:
        tovar_m = Gadjet.objects.get(unique_id=tovar_id)
        commentlar = Comment.objects.filter(gadjet=tovar_m)
        if request.method == "POST":
            first_name = request.POST.get("first_name")
            email = request.POST.get("email")
            message = request.POST.get("text")
            Comment.objects.create(
            first_name = first_name,
            email = email,
            message = message,
            gadjet=tovar_m
            )
            Reyting.objects.create(
                baholash=baholash,
                tovar=tovar_m
            )
            return redirect("/tovar/"+ tovar_id)
    elif kitob:
        tovar_m = Kitob.objects.get(unique_id=tovar_id)
        commentlar = Comment.objects.filter(kitob=tovar_m)
        if request.method == "POST":
            first_name = request.POST.get("first_name")
            email = request.POST.get("email")
            message = request.POST.get("text")
            Comment.objects.create(
            first_name = first_name,
            email = email,
            message = message,
            kitob=tovar_m
            )
            Reyting.objects.create(
                baholash=baholash,
                tovar=tovar_m
            )
            return redirect("/tovar/"+ tovar_id)
    elif texnika:
        tovar_m = Texnika.objects.get(unique_id=tovar_id)
        commentlar = Comment.objects.filter(texnika=tovar_m)
        if request.method == "POST":
            first_name = request.POST.get("first_name")
            email = request.POST.get("email")
            message = request.POST.get("text")
            Comment.objects.create(
            first_name = first_name,
            email = email,
            message = message,
            texnika=tovar_m
            )
            Reyting.objects.create(
                baholash=baholash,
                tovar=tovar_m
            )
            return redirect("/tovar/"+ tovar_id)
    elif notebook:
        tovar_m = Notebook.objects.get(unique_id=tovar_id)
        commentlar = Comment.objects.filter(notebook=tovar_m)
        if request.method == "POST":
            first_name = request.POST.get("first_name")
            email = request.POST.get("email")
            message = request.POST.get("text")
            Comment.objects.create(
            first_name = first_name,
            email = email,
            message = message,
            notebook=tovar_m
            )
            Reyting.objects.create(
                baholash=baholash,
                tovar=tovar_m
            )
            return redirect("/tovar/"+ tovar_id)
    elif expensive:
        tovar_m = Konditsioner.objects.get(unique_id=tovar_id)
        commentlar = Comment.objects.filter(expensive=tovar_m)
        if request.method == "POST":
            first_name = request.POST.get("first_name")
            email = request.POST.get("email")
            message = request.POST.get("text")
            Comment.objects.create(
            first_name = first_name,
            email = email,
            message = message,
            expensive=tovar_m
            )
            Reyting.objects.create(
                baholash=baholash,
                tovar=tovar_m
            )
            return redirect("/tovar/"+ tovar_id)
    elif tv:
        tovar_m = Tv.objects.get(unique_id=tovar_id)
        commentlar = Comment.objects.filter(tv=tovar_m)
        if request.method == "POST":
            first_name = request.POST.get("first_name")
            email = request.POST.get("email")
            message = request.POST.get("text")
            Comment.objects.create(
            first_name = first_name,
            email = email,
            message = message,
            tv=tovar_m
            )
            Reyting.objects.create(
                baholash=baholash,
                tovar=tovar_m
            )
            return redirect("/tovar/"+ tovar_id)
        # messages.warning(request, "Sizni habaringgiz yuborildi")
    else:
        tovar_m = False
        commentlar = {}



    return render(request, 'tovar.html', {"tovar": tovar_m, "commentlar": commentlar})





def search_page(request):
    tovar = Tovar.objects.all()
    gadjets = Gadjet.objects.all()
    tvs = Tv.objects.all()
    texnniks = Texnika.objects.all()
    kitobs = Kitob.objects.all()
    news = Konditsioner.objects.all()
    noutbook = Notebook.objects.all()
    natijalar = []

    if request.method == "GET":
        key = request.GET.get("key")
        if key:
            tovar = Tovar.objects.all().filter(name__icontains=key)
            if tovar:
                natijalar.append(tovar)
            gadjets = Gadjet.objects.all().filter(name__icontains=key)
            if gadjets:
                natijalar.append(gadjets)
            tvs = Tv.objects.all().filter(name__icontains=key)
            if tvs:
                natijalar.append(tvs)
            texnniks = Texnika.objects.all().filter(name__icontains=key)
            if texnniks:
                natijalar.append(texnniks)
            kitobs = Kitob.objects.all().filter(name__icontains=key)
            if kitobs:
                natijalar.append(kitobs)
            news = Konditsioner.objects.all().filter(name__icontains=key)
            if news:
                natijalar.append(news)
            noutbook = Notebook.objects.all().filter(name__icontains=key)
            if noutbook:
                natijalar.append(noutbook)
                

    
    context = {
        "tovar": tovar,
        "key": key,
        "gadjet": gadjets,
        "tv": tvs,
        "texnika": texnniks,
        "kitob": kitobs,
        "yangi": news,
        "noutbook": noutbook,
        "natijalar": natijalar


    }
    return render(request, 'search.html', context)
    
    


    
    
def shopingCart_page(request):
    carst = Cart.objects.all()
    context = {
        "carts": carst
    }
    return render(request, 'shoppingCart.html', context)

def like_page(request):
    like = Like.objects.all()
    context = {
        "like": like
    }
    return render(request, 'like.html', context)


#  login register logaut 

def register_page(request):
    if not request.user.is_authenticated:
        try:
            if request.method == "POST":
                username = request.POST.get("username")
                first_name = request.POST.get("first_name")
                last_name = request.POST.get("last_name")
                email = request.POST.get("email")
                password = request.POST.get("password")
                user = User.objects.create(
                    username=username,
                    first_name=first_name,
                    last_name=last_name,
                    email=email,
                    password=make_password(password)
                )
                login(request, user)
                return redirect("/")
        except IntegrityError as e:
            messages.error(request, f"siz register {e}, bor")    
        return render(request, 'register.html')
    else:
        return redirect("/")


def login_page(request):
        if not request.user.is_authenticated:
            try:
                username = request.POST.get("username")
                password = request.POST.get("password")
                user = authenticate(username=username, password=make_password(password))
                if user:
                    login(request, user)
                    return redirect("/")
                else:
                    messages.warning(request, "bunday user mavjud emas")
            except:
                print("xato")
            return render(request, 'login.html')
        else:
            return redirect("/")

def logaut_page(request):
    logout(request)
    return redirect("/")


def add_to_cart_page(request, tovarni_idsi):
    try:
        tovar = Tovar.objects.get(unique_id=tovarni_idsi)
        try:
            Cart.objects.get(tovar=tovar)
            messages.warning(request, "Savatchada bunday tovar mavjud")
            return redirect("/")
        except:
            Cart.objects.create(tovar=tovar)
    except Tovar.DoesNotExist:
        print("tovar yoq")  

    try:
        gadjet = Gadjet.objects.get(unique_id=tovarni_idsi)
        try:
            Cart.objects.get(gadjet=gadjet)
            messages.warning(request, "Savatchada bunday tovar mavjud")

            return redirect("/")
        except:
            Cart.objects.create(gadjet=gadjet)
    except Gadjet.DoesNotExist:
        print("tovar yoq")


    try:
        tv = Tv.objects.get(unique_id=tovarni_idsi)
        try:
            Cart.objects.get(tv=tv)
            messages.warning(request, "Savatchada bunday tovar mavjud")
            return redirect("/")
        except:
            Cart.objects.create(tv=tv)
    except Tv.DoesNotExist:
        print("tovar yoq")

    try:
        kitob = Kitob.objects.get(unique_id=tovarni_idsi)
        try:
            Cart.objects.get(kitob=kitob)
            messages.warning(request, "Savatchada bunday tovar mavjud")
            return redirect("/")
        except:
            Cart.objects.create(kitob=kitob)
    except Kitob.DoesNotExist:
        print("tovar yoq")

    try:
        texnika = Texnika.objects.get(unique_id=tovarni_idsi)
        try:
            Cart.objects.get(texnika=texnika)
            messages.warning(request, "Savatchada bunday tovar mavjud")
            return redirect("/")
        except:
            Cart.objects.create(texnika=texnika)
    except Texnika.DoesNotExist:
        print("tovar yoq")
    
    try:
        notebook = Notebook.objects.get(unique_id=tovarni_idsi)
        try:
            Cart.objects.get(notebook=notebook)
            messages.warning(request, "Savatchada bunday tovar mavjud")
            return redirect("/")
        except:
            Cart.objects.create(notebook=notebook)
    except Notebook.DoesNotExist:
        print("tovar yoq")

    try:
        expensiv = Konditsioner.objects.get(unique_id=tovarni_idsi)
        try:
            Cart.objects.get(expensiv=expensiv)
            messages.warning(request, "Savatchada bunday tovar mavjud")
            return redirect("/")
        except:
            Cart.objects.create(expensiv=expensiv)
    except Konditsioner.DoesNotExist:
        print("tovar yoq")
    return redirect("/")





def remove_page(request, tovar_id):
    try:
        cart = Cart.objects.get(id=tovar_id)
        cart.delete()
        return redirect("/cart/")
    except:
        pass





def contact_page(request):
    if request.method == "POST":
        first_name = request.POST.get("first_name")
        phone = request.POST.get("number")
        email = request.POST.get("email")
        message = request.POST.get("message")
        Contact.objects.create(
            first_name = first_name,
            phone = phone,
            email = email,
            message = message,
            
        )
        return redirect("/")
    return render(request, "contact.html")



def add_to_like_page(request, like_id):
    try:
        tovar = Tovar.objects.get(unique_id=like_id)
        try:
            Like.objects.get(tovar=tovar)
            messages.warning(request, "Savatchada bunday tovar mavjud")
            return redirect("/")
        except:
            Like.objects.create(tovar=tovar)
    except Tovar.DoesNotExist:
        print("tovar yoq")  

    try:
        gadjet = Gadjet.objects.get(unique_id=like_id)
        try:
            Like.objects.get(gadjet=gadjet)
            messages.warning(request, "Savatchada bunday tovar mavjud")

            return redirect("/")
        except:
            Like.objects.create(gadjet=gadjet)
    except Gadjet.DoesNotExist:
        print("tovar yoq")


    try:
        tv = Tv.objects.get(unique_id=like_id)
        try:
            Like.objects.get(tv=tv)
            messages.warning(request, "Savatchada bunday tovar mavjud")
            return redirect("/")
        except:
            Like.objects.create(tv=tv)
    except Tv.DoesNotExist:
        print("tovar yoq")

    try:
        kitob = Kitob.objects.get(unique_id=like_id)
        try:
            Like.objects.get(kitob=kitob)
            messages.warning(request, "Savatchada bunday tovar mavjud")
            return redirect("/")
        except:
            Like.objects.create(kitob=kitob)
    except Kitob.DoesNotExist:
        print("tovar yoq")

    try:
        texnika = Texnika.objects.get(unique_id=like_id)
        try:
            Like.objects.get(texnika=texnika)
            messages.warning(request, "Savatchada bunday tovar mavjud")
            return redirect("/")
        except:
            Like.objects.create(texnika=texnika)
    except Texnika.DoesNotExist:
        print("tovar yoq")
    
    try:
        notebook = Notebook.objects.get(unique_id=like_id)
        try:
            Like.objects.get(notebook=notebook)
            messages.warning(request, "Savatchada bunday tovar mavjud")
            return redirect("/")
        except:
            Like.objects.create(notebook=notebook)
    except Notebook.DoesNotExist:
        print("tovar yoq")

    try:
        expensiv = Konditsioner.objects.get(unique_id=like_id)
        try:
            Like.objects.get(expensiv=expensiv)
            messages.warning(request, "Savatchada bunday tovar mavjud")
            return redirect("/")
        except:
            Like.objects.create(expensiv=expensiv)
    except Konditsioner.DoesNotExist:
        print("tovar yoq")
    return redirect("/")
   


def remove_like_page(request, like_id):
    try:
        like = Like.objects.get(id=like_id)
        like.delete()
        return redirect("/like/")
    except:
        pass



