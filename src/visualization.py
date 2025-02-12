def plot_feature_importance(model, feature_names):
    """Plots feature importance for tree-based models.

    Args:
        model: Trained tree-based model.
        feature_names (list): List of feature names.
    """
    if hasattr(model, 'feature_importances_'):
        importances = model.feature_importances_
        plt.figure(figsize=(10, 5))
        sns.barplot(x=importances, y=feature_names)
        plt.xlabel('Feature Importance')
        plt.ylabel('Features')
        plt.title('Feature Importance')
        plt.show()
