# FAQ

## What apps are supported for accessing the Matrix server?

Element's [web](https://app.element.io),
[iOS](https://apps.apple.com/app/vector/id1083446067), and
[Android](https://play.google.com/store/apps/details?id=im.vector.app) apps.

## How do I create an account?

### On a smartphone

The registration flow we use doesn't work from either the
[iOS](https://github.com/element-hq/element-ios/issues/6507) or the
[Android](https://github.com/element-hq/element-android/issues/8192) app, so you
will need to open up the web browser on your phone, and navigate to the
[Element web app](https://app.element.io). Scroll to the bottom of the page and
tap `Go to Desktop Site`. Then, follow the directions under the next section,
"On a computer".

### On a computer

Navigate to the [Element web app](https://app.element.io) in your web browser.

You should see the following:

<img width="573" src="/images/faq-1.png">
<br/>
<br/>

Click on `Create Account`, which should take you to this screen:

<img width="573" src="/images/faq-2.png">
<br/>
<br/>

Click `Edit` under `Host account on`, on the right hand side, which should
open this pop-up: 

<img width="573" src="/images/faq-3.png">
<br/>
<br/>

Select `Other homeserver`, and type in `https://chat.warmupboston.org`. Then,
enter the username and password you would like to use.

I would recommend generating a secure password and storing it in a password
manager (I'd recommend [Bitwarden](https://bitwarden.com/) as a good free option,
if you don't already have one). Click `Continue`; you should be prompted to
enter your Registration Token. Do so, and then click `Continue`.

A message should appear which prompts you set up Secure Backup. This will provide
you with a key which will allow you to read previously sent or received messages
that are end-to-end encrypted when logging in on another device or logging
back in after logging out on this device.

<img width="573" src="/images/faq-4.png">
<br/>
<br/>

Select `Generate a Security Key` and click `Continue`. Store the generated key
somewhere safe, like in a password manager (such as Bitwarden).

If you don't receive the prompt to set up Secure Backup upon initially logging in,
set it up by clicking the gear icon in the bottom left of the screen and clicking
`All settings`:

<img width="573" src="/images/faq-5.png">
<br/>
<br/>

Then clicking on `Security & Privacy` on the left hand side of the pop up window,
and clicking `Set up` under `Encryption > Secure Backup`:

<img width="573" src="/images/faq-6.png">
<br/>
<br/>

Then, follow the instructions above.

## How is the Matrix server organized?

## How can I find Rooms that I'm not already in?

## Can I create a bio for my account?

## Can I sign into another Element account and remain signed into this Matrix server?

## What does it mean to verify a session?

### Across multiple devices or apps

### Between two users

## How can I make messages disappear a certain amount of time after being sent?
