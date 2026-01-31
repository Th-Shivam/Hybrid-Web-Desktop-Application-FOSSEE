from rest_framework import viewsets
from .models import Item, CSVHistory
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
    
    # Calculate simple stats
    # Using 'round' to make it look clean
    avg_flow = round(df['Flowrate'].mean(), 2)
    avg_pressure = round(df['Pressure'].mean(), 2)
    avg_temp = round(df['Temperature'].mean(), 2)
    
    # Count equipment types
    # converting to dict for easy json
    type_counts = df['Type'].value_counts().to_dict()
    
    # Return summary
    summary = {
        "total_rows": len(df),
        "average_metrics": {
            "flowrate": avg_flow,
            "pressure": avg_pressure,
            "temperature": avg_temp
        },
        "equipment_type_counts": type_counts
    }
    
    # Save to DB (only last 5 will be kept)
    CSVHistory.objects.create(
        file_name=file.name,
        summary_data=summary
    )
    
    return Response(summary)
