### **Week 2 Mentoring session log** 

##### **Mentor's feedback**

Object detection and recognition are two different things.

- Develop a scenario for recognising faces.
- What do you concretely want to achieve with your application?
  - one-to-many
  - many-to-many



**Our plan**

- Our scenario: 
  - pre-train our model with 20 m photos.
  - then recognise certain target faces.
  - Stage-1: our next target is o test the recognition accuracy.



**Feedback**
(although I understand the general flow of your project, it largely lacks important details of your project development. Need to further concretise them.)

- face-id (this requires astronomical work of photo comparison)
- Further concretise your app development scenario.

- Clarify the definition of rejection rate

- it can be difficult to achieve 5% rate for the faces of 4 team members.
- Confusion matrix: how are you going to improve the performance?
  - **<span style='color:red;'>Depending on your calculation methods, you will have to change the train dataset</span>.**
  - Clarify accuracy calculation method
- Apply conditions: amount of lights, angle
