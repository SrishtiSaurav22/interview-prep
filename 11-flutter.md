# Flutter Crash Course Roadmap

> Goal: Prepare for Flutter internship/junior developer interviews while building practical Flutter skills.

---

# Phase 1: Interview Essentials (Learn First)

These topics cover the majority of Flutter internship interview questions.

## Session 1: Flutter Fundamentals

### Concepts

* What is Flutter?
* Why Flutter?
* What is Dart?
* Flutter Architecture
* Everything is a Widget
* Widget Tree
* Material Design
* Cupertino Design

### Widgets

* MaterialApp
* Scaffold
* AppBar
* Text

### Key Questions

* What is Flutter?
* Why use Flutter?
* What is Dart?
* What is a Widget?
* What is a Widget Tree?

---

## Session 2: Layouts and UI Building

### Concepts

* Parent-Child Relationship
* Layout System
* Constraints

### Widgets

* Container
* Row
* Column
* Center
* SizedBox
* Padding
* Expanded
* Spacer
* Align

### Key Questions

* Difference between Row and Column?
* What is Expanded?
* Padding vs Margin?

---

## Session 3: Stateless vs Stateful Widgets

### Concepts

* Widget Lifecycle
* State
* UI Rebuilding

### Widgets

* StatelessWidget
* StatefulWidget

### Methods

* createState()
* build()
* setState()

### Key Questions

* Difference between Stateless and Stateful widgets?
* What does setState() do?
* When would you use a Stateful Widget?

---

## Session 4: User Input

### Widgets

* TextField
* TextEditingController
* ElevatedButton
* IconButton
* Checkbox
* Switch

### Concepts

* Handling User Input
* Forms
* Validation

### Key Questions

* How do you get text from a TextField?
* What is TextEditingController?

---

## Session 5: Navigation

### Concepts

* Routing
* Navigation Stack

### APIs

* Navigator.push()
* Navigator.pop()

### Topics

* Passing Data Between Screens
* Returning Data

### Key Questions

* How do you navigate between screens?
* What is Navigator?

---

## Session 6: Lists and Dynamic UI

### Widgets

* ListView
* ListView.builder
* GridView

### Concepts

* Dynamic Data
* Item Rendering

### Key Questions

* Why use ListView.builder?
* Difference between ListView and Column?

---

## Session 7: Async Programming

### Concepts

* Synchronous vs Asynchronous Code
* Futures

### Keywords

* Future
* async
* await

### Widgets

* FutureBuilder

### Key Questions

* What is a Future?
* Why use async/await?
* What is FutureBuilder?

---

## Session 8: API Calls

### Concepts

* REST APIs
* JSON
* Serialization

### Packages

* http

### Topics

* GET Requests
* POST Requests
* Parsing JSON
* Error Handling

### Key Questions

* How do you call an API?
* How do you parse JSON?

---

## Session 9: State Management Basics

### Concepts

* Local State
* Global State

### Tools

* setState()
* Provider (Overview)
* Riverpod (Overview)

### Key Questions

* What is State Management?
* Why not use setState everywhere?

---

## Session 10: Project Structure

### Example Structure

lib/

├── screens/

├── widgets/

├── models/

├── services/

├── providers/

├── utils/

└── main.dart

### Concepts

* Separation of Concerns
* Reusability
* Maintainability

### Key Questions

* How would you structure a Flutter project?

---

## Session 11: Widget Lifecycle

### Methods

* initState()
* build()
* dispose()

### Concepts

* Widget Creation
* Rebuilding
* Resource Cleanup

### Key Questions

* What is initState()?
* What is dispose()?

---

# Phase 2: Intermediate Flutter

## Session 12: Forms and Validation

* Form Widget
* GlobalKey
* Validators
* Error Handling

---

## Session 13: Local Storage

* SharedPreferences
* Secure Storage

---

## Session 14: Advanced Navigation

* Named Routes
* Route Arguments
* Deep Linking

---

## Session 15: Provider State Management

* ChangeNotifier
* Consumer
* Provider Architecture

---

