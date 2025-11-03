# Peptic Ulcer / Disease Detection System

A machine learning-based disease prediction system with an intuitive graphical user interface. Users can select symptoms and receive predictions about potential diseases, including peptic ulcers, along with detailed information and precautions.

## Technology Stack

- **Language**: Python 3.8+
- **ML Framework**: scikit-learn
- **Data Processing**: NumPy, Pandas
- **Visualization**: Matplotlib, Seaborn
- **GUI**: Tkinter
- **Algorithms**: Decision Tree, Random Forest, Gaussian Naive Bayes

## Features

- **Symptom-based Prediction**: Select from 132+ symptoms to predict diseases
- **Multiple ML Algorithms**: 
  - Decision Tree Classifier
  - Random Forest Classifier
  - Gaussian Naive Bayes
  - Auto (Ensemble) mode for best results
- **Comprehensive Disease Information**: 
  - Disease name and type identification
  - Brief medical description
  - Recommended precautions and care tips
- **User-Friendly Interface**: 
  - Colorful, intuitive Tkinter GUI
  - Scrollable symptom selection
  - Large result display area
  - No technical knowledge required

## Installation

### Prerequisites

- Python 3.8 or higher
- Required packages (see requirements below)

### Setup

1. **Clone or download the project files**

2. **Install required packages**:
   ```powershell
   pip install numpy pandas scikit-learn matplotlib seaborn
   ```

3. **Verify files are present**:
   - `PEP.py` - Core prediction engine
   - `ui.py` - Graphical user interface
   - `training.csv` - Training dataset
   - `Testing.csv` - Test dataset

## Usage

### Running the Application

1. **Open PowerShell or Command Prompt**

2. **Navigate to the project directory**:
   ```powershell
   cd "c:\Users\HELLO\OneDrive\Desktop\Peptic Ulcer Detection"
   ```

3. **Run the application**:
   ```powershell
   python ui.py
   ```

### Using the Interface

1. **Select Symptoms**:
   - Scroll through the symptom list on the left
   - Check all symptoms you are experiencing
   - Use mouse wheel for easy scrolling

2. **Choose Algorithm** (Optional):
   - "Auto (recommended)" - Uses ensemble voting for best accuracy
   - "tree" - Decision Tree
   - "random" - Random Forest
   - "gnb" - Gaussian Naive Bayes

3. **Get Prediction**:
   - Click the "Predict" button
   - View results showing:
     - Predicted disease name
     - Ulcer type (if applicable)
     - Brief medical description
     - Recommended precautions

## Project Structure

```
Peptic Ulcer Detection/
│
├── PEP.py                 # Core ML models and prediction logic
├── ui.py                  # Graphical user interface
├── training.csv           # Training dataset (symptoms → diseases)
├── Testing.csv            # Test dataset for validation
├── README.md              # This file
└── uk.py                  # Additional utilities (optional)
```

## Technical Details

### Machine Learning Algorithms

The system implements three supervised learning algorithms from scikit-learn:

1. **Decision Tree Classifier**
   - **Algorithm**: CART (Classification and Regression Trees)
   - **Purpose**: Creates a tree-like model of decisions based on feature values
   - **Advantages**: Fast predictions, interpretable, handles non-linear relationships
   - **Use Case**: Quick, explainable disease predictions

2. **Random Forest Classifier**
   - **Algorithm**: Ensemble of multiple decision trees with bootstrap aggregating (bagging)
   - **Purpose**: Combines predictions from multiple trees to improve accuracy and reduce overfitting
   - **Advantages**: High accuracy, robust to noise, handles large feature sets
   - **Use Case**: More reliable predictions through consensus

3. **Gaussian Naive Bayes**
   - **Algorithm**: Probabilistic classifier based on Bayes' theorem with Gaussian distribution assumption
   - **Purpose**: Calculates probability of each disease given the symptoms
   - **Advantages**: Fast training, works well with small datasets, probabilistic output
   - **Use Case**: Probability-based disease likelihood estimation

### Python Packages Used

#### Core Machine Learning
- **scikit-learn (>=0.23.0)**: Machine learning library
  - `sklearn.tree.DecisionTreeClassifier` - Decision tree implementation
  - `sklearn.ensemble.RandomForestClassifier` - Random forest implementation
  - `sklearn.naive_bayes.GaussianNB` - Naive Bayes implementation
  - `sklearn.model_selection.train_test_split` - Dataset splitting
  - `sklearn.metrics.accuracy_score` - Model evaluation

#### Data Processing & Analysis
- **NumPy (>=1.19.0)**: Numerical computing
  - Array operations
  - Mathematical functions
  - Data reshaping and manipulation
  
- **Pandas (>=1.1.0)**: Data manipulation and analysis
  - CSV file reading/writing
  - DataFrame operations
  - Data cleaning and preprocessing
  - Column normalization

#### Visualization (for data analysis)
- **Matplotlib (>=3.3.0)**: Plotting library
  - Data visualization
  - Model performance graphs
  
- **Seaborn (>=0.11.0)**: Statistical visualization
  - Enhanced plotting capabilities
  - Correlation matrices
  - Distribution plots

