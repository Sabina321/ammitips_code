
from django_twilio.decorators import twilio_view

from twilio.twiml import Response

             

@twilio_view
def gather_digits(request):
    twilio_response = Response()

    twilio_response.play('http://travellingscholar.com/ammi/message1.mp3') 

    twilio_response.play('http://travellingscholar.com/ammi/message2.mp3')
    with twilio_response.gather(action='respond', numDigits=1) as g:
#g.say('Assalaam walaikum, Ammi Tips par khush amdeed')
        #g.say(request)
        g.pause(length=1)
    return twilio_response


@twilio_view
def handle_response(request):
    digits = request.POST.get('Digits', '')
    twilio_response = Response()
    #twilio_response.play('http://travellingscholar.com/ammi/firstmessage.mp3')         
    if digits == '2':
        #digits3=request.POST.get('Digits','') 
        twilio_response.play('http://travellingscholar.com/ammi/message3b.mp3')
        twilio_response.play('http://travellingscholar.com/ammi/message4.mp3')
        req = 'http://23ee1813.ngrok.com/respond'
        #r2 = gather_digits(req)
         
        twilio_response.gather(action='respond2', numDigits=1)    
        
        #with twilio_response.gather(action='respond', numDigits=1) as g:
        #twilio_response.pause(length=1)
        #second_response= Response()

    if digits == '1':
        twilio_response.play('http://travellingscholar.com/ammi/message.mp3') 
    #    number = request.POST.get('From', '')
    #    twilio_response.say('A text message is on its way')
    #    twilio_response.sms('You looking lovely today!', to=number)
                                                           
    return twilio_response

@twilio_view
def handle_second_response(request):
    digits = request.POST.get('Digits', '') 
    twilio_response_two=Response()
    twilio_response_two.play('http://travellingscholar.com/ammi/message5a.mp3')
    twilio_response_two.gather(action='respond3', numDigits=1)  
    return twilio_response_two

@twilio_view
def handle_third_response(request):
    digits = request.POST.get('Digits', '')
    twilio_response_three=Response()
    #twilio_response_three.say(digits)
    twilio_response_three.play('http://travellingscholar.com/ammi/message6.mp3')
    twilio_response_three.gather(action='respond4', numDigits=1)
    return twilio_response_three

@twilio_view 
def handle_fourth_response(request):
    digits = request.POST.get('Digits', '')
    number = request.POST.get('From','')
    twilio_response_four=Response() 
    #twilio_response_four.say(digits)
    twilio_response_four.play('http://travellingscholar.com/ammi/message7a.mp3')
    twilio_response_four.sms('Your newborn will need lots of food to grow. The best food for your     newborn is your breastmilk. Feeding her honey or ghee is harmful and a          waste of your special milk.', to=number)
    return twilio_response_four


