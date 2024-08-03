# FAQ

## What apps are supported for accessing the Matrix server?

Element's [web](https://app.element.io),
[iOS](https://apps.apple.com/app/vector/id1083446067), and
[Android](https://play.google.com/store/apps/details?id=im.vector.app) apps.

## Can I sign in with my existing Matrix or Element account?

Because we are self-hosting the server and have disabled
[federation](https://element.io/features/closed-federation-and-open-federation),
which is the feature that allows users to have one account for multiple
servers, you will need to create an account specifically for this
Matrix server.

## Can I sign into another Matrix or Element account and remain signed into this Matrix server?

Unfortunately, there is
[currently no way](https://github.com/element-hq/roadmap/issues/11) to sign into
multiple Matrix accounts in any Element app.

If you need to log in to multiple Matrix accounts, you can install multiple
different [Matrix clients](https://matrix.org/ecosystem/clients/)
and use one for this server, and one for the other account.

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

Click on `Create Account`, which should take you to this screen:

<img width="573" src="/images/faq-2.png">

Click `Edit` under `Host account on`, on the right hand side, which should
open this pop-up: 

<img width="573" src="/images/faq-3.png">

Select `Other homeserver`, and type in `https://chat.warmupboston.org`. Then,
enter the username and password you would like to use.

I would recommend generating a secure password and storing it in a password
manager (I'd recommend [Bitwarden](https://bitwarden.com/) as a good free option,
if you don't already have one). Click `Continue`.

You should be prompted to enter your Registration Token. Do so, and then click `Continue`.

<img width="573" src="/images/faq-4.png">

A message should appear which prompts you set up Secure Backup. This will provide
you with a key which will allow you to read previously sent or received messages
that are end-to-end encrypted when logging in on another device or logging
back in after logging out on this device.

<img width="573" src="/images/faq-5.png">

Select `Generate a Security Key` and click `Continue`. Store the generated key
somewhere safe, like in a password manager (such as Bitwarden).

If you don't receive the prompt to set up Secure Backup upon initially logging in,
set it up by clicking the gear icon in the bottom left of the screen and clicking
`All settings`:

<img width="573" src="/images/faq-6.png">

Then clicking on `Security & Privacy` on the left hand side of the pop up window,
and clicking `Set up` under `Encryption > Secure Backup`:

<img width="573" src="/images/faq-7.png">

Then, follow the instructions above.

## How is the Matrix server organized?

"Room" is the Matrix term for what other platforms might call a channel or chatroom.
A "Space" is a group of Rooms, where things like the list of members can be managed
all together at the Space level.

Spaces that you are in appear at the top left of the screen in the Element web app,
below your profile picture. DMs with other users appear to the right of the Spaces
under the `People` heading, and Rooms you are in appear below that under the `Rooms`
heading.

<img width="573" src="/images/faq-8.png">

## How can I find Spaces or Rooms that I'm not already in?

To find a Space, in the Element web app, in the top left of the screen, below the
icons for the Spaces you are already in, click on the `+` button, and click
`Search for public spaces`.

<img width="573" src="/images/faq-9.png">

To find Rooms within a Space, first select the Space on the left hand side of the
screen, and then to the right of that, click the `+` button next to the `Rooms`
heading, then click on `Explore rooms`.

<img width="573" src="/images/faq-10.png">

## Can I create a bio for my account?

Unfortunately, user bios are
[not currently a feature](https://github.com/matrix-org/matrix-spec-proposals/issues/3795)
of Matrix. Feel free to put useful information about yourself, such as pronouns,
after your display name by clicking your profile picture in the top left, and
clicking `All Settings`:

<img width="573" src="/images/faq-11.png">

Then edit the value in the `Display Name` box:

<img width="573" src="/images/faq-12.png">

## What does it mean to verify a session?

Verifying a session is a way of proving that you are the same person when
logging in on a new device or app. Sessions can also be verified between two
users by exchanging information in person or over another communication channel
to prove that they are who they say they are on the Matrix server.

### Across multiple devices or apps

For instructions on verifying a session on a new device or in a new app, see
[the Element documentation](https://ems-docs.element.io/books/element-cloud-documentation/page/verify-new-login#bkmrk-scan-qr-code-on-anot).

### Between two users

For instructions on device verification between two users, see page 6 of
[the Element user guide](https://static.element.io/pdfs/element-user-guide.pdf).

## How can I make messages in a Room disappear a certain amount of time after being sent?

Currently, there is no UI for setting the retention policy (the period of time
after which messages will be deleted, if any) for a Room, but it is possible to
do so using the developer tools. You will need to be an Admin for the Room.

To open the developer tools, type `/devtools` into the chatbox at the bottom
of the screen in the Room for which you would like to set the retention policy
(where it says `Send an encrypted message...`), then hit `Enter` twice.

<img width="573" src="/images/faq-13.png">

Click `Send custom timeline event` under the `Room` heading. 

<img width="573" src="/images/faq-14.png">

Enter `m.room.retention` in the box labeled `Event Type`, and enter the
following in the box labeled `Event Content`:

```json
{
  "max_lifetime": "7d"
}
```

<img width="573" src="/images/faq-15.png">

Replace `7` with the number of days messages should be kept before
being deleted, then click the `Send` button.
