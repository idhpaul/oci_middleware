import oci

def createLanguageClient(config_path):

    config = oci.config.from_file(config_path, "DEFAULT")
    return oci.ai_language.AIServiceLanguageClient(config)

def TextTranslate(AI_client: oci.ai_language.AIServiceLanguageClient, translation_key, data, source_language_code, target_language_code):


    custom_retry_strategy = oci.retry.RetryStrategyBuilder(
        # Make up to 10 service calls
        max_attempts_check=True,
        max_attempts=10,

        # Don't exceed a total of 600 seconds for all service calls
        total_elapsed_time_check=True,
        total_elapsed_time_seconds=600,

        # Wait 45 seconds between attempts
        retry_max_wait_between_calls_seconds=45,

        # Use 2 seconds as the base number for doing sleep time calculations
        retry_base_sleep_time_seconds=2,

        # Retry on certain service errors:
        #
        #   - 5xx code received for the request
        #   - Any 429 (this is signified by the empty array in the retry config)
        #   - 400s where the code is QuotaExceeded or LimitExceeded
        service_error_check=True,
        service_error_retry_on_any_5xx=True,
        service_error_retry_config={
            400: ['QuotaExceeded', 'LimitExceeded'],
            429: []
        },

        # Use exponential backoff and retry with full jitter, but on throttles use
        # exponential backoff and retry with equal jitter
        backoff_type=oci.retry.BACKOFF_FULL_JITTER_EQUAL_ON_THROTTLE_VALUE
    ).get_retry_strategy()

    batch_language_translation_response:oci.ai_language.models.BatchLanguageTranslationResult = AI_client.batch_language_translation(
        batch_language_translation_details=oci.ai_language.models.BatchLanguageTranslationDetails(
            documents=[
                oci.ai_language.models.TextDocument(
                    key=translation_key,
                    text=data,
                    language_code=source_language_code)
            ],
            target_language_code=target_language_code),
        retry_strategy = custom_retry_strategy,
        )

    return batch_language_translation_response.data.documents[0].translated_text

def runLanguageModel(data, source_language_code, target_language_code, config_path="~/.oci/config", text_model_key="default_key"):
    
    language_client = createLanguageClient(config_path)
    return TextTranslate(language_client,text_model_key, data, source_language_code, target_language_code)

