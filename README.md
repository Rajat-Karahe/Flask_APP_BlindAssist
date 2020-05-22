# Flask_APP_BlindAssist
--
Live Deployed on Heroku :- https://blind-assist.herokuapp.com/

--------------------------------------------

![HomePage](/readme_images/home.png)

--------------------------------------------

![ResultPage](/readme_images/result.png)

--------------------------------------------

![AboutPage](/readme_images/about.png)

--------------------------------------------

Currency Denomination Identifier
--
This project is inspired by the tender of RBI(Reserve Bank of India) Dated July 26, 2019; 5:00 PM. to develop a Mobile Application for Aiding the Visually Impaired in Identifying Denominations of Indian Banknotes.

The goal of this project is to come up with a solution via a smart phone app, both on Android and iOS, which will leverage the power of deep learning image classification behind the scenes and help the blind individual to recognize the Indian currency denomination notes accurately and independently so he does not have to depend on others and can easily deal with cash transactions on his own. The app will recognize the note he is carrying and play a sound English or Hindi, depending upon the configuration, and let him know the value of the recognized note.

The Dataset
--
To accomplish this goal we created our own custom dataset the ICR dataset (Indian Currency Recognition dataset) which is a very rich dataset comprising of around 8000 Images of Indian currency denomination of all types "5", "10", "20", "50", "100", "200", "500", "2000" including all version of each note type available in market. This dataset is extremely rich as all the images taken are applicable to real world scenarios, different lightning situations, different camera capacities, currently we are still working to expand this dataset once done we will open source it.

Training
--
We used the power of deep learning to build a effective model which gives a good accuracy. we used the power of transfer learning by customizing a pre-trained mobilenetv2 model and we were able to achieve an accuracy of 99% on a validation image set of 900 images.
