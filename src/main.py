from data_preprocessing import load_data, clean_data, feature_engineering
from model_training import train_model, evaluate_model
from visualization import plot_feature_importance

if __name__ == "__main__":
    # Load data
    data = load_data('data.csv') 

    # Clean data
    clean_data = clean_data(data)

    # Feature engineering
    engineered_data = feature_engineering(clean_data)

    # Split data into features and target
    X = engineered_data.drop('target_column', axis=1) 
    y = engineered_data['target_column']

    # Split data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train a model
    model = train_model(X_train, y_train, model_name='decision_tree')

    # Evaluate the model
    mse = evaluate_model(model, X_test, y_test)
    print(f"Mean Squared Error: {mse}")

    # Plot feature importance (if applicable)
    plot_feature_importance(model, X.columns) 
