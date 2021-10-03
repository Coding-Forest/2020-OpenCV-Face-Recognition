# 4. Visualise results
epochs01 = np.arange(0, len(train_acc_1))
epochs02 = np.arange(0, len(train_acc_2))

profile = "Fine-tuning1: 8,000 images of 400 individuals\nFine-tuning2: 144,000 images of the same 400 individuals"
title_label = ["Loss Comparison", "Accuracy Comparison"]
results = [loss_results, acc_results]

for i in range(2):
    fig, ax = plt.subplots(figsize=(7, 5))
    ax.plot(epochs01, results[i][0], c='blue', label="Fine-tuning train 1")
    ax.plot(epochs01, results[i][1], c='dodgerblue', label="Fine-tuning valid 1")
    ax.plot(epochs02, results[i][2], c='red', label="Fine-tuning train 2")
    ax.plot(epochs02, results[i][3], c='coral', label="Fine-tuning valid 2")
    ax.set_xlim(-0.5, 9.5)
    ax.set_ylim()
    ax.set_title(title_label[i], fontsize=25)
    plt.legend()
    plt.tight_layout()
    plt.savefig(f"/content/here/MyDrive/FaceID/Fine_tuning/{title_label[i]}.png")    
plt.show()
