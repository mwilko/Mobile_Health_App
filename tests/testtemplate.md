### What module you're testing e.g. main menu, lifestyle questions, congnition
| \#  | OBJECTIVE | INPUT | EXPECTED RESULTS | ACTUAL RESULTS | ASSIGNED TO | DISCREPANCY | NOTES |
| --- | --------- | ----- | ---------------- | -------------- | ----------- | ----------- | ----- |
| FORMAT   | Information about what the feature you're testing (i.e. creating a username).      | What input you used.       | What you expected to happen.                  | What actually happened.                | Who is assigned to fix it if it doesn't work.             |
| 1 | Checking that the choice page is displayed when running the app. | Ran VSCode IDE. | Choice Page ran with expected buttons. | Choice Page ran with expected buttons.| N/A | FALSE |
| 2 | Testing functionality to Choice Menu buttons. | Pressing page buttons. | On Press, buttons direct the user to respective page. | Lifestyle button is directed to the Personal Details page. | Max Wilkinson | TRUE | Issue was caused by typo. Program was returning the 'show_personal_details' instead of the 'show_lifestyle'. |
| 3| Testing functionality to Choice Menu buttons | Pressing page buttons. | On Press, buttons direct the user to respective page. | On Press, buttons direct the user to respective page. | N/A | FALSE |
| 4 | Testing the sign in page runs and has proper format. | Run VSCode IDE. | Sign in page runs with no errors and has exepcted format. | Sign in page runs with no errors but the sign in label continues out of frame. | Max Wilkinson | TRUE | Fix: Font size of the label was decreased so the whole label would fit in the android screen. 
| 5 | Testing sign in page 'username' text input box. | Pressing and text input of "123123123". | Username box can be pressed and test data can be inputted | Username box can be pressed and test data can be inputted | N/A | FALSE |
| 6 | Testing sign in page 'password' text input box | Pressing and text input of "123123123". | Password box can be pressed and test data can be inputted | Password box can be pressed and test data can be inputted | N/A | FALSE |
| 7 | Testing username constraints. | "hello" | Password needs to be six letters long. | Password needs to be six letters long. | N/A | FALSE | 
| 8 | Testing login credentials. | Username: "123123123" Password: "123123123" | User logs in correctly. | User logs in correctly. | N/A | FALSE |
| 9 | Testing Personal Details correct age text input. | "21" | Program continues | Program continues | N/A | FALSE
| 10 | Testing Personal Details low range text input. | "0" | "Invalid age input. Please enter a valid age." | "Invalid age input. Please enter a valid age." | N/A | FALSE |
| 11 | Testing Personal Details high range text input. | "120" | "Invalid age input. Please enter a valid age." | "Invalid age input. Please enter a valid age." | N/A | FALSE |
| 12 | Testing Personal Details type text input. | "hello" | "Invalid age input. Please enter a valid age." | "Invalid age input. Please enter a valid age." | N/A | FALSE
| 13 | Testing Personal Details special character text input | "!!" | "Invalid age input. Please enter a valid age." | "Invalid age input. Please enter a valid age." | N/A | FALSE |
| 14 | Testing Personal Details correct height text input. | "70" | Program continues | Program continues | N/A | FALSE |
| 15 | Testing Personal Details type height text input. | "hello" | "Invalid height input. Please enter a valid height." | "Invalid height input. Please enter a valid height." | N/A | FALSE |
| 146 | Testing Personal Details high range height text input. | "1000" | "Invalid height input. Please enter a valid height." | "Invalid height input. Please enter a valid height." | N/A | FALSE |
| 16 | Testing Personal Details low range height text input. | "0" | "Invalid height input. Please enter a valid height." | "Invalid height input. Please enter a valid height." | N/A | FALSE |
| 17 | Testing Personal Details special character height text input. | "@@" | "Invalid height input. Please enter a valid height." | "Invalid height input. Please enter a valid height." | N/A | FALSE |
| 18 | Testing Personal Details correct weight text input. | "165" | Program continues | Program continues | N/A | FALSE |
| 19 | Testing Personal Details high range weight text input. | "1000" | "Invalid weight input. Please enter a valid weight." | "Invalid weight input. Please enter a valid weight." | N/A | FALSE |
| 20 | Testing Personal Details low range weight text input. | "0" | "Invalid weight input. Please enter a valid weight." | "Invalid weight input. Please enter a valid weight." | N/A | FALSE |
| 21 | Testing Personal Details special character weight text input. | "!!" | "Invalid weight input. Please enter a valid weight." | "Invalid weight input. Please enter a valid weight." | N/A | FALSE |
| 22 | Testing Personal Details none weight text input. | "" | "Invalid weight input. Please enter a valid weight." | "Invalid weight input. Please enter a valid weight." | N/A | FALSE |
| 23 | Testing Personal Details none age text input. | "" | "Invalid age input. Please enter a valid age." | "Invalid age input. Please enter a valid age." | N/A | FALSE |
| 23 | Testing Personal Details none height text input. | "" | "Invalid height input. Please enter a valid height." | "Invalid height input. Please enter a valid height." | N/A | FALSE |
| 17 | Testing Personal Details BMI label updating. | 
