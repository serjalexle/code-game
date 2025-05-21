# 📜 BX Header Error Documentation

This document describes possible errors that may occur when processing the **BX** header, along with their codes and messages.

---

## 🔹 1. Missing BX Header

### **Error Code**: `BX_HEADER_MISSING`

**HTTP Status**: `400 BAD REQUEST`\
**Description**: The request does not contain the required `BX` header, which is necessary for this route.

### **Response Format**

```json
{
    "error": "BX header is missing",
    "message": "BX header is required to access this route",
    "custom_code": "BX_HEADER_MISSING"
}
```

### **Possible Causes**

- The client did not include the `BX` header in the request.
- The request was sent without the required data.

### **How to Fix**

Before sending the request, make sure to include the `BX` header, for example:

```
BX: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
```

---

## 🔹 2. Invalid BX Header

### **Error Code**: `INVALID_BX_HEADER`

**HTTP Status**: `400 BAD REQUEST`\
**Description**: The provided `BX` header could not be decrypted or contains invalid data.

### **Response Format**

```json
{
    "error": "Invalid BX header",
    "message": "Invalid token format",
    "custom_code": "INVALID_BX_HEADER"
}
```

### **Possible Causes**

- The `BX` header is in an incorrect format.
- The provided data is corrupted or incorrectly encrypted.
- An outdated or invalid encryption key is being used.

### **How to Fix**

1. Ensure the `BX` header is being sent correctly.
2. Use a valid `BX` value that has been properly encrypted.
3. If using a token, check its validity.

---

## 📌 Additional Information

- All `BX`-related errors return a **400 BAD REQUEST** status.
- The `custom_code` field contains a unique error identifier, which can be used for handling on the client side.

📢 **If you encounter issues, verify the correctness of the **``** header and its format!**

