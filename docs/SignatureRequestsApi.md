# swagger_client.SignatureRequestsApi

All URIs are relative to *https://api.eurosign.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancel_signature_requests**](SignatureRequestsApi.md#cancel_signature_requests) | **POST** /signature-requests/{uuid}/cancel | Cancel a signature requests
[**create_signature_request**](SignatureRequestsApi.md#create_signature_request) | **POST** /signature-requests | Create a new signature request
[**get_signature_request**](SignatureRequestsApi.md#get_signature_request) | **GET** /signature-requests/{uuid} | Get signature requests test
[**get_signature_request_audit_trail**](SignatureRequestsApi.md#get_signature_request_audit_trail) | **GET** /signature-requests/{uuid}/audit-trail | Get the audit report of a signature requests
[**get_signature_request_recipient**](SignatureRequestsApi.md#get_signature_request_recipient) | **GET** /signature-requests/{uuid}/recipients/{recipientUuid} | Get a recipient of a signature requests
[**get_signature_request_recipients**](SignatureRequestsApi.md#get_signature_request_recipients) | **GET** /signature-requests/{uuid}/recipients | Get recipients of a signature requests
[**get_signature_requests**](SignatureRequestsApi.md#get_signature_requests) | **GET** /signature-requests | Get the list of signature requests
[**send_signature_request**](SignatureRequestsApi.md#send_signature_request) | **POST** /signature-requests/{uuid}/send | Send a signature requests
[**update_signature_request**](SignatureRequestsApi.md#update_signature_request) | **PATCH** /signature-requests/{uuid} | Update a signature requests

# **cancel_signature_requests**
> cancel_signature_requests(uuid)

Cancel a signature requests

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: eurosign_auth
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.SignatureRequestsApi(swagger_client.ApiClient(configuration))
uuid = 'uuid_example' # str | The signature request UUID

try:
    # Cancel a signature requests
    api_instance.cancel_signature_requests(uuid)
except ApiException as e:
    print("Exception when calling SignatureRequestsApi->cancel_signature_requests: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| The signature request UUID | 

### Return type

void (empty response body)

### Authorization

[eurosign_auth](../README.md#eurosign_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_signature_request**
> InlineResponse2001 create_signature_request(body=body)

Create a new signature request

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: eurosign_auth
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.SignatureRequestsApi(swagger_client.ApiClient(configuration))
body = swagger_client.Body() # Body | Input data format (optional)

try:
    # Create a new signature request
    api_response = api_instance.create_signature_request(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SignatureRequestsApi->create_signature_request: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body**](Body.md)| Input data format | [optional] 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

[eurosign_auth](../README.md#eurosign_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_signature_request**
> get_signature_request(uuid)

Get signature requests test

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: eurosign_auth
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.SignatureRequestsApi(swagger_client.ApiClient(configuration))
uuid = 'uuid_example' # str | Identifiant of a signature request

try:
    # Get signature requests test
    api_instance.get_signature_request(uuid)
except ApiException as e:
    print("Exception when calling SignatureRequestsApi->get_signature_request: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| Identifiant of a signature request | 

### Return type

void (empty response body)

### Authorization

[eurosign_auth](../README.md#eurosign_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_signature_request_audit_trail**
> get_signature_request_audit_trail(uuid)

Get the audit report of a signature requests

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: eurosign_auth
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.SignatureRequestsApi(swagger_client.ApiClient(configuration))
uuid = 'uuid_example' # str | Identifiant of a signature request

try:
    # Get the audit report of a signature requests
    api_instance.get_signature_request_audit_trail(uuid)
except ApiException as e:
    print("Exception when calling SignatureRequestsApi->get_signature_request_audit_trail: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| Identifiant of a signature request | 

### Return type

void (empty response body)

### Authorization

[eurosign_auth](../README.md#eurosign_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_signature_request_recipient**
> get_signature_request_recipient(uuid, recipient_uuid)

Get a recipient of a signature requests

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: eurosign_auth
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.SignatureRequestsApi(swagger_client.ApiClient(configuration))
uuid = 'uuid_example' # str | Identifiant of a signature request
recipient_uuid = 'recipient_uuid_example' # str | Identifiant of a recipient

try:
    # Get a recipient of a signature requests
    api_instance.get_signature_request_recipient(uuid, recipient_uuid)
except ApiException as e:
    print("Exception when calling SignatureRequestsApi->get_signature_request_recipient: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| Identifiant of a signature request | 
 **recipient_uuid** | **str**| Identifiant of a recipient | 

### Return type

void (empty response body)

### Authorization

[eurosign_auth](../README.md#eurosign_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_signature_request_recipients**
> get_signature_request_recipients(uuid)

Get recipients of a signature requests

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: eurosign_auth
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.SignatureRequestsApi(swagger_client.ApiClient(configuration))
uuid = 'uuid_example' # str | Identifiant of a signature request

try:
    # Get recipients of a signature requests
    api_instance.get_signature_request_recipients(uuid)
except ApiException as e:
    print("Exception when calling SignatureRequestsApi->get_signature_request_recipients: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| Identifiant of a signature request | 

### Return type

void (empty response body)

### Authorization

[eurosign_auth](../README.md#eurosign_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_signature_requests**
> InlineResponse200 get_signature_requests()

Get the list of signature requests

Retrieve the list of all the signature requests

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SignatureRequestsApi()

try:
    # Get the list of signature requests
    api_response = api_instance.get_signature_requests()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SignatureRequestsApi->get_signature_requests: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **send_signature_request**
> send_signature_request(uuid, sender_id)

Send a signature requests

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: eurosign_auth
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.SignatureRequestsApi(swagger_client.ApiClient(configuration))
uuid = 'uuid_example' # str | The signature request UUID
sender_id = 'sender_id_example' # str | The ID of the account_user sending the signature request

try:
    # Send a signature requests
    api_instance.send_signature_request(uuid, sender_id)
except ApiException as e:
    print("Exception when calling SignatureRequestsApi->send_signature_request: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| The signature request UUID | 
 **sender_id** | **str**| The ID of the account_user sending the signature request | 

### Return type

void (empty response body)

### Authorization

[eurosign_auth](../README.md#eurosign_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_signature_request**
> update_signature_request(uuid, body=body)

Update a signature requests

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: eurosign_auth
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.SignatureRequestsApi(swagger_client.ApiClient(configuration))
uuid = 'uuid_example' # str | The signature request UUID
body = swagger_client.Body1() # Body1 | Input data format (optional)

try:
    # Update a signature requests
    api_instance.update_signature_request(uuid, body=body)
except ApiException as e:
    print("Exception when calling SignatureRequestsApi->update_signature_request: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| The signature request UUID | 
 **body** | [**Body1**](Body1.md)| Input data format | [optional] 

### Return type

void (empty response body)

### Authorization

[eurosign_auth](../README.md#eurosign_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

