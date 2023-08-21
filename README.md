# **Disease_Predictor**
### **Discription**
  - Our project is a valuable and innovative Model that aims to provide a much-needed solution for people who may be unable to afford or access healthcare services. <br>
  - By using sophisticated algorithms and advanced data analysis techniques, our application can help users identify potential illnesses based on their symptoms.<br>
  - This technology has the potential to revolutionize the way people manage their health, particularly in areas where medical resources may be limited. <br>
  - Our project is a shining example of how technology can be leveraged to make a positive impact on society, by improving access to critical health information and   empowering people to take control of their wellbeing.<br>
  - This will help mainly those people who are poor or dont have the luxury to visit the doctors.

### **Prerequists**
* Tensorflow is also needed.
* pyttsx3 is also important to run the talk engine which will help the user who have sight issue.
* speech_recognition library is optional. Functions using this feature may be added in the future.

### **Installation**
* Assumuming the dataset is included in the same folder as `chatbot.py`.<br>
* You just need to run the file the required partition and data pre processing will be done by the file itself.<br>
* All three of these files are neccessary for the working of the program.
After that a `data_dict.pkl, final_nb_model.pkl, final_rf_model.pkl, final_svm_model.pkl, lamda.pkl` file will be created which will be used in the chatbot.
Now, just run the `chatbot_v_1.1.py` file.

### Working
* This program has two modes.
    - Chat only 
    - Talk and chat 
* people who have hearing issue can use chat only.
* people who have eye issue can use 2nd option.
* This software has 3 models( Naive bayes, Random forest, Support Vector Machine )
* This project is maily made to help people who don't have money to visit doctor.

### License
* GNU General Public License v3.0
