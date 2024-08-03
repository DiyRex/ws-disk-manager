from modules.hc_client import create_evs_client
from huaweicloudsdkevs.v2 import ListVolumesRequest
from huaweicloudsdkcore.exceptions import exceptions

def get_volumes(partial_volume_id=None):
    client = create_evs_client()

    try:
        request = ListVolumesRequest()
        response = client.list_volumes(request)
        volumes = response.to_dict().get('volumes', [])
        if partial_volume_id:
            for volume in volumes:
                if partial_volume_id in volume['id']:
                    return volume
            return None
        else:
            return volumes

    except exceptions.ClientRequestException as e:
        print(f"Status Code: {e.status_code}")
        print(f"Request ID: {e.request_id}")
        print(f"Error Code: {e.error_code}")
        print(f"Error Message: {e.error_msg}")
        return []
