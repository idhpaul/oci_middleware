import oci

from core.environment import OCI_OBJECTSTORAGE_BUCKET_NAME, OCI_OBJECTSTORAGE_BUCKET_NAMESPCE, OCI_TARGET_COMPARTMENT_ID


def createSpeechClient(config_path):

    config = oci.config.from_file(config_path, "DEFAULT")
    return oci.ai_speech.AIServiceSpeechClient(config)

def Transcription(AI_client: oci.ai_speech.AIServiceSpeechClient, objectName):

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

    create_transcription_job_response = AI_client.create_transcription_job(
        create_transcription_job_details=oci.ai_speech.models.CreateTranscriptionJobDetails(
            compartment_id=OCI_TARGET_COMPARTMENT_ID,
            input_location=oci.ai_speech.models.ObjectListInlineInputLocation(
                location_type="OBJECT_LIST_INLINE_INPUT_LOCATION",
                object_locations=[
                    oci.ai_speech.models.ObjectLocation(
                        namespace_name=OCI_OBJECTSTORAGE_BUCKET_NAMESPCE,
                        bucket_name=OCI_OBJECTSTORAGE_BUCKET_NAME,
                        object_names=[objectName])]),
            output_location=oci.ai_speech.models.OutputLocation(
                namespace_name=OCI_OBJECTSTORAGE_BUCKET_NAMESPCE,
                bucket_name=OCI_OBJECTSTORAGE_BUCKET_NAME,
                prefix="Output"),
            additional_transcription_formats=["SRT"],
        ),
        retry_strategy=custom_retry_strategy
    )

    print(create_transcription_job_response.data)
    return create_transcription_job_response.data.id

def getTrnascriptionJob(jobID):

    speech_client = createSpeechClient("~/.oci/config")

    get_transcription_job_response = speech_client.get_transcription_job(
        transcription_job_id=jobID,
    )

    # Get the data from response
    print(get_transcription_job_response.data.lifecycle_state)
    return get_transcription_job_response.data.lifecycle_state

def runSpeechModel(objectName, config_path="~/.oci/config"):
    
    speech_client = createSpeechClient(config_path)
    job_id = Transcription(speech_client, objectName)

    #getTrnascriptionJob(speech_client,job_id)
    return job_id



