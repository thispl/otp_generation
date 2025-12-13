# Copyright (c) 2025, OTP Generation and contributors
# For license information, please see license.txt

import frappe
from frappe.utils import now_datetime


def expire_otps():
	"""
	Scheduled function to expire OTPs that have passed their expiry time
	This should be run periodically (e.g., every 5-10 minutes)
	"""
	try:
		expired_otps = frappe.get_all(
			"OTP", filters={"status": "Valid", "expiry": ["<", now_datetime()]}, fields=["name"]
		)

		count = 0
		for otp in expired_otps:
			try:
				otp_doc = frappe.get_doc("OTP", otp.name)
				otp_doc.status = "Expired"
				otp_doc.save(ignore_permissions=True)
				count += 1
			except Exception as e:
				frappe.log_error(f"Error expiring OTP {otp.name}: {e}", "OTP Expiration")

		return {"expired_count": count}
	except Exception as e:
		frappe.log_error(f"Error in expire_otps scheduled function: {e}", "OTP Expiration")
		return {"expired_count": 0, "error": e}
