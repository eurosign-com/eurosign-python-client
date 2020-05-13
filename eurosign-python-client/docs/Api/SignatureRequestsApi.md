# Eurosign\SignatureRequestsApi

All URIs are relative to *https://api.eurosign.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancelSignatureRequests**](SignatureRequestsApi.md#cancelsignaturerequests) | **POST** /signature-requests/{uuid}/cancel | Cancel a signature requests
[**createSignatureRequest**](SignatureRequestsApi.md#createsignaturerequest) | **POST** /signature-requests | Create a new signature request
[**getSignatureRequest**](SignatureRequestsApi.md#getsignaturerequest) | **GET** /signature-requests/{uuid} | Get signature requests test
[**getSignatureRequestAuditTrail**](SignatureRequestsApi.md#getsignaturerequestaudittrail) | **GET** /signature-requests/{uuid}/audit-trail | Get the audit report of a signature requests
[**getSignatureRequestRecipient**](SignatureRequestsApi.md#getsignaturerequestrecipient) | **GET** /signature-requests/{uuid}/recipients/{recipientUuid} | Get a recipient of a signature requests
[**getSignatureRequestRecipients**](SignatureRequestsApi.md#getsignaturerequestrecipients) | **GET** /signature-requests/{uuid}/recipients | Get recipients of a signature requests
[**getSignatureRequests**](SignatureRequestsApi.md#getsignaturerequests) | **GET** /signature-requests | Get the list of signature requests
[**sendSignatureRequest**](SignatureRequestsApi.md#sendsignaturerequest) | **POST** /signature-requests/{uuid}/send | Send a signature requests
[**updateSignatureRequest**](SignatureRequestsApi.md#updatesignaturerequest) | **PATCH** /signature-requests/{uuid} | Update a signature requests

# **cancelSignatureRequests**
> cancelSignatureRequests($uuid)

Cancel a signature requests

### Example
```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure OAuth2 access token for authorization: eurosign_auth
$config = Eurosign\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

$apiInstance = new Eurosign\Api\SignatureRequestsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$uuid = "uuid_example"; // string | The signature request UUID

try {
    $apiInstance->cancelSignatureRequests($uuid);
} catch (Exception $e) {
    echo 'Exception when calling SignatureRequestsApi->cancelSignatureRequests: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **string**| The signature request UUID |

### Return type

void (empty response body)

### Authorization

[eurosign_auth](../../README.md#eurosign_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **createSignatureRequest**
> \Eurosign\Model\InlineResponse2001 createSignatureRequest($body)

Create a new signature request

### Example
```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure OAuth2 access token for authorization: eurosign_auth
$config = Eurosign\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

$apiInstance = new Eurosign\Api\SignatureRequestsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$body = new \Eurosign\Model\Body(); // \Eurosign\Model\Body | Input data format

try {
    $result = $apiInstance->createSignatureRequest($body);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling SignatureRequestsApi->createSignatureRequest: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**\Eurosign\Model\Body**](../Model/Body.md)| Input data format | [optional]

### Return type

[**\Eurosign\Model\InlineResponse2001**](../Model/InlineResponse2001.md)

### Authorization

[eurosign_auth](../../README.md#eurosign_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **getSignatureRequest**
> getSignatureRequest($uuid)

Get signature requests test

### Example
```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure OAuth2 access token for authorization: eurosign_auth
$config = Eurosign\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

$apiInstance = new Eurosign\Api\SignatureRequestsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$uuid = "uuid_example"; // string | Identifiant of a signature request

try {
    $apiInstance->getSignatureRequest($uuid);
} catch (Exception $e) {
    echo 'Exception when calling SignatureRequestsApi->getSignatureRequest: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **string**| Identifiant of a signature request |

### Return type

void (empty response body)

### Authorization

[eurosign_auth](../../README.md#eurosign_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **getSignatureRequestAuditTrail**
> getSignatureRequestAuditTrail($uuid)

Get the audit report of a signature requests

### Example
```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure OAuth2 access token for authorization: eurosign_auth
$config = Eurosign\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

$apiInstance = new Eurosign\Api\SignatureRequestsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$uuid = "uuid_example"; // string | Identifiant of a signature request

try {
    $apiInstance->getSignatureRequestAuditTrail($uuid);
} catch (Exception $e) {
    echo 'Exception when calling SignatureRequestsApi->getSignatureRequestAuditTrail: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **string**| Identifiant of a signature request |

### Return type

void (empty response body)

### Authorization

[eurosign_auth](../../README.md#eurosign_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **getSignatureRequestRecipient**
> getSignatureRequestRecipient($uuid, $recipient_uuid)

Get a recipient of a signature requests

### Example
```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure OAuth2 access token for authorization: eurosign_auth
$config = Eurosign\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

$apiInstance = new Eurosign\Api\SignatureRequestsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$uuid = "uuid_example"; // string | Identifiant of a signature request
$recipient_uuid = "recipient_uuid_example"; // string | Identifiant of a recipient

try {
    $apiInstance->getSignatureRequestRecipient($uuid, $recipient_uuid);
} catch (Exception $e) {
    echo 'Exception when calling SignatureRequestsApi->getSignatureRequestRecipient: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **string**| Identifiant of a signature request |
 **recipient_uuid** | **string**| Identifiant of a recipient |

### Return type

void (empty response body)

### Authorization

[eurosign_auth](../../README.md#eurosign_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **getSignatureRequestRecipients**
> getSignatureRequestRecipients($uuid)

Get recipients of a signature requests

### Example
```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure OAuth2 access token for authorization: eurosign_auth
$config = Eurosign\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

$apiInstance = new Eurosign\Api\SignatureRequestsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$uuid = "uuid_example"; // string | Identifiant of a signature request

try {
    $apiInstance->getSignatureRequestRecipients($uuid);
} catch (Exception $e) {
    echo 'Exception when calling SignatureRequestsApi->getSignatureRequestRecipients: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **string**| Identifiant of a signature request |

### Return type

void (empty response body)

### Authorization

[eurosign_auth](../../README.md#eurosign_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **getSignatureRequests**
> \Eurosign\Model\InlineResponse200 getSignatureRequests()

Get the list of signature requests

Retrieve the list of all the signature requests

### Example
```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

$apiInstance = new Eurosign\Api\SignatureRequestsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);

try {
    $result = $apiInstance->getSignatureRequests();
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling SignatureRequestsApi->getSignatureRequests: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**\Eurosign\Model\InlineResponse200**](../Model/InlineResponse200.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **sendSignatureRequest**
> sendSignatureRequest($uuid, $sender_id)

Send a signature requests

### Example
```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure OAuth2 access token for authorization: eurosign_auth
$config = Eurosign\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

$apiInstance = new Eurosign\Api\SignatureRequestsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$uuid = "uuid_example"; // string | The signature request UUID
$sender_id = "sender_id_example"; // string | The ID of the account_user sending the signature request

try {
    $apiInstance->sendSignatureRequest($uuid, $sender_id);
} catch (Exception $e) {
    echo 'Exception when calling SignatureRequestsApi->sendSignatureRequest: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **string**| The signature request UUID |
 **sender_id** | **string**| The ID of the account_user sending the signature request |

### Return type

void (empty response body)

### Authorization

[eurosign_auth](../../README.md#eurosign_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **updateSignatureRequest**
> updateSignatureRequest($uuid, $body)

Update a signature requests

### Example
```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure OAuth2 access token for authorization: eurosign_auth
$config = Eurosign\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

$apiInstance = new Eurosign\Api\SignatureRequestsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$uuid = "uuid_example"; // string | The signature request UUID
$body = new \Eurosign\Model\Body1(); // \Eurosign\Model\Body1 | Input data format

try {
    $apiInstance->updateSignatureRequest($uuid, $body);
} catch (Exception $e) {
    echo 'Exception when calling SignatureRequestsApi->updateSignatureRequest: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **string**| The signature request UUID |
 **body** | [**\Eurosign\Model\Body1**](../Model/Body1.md)| Input data format | [optional]

### Return type

void (empty response body)

### Authorization

[eurosign_auth](../../README.md#eurosign_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

