# kama/app.py

import streamlit as st
from .core.kama import Kama
from .ui import (
    resource,
    big_data,
    cloud,
    models,
    prediction,
    data_ops,
    text_ops,
    image_ops
)
from .utils.helpers import display_message

# إنشاء كائن من لغة Kama
kama_lang = Kama()

# تهيئة حالة الجلسة
if 'data_chunks' not in st.session_state:
    st.session_state.data_chunks = None
if 'processed_data' not in st.session_state:
    st.session_state.processed_data = None
if 'loaded_model' not in st.session_state:
    st.session_state.loaded_model = None
if 'plotted_data' not in st.session_state:
     st.session_state.plotted_data = None
if 'tensor_data' not in st.session_state:
     st.session_state.tensor_data = None
if 'cleaned_data' not in st.session_state:
     st.session_state.cleaned_data = None
if 'transformed_data' not in st.session_state:
      st.session_state.transformed_data = None
if 'grouped_data' not in st.session_state:
    st.session_state.grouped_data = None
if 'x_train' not in st.session_state:
     st.session_state.x_train = None
if 'x_test' not in st.session_state:
     st.session_state.x_test = None
if 'y_train' not in st.session_state:
     st.session_state.y_train = None
if 'y_test' not in st.session_state:
    st.session_state.y_test = None
if 'trained_model' not in st.session_state:
    st.session_state.trained_model = None
if 'tuned_model' not in st.session_state:
    st.session_state.tuned_model = None
if 'tokens' not in st.session_state:
     st.session_state.tokens = None
if 'filtered_tokens' not in st.session_state:
     st.session_state.filtered_tokens = None
if 'word_embeddings' not in st.session_state:
     st.session_state.word_embeddings = None
if 'sentiment_result' not in st.session_state:
     st.session_state.sentiment_result = None
if 'loaded_image' not in st.session_state:
    st.session_state.loaded_image = None
if 'resized_image' not in st.session_state:
     st.session_state.resized_image = None
if 'filtered_image' not in st.session_state:
     st.session_state.filtered_image = None

# واجهة المستخدم الرئيسية
st.title("Kama Programming Language")
st.write("Welcome to the Kama Programming Language!")

# وظيفة لتنفيذ الكود
def execute_code():
    with st.spinner("Executing code..."):
        output = kama_lang.execute(st.session_state.code)
        st.session_state.output = output

# واجهة إدخال الكود وتنفيذه
with st.form("code_form"):
    st.session_state.code = st.text_area("Enter your code here:")
    submitted = st.form_submit_button("Execute")
    if submitted:
         execute_code()
if 'output' in st.session_state:
    st.write("Output:", st.session_state.output)


# عرض واجهات المستخدم المختلفة
resource.resource_management_ui()
big_data.big_data_processing_ui()
cloud.cloud_upload_ui()
models.pretrained_models_ui()
models.model_management_ui()
prediction.prediction_ui()
data_ops.data_shape_ui()
data_ops.data_plot_ui()
data_ops.data_tensor_ui()
data_ops.data_clean_ui()
data_ops.data_transform_ui()
data_ops.data_split_ui()
data_ops.data_group_ui()
text_ops.tokenize_text_ui()
text_ops.remove_stopwords_ui()
text_ops.create_word_embeddings_ui()
text_ops.sentiment_analysis_ui()
image_ops.image_processing_ui()