import oci

from core.environment.environment import OCI_OBJECTSTORAGE_BUCKET_NAME, OCI_OBJECTSTORAGE_BUCKET_NAMESPCE, OCI_TARGET_COMPARTMENT_ID


def createSpeechClient(config_path):

    config = oci.config.from_file(config_path, "DEFAULT")
    return oci.ai_speech.AIServiceSpeechClient(config)

def Transcription(AI_client: oci.ai_speech.AIServiceSpeechClient, objectName):

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
            additional_transcription_formats=["SRT"]
        )
    )

    print(create_transcription_job_response.data)
    return create_transcription_job_response.data.id

def getTrnascriptionJob(AI_client: oci.ai_speech.AIServiceSpeechClient, jobID):
    get_transcription_job_response = AI_client.get_transcription_job(
        transcription_job_id=jobID,
    )

    # Get the data from response
    print(get_transcription_job_response.data.lifecycle_state)

def runSpeechModel(objectName, config_path="~/.oci/config"):
    
    speech_client = createSpeechClient(config_path)
    job_id = Transcription(speech_client, objectName)

    getTrnascriptionJob(speech_client,job_id)



