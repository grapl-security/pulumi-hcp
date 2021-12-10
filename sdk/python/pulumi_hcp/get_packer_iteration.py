# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = [
    'GetPackerIterationResult',
    'AwaitableGetPackerIterationResult',
    'get_packer_iteration',
    'get_packer_iteration_output',
]

@pulumi.output_type
class GetPackerIterationResult:
    """
    A collection of values returned by getPackerIteration.
    """
    def __init__(__self__, author_id=None, bucket_name=None, channel=None, created_at=None, fingerprint=None, id=None, incremental_version=None, organization_id=None, project_id=None, ulid=None, updated_at=None):
        if author_id and not isinstance(author_id, str):
            raise TypeError("Expected argument 'author_id' to be a str")
        pulumi.set(__self__, "author_id", author_id)
        if bucket_name and not isinstance(bucket_name, str):
            raise TypeError("Expected argument 'bucket_name' to be a str")
        pulumi.set(__self__, "bucket_name", bucket_name)
        if channel and not isinstance(channel, str):
            raise TypeError("Expected argument 'channel' to be a str")
        pulumi.set(__self__, "channel", channel)
        if created_at and not isinstance(created_at, str):
            raise TypeError("Expected argument 'created_at' to be a str")
        pulumi.set(__self__, "created_at", created_at)
        if fingerprint and not isinstance(fingerprint, str):
            raise TypeError("Expected argument 'fingerprint' to be a str")
        pulumi.set(__self__, "fingerprint", fingerprint)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if incremental_version and not isinstance(incremental_version, int):
            raise TypeError("Expected argument 'incremental_version' to be a int")
        pulumi.set(__self__, "incremental_version", incremental_version)
        if organization_id and not isinstance(organization_id, str):
            raise TypeError("Expected argument 'organization_id' to be a str")
        pulumi.set(__self__, "organization_id", organization_id)
        if project_id and not isinstance(project_id, str):
            raise TypeError("Expected argument 'project_id' to be a str")
        pulumi.set(__self__, "project_id", project_id)
        if ulid and not isinstance(ulid, str):
            raise TypeError("Expected argument 'ulid' to be a str")
        pulumi.set(__self__, "ulid", ulid)
        if updated_at and not isinstance(updated_at, str):
            raise TypeError("Expected argument 'updated_at' to be a str")
        pulumi.set(__self__, "updated_at", updated_at)

    @property
    @pulumi.getter(name="authorId")
    def author_id(self) -> str:
        """
        The name of the person who created this iteration.
        """
        return pulumi.get(self, "author_id")

    @property
    @pulumi.getter(name="bucketName")
    def bucket_name(self) -> str:
        """
        The slug of the HCP Packer Registry image bucket to pull from.
        """
        return pulumi.get(self, "bucket_name")

    @property
    @pulumi.getter
    def channel(self) -> str:
        """
        The channel that points to the version of the image you want.
        """
        return pulumi.get(self, "channel")

    @property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> str:
        """
        Creation time of this iteration
        """
        return pulumi.get(self, "created_at")

    @property
    @pulumi.getter
    def fingerprint(self) -> str:
        """
        The unique fingerprint associated with this iteration; often a git sha.
        """
        return pulumi.get(self, "fingerprint")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="incrementalVersion")
    def incremental_version(self) -> int:
        """
        Incremental version of this iteration
        """
        return pulumi.get(self, "incremental_version")

    @property
    @pulumi.getter(name="organizationId")
    def organization_id(self) -> str:
        """
        The ID of the organization this HCP Packer registry is located in.
        """
        return pulumi.get(self, "organization_id")

    @property
    @pulumi.getter(name="projectId")
    def project_id(self) -> str:
        """
        The ID of the project this HCP Packer registry is located in.
        """
        return pulumi.get(self, "project_id")

    @property
    @pulumi.getter
    def ulid(self) -> str:
        """
        The ULID of this iteration.
        """
        return pulumi.get(self, "ulid")

    @property
    @pulumi.getter(name="updatedAt")
    def updated_at(self) -> str:
        """
        Time this build was last updated.
        """
        return pulumi.get(self, "updated_at")


class AwaitableGetPackerIterationResult(GetPackerIterationResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetPackerIterationResult(
            author_id=self.author_id,
            bucket_name=self.bucket_name,
            channel=self.channel,
            created_at=self.created_at,
            fingerprint=self.fingerprint,
            id=self.id,
            incremental_version=self.incremental_version,
            organization_id=self.organization_id,
            project_id=self.project_id,
            ulid=self.ulid,
            updated_at=self.updated_at)


def get_packer_iteration(bucket_name: Optional[str] = None,
                         channel: Optional[str] = None,
                         opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetPackerIterationResult:
    """
    > **Note:** This feature is currently in beta.

    The Packer Image data source iteration gets the most recent iteration (or build) of an image, given a channel.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_hcp as hcp

    hardened_source = hcp.get_packer_iteration(bucket_name="hardened-ubuntu-16-04",
        channel="megan-test")
    ```


    :param str bucket_name: The slug of the HCP Packer Registry image bucket to pull from.
    :param str channel: The channel that points to the version of the image you want.
    """
    __args__ = dict()
    __args__['bucketName'] = bucket_name
    __args__['channel'] = channel
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('hcp:index/getPackerIteration:getPackerIteration', __args__, opts=opts, typ=GetPackerIterationResult).value

    return AwaitableGetPackerIterationResult(
        author_id=__ret__.author_id,
        bucket_name=__ret__.bucket_name,
        channel=__ret__.channel,
        created_at=__ret__.created_at,
        fingerprint=__ret__.fingerprint,
        id=__ret__.id,
        incremental_version=__ret__.incremental_version,
        organization_id=__ret__.organization_id,
        project_id=__ret__.project_id,
        ulid=__ret__.ulid,
        updated_at=__ret__.updated_at)


@_utilities.lift_output_func(get_packer_iteration)
def get_packer_iteration_output(bucket_name: Optional[pulumi.Input[str]] = None,
                                channel: Optional[pulumi.Input[str]] = None,
                                opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetPackerIterationResult]:
    """
    > **Note:** This feature is currently in beta.

    The Packer Image data source iteration gets the most recent iteration (or build) of an image, given a channel.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_hcp as hcp

    hardened_source = hcp.get_packer_iteration(bucket_name="hardened-ubuntu-16-04",
        channel="megan-test")
    ```


    :param str bucket_name: The slug of the HCP Packer Registry image bucket to pull from.
    :param str channel: The channel that points to the version of the image you want.
    """
    ...
