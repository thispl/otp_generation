# OTP Generation

A generic, reusable Frappe app for One-Time Password (OTP) generation and verification.  
Supports Email and SMS delivery methods with flexible configuration.

![otp](https://github.com/user-attachments/assets/346e6a08-07c2-4d55-a482-3cf8b694e61e)

---

<details>
<summary><strong>✨ Features</strong></summary>

- ✅ **Generic & Reusable**: Works with any Frappe app
- ✅ **Multiple Delivery Methods**: Email, SMS, or Both
- ✅ **Flexible OTP Types**: Numeric or Mixed (letters + digits)
- ✅ **Configurable Length**: 4–10 characters
- ✅ **Automatic Expiration**: Scheduled job expires OTPs automatically
- ✅ **Email Integration**: Uses Frappe's standard `sendmail` with Email Templates
- ✅ **SMS Integration**: Custom sender functions via configuration
- ✅ **SMS Integration Check**: Server-side validation ensures SMS integration method exists before saving
- ✅ **RESTful API**: Easy-to-use API endpoints
- ✅ **Security**: Uses Python's `secrets` module for cryptographically secure random generation

</details>

---

<details>
<summary><strong>📦 Installation</strong></summary>

<br>

### Self-Hosted (Bench)

```bash
cd $PATH_TO_YOUR_BENCH
bench get-app https://github.com/omarrtarek29/otp_generation --branch develop
bench --site [your-site] install-app otp_generation
```

---

### Frappe Cloud (Marketplace)

This app can be installed directly from the Frappe Cloud Marketplace.

Steps:
1. Visit: https://cloud.frappe.io/marketplace/apps/otp_generation
2. Click **Install**
3. Select your site
4. Confirm the installation

No bench commands are required for Frappe Cloud installations.

</details>

---

<details>
<summary><strong>⚙️ Configuration</strong></summary>

### 1. OTP Settings

Go to **OTP Settings** and configure:

#### Basic Settings
- **Expiry Time (Minutes)**: Default 10 minutes
- **OTP Length**: 4–10 characters (default 6)
- **OTP Code Type**:
  - `Numeric`
  - `Mixed`

#### Delivery Configuration

**OTP Delivery Type**
- Email
- SMS
- Both

**Email Delivery**
- Email Account
- Email Template (must include `{{ otp_code }}`)

**SMS Delivery**
- SMS Sender Function (e.g. `custom_app.utils.send_sms`)

---

### 2. Email Template Setup

Example:

```
Subject: Your OTP Code is {{ otp_code }}

Message:
Your OTP code is: {{ otp_code }}
This code will expire in {{ expiry_time_minutes }} minutes.
```

---

### 3. SMS Sender Function

```python
def send_sms(otp_code, phone, **kwargs):
    purpose = kwargs.get("purpose", "verification")

    import requests
    response = requests.post(
        "https://your-sms-gateway.com/send",
        data={
            "phone": phone,
            "message": f"Your OTP code for {purpose} is: {otp_code}"
        }
    )

    return {"success": True, "message_id": response.json().get("id")}
```

Set **SMS Sender Function** to:
```
custom_app.utils.send_sms
```

</details>

---

<details>
<summary><strong>🚀 Usage</strong></summary>

### REST API

#### Generate OTP

```bash
POST /api/method/otp_generation.api.send_otp
```

```json
{
  "email": "user@example.com",
  "purpose": "sign_up"
}
```

---

#### Validate OTP

```bash
POST /api/method/otp_generation.api.validate_otp
```

```json
{
  "otp_code": "123456",
  "email": "user@example.com",
  "purpose": "sign_up"
}
```

---

### Client-side (JavaScript / React)

```javascript
frappe.call({
  method: "otp_generation.api.send_otp",
  args: {
    email: "user@example.com",
    purpose: "sign_up"
  }
});
```

</details>

---

<details>
<summary><strong>⏱ Scheduled Tasks</strong></summary>

```python
scheduler_events = {
    "cron": {
        "*/10 * * * *": [
            "otp_generation.tasks.expire_otps"
        ]
    }
}
```

</details>

---

<details>
<summary><strong>📄 DocTypes</strong></summary>

### OTP
- otp_code
- status
- expiry
- purpose
- delivery_method
- email
- phone
- user (optional)

### OTP Settings
System-wide configuration.

</details>

---

<details>
<summary><strong>🔐 Security Considerations</strong></summary>

- Cryptographically secure OTP generation
- One-time use OTPs
- Automatic expiry
- Scheduled cleanup
- Guest access supported for signup flows

</details>

---

<details>
<summary><strong>🤝 Contributing</strong></summary>

```bash
cd apps/otp_generation
pre-commit install
```

Tools used:
- ruff
- eslint
- prettier
- pyupgrade

</details>

---

## License

MIT
