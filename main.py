from __future__ import print_function
import requests
 
def build_response_payload( title, output, reprompt_text, should_end_session ):
    return {
        'outputSpeech': {
            'type': 'PlainText',
            'text': output
        },
        'card': {
            'type': 'Simple',
            'title': "alexaHelloWorld - " + title,
            'content': "alexaHelloWorld - " + output
        },
        'reprompt': {
            'outputSpeech': {
                'type': 'PlainText',
                'text': reprompt_text
            }
        },
        'shouldEndSession': should_end_session
    }
 
def build_response( session_attributes, speechlet_response ):
    return {
        'version': '1.0',
        'sessionAttributes': session_attributes,
        'response': speechlet_response
    }
 
def say_hello_world():
    session_attributes = {}
    r = requests.post('https://requestb.in/1d8vb801', data={"ts":"light on"})
    card_title = "Hello World"
    speech_output = "Hello vish"
    should_end_session = True
    return build_response( session_attributes, build_response_payload( card_title, speech_output, speech_output, should_end_session ) )
 
def lambda_handler( event, context ):
    return say_hello_world()