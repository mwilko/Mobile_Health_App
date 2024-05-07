### What module you're testing e.g. main menu, lifestyle questions, cognition
| \#  | OBJECTIVE | INPUT | EXPECTED RESULTS | ACTUAL RESULTS | ASSIGNED TO | DISCREPANCY | NOTES |
| --- | --------- | ----- | ---------------- | -------------- | ----------- | ----------- | ----- |
| 1 | Checking that the choice page is displayed when running the app. | Ran VSCode IDE. | Choice Page ran with expected buttons. | Choice Page ran with expected buttons.| N/A | FALSE |
| 2.0 | Testing functionality to Choice Menu buttons. | Pressing page buttons. | On Press, buttons direct the user to respective page. | Lifestyle button is directed to the Personal Details page. | Max Wilkinson | TRUE | Issue was caused by typo. Program was returning the 'show_personal_details' instead of the 'show_lifestyle'. |
| 2.1 | Testing functionality to Choice Menu buttons | Pressing page buttons. | On Press, buttons direct the user to respective page. | On Press, buttons direct the user to respective page. | N/A | FALSE |
| 3.0 | Testing the sign in page runs and has proper format. | Run VSCode IDE. | Sign in page runs with no errors and has exepcted format. | Sign in page runs with no errors but the sign in label continues out of frame. | Max Wilkinson | TRUE | Fix: Font size of the label was decreased so the whole label would fit in the android screen. 
| 3.1 | Testing sign in page 'username' text input box. | Pressing and text input of "123123123". | Username box can be pressed and test data can be inputted | Username box can be pressed and test data can be inputted | N/A | FALSE |
| 4 | Testing sign in page 'password' text input box | Pressing and text input of "123123123". | Password box can be pressed and test data can be inputted | Password box can be pressed and test data can be inputted | N/A | FALSE |
| 5 | Testing username constraints. | "hello" | Password needs to be six letters long. | Password needs to be six letters long. | N/A | FALSE | 
| 6 | Testing login credentials. | Username: "123123123" Password: "123123123" | User logs in correctly. | User logs in correctly. | N/A | FALSE |
| 7 | Testing Personal Details correct age text input. | "21" | Program continues | Program continues | N/A | FALSE
| 8 | Testing Personal Details low range text input. | "0" | "Invalid age input. Please enter a valid age." | "Invalid age input. Please enter a valid age." | N/A | FALSE |
| 9 | Testing Personal Details high range text input. | "120" | "Invalid age input. Please enter a valid age." | "Invalid age input. Please enter a valid age." | N/A | FALSE |
| 10 | Testing Personal Details type text input. | "hello" | "Invalid age input. Please enter a valid age." | "Invalid age input. Please enter a valid age." | N/A | FALSE
| 11 | Testing Personal Details special character text input | "!!" | "Invalid age input. Please enter a valid age." | "Invalid age input. Please enter a valid age." | N/A | FALSE |
| 12 | Testing Personal Details correct height text input. | "70" | Program continues | Program continues | N/A | FALSE |
| 13 | Testing Personal Details type height text input. | "hello" | "Invalid height input. Please enter a valid height." | "Invalid height input. Please enter a valid height." | N/A | FALSE |
| 14 | Testing Personal Details high range height text input. | "1000" | "Invalid height input. Please enter a valid height." | "Invalid height input. Please enter a valid height." | N/A | FALSE |
| 15 | Testing Personal Details low range height text input. | "0" | "Invalid height input. Please enter a valid height." | "Invalid height input. Please enter a valid height." | N/A | FALSE |
| 16 | Testing Personal Details special character height text input. | "@@" | "Invalid height input. Please enter a valid height." | "Invalid height input. Please enter a valid height." | N/A | FALSE |
| 17 | Testing Personal Details correct weight text input. | "165" | Program continues | Program continues | N/A | FALSE |
| 18 | Testing Personal Details high range weight text input. | "1000" | "Invalid weight input. Please enter a valid weight." | "Invalid weight input. Please enter a valid weight." | N/A | FALSE |
| 19 | Testing Personal Details low range weight text input. | "0" | "Invalid weight input. Please enter a valid weight." | "Invalid weight input. Please enter a valid weight." | N/A | FALSE |
| 20 | Testing Personal Details special character weight text input. | "!!" | "Invalid weight input. Please enter a valid weight." | "Invalid weight input. Please enter a valid weight." | N/A | FALSE |
| 21 | Testing Personal Details none weight text input. | "" | "Invalid weight input. Please enter a valid weight." | "Invalid weight input. Please enter a valid weight." | N/A | FALSE |
| 22 | Testing Personal Details none age text input. | "" | "Invalid age input. Please enter a valid age." | "Invalid age input. Please enter a valid age." | N/A | FALSE |
| 23 | Testing Personal Details none height text input. | "" | "Invalid height input. Please enter a valid height." | "Invalid height input. Please enter a valid height." | N/A | FALSE |
| 24.0 | Testing Personal Details BMI label updating. | Age: 21, Height: 165, Weight: 80 | BMI label doesnt update. | Max Wilkinson | TRUE | Fix: Made the BMI label to update when pressing the submit handler. |
| 24.1 | Testing Personal Details BMI label updating. | Age: 21, Height: 165, Weight: 80 | BMI label updates to: 29 | BMI label updates to: 29 | N/A | FALSE |
| 25 | Testing Nutrition page's correct calorie text input. | "1500" | Program continues | Program continues | N/A | FALSE |
| 26 | Testing Nutrition page's type calorie text input. | "sdsd" | "Error, please enter a valid number of calories" | "Error, please enter a valid number of calories" | N/A | FALSE |
| 27 | Testing Nutrition page's high range calorie text input. | "10000" | "Error, please enter a valid number of calories" | "Error, please enter a valid number of calories" | N/A | FALSE |
| 28 | Testing Nutrition page's low range calorie text input. | "0" | "Error, please enter a valid number of calories" | "Error, please enter a valid number of calories" | N/A | FALSE |
| 29 | Testing Nutrition page's none calorie text input. | "" | "Error, please enter a valid number of calories" | "Error, please enter a valid number of calories" | N/A | FALSE |
| 30 | Testing Nutrition page's special character calorie text input. | "@@" | "Error, please enter a valid number of calories" | "Error, please enter a valid number of calories" | N/A | FALSE |
| 31 | Testing Nutrition page's submit button. | Click submit button | "Success, Calories saved successfully" | "Success, Calories saved successfully" | N/A | FALSE |
| 32 | Personal Details page's submit button with all correct data inputs. | Click submit button | "Success!, Details saved! Your BMI has been updated" | "Success!, Details saved! Your BMI has been updated" | N/A | FALSE |
| 33 | Personal Details page's submit button with all incorrect data inputs. | Click submit button | Error message outputted respective of the incorrect data. | Error message outputted respective of the incorrect data. | N/A | FALSE |
| 34 | Heart Rate page's correct hr text input. | "122" | Program continues. | Program continues. | N/A | FALSE |
| 35 | Heart Rate page's type hr text input. | "hello" | "Error, Please enter a valid heart rate." | "Error, Please enter a valid heart rate." | N/A | FALSE |
| 36 | Heart Rate page's none hr text input. | "" | "Error, Please enter a valid heart rate." | "Error, Please enter a valid heart rate." | N/A | FALSE |
| 37 | Heart Rate page's low range hr text input. | "0" | "Error, Please enter a valid heart rate." | "Error, Please enter a valid heart rate." | N/A | FALSE |
| 38 | Heart Rate page's high range hr text input. | "210" | "Error, Please enter a valid heart rate." | "Error, Please enter a valid heart rate." | N/A | FALSE |
| 39 | Heart Rate page's submit button saved data. | Select button | "Success, Heart rate saved succesfully." | "Success, Heart rate saved succesfully." | N/A | FALSE |
| 40 | Sleep page's correct text input. | "8" | Program continues | Program continues | N/A | FALSE |
| 41 | Sleep page's high range text input. | "25" | "Error! Input must be a positive integer. Hours: '25' is above the range. Please try again." | "Error! Input must be a positive integer. Hours: '25' is above the range. Please try again." | N/A | FALSE |
| 42 | Sleep page's low range text input. | "0" | "Error! Input must be a positive integer. Hours: '0' is below the range. Please try again." | "Error! Input must be a positive integer. Hours: '0' is below the range. Please try again." | N/A | FALSE |
| 43 | Sleep page's special character text input. | "%%" | "Error! Input must be an integer. Please try again." | "Error! Input must be an integer. Please try again." | N/A | FALSE |
| 44 | Sleep page's type text input. | "hello" | "Error! Input must be an integer. Please try again." | "Error! Input must be an integer. Please try again." | N/A | FALSE |
| 45 | Sleep page's correct submit button. | Click submit button | "Success, Hourly sleep saved successfully." | "Success, Hourly sleep saved successfully." | N/A | FALSE |
| 46 | Sleep page's incorrect submit button. | Click submit button | "Error!", "Input must be an integer. Please try again." | "Error!", "Input must be an integer. Please try again." | N/A | FALSE |
| 47.0 | Personal Detail's page uses int for all inputs. | 21, 165, 80 | All inputs are int. | Most inputs are int but when going back and returning to the page, the values are set to float. | Max Wilkinson | TRUE | Fix: replace float constraints with integers.
| 47.1 | Personal Detail's page uses int for all inputs. | 21, 165, 80 | All inputs are int. | Most inputs are int but when going back and returning to the page, the values are set to float. | Max Wilkinson | TRUE | Fix: replace float constraints with integers.
| 48 | Cognition page spelling button directs properly | Click Spelling button | Directed properly. | Directed properly. |N/A | FALSE |
| 49 | Cognition page memory button directs properly | Click Memory button | Directed properly. | Directed properly. |N/A | FALSE |
| 50 | Cognition page maths button directs properly | Click Maths button | Directed properly. | Directed properly. |N/A | FALSE |
| 51 | Sleep page back button directs properly | Click back button | Directed properly. | Directed properly. |N/A | FALSE |
| 52 | Heart Rate page back button directs properly | Click back button | Directed properly. | Directed properly. |N/A | FALSE |
| 53 | Personal Details page back button directs properly | Click back button | Directed properly. | Directed properly. |N/A | FALSE |
| 54 | Cognitive page back button directs properly | Click back button | Directed properly. | Directed properly. |N/A | FALSE |
| 55 | Cognitive Memory back button directs properly | Click back button | Directed properly. | Directed properly. |N/A | FALSE |
| 56 | Cognitive Spelling back button directs properly | Click back button | Directed properly. | Directed properly. |N/A | FALSE |
| 57 | Cognitive Maths back button directs properly | Click back button | Directed properly. | Directed properly. |N/A | FALSE |
| 58 | Cognitive Memory Incorrect button 1 doesnt increment score | Click incorrect button 1 | Not incremented score var. | Not incremented score var. |N/A | FALSE |
| 59 | Cognitive Memory Incorrect button 2 doesnt increment score | Click incorrect button 2 | Not incremented score var. | Not incremented score var. |N/A | FALSE |
| 60 | Cognitive Memory Correct button does increment score | Click correct button | incremented score var. | incremented score var. |N/A | FALSE |
| 61 | Cognitive Spelling Correct button does increment score | Click correct button | incremented score var. | incremented score var. |N/A | FALSE |
| 62 | Cognitive Maths Correct button does increment score | Click correct button | incremented score var. | incremented score var. |N/A | FALSE |
| 63 | Cognitive Spelling Incorrect button 1 doesnt increment score | Click incorrect button | doeesnt incremented score var. | doesnt incremented score var. |N/A | FALSE |
| 64 | Cognitive Spelling Incorrect button 2 doesnt increment score | Click incorrect button | doeesnt incremented score var. | doesnt incremented score var. |N/A | FALSE |
| 65 | Cognitive Math Incorrect button 1 doesnt increment score | Click incorrect button | doeesnt incremented score var. | doesnt incremented score var. |N/A | FALSE |
| 66 | Cognitive Math Incorrect button 2 doesnt increment score | Click incorrect button | doeesnt incremented score var. | doesnt incremented score var. |N/A | FALSE |
| 67 | Lifestyle page's Exercise directs properly. | Click exercise button | directs properly. | directs properly. |N/A | FALSE |
| 68 | Lifestyle page's Blood Pressure directs properly. | Click blood pressure button | directs properly. | directs properly. |N/A | FALSE |
| 69.0 | Lifestyle page's Walking directs properly. | Click walking button | directs properly. | directs to blood pressure. | Jack Honour | TRUE | Fix: swap handler from blood pressure to walking. |
| 69.1 | Lifestyle page's Walking directs properly. | Click walking button | directs properly. | directs properly. | N/A | FALSE |
| 70 | Lifestyle page's Cholesterol directs properly. | Click cholesterol button | directs properly. | directs properly. | N/A | FALSE |
| 71 | Lifestyle page's Diabetes directs properly. | Click diabetes button | directs properly. | directs properly. | N/A | FALSE |
| 72 | Lifestyle page's Smoker directs properly. | Click smoker button | directs properly. | directs properly. | N/A | FALSE |
| 73 | Lifestyle page's Stroke directs properly. | Click stroke button | directs properly. | directs properly. | N/A | FALSE |
| 74 | Lifestyle page's Back button directs properly. | Click back button | directs properly. | directs properly. | N/A | FALSE |
| 75 | Stroke yes button saves. | Click yes button | boolean value saves 1. | boolean value saves 1. | N/A | FALSE |
| 76 | Stroke no button saves. | Click no button | boolean value saves 0. | boolean value saves 0. | N/A | FALSE |
| 77 | Stroke back button directs properly. | Click back button | directs properly. | directs properly. | N/A | FALSE |
| 78 | Smoker yes button saves. | Click yes button | boolean value saves 1. | boolean value saves 1. | N/A | FALSE |
| 79 | Smoker no button saves. | Click no button | boolean value saves 0. | boolean value saves 0. | N/A | FALSE |
| 80 | Smoker back button directs properly. | Click back button | directs properly. | directs properly. | N/A | FALSE |
| 81 | Diabetes yes button saves. | Click yes button | boolean value saves 1. | boolean value saves 1. | N/A | FALSE |
| 82 | Diabetes no button saves. | Click no button | boolean value saves 0. | boolean value saves 0. | N/A | FALSE |
| 83 | Diabetes back button directs properly. | Click back button | directs properly. | directs properly. | N/A | FALSE |
| 84 | Cholesterol yes button saves. | Click yes button | boolean value saves 1. | boolean value saves 1. | N/A | FALSE |
| 85 | Cholesterol no button saves. | Click no button | boolean value saves 0. | boolean value saves 0. | N/A | FALSE |
| 86 | Cholesterol back button directs properly. | Click back button | directs properly. | directs properly. | N/A | FALSE |
| 87 | Blood Pressure yes button saves. | Click yes button | boolean value saves 1. | boolean value saves 1. | N/A | FALSE |
| 88 | Blood Pressure no button saves. | Click no button | boolean value saves 0. | boolean value saves 0. | N/A | FALSE |
| 89 | Blood Pressure back button directs properly. | Click back button | directs properly. | directs properly. | N/A | FALSE |
| 90 | Walking yes button saves. | Click yes button | boolean value saves 1. | boolean value saves 1. | N/A | FALSE |
| 91 | Walking no button saves. | Click no button | boolean value saves 0. | boolean value saves 0. | N/A | FALSE |
| 92 | Walking back button directs properly. | Click back button | directs properly. | directs properly. | N/A | FALSE |
| 93 | Exercise yes button saves. | Click yes button | boolean value saves 1. | boolean value saves 1. | N/A | FALSE |
| 94 | Exercise no button saves. | Click no button | boolean value saves 0. | boolean value saves 0. | N/A | FALSE |
| 95 | Exercise back button directs properly. | Click back button | directs properly. | directs properly. | N/A | FALSE |
| 95.0 | Pose Analysis' Analyse Pose - Picture opens camera. | click analyse pose - picture button | camera opens. | camera doesnt open. | Jack Honour | TRUE | Fix: wrong module was chosen to access the mobile camera. | 
| 95.1 | Pose Analysis' Analyse Pose - Picture opens camera. | click analyse pose - picture button | camera opens. | camera doesnt open. | Jack Honour | TRUE | Fix: module isnt accessable by BeeWare libary, using another method. |
| 95.2 | Pose Analysis' Analyse Pose - Picture opens camera. | click analyse pose - picture button | camera opens. | camera doesnt open. | Jack Honour | TRUE | Fix: Contributed to Open Source Toga repo, a technology used in BeeWare to enble camera access.
| 95.3 | Pose Analysis' Analyse Pose - Picture opens camera. | click analyse pose - picture button | camera opens. | camera opens. | N/A | FALSE |
| 96 | Pose Analysis' Analyse Pose - Picture (Gallery) gallery can be accessed. | Click analyse pose - picture (gallery) button | gallery can be accessed. | gallery can be accessed. | N/A | FALSE |
| 97 | Pose Analysis' Analyse Pose - Video button takes video of user and proccesses frame by frame. | Click analyse pose - video button | video is taken and proccessed frame by frame. | video is taken and proccessed frame by frame. | N/A | FALSE |
| 98 | Pose Analysis' Analyse Pose - Video (Gallery) button takes video of user and proccesses frame by frame. | Click analyse pose - video (gallery) button | gallery is accessed and vid proccessed frame by frame. | gallery is accessed and vid proccessed frame by frame. | N/A | FALSE |
| 99 | Menu Bar's Health Analysis button directs to users predictions (data not complete). | Click health analysis button | directed properly and placement data is there. | directed properly and placement data is there. | N/A | FALSE |
| 100 | Menu Bar's Main Menu button directs to choice menu. | Click main menu button | directed properly and choice menu is there. | directed properly and choice menu is there. | N/A | FALSE |
| 101 | Cognitive page has reset button and score is reset when pressed. | Click reset score button | score is reset. (see in title label) | score is reset. (see in title label) | N/A | FALSE |
| 102 | Checking the cognitive menu is displayed when the cognition button is pressed. | Pressing cognition button. | On press, button directs user to the cognitive menu page. | Cognitive menu page ran with the expected button. | N/A | FALSE |
| 103.0 | Testing the functionality of the cognitive menu buttons.  | Pressing page buttons. | On press, buttons direct the user to their respective pages. | When pressed, it does nothing. | Sumayyah Mohd Azmi | TRUE | Issue was that one of the toga boxes had “background_color” in the wrong place so it wouldn’t run at all. |
| 103.1 | Testing the functionality of the cognitive menu buttons. | Pressing page buttons. | On press, buttons direct the user to their respective pages. | On press, buttons direct the user to their respective pages. | N/A | FALSE |
| 104.0 | Checking that the words are labelled correctly on the buttons. | Ran the code. | The words in the text file are displayed correctly. | The buttons were blank. | Sumayyah Mohd Azmi | TRUE | Issue was caused by logic being in the wrong order – the UI would not be updated with the new spellings. |
| 104.1 | Checking that the words are labelled correctly on the buttons. | Ran the code. | The words in the text file are displayed correctly. | The words in the text file are displayed correctly. | N/A | FALSE |
| 105 | Testing functionality of selecting a spelling choice.| Pressed one of the spelling choices. | If correct, the user’s correct answers are incremented and the UI updates with a new question. If incorrect, only the UI updates with a new question. | Functionality works as expected. | N/A | FALSE |
| 106 | Testing the end of the game. | Played until all questions were answered. | End game dialog appears with the correct number of answers. User is returned to cognitive menu. | End game dialog appears with the correct number of answers. User is returned to cognitive menu. | N/A | FALSE |
| 107 | Cognitive Spelling back button directs properly. | Click back button. | Directed properly. | Directed properly. | N/A | FALSE |
| 108 | Check initialisation of memory game. | On memory button press, code is run. | Memory game UI is displayed with a label, play button and back button. | Memory game UI is displayed with a label, play button and back button. | N/A | FALSE |
| 109 | Test playing the memory game. | Clicked on the “Play Memory Game” button. | A new game with hidden tiles is displayed. | A new game with hidden tiles is displayed. | N/A | FALSE |
| 110 | Test tile clicking functionality. | Tiles are revealed upon clicking. | Tiles are selected but not revealed upon clicking. | N/A | FALSE |
| 111.0 | Test matching tiles functionality. | Clicked on two matching tiles. | Tiles remain revealed and status label shows “Match!” | Tiles remain revealed and status label shows “Match!” | Sumayyah Mohd Azmi | TRUE | After showing one pair, if another pair is chosen the UI is reset and the tiles, except the new pair, are shown as “?”. The issue was solved by a new list being added to have the total pairs (“end_selected”) that could then be shown in the updated UI. |
| 111.1 | Test matching tiles functionality. | Clicked on two matching tiles. | Tiles remain revealed and status label shows “Match!” | Tiles remain revealed and status label shows “Match!” | N/A | FALSE |
| 112 | Testing non-matching tiles functionality. | Clicked on two non-matching tiles. | Tiles are hidden again, and the status label shows “Try again!” | Tiles are hidden again, and the status label shows “Try again!” | N/A | FALSE |
| 113 | Test ending the game with a score greater than 10. | Matched all tiles with less than 10 tries. | End game dialog displays, and cognitive score is 10. | End game dialog displays, and cognitive score is 10. | N/A | FALSE |
| 114 | Test ending the game with a score less than or equal to 10. | Matched all tiles with 10 or more tries. | End game dialog displays, and cognitive score equals the score. | End game dialog displays, and cognitive score equals the score. | N/A| FALSE |
| 115 | Exit button in memory game directs properly. | Directed properly. | Directed properly. | N/A | FALSE |
| 116 | Cognitive Memory back button directs properly. | Directed properly. | Directed properly. | N/A | FALSE |
| 117 | Checking that a new maths question is generated upon initialisation. | Ran the code when Maths button is pressed in cognitive menu. | A new arithmetic question with the correct answer is displayed. | A new arithmetic question with the correct answer is displayed. | N/A | FALSE |
| 118.0 | Maths correct integer input. | 9 | Program continues to the next question (UI updates), correct answers increase. | Program continues to the next question (UI updates), correct answers increase. | N/A | FALSE |
| 118.1 | Maths incorrect integer input. | 14 | Program continues to the next question (UI updates). | Program continues to the next question (UI updates). | N/A | FALSE |
| 118.2 | Maths float input when divide. | 0.23423 | Program continues to the next question (UI updates). | Program continues to the next question (UI updates). | N/A | FALSE |
| 118.3 | Maths float input when not divide. | 1.43 | Program continues to the next question (UI updates). | Program continues to the next question (UI updates). | N/A | FALSE |
| 118.4 | Maths text input. | “text” | Value Error, moves to the next question (UI updates). | Value Error, moves to the next question (UI updates). | N/A | FALSE |
| 119 | Testing the end of the game. | Played until all questions were answered. | End game dialog appears with the correct number of answers. User is returned to cognitive menu. | End game dialog appears with the correct number of answers. User is returned to cognitive menu. | N/A | FALSE |
| 120 | Cognitive Maths back button directs properly. | Click back button. | Directed properly. | Directed properly. | N/A | FALSE |
| 121 | Checking variations of MLA predictions | Enter details of a healthy person (Low BMI, >100 mins of exercise, no risk factors) | A low percentage estimate of heart disease | Heart Disease Estimate: 18.15% | N/A | FALSE |
| 121.1 | Checking variations of MLA predictions | Enter details of a mid-health person (Low BMI, >100 mins of exercise, several risk factors) | A greater estimate of heart disease | Heart Disease Estimate: 29.03% | N/A | FALSE |
| 121.2 | Checking variations of MLA predictions | Enter details of an unhealthy person (High BMI, <100 mins of exercise, all the risk factors) | An even greater estimate of heart disease | Heart Disease Estimate: 48.52% | N/A | FALSE |
