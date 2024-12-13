# kama/__init__.py

import logging
from .core.kama import Kama

# محاولة استيراد الأوامر من commands.py
try:
    from .commands.data import (
        load_data,
        load_large_data,
        process_large_data,
        get_data_shape,
        plot_data,
        convert_to_tensor,
        clean_data,
        transform_data,
        split_data,
        group_data
    )
    from .commands.models import (
         train_model,
         evaluate_model,
         train_dnn,
         train_traditional_model,
         tune_model,
         save_model,
         load_model,
         predict
    )
    from .commands.cloud import (
         upload_to_gcloud,
        upload_to_aws
    )
    from .commands.text import (
        tokenize_text,
        remove_stopwords,
        create_word_embeddings,
        sentiment_analysis
    )
    from .commands.image import (
         load_image,
         resize_image,
         apply_filter,
         detect_objects
    )
    commands_loaded = True
except ImportError as e:
    logging.error(f"Error importing commands: {str(e)}")
    commands_loaded = False

# تهيئة الكائن الرئيسي للغة
kama_lang = Kama()

# إضافة الأوامر إلى السياق إذا تم تحميلها بنجاح
if commands_loaded:
    command_list = {
        'load_data': load_data,
        'load_large_data': load_large_data,
        'process_large_data': process_large_data,
        'get_data_shape': get_data_shape,
        'plot_data': plot_data,
        'convert_to_tensor': convert_to_tensor,
        'clean_data': clean_data,
        'transform_data': transform_data,
        'split_data': split_data,
        'group_data': group_data,
        'train_model': train_model,
        'evaluate_model': evaluate_model,
        'train_dnn': train_dnn,
        'train_traditional_model': train_traditional_model,
        'tune_model': tune_model,
        'save_model': save_model,
        'load_model': load_model,
        'predict': predict,
         'upload_to_gcloud': upload_to_gcloud,
        'upload_to_aws': upload_to_aws,
         'tokenize_text': tokenize_text,
        'remove_stopwords': remove_stopwords,
        'create_word_embeddings': create_word_embeddings,
        'sentiment_analysis': sentiment_analysis,
        'load_image': load_image,
        'resize_image': resize_image,
        'apply_filter': apply_filter,
        'detect_objects': detect_objects
    }

    # إضافة الأوامر للسياق
    for cmd_name, cmd_func in command_list.items():
        kama_lang.context[cmd_name] = cmd_func

    print("Commands loaded successfully!")

else:
    print("Commands loading failed. Please check the installation.")