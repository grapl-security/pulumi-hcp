// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;
using Pulumi.Utilities;

namespace Pulumi.Hcp
{
    public static class GetHvn
    {
        /// <summary>
        /// The HVN data source provides information about an existing HashiCorp Virtual Network.
        /// 
        /// {{% examples %}}
        /// ## Example Usage
        /// {{% example %}}
        /// 
        /// ```csharp
        /// using Pulumi;
        /// using Hcp = Pulumi.Hcp;
        /// 
        /// class MyStack : Stack
        /// {
        ///     public MyStack()
        ///     {
        ///         var example = Output.Create(Hcp.GetHvn.InvokeAsync(new Hcp.GetHvnArgs
        ///         {
        ///             HvnId = @var.Hvn_id,
        ///         }));
        ///     }
        /// 
        /// }
        /// ```
        /// {{% /example %}}
        /// {{% /examples %}}
        /// </summary>
        public static Task<GetHvnResult> InvokeAsync(GetHvnArgs args, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.InvokeAsync<GetHvnResult>("hcp:index/getHvn:getHvn", args ?? new GetHvnArgs(), options.WithVersion());

        /// <summary>
        /// The HVN data source provides information about an existing HashiCorp Virtual Network.
        /// 
        /// {{% examples %}}
        /// ## Example Usage
        /// {{% example %}}
        /// 
        /// ```csharp
        /// using Pulumi;
        /// using Hcp = Pulumi.Hcp;
        /// 
        /// class MyStack : Stack
        /// {
        ///     public MyStack()
        ///     {
        ///         var example = Output.Create(Hcp.GetHvn.InvokeAsync(new Hcp.GetHvnArgs
        ///         {
        ///             HvnId = @var.Hvn_id,
        ///         }));
        ///     }
        /// 
        /// }
        /// ```
        /// {{% /example %}}
        /// {{% /examples %}}
        /// </summary>
        public static Output<GetHvnResult> Invoke(GetHvnInvokeArgs args, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.Invoke<GetHvnResult>("hcp:index/getHvn:getHvn", args ?? new GetHvnInvokeArgs(), options.WithVersion());
    }


    public sealed class GetHvnArgs : Pulumi.InvokeArgs
    {
        /// <summary>
        /// The ID of the HashiCorp Virtual Network (HVN).
        /// </summary>
        [Input("hvnId", required: true)]
        public string HvnId { get; set; } = null!;

        public GetHvnArgs()
        {
        }
    }

    public sealed class GetHvnInvokeArgs : Pulumi.InvokeArgs
    {
        /// <summary>
        /// The ID of the HashiCorp Virtual Network (HVN).
        /// </summary>
        [Input("hvnId", required: true)]
        public Input<string> HvnId { get; set; } = null!;

        public GetHvnInvokeArgs()
        {
        }
    }


    [OutputType]
    public sealed class GetHvnResult
    {
        /// <summary>
        /// The CIDR range of the HVN.
        /// </summary>
        public readonly string CidrBlock;
        /// <summary>
        /// The provider where the HVN is located.
        /// </summary>
        public readonly string CloudProvider;
        /// <summary>
        /// The time that the HVN was created.
        /// </summary>
        public readonly string CreatedAt;
        /// <summary>
        /// The ID of the HashiCorp Virtual Network (HVN).
        /// </summary>
        public readonly string HvnId;
        /// <summary>
        /// The provider-assigned unique ID for this managed resource.
        /// </summary>
        public readonly string Id;
        /// <summary>
        /// The ID of the HCP organization where the HVN is located.
        /// </summary>
        public readonly string OrganizationId;
        /// <summary>
        /// The ID of the HCP project where the HVN is located.
        /// </summary>
        public readonly string ProjectId;
        /// <summary>
        /// The provider account ID where the HVN is located.
        /// </summary>
        public readonly string ProviderAccountId;
        /// <summary>
        /// The region where the HVN is located.
        /// </summary>
        public readonly string Region;
        /// <summary>
        /// A unique URL identifying the HVN.
        /// </summary>
        public readonly string SelfLink;

        [OutputConstructor]
        private GetHvnResult(
            string cidrBlock,

            string cloudProvider,

            string createdAt,

            string hvnId,

            string id,

            string organizationId,

            string projectId,

            string providerAccountId,

            string region,

            string selfLink)
        {
            CidrBlock = cidrBlock;
            CloudProvider = cloudProvider;
            CreatedAt = createdAt;
            HvnId = hvnId;
            Id = id;
            OrganizationId = organizationId;
            ProjectId = projectId;
            ProviderAccountId = providerAccountId;
            Region = region;
            SelfLink = selfLink;
        }
    }
}