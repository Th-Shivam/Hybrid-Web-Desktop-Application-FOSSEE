from rest_framework import viewsets
from .models import Item
from .serializers import ItemSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
import pandas as pd

class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

@api_view(['POST'])
def upload_csv(request):
    # Just assume file is there
    file = request.FILES['file']
    
    # Read CSV using pandas
    df = pd.read_csv(file)
    
    # Return count
    return Response({"rows": len(df)})
