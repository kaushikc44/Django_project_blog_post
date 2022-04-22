from django.shortcuts import render,redirect


from django.contrib.auth import login
from .forms import NewUserForm
from .models import Maker, Tweet
from django.views.generic import DetailView, ListView
from django.contrib import messages
# Create your views here.

# def home(request):
#     name = Maker.objects.all()
#     context = {'name':name}
#     return render(request,'home.html',context)

class ForumListDetail(ListView):
	model = Maker
	template_name = "home.html"
	
	def get(self, request):
		name = Maker.objects.all()
		ctx = {"name": name}
		return render(request, self.template_name, ctx)


def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect(home)
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request,"signup.html", context={"register_form":form})


class ForumDetailView(DetailView):
	model = Tweet
	template_name = "profile.html"
	def get(self, request, pk):
		user = Tweet.objects.get(id=pk)
		context = {'user':user}
		return render(request,self.template_name,context)