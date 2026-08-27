# SecureChat Android — Interface Design Plan

## Product direction

SecureChat is a privacy-first Android messaging prototype for portrait orientation and one-handed use. The visual language is calm, trustworthy, and lightweight rather than copying Messenger or Telegram directly. The prototype will clearly distinguish local demo behavior from production-grade encrypted network behavior.

## Screen list

| Screen | Primary content and functionality |
|---|---|
| Conversations | Recent private and group conversations, unread counts, last-message preview, online indicators, search, and a compose button. |
| Chat | Conversation header, message bubbles, reply/attachment/action controls, typing state, delivery/read state, and message composer. |
| New conversation | Searchable contacts and suggested contacts; starts a private conversation. |
| New group | Select contacts, choose group name/avatar, and create a group conversation. |
| Group details | Group avatar/name, members, mute notifications, shared media entry point, and leave/report controls. |
| Profile and privacy | Display name, username, avatar placeholder, online visibility, read receipts, disappearing-message preference, blocked users, and active sessions. |
| Settings | Notifications, appearance, storage, security information, help, and sign-out. |
| Security center | Plain-language explanation of encryption status, device/session list, verification status, and warning states. |

## Layout and interaction

The app uses a bottom tab bar with Conversations and Settings. The Conversations screen has a compact top header with the product mark, search action, and new-chat action. Conversation rows are at least 64dp high for comfortable one-handed tapping. The primary action button sits in the lower-right area above the safe-area inset.

The Chat screen keeps the message composer anchored above the keyboard. The attachment button opens a bottom sheet with photo, file, camera, voice message, and contact actions. Long-pressing a message opens actions for reply, copy, forward, react, delete, and report. Destructive actions require confirmation. The back action always returns to the conversation list without losing draft text.

## Color choices

The brand uses deep midnight navy `#0B1220` for security and trust, electric cyan `#26C6DA` for primary actions and sent-message accents, soft ice `#F4F8FB` for light surfaces, slate `#64748B` for secondary text, and mint `#22C55E` for online and verified states. Error states use `#DC2626`, while warning states use `#D97706`. Dark mode uses navy surfaces with high-contrast off-white text; the cyan accent remains reserved for actionable or selected states.

## Key user flows

1. The user opens Conversations, taps a person, types a message, taps send, and sees a pending state change to delivered and then read when the conversation is opened.
2. The user taps New conversation, searches a contact, opens the profile preview, and starts a private chat.
3. The user taps New group, selects contacts, enters a group name, creates the group, and lands in the group chat.
4. The user long-presses a message, chooses Reply or React, and sees the related context rendered above the composer or attached to the message bubble.
5. The user opens Profile and privacy, changes read receipts or disappearing messages, and sees the setting persist locally.
6. The user opens Security center, reviews active sessions, and can revoke a session. Production implementation must use device-secure key storage and an audited end-to-end encryption protocol; this prototype must not claim production-grade encryption until the backend and cryptographic review are complete.

## Security vocabulary

A conversation is the shared logical thread. A message has an id, sender, timestamp, delivery state, read state, optional reply reference, and optional attachment metadata. A device session represents one logged-in device. A cryptographic identity key belongs to a user/device pair, while a conversation key is rotated when membership or security state changes. The prototype will use these names consistently so a future backend can be added without changing the user-facing model.
