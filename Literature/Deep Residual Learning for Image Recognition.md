## **Deep Residual Learning for Image Recognition**

#### **Adding Depth (causes degradation)**

- **Advantages**: generalise better, achieve lower error rates
- **Problem**: optimisation is challenging
  - This is **NOT a problem of overfitting**.
  - In Overfitting, the test error is high while the training error is low.
  - Not an overfitting of too many parameters.
  - *"Degradation (of training accuracy) indicates that not all systems are similarly easy to optimise."*

- The paper posits that the problem must be with the easiness of optimisation and not overfitting.
- So if the additional layers are **identity functions**, than the deeper network **should be at least achieve the same accuracy** as the original model.
- But in deeper networks, the models don't learn the identity functions. Why don't they do so then? : **Because we initialise most weights towards zero (0)**.
- Models usually take samples from Gaussian distributions which have stds about the mean of 0.
- In fact, **identity functions in convolutional networks are pretty difficult to learn.**

#### **Residual connections**

- So the paper questions**:** ***"\****Can we* ***make the identity function default function?"\***
- Instead of trying to produce identity values through a complex deep Conv layers, set the identity function as default so you get the identity values by default (stay x), and learn whatever you need to change.
- Turns out that this approach is highly accurate.

- Classic question of "**WHEN to use Batch Normalisation (BS)?**"

- Residual learning model adopts BS right after each convolution and before activation.