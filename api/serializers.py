from rest_framework import serializers


try:

    from home.models import OfferLetter

except:
    pass 

class OfferLetterSerializer(serializers.ModelSerializer):
    class Meta:

        try:
            model = OfferLetter
        except:
            pass    
        fields = '__all__'

