import model
import evaluation
import preprocess
import tuning


X_train, X_test, y_train, y_test = preprocess.load_train_test()


def test_stacked_ensemble():
    stacked = [model.LinearModel()]
    evaluation.estimate(
        model.StackedEnsembleModel(learners=stacked, next_model=model.LinearModel()),
        X_train, X_test, y_train, y_test,
        use_confusion_matrix=True
    )
