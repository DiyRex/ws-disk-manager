# from dotenv import load_dotenv
import os
from huaweicloudsdkcore.auth.credentials import BasicCredentials
from huaweicloudsdkevs.v2.evs_client import EvsClient
from huaweicloudsdkevs.v2.region.evs_region import EvsRegion

# load_dotenv()

def create_evs_client():
    credentials = BasicCredentials(os.getenv("HUAWEICLOUD_SDK_AK"), os.getenv("HUAWEICLOUD_SDK_SK"))
    client = EvsClient.new_builder() \
        .with_credentials(credentials) \
        .with_region(EvsRegion.value_of(os.getenv("REGION"))) \
        .build()
    return client
