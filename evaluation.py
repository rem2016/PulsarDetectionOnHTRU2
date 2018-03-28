import numpy as np
import pandas as pd
from sklearn.metrics import confusion_matrix, recall_score, precision_recall_curve, roc_auc_score


def cross_validation(learner, X, y, ):
    pass


def estimate(model, features_train, features_test, labels_train, labels_test):
    clf = model
    clf.fit(features_train, labels_train.values.ravel())
    pred = clf.predict(features_test)
    return confusion_matrix(labels_test, pred)

    # print("the recall for this model is :", cnf_matrix[1, 1] / (cnf_matrix[1, 1] + cnf_matrix[1, 0]))
    # fig = plt.figure(figsize=(6, 3))  # to plot the graph
    # print("TP", cnf_matrix[1, 1,])  # no of fraud transaction which are predicted fraud
    # print("TN", cnf_matrix[0, 0])  # no. of normal transaction which are predited normal
    # print("FP", cnf_matrix[0, 1])  # no of normal transaction which are predicted fraud
    # print("FN", cnf_matrix[1, 0])  # no of fraud Transaction which are predicted normal
    # sns.heatmap(cnf_matrix, cmap="coolwarm_r", annot=True, linewidths=0.5)
    # plt.title("Confusion_matrix")
    # plt.xlabel("Predicted_class")
    # plt.ylabel("Real class")
    # plt.show()
    # print("\n----------Classification Report------------------------------------")
    # print(classification_report(labels_test, pred))


__all__ = ['cross_validation']
