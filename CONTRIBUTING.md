# 🤝 Contributing to MTProto Proxy Manager Bot

Thank you for your interest in contributing! We welcome bug reports, feature requests, and pull requests.

---

## 📖 Getting Started

### Prerequisites

- Python 3.9+
- Git
- Basic knowledge of Python and Telegram Bot API

### Setup Development Environment

1. **Fork the repository**

   ```bash
   git clone https://github.com/YOUR-USERNAME/mtproto-proxy-bot.git
   cd mtproto-proxy-bot
   ```

2. **Create a virtual environment**

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Create a `.env` file for testing**
   ```bash
   cp .env.example .env
   # Edit .env with your test bot token
   ```

---

## 🐛 Reporting Bugs

Found a bug? Please open an issue with:

- **Clear title** describing the problem
- **Steps to reproduce** the issue
- **Expected vs actual behavior**
- **Environment**: OS, Python version, relevant packages
- **Logs** from `logs/bot.log` or terminal output

Example:

```
Title: Bot crashes when creating proxy with invalid port
Steps:
1. Run /create
2. Enter domain: example.com
3. Enter port: 99999
4. Bot crashes with PermissionError

Expected: User gets error message "Invalid port"
Actual: Bot stops responding
```

---

## ✨ Feature Requests

Want a new feature? Open an issue with:

- **Description** of what you want to add
- **Use case** - why is this useful?
- **Proposed implementation** (optional)

---

## 🔧 Making Changes

### Code Style

- Follow **PEP 8** guidelines
- Use **type hints** for functions
- Add **docstrings** for classes and functions
- Keep lines under 100 characters

### File Organization

```
bot/
├── handlers/    # Add new command handlers here
├── services/    # Add business logic here
├── keyboards/   # Add UI elements here
└── utils/       # Add helper functions here
```

### Making a Pull Request

1. **Create a branch**

   ```bash
   git checkout -b feature/your-feature-name
   # or for bugs:
   git checkout -b fix/bug-description
   ```

2. **Make your changes**
   - Write clean, documented code
   - Test thoroughly
   - Keep commits atomic and well-message

3. **Commit with clear messages**

   ```bash
   git commit -m "Add feature: proxy restart with timeout"
   git commit -m "Fix: handle invalid domain names"
   ```

4. **Push and open PR**

   ```bash
   git push origin feature/your-feature-name
   ```

5. **PR Requirements**
   - Clear title and description
   - Link related issues (e.g., "Fixes #123")
   - Test on Ubuntu 20.04+ / Debian
   - No breaking changes without discussion

---

## 📋 Areas to Contribute

### High Priority

- [ ] Add web UI dashboard (not just bot commands)
- [ ] Support for multiple Telegram bot accounts
- [ ] Better region detection for port recommendations
- [ ] Database migration from JSON to SQLite

### Medium Priority

- [ ] Docker support
- [ ] Ansible playbook for auto-deployment
- [ ] More MTG obfuscation options
- [ ] Admin panel for password-protected access

### Good for Beginners

- [ ] Add more error handling
- [ ] Improve logging messages
- [ ] Add more emoji in bot responses
- [ ] Improve documentation and comments
- [ ] Add unit tests

---

## 🧪 Testing

Before submitting a PR, test your changes:

```bash
# Test the bot locally
python3 main.py

# Test specific handler
python3 -m pytest bot/handlers/test_proxy.py  # Future: add tests

# Check code style
# pip install pylint
pylint bot/
```

---

## 📚 Documentation

- Update [README.md](README.md) if you change features
- Add comments for non-obvious code
- Update [CONTRIBUTING.md](CONTRIBUTING.md) if process changes

---

## 💬 Questions?

- Open a GitHub Discussion
- Check existing issues for answers
- Contact maintainers

---

## 📝 License

By contributing, you agree your code will be licensed under the [MIT License](LICENSE).

---

## ⚡ Quick Checklist for PR

- [ ] Code follows PEP 8
- [ ] Commits are clear and atomic
- [ ] Related issue is linked
- [ ] No breaking changes
- [ ] Tested on Linux/Unix
- [ ] `.env` file not committed
- [ ] Updated relevant documentation

Thank you for contributing! 🎉