## Session 16: Riverpod Basics

* Providers
* State Providers
* Future Providers

---

## Session 17: Networking Architecture

* Repository Pattern
* API Services
* Dependency Injection

---

# Phase 3: Production Flutter

## Session 18: Firebase

* Authentication
* Firestore
* Storage
* Notifications

---

## Session 19: Architecture

* MVC
* MVVM
* Clean Architecture

---

## Session 20: Testing

* Unit Testing
* Widget Testing
* Integration Testing

---

## Session 21: Performance Optimization

* const Widgets
* Lazy Loading
* Image Optimization
* Rebuild Optimization

---

## Session 22: Flutter Deployment

### Android

* APK
* AAB
* Play Store

### iOS

* TestFlight
* App Store

---

# Interview Revision Checklist

Before any Flutter interview, make sure you can confidently answer:

* What is Flutter?
* What is Dart?
* What is a Widget?
* What is a Widget Tree?
* Stateless vs Stateful Widgets
* What is setState()?
* What is BuildContext?
* What is Navigator?
* What is a Future?
* What is async/await?
* What is FutureBuilder?
* How do you call an API?
* What is State Management?
* What is Provider?
* What is dispose()?
* How would you structure a Flutter project?

---

# Portfolio Projects

## Beginner

* Counter App
* To-Do App
* Notes App
* Calculator

## Intermediate

* Weather App
* Expense Tracker
* Movie Browser
* Recipe App

## Advanced

* E-Commerce App
* Chat Application
* Social Media Clone


# Flutter Interview Preparation
* Book Management Platform (Biblo)
---
# Phase 1 Interview Prepation Notes

## Session 1: Flutter Fundamentals
### 1. What is Flutter?
Google's cross-platform UI framework for building Android, iOS, Web and desktop applications using a single Dart codebase.

### What is Dart?
Dart is an open-source, client optimised and object-oriented programming langauge developed by Google and used by Flutter.

**Example:**
```
void main()
{
  print("Hello");
}
```
### 3. What is a widget?
* Everything in Flutter is a widget.
* **Analogy:**
Like a LEGO brick. You combine small bricks (buttons, text, etc.) to build a complex architecture.
* **Technical:**
The basic building block of Flutter UI. Widgets are immutable configurations that describe what the UI should look like given its current configuration and state.
* **Example:**
```
const Text(
  "Hello world",
  style: TextStyle(fontSize: 20),
);
```

### 4. What is a widget tree?
Flutter UI is built as a hierarchy of widgets.
```
MaterialApp
|_> Scaffold
    |_> Center
        |_> Text
```

 ### 5. What is MaterialApp?
* **Analogy:** 
The foundation and frame of a house. It doesn't decide what furniture goes in each room, but it sets up the plumbing, electrical wiring, and blueprint standard (like Material Design style) so everything else works together.
* **Technical Explanation:** 
A core convenience widget that wraps your entire application. It configures the top-level Navigator, sets up global themes, handles localization, and enforces Google’s Material Design visual language across the app.
* **Example:**
```
void main() => runApp(
      const MaterialApp(
        home: Scaffold(
          body: Center(child: Text('Home Page')),
        ),
      ),
    );
```

### 6. What is scaffold?
* **Analogy:** 
A blank room with pre-installed fixtures. It gives you a ceiling grid (AppBar), a floor space (BottomNavigationBar), and walls (Drawer), leaving you to just bring in the furniture (Body).

* **Technical Explanation:** 
A structural widget that provides a consistent visual layout structure for a Material Design screen. It automatically manages the positioning and spacing of common top-level UI components like app bars, snackbars, and floating action buttons.

* **Code Example:**
```
const Scaffold(
  appBar: AppBar(title: Text('My App')),
  body: Center(child: Text('Content Goes Here')),
  floatingActionButton: FloatingActionButton(
    onPressed: null,
    child: Icon(Icons.add),
  ),
);
```

### 7. What is build() method?
* **Analogy:** 
A factory blueprint printer. Every time the factory manager says "the design changed" or "print a new one," the printer spits out a fresh, pixel-perfect layout based on the instructions it was given.

