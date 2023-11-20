import oci

def createLanguageClient(config_path):

    config = oci.config.from_file(config_path, "DEFAULT")
    return oci.ai_language.AIServiceLanguageClient(config)

def TextTranslate(AI_client: oci.ai_language.AIServiceLanguageClient, translation_key, data, source_language_code, target_language_code):

    batch_language_translation_response:oci.ai_language.models.BatchLanguageTranslationResult = AI_client.batch_language_translation(
        batch_language_translation_details=oci.ai_language.models.BatchLanguageTranslationDetails(
            documents=[
                oci.ai_language.models.TextDocument(
                    key=translation_key,
                    text=data,
                    language_code=source_language_code)
            ],
            target_language_code=target_language_code),
        )

    return batch_language_translation_response.data.documents[0].translated_text

def runLanguageModel(data, source_language_code, target_language_code, config_path="~/.oci/config", text_model_key="default_key"):
    
    language_client = createLanguageClient(config_path)
    return TextTranslate(language_client,text_model_key, data, source_language_code, target_language_code)

