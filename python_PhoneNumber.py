import phonenumbers


number1="+14103333333"
number2="+905466827029"

from phonenumbers import geocoder
number=phonenumbers.parse(number1)
print(geocoder.description_for_number(number,'tr'))

from phonenumbers import carrier
number = phonenumbers.parse(number2)
print(carrier.name_for_number(number,'tr'))

from phonenumbers import timezone
number=phonenumbers.parse(number1)
print(timezone.time_zones_for_number(number))

