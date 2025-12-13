app_name = "otp_generation"
app_title = "OTP Generation"
app_publisher = "omar"
app_description = "Frappe App for OTP Generation"
app_email = "omar.tarek29@hotmail.com"
app_license = "mit"

# Apps
# ------------------

# required_apps = []

# Each item in the list will be shown as an app in the apps page
# add_to_apps_screen = [
# 	{
# 		"name": "otp_generation",
# 		"logo": "/assets/otp_generation/logo.png",
# 		"title": "OTP Generation",
# 		"route": "/otp_generation",
# 		"has_permission": "otp_generation.api.permission.has_app_permission"
# 	}
# ]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/otp_generation/css/otp_generation.css"
# app_include_js = "/assets/otp_generation/js/otp_generation.js"

# include js, css files in header of web template
# web_include_css = "/assets/otp_generation/css/otp_generation.css"
# web_include_js = "/assets/otp_generation/js/otp_generation.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "otp_generation/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "otp_generation/public/icons.svg"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "otp_generation.utils.jinja_methods",
# 	"filters": "otp_generation.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "otp_generation.install.before_install"
# after_install = "otp_generation.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "otp_generation.uninstall.before_uninstall"
# after_uninstall = "otp_generation.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "otp_generation.utils.before_app_install"
# after_app_install = "otp_generation.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "otp_generation.utils.before_app_uninstall"
# after_app_uninstall = "otp_generation.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "otp_generation.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
# 	}
# }

# Scheduled Tasks
# ---------------

scheduler_events = {"cron": {"*/10 * * * *": ["otp_generation.tasks.expire_otps"]}}

# OTP Sender Hooks
# ---------------
# Register sender functions for OTP delivery
# Other apps can register their email/SMS sender functions here
# Example in resk_app/hooks.py:
# otp_email_sender = ["resk_app.utils.send_otp_email"]
# otp_sms_sender = ["resk_app.utils.send_otp_sms"]
#
# Sender functions should accept:
# - otp_code: The OTP code to send
# - email: Email address (for email senders)
# - phone: Phone number (for SMS senders)
# - purpose: Purpose of OTP (optional)
# - **kwargs: Additional arguments
#
# Example sender function:
# def send_otp_email(otp_code, email, purpose=None, **kwargs):
#     frappe.sendmail(
#         recipients=[email],
#         subject=f"Your OTP for {purpose}",
#         message=f"Your OTP is: {otp_code}"
#     )
#     return {"status": "sent"}

# Testing
# -------

# before_tests = "otp_generation.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "otp_generation.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "otp_generation.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["otp_generation.utils.before_request"]
# after_request = ["otp_generation.utils.after_request"]

# Job Events
# ----------
# before_job = ["otp_generation.utils.before_job"]
# after_job = ["otp_generation.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"otp_generation.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }
