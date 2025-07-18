Hello  = print("""

	YOUR MENU...


Select->
	1-> Phone book
	2-> Messages
	3-> Chat
	4-> Call register
	5-> Tones
	6-> Setting
	7-> Call divert
	8-> Games
	9-> Calculator
	10-> Reminders
	11-> Clock
	12-> Profiles
	13-> SIM services


                """)

menu = int(input('Enter 1 to display phone book: \n'))
match menu:
	case 1:
		print("""

		1-> Search
		2-> Service Nos
		3-> Add name
		4-> Erase
		5-> Edit
		6-> Assign tone
		7-> Send b'card
		8-> Option
		9-> Speed dails
		10-> Voice tags
		""")
		menu2 = int(input('Enter a number from above:\n'))
		match menu2:
			case 1:
				print("Search")
			case 2:
				print("Service Nos")
			case 3:
				print("Add Name")
			case 4: 
				print("Erase")
			case 5:
				print("Edit")
			case 6:
				print("Assign tone")
			case 7:
				print("Send b'card")
			case 9:
				print("Speed Dail")
			case 10:
				print("Voice tags")
			case 8:
				print("""

			              OPTION

			              Select-->

			              1-> Type of View
			              2-> Memory Statut

			              """)
				menu4 = int(input('Enter a number from above:\n'))
				match menu4:
						case 1:
							print("Type of View")
						case 2:
							print("Memory Statut")
						case _:
							print('default')
			
                       

  
		

	case 2:
 	
		print("""
		        1-> Write messages
			2-> Inbox
			3-> Outbox
			4-> Picture messages
			5-> Templates
			6-> Smiley
			7-> Message setting
			8-> Info service
			9-> Voice mailbox number
			10-> Service command editor
                        """)

		menu4 = int(input('Enter a number from above:\n'))
		match menu4:
			case 1:
				print("Write messages")
			case 2:
				print("Inbox")
			case 3:
				print("Outbox")
			case 4: 
				print("Picture messages")
			case 5:
				print("Templates")
			case 6:
				print("Smiley")
			case 8:
				print("Info service")
			case 9:
				print("Voice mailbox number")
			case 10:
				print("Service command editor")
			case 7:
				print("""

			              Message setting

			              Select-->

			              1-> Set 1
			              2-> common

			              """)
		menu5 = int(input('Enter a number from above:\n'))
		match menu5:
						case 1:
							print("""
								1-> Message centre number
								2-> Message sent as
								3-> Message validity""")
							menu6 = int(input('Enter a number from above:\n'))
							match menu6:
								case 1:
									print("Message centre number")
								case 2:
									print("Message sent as")
								case 3: 
									print("Message validity")
	

						case 2:
							print("""
								1-> Delivery report
								2-> Reply via same centre
							       	3-> Chaeacter support""")
							menu7 = int(input('Enter a number from above:\n'))
							match menu7:
								case 1:
									print("Delivery report")
								case 2:
									print("Reply via same centre")
								case 3: 
									print("")
						

						case _:
							print('default')

	case 3:
		print("""
			
			 Chat""")			
				

	case 4:
		print("""

			1-> Missed calls
			2-> Received calls	
			3-> Dialled numbers
			4-> Erase recent calls
			5-> Show call duration
			6-> Show call costs
			7-> Calls cost settings
			8-> Prepaid credit""")

		menu8 = int(input('Enter a number from above:\n'))
		match menu8:
			case 1:
				print('Missed calls')
			case 2:
				print('Received calls')
			case 3:
				print('Dailled number')
			case 4:
				print('Erase recent calls')
			case 5:
				print("""
					1-> Last call duration
					2-> All calls duration
					3-> Received calls duration
					4-> Dialled calls duration
					5-> Clear timers""")
				menu9 = int(input('Enter a number from above:\n'))
				match menu9:
					case 1:
						print('Last call duration')
					case 2:
						print('All calls duration')
					case 3:
						print('Received calls duration')
					case 4:
						print('Dialled calls duration')
					case 5: 
						print('Clear timers')
	
			case 6:
				print("""
					1-> Last call cost
					2-> All call's cost
					3-> Clear counters""")
				menu10 = int(input('Enter a number from above:\n'))
				match menu10:
					case 1:
						print('Last call cost')
					case 2:
						print("All call's cost")
					case 3:
						print('Clear counters')


			case 7:
				print("""
					1-> Call csot limit
					2-> Show costs in""")
				menu11 = int(input('Enter a number from above:\n'))
				match menu11:
					case 1:
						print('Call cost limit')
					case 2:
						priint('Show costs in')
			case 8:
				print("Prepaid credit") 

	case 5:
		print("""
			TONES
			1-> Ringing tone
			2-> Ringing volume
			3-> Incoming alart
			4-> Composer
			5-> Message alert tone
			6-> Keypad tones
			7-> Warning and game tones
			8-> Vibrating alert
			9-> Screen saver""")
				
		menu12 = int(input('Enter a number from above:\n'))
		match menu12:
					case 1:
						print('Ringing tone')
					case 2:
						print('Ringing volume')
					case 3:
						print('Incoming alart')
					case 4:
						print('Composer')
					case 5:
						print('Message alert tone')
					case 6:
						print('Keypad tones')
					case 7:
						print('Warning and game tones')
					case 8:
						print('Vibrating alert')
					case 9: 
						print('Screen saver')

	case 6:
		print("""

			SETTINGS
			
			1-> Call settings
			2-> Phone setting
			3-> Security settings
			4-> Restore factory settings """)

		menu13 = int(input('Enter a number from above:\n'))
		match menu13:
			case 1:
				print("""
					CALL SETTINGS
					1-> Automatic redial
					2-> Speed dialing
					3-> Call waiting option
					4-> Own number sending
					5-> Phone line in use
					6-> Automatic answer """)

				menu14 = int(input('Enter a number from above:\n'))
				match menu14:
					
					case 1: 
						print('Automatic redial')
					case 2:
						print('Speed dialing')
					case 3:
						print('Call waiting option')
					case 4:
						print('Own number sending')
					case 5:
						print('Phone line in use')
					case 6:
						print('Automatic answer')
			case 2:
				print("""
					PHONE SETTING

					
							1-> Language
							2-> Cell info display
							3-> Welcome note
							4-> Network selection
							5-> Lights
							6-> Confirm SIM service action""")

				menu15 = int(input('Enter a number form above:'))
				match menu15:
							case 1:
								print('Language')
							case 2:
								print('Cell info')
							case 3: 
								print('Welcome note')
							case 4: 
								print('Network selection')
							case 5:
								print('Lights')
							case 6:
								print('Confirm SIM service action')
			case 3:
				print("""

					SECURITY SETTINGS
					
					1-> PIN code request
					2-> Call barring service
					3-> Fixed dialling
					4-> Closed user group
					5-> Phone security
					6-> Change access codes""")

				menu16 = int(input('Enter a number form above:'))
				match menu16:

							case 1:
								print('PIN code request')
							case 2:
								print('Call barring service')
							case 3: 
								print('Fixed dialling')
							case 4: 
								print('Closed user group')
							case 5:
								print('Phone security')
							case 6:
								print('Change access codes')

			case 4:
				print("Restore factory settings")

	case 7:
		print("Call divert")
	case 8:
		print("Games")
	case 9:
		print("Calculator")
	case 10:
		print("Reminder")
	case 11:
		print("""

			CLOCK

			1-> Alarm clock
			2-> Clock setting
			3-> Date setting
			4-> Stopwatch
			5-> Countdown timer
			6-> Auto update of date and time""")

		menu16 = int(input('Enter a number from above:'))
		match menu16:
				case 1:
					print('Alarm clock')
				case 2:
					print('Clock setting')
				case 3:
					print('Date setting')
				case 4:
					print('Stopwatch')
				case 5:
					print('Countdown timer')
				case 6:
					print('Auto update of date and time')
	case 12:
		print('Profiles')
	case 13:
		print('SIM services')
				

						




		
