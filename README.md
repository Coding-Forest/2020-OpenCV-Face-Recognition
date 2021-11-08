# 2021-OpenCV-Face-Recognition
Face Recognition application development project using OpenCV and a FR model. 


## Models & libraries studied:
1) MTCNN 
2) FaceNet-PyTorch
3) ResNet
4) face_recognition


References
1) PyTorch + inception_resnet_v1 Fine-Tuning
https://ichi.pro/ko/pytorchleul-sayonghayeo-eolgul-eul-insighadolog-eolgul-insig-bunlyugileul-mise-jojeong-228743039523449
2) timesler - facenet-pytorch
https://github.com/timesler/facenet-pytorch#pretrained-models
3) How to Train Your ResNet: The Jindo Dog (Thierry Laplanche)
https://medium.com/analytics-vidhya/how-to-train-your-resnet-the-jindo-dog-50551117381d

BOOKS 
1) Practical Deep Learning for Cloud, Mobile, and Edge by Anirudh Koul, Siddha Ganju, and Meher Kasam (O’Reilly, 2019)

DATASETS

    #!mkdir -p ~/.kaggle/   
    !cp /content/kaggle.json ~/.kaggle/    
    !ls ~/.kaggle  
    - Upload your kaggle.json credential.  
    
    ref                                              title                                      size  lastUpdated          downloadCount  
    -----------------------------------------------  ----------------------------------------  -----  -------------------  -------------  
    andrewmvd/animal-faces                           Animal Faces                              696MB  2020-05-22 06:49:01           3487  
    ashwingupta3012/human-faces                      Human Faces                                 2GB  2020-09-21 04:09:12           2789  
    soumikrakshit/anime-faces                        Anime Faces                               441MB  2019-05-16 10:38:47           5593  
    kostastokis/simpsons-faces                       Simpsons Faces                            442MB  2018-09-28 17:38:04           5998  
    selfishgene/youtube-faces-with-facial-keypoints  YouTube Faces With Facial Keypoints        16GB  2021-10-06 03:11:11           8191  
    dansbecker/5-celebrity-faces-dataset             5 Celebrity Faces Dataset                   5MB  2017-11-10 04:08:41          12041  
    jessicali9530/celeba-dataset                     CelebFaces Attributes (CelebA) Dataset      1GB  2018-06-01 20:08:48          62444  
    jessicali9530/lfw-dataset                        Labelled Faces in the Wild (LFW) Dataset  112MB  2018-05-17 19:57:27           9295  
    arnaud58/flickrfaceshq-dataset-ffhq              Flickr-Faces-HQ Dataset (FFHQ)             19GB  2020-03-09 12:24:45           3057  
    xhlulu/140k-real-and-fake-faces                  140k Real and Fake Faces                    4GB  2020-02-10 17:11:35           2239  
    atulanandjha/lfwpeople                           LFW - People (Face Recognition)           232MB  2019-11-15 19:45:43           8323  
    dataturks/face-detection-in-images               Face Detection in Images                   55KB  2018-07-12 09:34:14          12377  
    gasgallo/faces-data-new                          faces_data_new                             90MB  2018-08-16 07:44:30           3981  
    sahilyagnik/olivetti-faces                       Olivetti Faces                              2MB  2018-02-05 00:56:12            699  
    greatgamedota/ffhq-face-data-set                 FFHQ Face Data Set                          2GB  2019-10-12 22:12:09           1490  
    tbourton/photoshopped-faces                      Photoshopped faces                          3GB  2021-05-01 08:53:23             46  
    tunguz/1-million-fake-faces                      1 Million Fake Faces - 1                   17GB  2019-11-14 01:59:47           1406  
    kasikrit/att-database-of-faces                   AT&T Database of Faces                      4MB  2019-12-17 02:47:06           5787  
    dmitryyemelyanov/riga-faces                      Riga Faces                                 98MB  2021-02-17 12:31:06             25  
    havingfun/100-bollywood-celebrity-faces          Bollywood Celebrity Faces                   2GB  2020-03-21 10:15:17           1704 

    # Change the permissions of the file.  
    !chmod 600 ~/.kaggle/kaggle.json  
