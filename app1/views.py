from django.shortcuts import render, redirect
from .forms import FlickForm
from app1.models import Flick,Flick2
import os
import boto3
from django.http import JsonResponse


def put_pics(title, description, tags, s3picture):
    # region = boto3.session.Session().region_name
    region = os.getenv('AWS_REGION')
    # print(region)
    # i=input("pause")
    dynamodb = boto3.resource('dynamodb', region_name=region) # low-level client
    table = dynamodb.Table('pics2')
    response = table.put_item(
    Item={
            'title': title,
            'description': description,
            'tags': tags,
            's3picture': s3picture,
        }
    )
    return response

def get_pics():
    region = os.getenv('AWS_REGION')
    dynamodb = boto3.resource('dynamodb', region_name=region) # low-level client
    table = dynamodb.Table('pics2')
    response = table.scan()
    items = response['Items']
    while 'LastEvaluatedKey' in response:
        response = table.scan(ExclusiveStartKey=response['LastEvaluatedKey'])
        items.extend(response['Items'])
    return items

def index(request):
    if request.method == 'POST':
        form = FlickForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            title = request.POST.get('title', None)
            desc = request.POST.get('description', None)
            tags = request.POST.get('tags', None)
            s3picture = request.FILES.get('picture', None)
            put_response = put_pics(title, desc, tags, str(s3picture))
            print("Put movie succeeded:")
            return redirect('index')
    else:
        #flicks = Flick.objects.all()
        items = get_pics()
        #print(items)
        form = FlickForm()
    return render(request, 'app1/index.html', {'form': form,'flicks':items})







def testboto_createtable(request):
    # Get the service resource.
    region = os.getenv('AWS_REGION')
    dynamodb = boto3.resource('dynamodb', region_name=region)

    # Create the DynamoDB table.
    table = dynamodb.create_table(
        TableName='pics2',
        KeySchema=[
            {
                'AttributeName': 'title',
                'KeyType': 'HASH'
            },
            {
                'AttributeName': 'description',
                'KeyType': 'RANGE'
            }
        ],
        AttributeDefinitions=[
            {
                'AttributeName': 'title',
                'AttributeType': 'S'
            },
            {
                'AttributeName': 'description',
                'AttributeType': 'S'
            }
        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 5,
            'WriteCapacityUnits': 5
        }
    )

    # Wait until the table exists.
    table.wait_until_exists()

    # Print out some data about the table.
    print(table.item_count)
    return JsonResponse("create complete complete",safe=False)














def test(request):
    # create a new object
    obj = Flick2(id=1, title='Test', description='This is a test object',tags= 'tt' ,picture='pp')
    obj.save()
    # retrieve an object
    obj = Flick2.get(1)
    return JsonResponse(obj,safe=False)

# def my_view(request):
#     dynamodb = boto3.resource('dynamodb', region_name='your-region-name', aws_access_key_id='your-access-key', aws_secret_access_key='your-secret-key')
#     table = dynamodb.Table('your-table-name')

#     item = {
#         'id': '1',
#         'name': 'Test',
#         'description': 'This is a test object',
#     }

#     # add the item to the table
#     table.put_item(Item=item)

#     # retrieve an item
#     response = table.get_item(Key={'id': '1'})

#     # return the item as JSON
#     return JsonResponse(response['Item'])