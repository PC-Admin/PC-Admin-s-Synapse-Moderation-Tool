
import user_commands
import room_commands
import server_commands
import rdlist_commands
import hardcoded_variables

# check if homeserver url is hard coded, if not set it

if hardcoded_variables.homeserver_url == "matrix.example.org":
	homeserver_url = input("What is the URL of your server? Eg: matrix.example.org ")

# check if base url is hard coded, if not set it

if hardcoded_variables.base_url == "example.org":
	base_url = input("What is the URL of your server? Eg: example.org ")

# check if access token is hard coded, if not set it

length_access_token = len(hardcoded_variables.access_token)

if length_access_token == 0:
	access_token = input("Please enter access token for server admin account: ")

# loop menu for various moderation actions

pass_token = False
while pass_token == False:
	print("\n##########################")
	print("# MATRIX MODERATION TOOL #")
	print("##########################")
	print("\nA tool for making common Synapse moderation tasks easier. Created by @PC-Admin.")
	print("\n----------------------------------------------")
	print("\n#### User Account Commands ####\t\t\t#### Room Commands ####")
	print("1) Deactivate a user account.\t\t\t14) List details of a room.")
	print("2) Deactivate multiple user accounts.\t\t15) Export the state events of a target room.")
	print("3) Create a user account.\t\t\t16) List rooms in public directory.")
	print("4) Create multiple user accounts.\t\t17) Remove a room from the public directory.")
	print("5) Reset a users password.\t\t\t18) Remove multiple rooms from the public directory.")
	print("6) Whois user account.\t\t\t\t19) Redact a room event.")
	print("7) Whois multiple user accounts.\t\t20) List/Download all media in a room.")
	print("8) Query user account.\t\t\t\t21) Download media from multiple rooms.")
	print("9) Query multiple user accounts.\t\t22) Quarantine all media in a room.")
	print("10) List room memberships of user.\t\t23) Shutdown a room.")
	print("11) Promote a user to server admin.\t\t24) Shutdown multiple rooms.")
	print("12) List all user accounts.\t\t\t25) Delete a room.")
	print("13) Quarantine all media a users uploaded.\t26) Delete multiple rooms.")
	print("\t\t\t\t\t\t27) Purge the event history of a room to a specific timestamp.")
	print("\t\t\t\t\t\t28) Purge the event history of multiple rooms to a specific timestamp.")
	print("\n#### Server Commands ####")
	print("29) Delete and block a specific media.")
	print("30) Purge remote media repository up to a certain date.")
	print("31) Prepare database for copying events of multiple rooms.")
	print("\n#### rdlist ####")
	print("32) Block all rooms with specific rdlist tags.")
	print("34) Block all rooms with recommended rdlist tags.")
	print("\n#### ipinfo.io ####")
	print("40) Analyse a users country of origin.")
	print("41) Analyse multiple users country of origin.")
	print("\nPlease enter a number from the above menu, or enter 'q' or 'e' to exit.\n")
	menu_input = input()
	if menu_input == "1":
		user_commands.deactivate_account('')
	elif menu_input == "2":
		user_commands.deactivate_multiple_accounts()
	elif menu_input == "3":
		user_commands.create_account('','')
	elif menu_input == "4":
		user_commands.create_multiple_accounts()
	elif menu_input == "5":
		user_commands.reset_password('','')
	elif menu_input == "6":
		user_commands.whois_account('')
	elif menu_input == "7":
		user_commands.whois_multiple_accounts()
	elif menu_input == "8":
		user_commands.query_account()
	elif menu_input == "9":
		user_commands.query_multiple_accounts()
	elif menu_input == "10":
		user_commands.list_joined_rooms('')
	elif menu_input == "11":
		user_commands.set_user_server_admin('')
	elif menu_input == "12":
		user_commands.list_accounts()
	elif menu_input == "13":
		user_commands.quarantine_users_media()
	elif menu_input == "14":
		room_commands.list_room_details('')
	elif menu_input == "15":
		room_commands.export_room_state('')
	elif menu_input == "16":
		room_commands.list_directory_rooms()
	elif menu_input == "17":
		room_commands.remove_room_from_directory('')
	elif menu_input == "18":
		room_commands.remove_multiple_rooms_from_directory()
	elif menu_input == "19":
		room_commands.redact_room_event()
	elif menu_input == "20":
		room_commands.list_and_download_media_in_room('','','','./')
	elif menu_input == "21":
		room_commands.download_media_from_multiple_rooms()
	elif menu_input == "22":
		room_commands.quarantine_media_in_room()
	elif menu_input == "23":
		room_commands.shutdown_room('','','','','','')
	elif menu_input == "24":
		room_commands.shutdown_multiple_rooms()
	elif menu_input == "25":
		room_commands.delete_room('')
	elif menu_input == "26":
		room_commands.delete_multiple_rooms()
	elif menu_input == "27":
		room_commands.purge_room_to_timestamp('','')
	elif menu_input == "28":
		room_commands.purge_multiple_rooms_to_timestamp()
	elif menu_input == "29":
		server_commands.delete_block_media()
	elif menu_input == "30":
		server_commands.purge_remote_media_repo()
	elif menu_input == "31":
		server_commands.prepare_database_copy_of_multiple_rooms()
	elif menu_input == "32":
		rdlist_commands.block_all_rooms_with_rdlist_tags(False,'','','','','')
	elif menu_input == "34":
		rdlist_commands.block_recommended_rdlist_tags()
	elif menu_input == "40":
		user_commands.analyse_account_ip('')
	elif menu_input == "41":
		user_commands.analyse_multiple_account_ips()
	elif menu_input == "q" or menu_input == "Q" or menu_input == "e" or menu_input == "E":
		print("\nExiting...\n")
		pass_token = True
	else:
		print("\nIncorrect input detected, please select a number from 1 to 41!\n")

