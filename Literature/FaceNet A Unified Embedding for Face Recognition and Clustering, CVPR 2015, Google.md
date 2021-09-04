### **FaceNet: A Unified Embedding for Face Recognition and Clustering, CVPR 2015, Google**

Face Recognition (FR) system

- **Raw input image (needs "face processing")**
  - Crop
  - Frontalisation: face alignment: change the angle of the face (align) by identifying landmarks.
  - **Face processing**
    - one-to-many
    - many-to-one



**Some popular models in the history**

- Hand-crafted Learned Filter (84.02% accuracy) (very complex algorithm)
- AlexNet: 97.35% accuracy 

![image-20210904160818027](C:\Users\youre\AppData\Roaming\Typora\typora-user-images\image-20210904160818027.png)

- <span style='color: red;'>**FaceNet learns to map**</span> one image (128, 128, 3) to another (128, 128, 3).



#### **Characteristics of FaceNet (by Google, CVPR 2015)**

- Very Deep Network (ZFNet, GoogleNet)
- No face alignment 
- Single model
- Verification loss only: Face l2 Embedding.
  - identification: k-NN classification
  - clustering: k-means clustering

![image-20210904161708680](C:\Users\youre\AppData\Roaming\Typora\typora-user-images\image-20210904161708680.png)

![image-20210904161916936](C:\Users\youre\AppData\Roaming\Typora\typora-user-images\image-20210904161916936.png)



****

**Conclusion**

- In face recognition, dataset & pre-processing is **very important**.

- Metric learning vs Clssification loss depends on application.

  - Open-set / closed-set
  - identification (facebook) / verification (security, face ID)

  

**Metric learning in computer vision** 

- Face recognition
- Image retrieval
- Person re-identification
- Scene recognition
- Object tracking



**Challenges in Face recognition** 

- small inter-class variations / large intra-class variations 

  - facial expressions and emotions
    - happy face, crying face, age ...

- Small discriminant features, low resolution, hard occlusions

- **Cross-factor FR**

  (a) cross-pose

  (b) cross-age

  (c) make-up

- **Heterogeneous FR** 

  (d) NIV-VIS 

  (e) low resolution 

  (f) matching photo-sketch

- **Multiple (or single) media FR**

  (g) low-show

  (h) template-based

  (i) video

- **FR in industry**

  (j) 3D

  (k) anti-spoofing (sorting fake faces)

  (l) mobile devices 

  (m) partial (only partial face features are available.)



**References**

Taeho Kim (2018) PR-127: FaceNet https://www.youtube.com/watch?v=0k3X-9y_9S8&ab_channel=TaeohKim

