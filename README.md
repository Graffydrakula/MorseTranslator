# Morse Code Encoder & Decoder (GUI + Logic)

A simple Morse Code translator built with Python and Tkinter.  
It can **encode** normal text to Morse code and **decode** it back.  
All Morse symbols follow the **International Morse Code** standard.

---

## 🔍 Features

- ✅ Encode from text to Morse code  
- ✅ Decode Morse code back to text  
- ✅ Copy & paste support for both fields  
- ✅ Input normalization (`.strip()`, `.upper()`, etc.)  
- ✅ Detects unknown characters and shows clean error messages  
- ✅ Full support for symbols like `?`, `!`, `=)` and spaces  
- ✅ Unit tests included (with `unittest`)  

---

## 🧪 Tests

You can run tests with:

```bash
python3 tests.py
```

The tests check encoding, decoding, and how the app handles unknown or mixed symbols (like using Cyrillic inside English text).

---

## 🖼 GUI Notes

The GUI is written using **Tkinter**, and follows a **composition pattern** — the main `Tk()` instance is passed to a separate `MorseApp` class.

This design was chosen **intentionally** over inheriting from `tk.Tk`, because:

- It improves modularity and scalability  
- It's easier to maintain and test  
- Keeps logic and GUI separation cleaner  

Still, inheritance (like `class MorseApp(tk.Tk)`) would also work fine for small apps — and this was considered during development.

---

## 🧠 Project Purpose

This project was built as a **self-contained training exercise** to practice:
- Object-Oriented Programming (OOP)
- Separation of concerns (logic vs GUI)
- Clean error handling
- Simple testing and GUI design

---

## 💡 Usage

- Type or paste your text in the input field  
- Click **"To Morse"** or **"To English"** than **"Translate"**
- Copy the result using the **"Copy"** button  
- Paste Morse code back using **"Paste"**  

Unknown characters or Morse symbols will be marked clearly with messages like:  
> `"Error, 'Ж' is unknown Symbol."`  
or  
> `'Goo<"----" Is Unknown Symbol>d Day'`

---

## 🔧 Requirements

- `tkinter`
- `pyperclip`
- `unittest`

---

## 📁 Files Overview

```
morse_code/
├── decoder.py      # Main encoding/decoding logic
├── main.py         # GUI logic using Tkinter
├── tests.py        # Unit tests
```

---

## ✅ Status

🟢 Project is working and stable.  
More features (e.g., sound playback, themes) can be added later.

---

## 🙋 About the Author

This project was created by [Ivan Davydenko](https://www.linkedin.com/in/ivan-s-davydenko/)

- 📧 Email: ivan.s.davydenko@gmail.com  
- 🐙 GitHub: [github.com/Graffydrakula](https://github.com/Graffydrakula)  
- 💼 LinkedIn: [linkedin.com/in/ivan-s-davydenko](https://www.linkedin.com/in/ivan-s-davydenko/)

---

## 📬 Feedback

Feel free to test it, break it, and improve it.  
It’s a learning project, but already clean and reliable.