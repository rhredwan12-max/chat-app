# Project TODO

- [x] Define Android portrait-first interface design in design.md
- [x] Remove Robi/Airtel zero-rating from product scope
- [x] Generate and configure unique SecureChat app branding assets
- [x] Replace starter home screen with Conversations interface
- [x] Add Chat screen with composer and message actions
- [x] Add New conversation flow
- [x] Add New group flow
- [x] Add Profile, Privacy, Settings, and Security Center screens
- [ ] Add local persistence for prototype conversations and settings
- [x] Add delivery/read, typing, reply, reactions, and disappearing-message states
- [x] Add attachment picker UI for photo, file, camera, voice message, and contact
- [x] Add secure-session vocabulary and production encryption boundary notice
- [ ] Add deterministic unit tests for message state and local settings behavior
- [x] Verify Android preview and resolve runtime/type errors
- [ ] Document production backend, E2EE audit, push notification, and hosting requirements

- [x] Add phone-number registration and login flow
- [ ] Add OTP verification states and resend cooldown UI
- [x] Add number visibility controls: Everyone, Contacts, Nobody
- [x] Add profile photo, bio, username, online status, last seen, read receipt, typing, and shared media visibility controls
- [x] Add message request permissions: Everyone, Contacts, Nobody, with block/report handling
- [x] Add group invitation, calls, voice/video, and contact discovery permissions
- [x] Add per-user exceptions for allowed and blocked visibility
- [x] Add owner/admin role model with audit logs, user bans, reports, feature flags, and no plaintext E2EE message access
- [x] Add a secure owner setup flow so only the designated owner can manage platform controls
- [ ] Add deterministic tests for privacy matrix and admin permission boundaries

- [ ] Optimize startup for fast first render on ordinary Android devices
- [x] Keep chat list immediately available with lightweight local cache
- [ ] Defer non-critical screens and heavy assets until after first render
- [x] Reduce image/icon payloads and remove unnecessary startup work
- [x] Optimize FlatList rendering and message composer responsiveness
- [ ] Measure cold start and warm start behavior on Android preview

- [ ] Add language selector for বাংলা, English, and العربية
- [ ] Add complete translations for tabs, chat, settings, privacy, permissions, security, and owner console
- [ ] Persist selected language locally across app restarts
- [ ] Enable Arabic right-to-left layout and correct text alignment
- [ ] Verify Bengali, English, and Arabic message composition and rendering
- [ ] Test language switching across all available screens

- [ ] Prepare Android installable APK build configuration
- [ ] Confirm app icon, package identifier, portrait orientation, and Android permissions before build
- [ ] Do not publish or deploy until the owner explicitly approves it
- [ ] Provide APK through the approved build flow when owner is ready

- [x] Keep phone number input completely blank on first launch
- [ ] Require successful OTP verification before entering the main chat area
- [ ] Prevent navigation to chats when verification is incomplete
- [x] Diagnose why the current preview is not opening
- [x] Prepare the approved APK build handoff without publishing

- [x] Owner approved installable APK build request
- [x] Verify latest checkpoint is suitable for APK build
- [ ] Start approved APK build flow without app-store publishing
- [ ] Deliver the generated APK download file and installation instructions

- [ ] Add Continue with Google entry option beside phone-number login
- [ ] Add email-based account identity handling without pre-filled email
- [ ] Connect Google OAuth callback to verified main-area entry
- [ ] Keep phone OTP and Google sign-in sessions separate and revocable
- [ ] Add authentication error, cancellation, and retry states
- [ ] Test both authentication paths on Android preview
