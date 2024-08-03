from modules.hc_client import create_evs_client
from huaweicloudsdkevs.v2 import ResizeVolumeRequest, ResizeVolumeRequestBody, OsExtend, BssParamForResizeVolume
from huaweicloudsdkcore.exceptions import exceptions

def extend_volume(volume_id=None, new_size=None):
    client = create_evs_client()

    try:
        os_extend = OsExtend(new_size=new_size)
        bss_param = BssParamForResizeVolume()
        request_body = ResizeVolumeRequestBody(os_extend=os_extend, bss_param=bss_param)
        request = ResizeVolumeRequest(volume_id=volume_id, body=request_body)
        response = client.resize_volume(request)
        
        # Check if the response contains a job_id (assuming job_id is a direct attribute)
        if hasattr(response, 'job_id') and response.job_id:
            return True
        else:
            return False
        
    except exceptions.ClientRequestException as e:
        print(f"Status Code: {e.status_code}")
        print(f"Request ID: {e.request_id}")
        print(f"Error Code: {e.error_code}")
        print(f"Error Message: {e.error_msg}")
        return False
