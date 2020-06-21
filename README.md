# Segmentation of Nucleus and Cytoplasm from Unit Papanicolaou Smear Images using Deep Semantic Networks

Pap smear images require very efficient segmentation techniques to improve the prediction of carcinoma. Conventional techniques are not efficient for the entire dataset. The proposed technique, segmentation using semantic network, highlights the effective use of network architecture, available data, optimization algorithms and high- end computing; improving the efficiency in classifying cellular components, the nucleus and cytoplasm, in the unit pap image. High accuracy actually representing the human perception of vision has been achieved. 


# Papnicolaou Smear Images -PAP Smear Test
A Pap (-anicoalau smear is used to screen for cervical cancer. The presence of pre-cancerous or cancerous cells on the cervix can be detected using this test. A precancerous cell is one in which the genetic information has been modified and exhibits abnormal cell division. A cancerous cell is one in which the cell is devoid of cytoplasm. This procedure is usually carried out in women who are in the age group of 21- 65 years. The pap cells are obtained from different areas of the cervix using cyto-brush, cotton stick or a wooden stick. 
The cells are mostly derived from columnar epithelium and the squamous epithelium. The cervix has two parts – the upper part the columnar epithelium and the lower part the squamous epithelium. The specimen is smeared onto a glass slide and is stained using Papanicolaou method so that the components of the cells are highlighted with specific colours.The Pap smear database consists of 917 such microscopic images collected for different cases from different locations. 


# Pre-Processing 
The segmentation of cells from the Pap smear is difficult even for trained cyto- technicians. A new database created from the smear images using the Champ software was also used as the target images. The Pap smear images have three classes: nucleus, cytoplasm and background. Three different colors, red, blue and black were assigned to these classes respectively. One of the important requirements in semantic segmentation is that the input and the output images should be of the same dimension. Hence to achieve this, zero- padding of images has been done and it was ensured that all images are of the size 128 x 128.  

The available database is enlarged by means of horizontal and vertical flipping of images. At the end of preprocessing, the enlarged datasets of the input and the target images were available for the training process. 


# Instructions to Execute

The various versions of the image database, original, only preprocessed and preprocessed + augmented are included in this repo. In case of adding more classes or increasing the augmented image count,use preprocessing jupyter notebook.

Use train.py to start training. The following are the arguments that can be passed on to the training script.


1. **--num_epochs** , default=10, 'Number of epochs to train for'

2. **--epoch_start_i**, default=0, 'Start counting epochs from this number'

3. **--checkpoint_step**, default=1, 'How often to save checkpoints (epochs)'

4. **--validation_step**, default=1, 'How often to perform validation (epochs)'

5. **--image**, default=None, 'The image you want to predict on. Only valid in "predict" mode.'

6. **--continue_training**, default=False, 'Whether to continue training from a checkpoint'

7. **--dataset**, default="PAP", 'Dataset you are using.'

8. **--crop_height**, default=128, 'Height of cropped input image to network'

9. **--crop_width**, default=128, 'Width of cropped input image to network'

10. **--batch_size**, default=1, 'Number of images in each batch'

11. **--num_val_images**, default=913 , 'The number of images to used for validations'

12. **--h_flip**, default=False, 'Whether to randomly flip the image horizontally for data augmentation'

13. **--v_flip**, default=False, 'Whether to randomly flip the image vertically for data augmentation'

14. **--brightness**, default=None, 'Whether to randomly change the image brightness for data augmentation. Specifies the max bightness change as a factor between 0.0 and 1.0. For example, 0.1 represents a max brightness change of 10%% (+-).'

15. **--rotation**, default=None, 'Whether to randomly rotate the image for data augmentation. Specifies the max rotation angle in degrees.'

16. **--model**, default="FC-DenseNet56", 'The model you are using. See model_builder.py for supported models'

17. **--frontend**, default="ResNet101", 'The frontend you are using. See frontend_builder.py for supported models'

# Team

**Abhinaav Ramesh, Akshaya Sapthasri M, Anusha V, Nivetha S**

Department of Biomedical Engineering, PSG College of Technology

**Reference CodeBase**
https://github.com/GeorgeSeif/Semantic-Segmentation-Suite.git



