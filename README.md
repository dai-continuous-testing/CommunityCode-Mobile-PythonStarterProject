# Community Code - Mobile - Python Starter Project
This project demonstrates how to write tests for Continuous Testing Cloud using Python. Once cloned and set up properly, it runs as is.

## Setting Up the Sample Project

1. Clone the sample project.
    ```bash
    git clone https://github.com/ExperitestOfficial/CommunityCode-Mobile-PythonStarterProject
    cd CommunityCode-Mobile-PythonStarterProject
    ```
1. Set up authentication by updating these  parameters in [cloud.properties](cloud.properties):
    * url - URL for the cloud to run the test in. For example, https://company.experitest.com/
    * accessKey -  Personal authentication. See [Obtaining Access Key](https://docs.digital.ai/bundle/TE/page/obtaining_access_key.html) to learn how to obtain an access key.
1. Make sure that Python 3 is installed.
1. Install the dependencies.
```bash
pip install -r requirements.txt
```

## Running Tests
To run all tests in this project, run this on the command line: 

```bash
python -m unittest
```

## Upload Application to the Cloud

The example tests in native_demo use a demo application.
To upload your own application to cloud:
1. Log in to the cloud using a browser.
1. In the left menu click Applications.
1. Click Upload.
1. Click the application file to upload.

In your tests, change the application capabilities to your own app in the following lines:
* For Android:
```
options.app = 'cloud:com.experitest.ExperiBank/.LoginActivity'
options.appPackage = 'com.experitest.ExperiBank'
options.appActivity = '.LoginActivity'
```
* For iOS:
```
options.app = 'cloud:com.experitest.ExperiBank'
options.bundleId = 'com.experitest.ExperiBank'
```
For more ways to upload your application to the cloud, see [Native Applications Testing](https://docs.digital.ai/bundle/TE/page/native_applications_testing.html).

## Desired Capabilities

Continuous Cloud Testing expands Appium's capabilities and allows better control over the device and test.
In these examples we use the desired capabilities to set the test name and choose devices to run on, as well as set the application.
See [Capabilities in Appium Based Tests](https://docs.digital.ai/bundle/TE/page/capabilties_in_appium_based_tests.html) to learn how to customize the desired capabilities for your tests.

## Documentation
To find out more about Continuous Cloud Testing usage, features, and best practices, visit our online [documentation](https://docs.digital.ai/bundle/TE/page/test_execution_home.html).

## Support
If you encounter an issue that is not covered here or in our online documentation, contact us at [support@digital.ai](mailto:support@digital.ai).
