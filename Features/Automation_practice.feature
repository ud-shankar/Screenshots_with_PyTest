Feature: Login
Different channels are provided for user to login/sign-up

    Scenario: User is trying to Login using the correct username and password textbox
        Given User opens login in page
        When User enters username and password and clicks sign-in button
        And User is in Home page
        Then User is logged-in

    Scenario: User is trying to click on my address with incorrect locator (Auto screenshot feature)
        Given User opens login in page
        When User enters username and password and clicks sign-in button
        And User is in Home page
        Then User clicks on My address with incorrect locator and screenshot is captured