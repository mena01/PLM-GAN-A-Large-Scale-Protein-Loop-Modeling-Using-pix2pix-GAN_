Determining the tertiary structure of a protein is of great importance as it reveals the protein’s properties and functions. However, these structures are highly complex 3-dimensional configurations consisting of a variety of bonds, such as ionic, hydrophobic, and disulfide. Tertiary structures may exhibit missing regions or require the reconstruction of certain segments. The challenge of predicting and regenerating these regions is known as a loop modeling problem. In this work, we introduce novel models called pix2pix GAN and PLM-GAN for reconstructing missing regions of different protein structures and regenerating them while maintaining their features (backbone, local, and distal).
This study presents novel models, pix2pix GAN and PLM-GAN, that are capable of reconstructing missing regions of various protein structures while preserving their features, including the backbone, local, and distal properties. Our contributions can be summarized in five parts: I) The application of pix2pix GAN to generate and in-paint distance matrices of protein structures. II) The development of the PLM-GAN model by integrating residual blocks into the U-Net network of the Generative Adversarial Network (GAN), based on the pix2pix GAN model. III) The proposal of a new loss function called the Missing to Real regions loss (LMTR) in the GAN. IV) The pairing of two different distance matrices, one for the native protein structure and the other for the same structure but with a loop region that changes in each successive epoch. V) Increasing the length of the missing region up to 30 amino acids and the length of the protein by 128 amino acids.

We applied the pix2pix GAN and PLM-GAN models to natural proteins (4ZCB, 3fjb, and 2rez) and obtained promising experimental results. Our models offer a practical solution to the challenge of loop modeling in protein design, representing a significant advancement in simplifying protein design models. Furthermore, these models have the potential to enhance other models for protein-protein interactions and drug design, enabling further innovation and progress in the field.

- The dataset directory contains PDB IDs for proteins, as well as code to download PDB files and generate distance matrices for the training and testing datasets.

- "Network_Weights" directory contains the weights of the network used to generate and inpaint distance matrices for protein structures that have missing regions in random regions.


![Dist](https://user-images.githubusercontent.com/73284871/231022422-1597d66d-0d2e-4ea7-9790-aba4b2f29a4e.png)

### We utilize the MMD algorithm to fold the distance matrix that is generated and inpainted by the pix2pix GAN and PLM-GAN models.

![Folding](https://user-images.githubusercontent.com/73284871/231023038-a4852e3e-e5b1-4ad2-8dc9-5056a0b0bc58.png)


#### We offer the inpaint network and its weights, along with the R code for folding protein structures.

#### The dataset directory includes PDB IDs for proteins, along with code for downloading PDB files and generating distance matrices for the training and testing datasets.









