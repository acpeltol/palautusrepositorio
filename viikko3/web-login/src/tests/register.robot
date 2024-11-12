*** Settings ***
Resource  resource.robot
Suite Setup     Open And Configure Browser
Suite Teardown  Close Browser
Test Setup      Reset Application Create User And Go To Register Page

*** Test Cases ***

Register With Valid Username And Password
    Set Username  Hella
    Set Password  Kevin_123
    Set Password_confirmation  Kevin_123
    Submit Credentials
    Title Should Be  Welcome to Ohtu Application!


Register With Too Short Username And Valid Password
    Set Username  Al
    Set Password  Kevin_123
    Set Password_confirmation  Kevin_123
    Submit Credentials
    Register Should Fail With Message  Username must be atleast 3 chars long

Register With Valid Username And Too Short Password
    Set Username  Alvin
    Set Password  Ke1
    Set Password_confirmation  Ke1
    Submit Credentials
    Register Should Fail With Message  Username must be atleast 8 chars long

Register With Valid Username And Invalid Password
# salasana ei sisällä halutunlaisia merkkejä
    Set Username  Alvun
    Set Password  Kevincostner
    Set Password_confirmation  Kevincostner
    Submit Credentials
    Register Should Fail With Message  Invalid password

Register With Nonmatching Password And Password Confirmation
    Set Username  Alvun
    Set Password  Kevin_123
    Set Password_confirmation  Kevin_125
    Submit Credentials
    Register Should Fail With Message  Password was not confirmed

Register With Username That Is Already In Use
    Set Username  Hella
    Set Password  Kevin_123
    Set Password_confirmation  Kevin_123
    Submit Credentials
    Go To Register Page
    Set Username  Hella
    Set Password  Kevin_123
    Set Password_confirmation  Kevin_123
    Submit Credentials
    Register Should Fail With Message  User with username Hella already exists

Login After Successful Registration
    Set Username  Hella
    Set Password  Kevin_123
    Set Password_confirmation  Kevin_123
    Submit Credentials
    Go To Login Page
    Set Username  Hella
    Set Password  Kevin_123
    Click Button  Login
    Login Should Succeed

Login After Failed Registration
    Set Username  Al
    Set Password  Kevin_123
    Set Password_confirmation  Kevin_123
    Submit Credentials
    Go To Login Page
    Set Username  Al
    Set Password  Kevin_123
    Click Button  Login
    Login Should Fail With Message  Invalid username or password

*** Keywords ***
Login Should Succeed
    Main Page Should Be Open

#Register Should Succeed
#    Main Page Should Be Open

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Login Should Fail With Message
    [Arguments]  ${message}
    Login Page Should Be Open
    Page Should Contain  ${message}

Submit Credentials
    Click Button  Register

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password_confirmation
    [Arguments]  ${password_confirmation}
    Input Password  password_confirmation  ${password_confirmation}

*** Keywords ***
Reset Application Create User And Go To Register Page
    Reset Application
    Go To Register Page