* **Technical Explanation:** 
A mandatory method in every framework widget that returns a widget tree. It is called by Flutter whenever the widget needs to be rendered for the first time or when its state/dependencies change, rebuilding the UI to reflect updated data.

* **Code Example:**
```
@override
Widget build(BuildContext context) {
  return const Center(
    child: Text('Rendered UI'),
  );
}
```

### 8. What is BuildContext?
* **Analogy:** 
It is like your GPS coordinates in a giant apartment building. If you want to order food to your door (find a Theme) or find the nearest exit (find the Navigator), you have to know exactly which floor and room number you are currently standing in.

* **Technical Explanation:** 
It is a reference token that tells Flutter exactly where a specific widget sits inside the massive widget tree. Without it, a widget cannot talk to its parent widgets or look up global app settings.

* **Code Example:**
```
@override
Widget build(BuildContext context) {
  // Uses context to look up the global text theme
  return Text(
    'Styled Text',
    style: Theme.of(context).textTheme.headlineMedium,
  );
}
```
```
@override
Widget build(BuildContext context) {
  // "Hey context, look up the tree and find the nearest Navigator 
  // so we can bounce to the next screen."
  return ElevatedButton(
    onPressed: () => Navigator.pop(context),
    child: const Text('Go Back'),
  );
}
```
### 9. What are global app settings?
* **Analogy:** 
The central AC system in an apartment building. Instead of every room buying its own standalone AC unit, the building has one giant central unit. Any room can simply plug into the wall vent (Theme.of(context)) to get cold air.

* **Technical Explanation:** 
Configuration data (like colors, fonts, or localized text) provided high up in the widget tree using InheritedWidget. Lower widgets use their BuildContext to look up this central data without having to pass it down manually through every single widget constructor.

* **Code Example:**
```
// Setting a global theme at the root
MaterialApp(
  theme: ThemeData(primaryColor: Colors.deepPurple),
  home: const MyScreen(),
);

// Accessing that global theme deep inside the app
Widget build(BuildContext context) {
  return Container(
    color: Theme.of(context).primaryColor, 
  );
}
```
### 10. What is the difference between Material Design and  Cupertino Design?

## Material Design vs. Cupertino Design

Here is the direct breakdown comparing Google's and Apple's design languages as implemented in Flutter:

| Feature                | Material Design (`material.dart`)                                         | Cupertino Design (`cupertino.dart`)                                          |
| ---------------------- | ------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| **Origin / Blueprint** | Google's Material Design system (Android focus)                           | Apple's Human Interface Guidelines (iOS focus)                               |
| **Visual Philosophy**  | Focuses on layers, depth, and shadows (mimics physical paper)             | Focuses on clarity, thin lines, and blurring (translucency)                  |
| **Top Bar**            | `AppBar` (Bold color fill, shadow underneath, title usually left-aligned) | `CupertinoNavigationBar` (Translucent background, no shadow, centered title) |
| **Primary Button**     | `ElevatedButton` (Shadows, ripples, distinct elevation levels)            | `CupertinoButton` (Flat, zero shadows, fades opacity when tapped)            |
| **Loading Spinner**    | `CircularProgressIndicator` (A continuous spinning line)                  | `CupertinoActivityIndicator` (A rotating wheel of ticks)                     |
| **Dialog Boxes**       | `AlertDialog` (Sharp corners, flat buttons at the bottom right)           | `CupertinoAlertDialog` (Highly rounded corners, segmented action bars)       |
| **Switches / Toggles** | `Switch` (Thumb slider sitting on top of an elongated track)              | `CupertinoSwitch` (Thumb slider integrated smoothly inside a pill shape)     |
| **Page Transition**    | Slides upward or fades in from the bottom                                 | Slides in smoothly from the right side of the screen                         |

> **Design Tip:** You don't have to choose just one! Many production apps use platform-aware widgets or conditional checks such as `Platform.isIOS` to display Cupertino widgets on iOS and Material widgets on Android automatically.