#### User Interface
- **Tkinter**: Python's standard GUI library (built-in)
  - Main application window
  - Symptom selection checkboxes
  - Result display
  - Button and label widgets
  - ScrolledText for text display

### Machine Learning Models

The system uses three trained classifiers:

1. **Decision Tree Classifier**: Fast, interpretable predictions
2. **Random Forest Classifier**: Ensemble of trees for robust predictions
3. **Gaussian Naive Bayes**: Probabilistic classifier

### Auto (Ensemble) Mode

When "Auto" is selected, the system:
- Queries all three algorithms
- Performs majority voting
- Returns the most agreed-upon prediction
- Falls back to Decision Tree on ties

### Dataset

- **Symptoms**: 132 medical symptoms
- **Diseases**: 41 different conditions including:
  - Peptic Ulcer Disease
  - Gastroenteritis
  - Diabetes
  - Hypertension
  - Various infections
  - And more...

### Data Processing Pipeline

1. **Data Loading**:
   - CSV files loaded using Pandas
   - Column name normalization (removing spaces)
   
2. **Feature Engineering**:
   - Binary encoding of symptoms (1 = present, 0 = absent)
   - 132 symptom features per patient record
   
3. **Label Encoding**:
   - Disease names mapped to integer classes
   - Normalized string matching for consistency
   
4. **Model Training**:
   - Train-test split using provided datasets
   - Each algorithm trained on the same feature set
   - Models cached for fast subsequent predictions

5. **Prediction**:
   - User symptoms converted to binary feature vector
   - Model inference using trained classifiers
   - Ensemble voting in Auto mode

## Disease Information Coverage

The system provides detailed information for common conditions including:
- Peptic Ulcer Disease
- Fungal Infections
- GERD (Gastroesophageal Reflux Disease)
- Gastroenteritis
- Urinary Tract Infections
- Hypertension
- Diabetes
- Dengue Fever
- Malaria
- Typhoid
- Common Cold
- Pneumonia

For other diseases, generic precautions and advice are provided.

## Model Performance

Current model metrics:
- Training Accuracy: ~100%
- Test Accuracy: ~100%

*Note: High accuracy may indicate data characteristics. Always consult healthcare professionals for medical diagnosis.*

## Important Disclaimer

⚠️ **This system is for educational and informational purposes only.**

- **NOT a substitute** for professional medical advice
- **Always consult** a licensed healthcare provider for diagnosis
- **Do not self-medicate** based on predictions
- Seek immediate medical attention for serious symptoms

## API Usage (Advanced)

You can use the prediction function programmatically:

```python
from PEP import predict_symptoms

# Predict with symptoms
symptoms = ['stomach_pain', 'acidity', 'vomiting']
disease = predict_symptoms(symptoms, algorithm='tree')
print(f"Predicted: {disease}")

# Use ensemble voting
disease = predict_symptoms(symptoms, algorithm='auto')
```

## Troubleshooting

### Common Issues

1. **Import Errors**:
   ```powershell
   pip install --upgrade numpy pandas scikit-learn
   ```

2. **CSV Not Found**:
   - Ensure `training.csv` and `Testing.csv` are in the same folder as `PEP.py`

3. **UI Not Showing**:
   - Check Python version: `python --version`
   - Ensure Tkinter is installed (usually comes with Python)

4. **Slow Performance**:
   - Models build on first run; subsequent predictions are fast
   - Close and reopen if UI becomes unresponsive

## Development

### Adding New Disease Information

Edit `ui.py` and add to the `DISEASE_INFO` dictionary:

```python
DISEASE_INFO = {
    'diseasename': {
        'title': 'Disease Display Name',
        'note': 'Brief description...',
        'precautions': [
            'Precaution 1',
            'Precaution 2',
            # ...
        ]
    }
}
```

### Retraining Models

Modify `PEP.py` and call:
```python
build_models(verbose=True)
```

## Requirements

### Python Version
- Python 3.8 or higher

### Required Packages

```
numpy>=1.19.0           # Numerical computing and array operations
pandas>=1.1.0           # Data manipulation and CSV handling
scikit-learn>=0.23.0    # Machine learning algorithms and tools
matplotlib>=3.3.0       # Data visualization and plotting
seaborn>=0.11.0         # Statistical data visualization
```

### Installation Command

```powershell
pip install -r requirements.txt
```

Or install individually:
```powershell
pip install numpy pandas scikit-learn matplotlib seaborn
```

## Credits

- **Dataset**: Medical symptoms and disease mappings
- **ML Libraries**: scikit-learn, NumPy, Pandas
- **UI Framework**: Tkinter (Python standard library)

## License

This project is intended for educational purposes.

## Contact & Support

For issues or questions about the project, please refer to the source code documentation or consult with your course instructor.

---

**Version**: 1.0  
**Last Updated**: November 2, 2025
#   S m a r t - D i a g n o s t i c s - L e v e r a g i n g - M a c h i n e - L e a r n i n g - f o r - I m p r o v e d - D e t e c t i o n - o f - P e p t i c - U l c e r s 
 
 
