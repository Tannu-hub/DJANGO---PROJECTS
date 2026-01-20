from django.shortcuts import render
from feedbackapp.models import FeedbackModel

# Create your views here.
def form_view(request):
    submitted = False
    if request.method == 'POST':
        a = request.POST['name']
        b = request.POST.get('feedback')
        FeedbackModel.objects.create(name = a,feedback = b)
        submitted = True
    
    return render(request,'form.html',{'submitted':submitted})

def Feedback_view(request):
    all_feedbacks = FeedbackModel.objects.all()
    return render(request,'feedback.html',{'all_feedbacks':all_feedbacks})

































































