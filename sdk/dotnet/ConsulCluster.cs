// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Hcp
{
    /// <summary>
    /// The Consul cluster resource allows you to manage an HCP Consul cluster.
    /// 
    /// ## Example Usage
    /// 
    /// ```csharp
    /// using Pulumi;
    /// using Hcp = Pulumi.Hcp;
    /// 
    /// class MyStack : Stack
    /// {
    ///     public MyStack()
    ///     {
    ///         var exampleHvn = new Hcp.Hvn("exampleHvn", new Hcp.HvnArgs
    ///         {
    ///             HvnId = "hvn",
    ///             CloudProvider = "aws",
    ///             Region = "us-west-2",
    ///             CidrBlock = "172.25.16.0/20",
    ///         });
    ///         var exampleConsulCluster = new Hcp.ConsulCluster("exampleConsulCluster", new Hcp.ConsulClusterArgs
    ///         {
    ///             ClusterId = "consul-cluster",
    ///             HvnId = exampleHvn.HvnId,
    ///             Tier = "development",
    ///         });
    ///     }
    /// 
    /// }
    /// ```
    /// 
    /// ## Import
    /// 
    /// # The import ID is {cluster_id}
    /// 
    /// ```sh
    ///  $ pulumi import hcp:index/consulCluster:ConsulCluster example consul-cluster
    /// ```
    /// </summary>
    [HcpResourceType("hcp:index/consulCluster:ConsulCluster")]
    public partial class ConsulCluster : Pulumi.CustomResource
    {
        /// <summary>
        /// Enables automatic HVN to HVN peering when creating a secondary cluster in a federation. The alternative to using the auto-accept feature is to create an `hcp.HvnPeeringConnection` resource that explicitly defines the HVN resources that are allowed to communicate with each other.
        /// </summary>
        [Output("autoHvnToHvnPeering")]
        public Output<bool> AutoHvnToHvnPeering { get; private set; } = null!;

        /// <summary>
        /// The provider where the HCP Consul cluster is located.
        /// </summary>
        [Output("cloudProvider")]
        public Output<string> CloudProvider { get; private set; } = null!;

        /// <summary>
        /// The ID of the HCP Consul cluster.
        /// </summary>
        [Output("clusterId")]
        public Output<string> ClusterId { get; private set; } = null!;

        /// <summary>
        /// Denotes the Consul connect feature should be enabled for this cluster.  Default to true.
        /// </summary>
        [Output("connectEnabled")]
        public Output<bool?> ConnectEnabled { get; private set; } = null!;

        /// <summary>
        /// Denotes that automatic Consul upgrades are enabled.
        /// </summary>
        [Output("consulAutomaticUpgrades")]
        public Output<bool> ConsulAutomaticUpgrades { get; private set; } = null!;

        /// <summary>
        /// The cluster CA file encoded as a Base64 string.
        /// </summary>
        [Output("consulCaFile")]
        public Output<string> ConsulCaFile { get; private set; } = null!;

        /// <summary>
        /// The cluster config encoded as a Base64 string.
        /// </summary>
        [Output("consulConfigFile")]
        public Output<string> ConsulConfigFile { get; private set; } = null!;

        /// <summary>
        /// The private URL for the Consul UI.
        /// </summary>
        [Output("consulPrivateEndpointUrl")]
        public Output<string> ConsulPrivateEndpointUrl { get; private set; } = null!;

        /// <summary>
        /// The public URL for the Consul UI. This will be empty if `public_endpoint` is `false`.
        /// </summary>
        [Output("consulPublicEndpointUrl")]
        public Output<string> ConsulPublicEndpointUrl { get; private set; } = null!;

        /// <summary>
        /// The accessor ID of the root ACL token that is generated upon cluster creation. If a new root token is generated using the `hcp_consul_root_token` resource, this field is no longer valid.
        /// </summary>
        [Output("consulRootTokenAccessorId")]
        public Output<string> ConsulRootTokenAccessorId { get; private set; } = null!;

        /// <summary>
        /// The secret ID of the root ACL token that is generated upon cluster creation. If a new root token is generated using the `hcp_consul_root_token` resource, this field is no longer valid.
        /// </summary>
        [Output("consulRootTokenSecretId")]
        public Output<string> ConsulRootTokenSecretId { get; private set; } = null!;

        /// <summary>
        /// The Consul snapshot interval.
        /// </summary>
        [Output("consulSnapshotInterval")]
        public Output<string> ConsulSnapshotInterval { get; private set; } = null!;

        /// <summary>
        /// The retention policy for Consul snapshots.
        /// </summary>
        [Output("consulSnapshotRetention")]
        public Output<string> ConsulSnapshotRetention { get; private set; } = null!;

        /// <summary>
        /// The Consul version of the cluster.
        /// </summary>
        [Output("consulVersion")]
        public Output<string> ConsulVersion { get; private set; } = null!;

        /// <summary>
        /// The Consul data center name of the cluster. If not specified, it is defaulted to the value of `cluster_id`.
        /// </summary>
        [Output("datacenter")]
        public Output<string> Datacenter { get; private set; } = null!;

        /// <summary>
        /// The ID of the HVN this HCP Consul cluster is associated to.
        /// </summary>
        [Output("hvnId")]
        public Output<string> HvnId { get; private set; } = null!;

        /// <summary>
        /// The minimum Consul version of the cluster. If not specified, it is defaulted to the version that is currently recommended by HCP.
        /// </summary>
        [Output("minConsulVersion")]
        public Output<string?> MinConsulVersion { get; private set; } = null!;

        /// <summary>
        /// The ID of the organization this HCP Consul cluster is located in.
        /// </summary>
        [Output("organizationId")]
        public Output<string> OrganizationId { get; private set; } = null!;

        /// <summary>
        /// The `self_link` of the HCP Consul cluster which is the primary in the federation setup with this HCP Consul cluster. If not specified, it is a standalone cluster.
        /// </summary>
        [Output("primaryLink")]
        public Output<string?> PrimaryLink { get; private set; } = null!;

        /// <summary>
        /// The ID of the project this HCP Consul cluster is located in.
        /// </summary>
        [Output("projectId")]
        public Output<string> ProjectId { get; private set; } = null!;

        /// <summary>
        /// Denotes that the cluster has a public endpoint for the Consul UI. Defaults to false.
        /// </summary>
        [Output("publicEndpoint")]
        public Output<bool?> PublicEndpoint { get; private set; } = null!;

        /// <summary>
        /// The region where the HCP Consul cluster is located.
        /// </summary>
        [Output("region")]
        public Output<string> Region { get; private set; } = null!;

        /// <summary>
        /// The number of Consul server nodes in the cluster.
        /// </summary>
        [Output("scale")]
        public Output<int> Scale { get; private set; } = null!;

        /// <summary>
        /// A unique URL identifying the HCP Consul cluster.
        /// </summary>
        [Output("selfLink")]
        public Output<string> SelfLink { get; private set; } = null!;

        /// <summary>
        /// The t-shirt size representation of each server VM that this Consul cluster is provisioned with. Valid option for development tier - `x_small`. Valid options for other tiers - `small`, `medium`, `large`. For more details - https://cloud.hashicorp.com/pricing/consul. Upgrading the size of a cluster after creation is allowed.
        /// </summary>
        [Output("size")]
        public Output<string> Size { get; private set; } = null!;

        /// <summary>
        /// The tier that the HCP Consul cluster will be provisioned as.  Only `development`, `standard` and `plus` are available at this time. See [pricing information](https://cloud.hashicorp.com/pricing/consul).
        /// </summary>
        [Output("tier")]
        public Output<string> Tier { get; private set; } = null!;


        /// <summary>
        /// Create a ConsulCluster resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public ConsulCluster(string name, ConsulClusterArgs args, CustomResourceOptions? options = null)
            : base("hcp:index/consulCluster:ConsulCluster", name, args ?? new ConsulClusterArgs(), MakeResourceOptions(options, ""))
        {
        }

        private ConsulCluster(string name, Input<string> id, ConsulClusterState? state = null, CustomResourceOptions? options = null)
            : base("hcp:index/consulCluster:ConsulCluster", name, state, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing ConsulCluster resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static ConsulCluster Get(string name, Input<string> id, ConsulClusterState? state = null, CustomResourceOptions? options = null)
        {
            return new ConsulCluster(name, id, state, options);
        }
    }

    public sealed class ConsulClusterArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// Enables automatic HVN to HVN peering when creating a secondary cluster in a federation. The alternative to using the auto-accept feature is to create an `hcp.HvnPeeringConnection` resource that explicitly defines the HVN resources that are allowed to communicate with each other.
        /// </summary>
        [Input("autoHvnToHvnPeering")]
        public Input<bool>? AutoHvnToHvnPeering { get; set; }

        /// <summary>
        /// The ID of the HCP Consul cluster.
        /// </summary>
        [Input("clusterId", required: true)]
        public Input<string> ClusterId { get; set; } = null!;

        /// <summary>
        /// Denotes the Consul connect feature should be enabled for this cluster.  Default to true.
        /// </summary>
        [Input("connectEnabled")]
        public Input<bool>? ConnectEnabled { get; set; }

        /// <summary>
        /// The Consul data center name of the cluster. If not specified, it is defaulted to the value of `cluster_id`.
        /// </summary>
        [Input("datacenter")]
        public Input<string>? Datacenter { get; set; }

        /// <summary>
        /// The ID of the HVN this HCP Consul cluster is associated to.
        /// </summary>
        [Input("hvnId", required: true)]
        public Input<string> HvnId { get; set; } = null!;

        /// <summary>
        /// The minimum Consul version of the cluster. If not specified, it is defaulted to the version that is currently recommended by HCP.
        /// </summary>
        [Input("minConsulVersion")]
        public Input<string>? MinConsulVersion { get; set; }

        /// <summary>
        /// The `self_link` of the HCP Consul cluster which is the primary in the federation setup with this HCP Consul cluster. If not specified, it is a standalone cluster.
        /// </summary>
        [Input("primaryLink")]
        public Input<string>? PrimaryLink { get; set; }

        /// <summary>
        /// Denotes that the cluster has a public endpoint for the Consul UI. Defaults to false.
        /// </summary>
        [Input("publicEndpoint")]
        public Input<bool>? PublicEndpoint { get; set; }

        /// <summary>
        /// The t-shirt size representation of each server VM that this Consul cluster is provisioned with. Valid option for development tier - `x_small`. Valid options for other tiers - `small`, `medium`, `large`. For more details - https://cloud.hashicorp.com/pricing/consul. Upgrading the size of a cluster after creation is allowed.
        /// </summary>
        [Input("size")]
        public Input<string>? Size { get; set; }

        /// <summary>
        /// The tier that the HCP Consul cluster will be provisioned as.  Only `development`, `standard` and `plus` are available at this time. See [pricing information](https://cloud.hashicorp.com/pricing/consul).
        /// </summary>
        [Input("tier", required: true)]
        public Input<string> Tier { get; set; } = null!;

        public ConsulClusterArgs()
        {
        }
    }

    public sealed class ConsulClusterState : Pulumi.ResourceArgs
    {
        /// <summary>
        /// Enables automatic HVN to HVN peering when creating a secondary cluster in a federation. The alternative to using the auto-accept feature is to create an `hcp.HvnPeeringConnection` resource that explicitly defines the HVN resources that are allowed to communicate with each other.
        /// </summary>
        [Input("autoHvnToHvnPeering")]
        public Input<bool>? AutoHvnToHvnPeering { get; set; }

        /// <summary>
        /// The provider where the HCP Consul cluster is located.
        /// </summary>
        [Input("cloudProvider")]
        public Input<string>? CloudProvider { get; set; }

        /// <summary>
        /// The ID of the HCP Consul cluster.
        /// </summary>
        [Input("clusterId")]
        public Input<string>? ClusterId { get; set; }

        /// <summary>
        /// Denotes the Consul connect feature should be enabled for this cluster.  Default to true.
        /// </summary>
        [Input("connectEnabled")]
        public Input<bool>? ConnectEnabled { get; set; }

        /// <summary>
        /// Denotes that automatic Consul upgrades are enabled.
        /// </summary>
        [Input("consulAutomaticUpgrades")]
        public Input<bool>? ConsulAutomaticUpgrades { get; set; }

        /// <summary>
        /// The cluster CA file encoded as a Base64 string.
        /// </summary>
        [Input("consulCaFile")]
        public Input<string>? ConsulCaFile { get; set; }

        /// <summary>
        /// The cluster config encoded as a Base64 string.
        /// </summary>
        [Input("consulConfigFile")]
        public Input<string>? ConsulConfigFile { get; set; }

        /// <summary>
        /// The private URL for the Consul UI.
        /// </summary>
        [Input("consulPrivateEndpointUrl")]
        public Input<string>? ConsulPrivateEndpointUrl { get; set; }

        /// <summary>
        /// The public URL for the Consul UI. This will be empty if `public_endpoint` is `false`.
        /// </summary>
        [Input("consulPublicEndpointUrl")]
        public Input<string>? ConsulPublicEndpointUrl { get; set; }

        /// <summary>
        /// The accessor ID of the root ACL token that is generated upon cluster creation. If a new root token is generated using the `hcp_consul_root_token` resource, this field is no longer valid.
        /// </summary>
        [Input("consulRootTokenAccessorId")]
        public Input<string>? ConsulRootTokenAccessorId { get; set; }

        /// <summary>
        /// The secret ID of the root ACL token that is generated upon cluster creation. If a new root token is generated using the `hcp_consul_root_token` resource, this field is no longer valid.
        /// </summary>
        [Input("consulRootTokenSecretId")]
        public Input<string>? ConsulRootTokenSecretId { get; set; }

        /// <summary>
        /// The Consul snapshot interval.
        /// </summary>
        [Input("consulSnapshotInterval")]
        public Input<string>? ConsulSnapshotInterval { get; set; }

        /// <summary>
        /// The retention policy for Consul snapshots.
        /// </summary>
        [Input("consulSnapshotRetention")]
        public Input<string>? ConsulSnapshotRetention { get; set; }

        /// <summary>
        /// The Consul version of the cluster.
        /// </summary>
        [Input("consulVersion")]
        public Input<string>? ConsulVersion { get; set; }

        /// <summary>
        /// The Consul data center name of the cluster. If not specified, it is defaulted to the value of `cluster_id`.
        /// </summary>
        [Input("datacenter")]
        public Input<string>? Datacenter { get; set; }

        /// <summary>
        /// The ID of the HVN this HCP Consul cluster is associated to.
        /// </summary>
        [Input("hvnId")]
        public Input<string>? HvnId { get; set; }

        /// <summary>
        /// The minimum Consul version of the cluster. If not specified, it is defaulted to the version that is currently recommended by HCP.
        /// </summary>
        [Input("minConsulVersion")]
        public Input<string>? MinConsulVersion { get; set; }

        /// <summary>
        /// The ID of the organization this HCP Consul cluster is located in.
        /// </summary>
        [Input("organizationId")]
        public Input<string>? OrganizationId { get; set; }

        /// <summary>
        /// The `self_link` of the HCP Consul cluster which is the primary in the federation setup with this HCP Consul cluster. If not specified, it is a standalone cluster.
        /// </summary>
        [Input("primaryLink")]
        public Input<string>? PrimaryLink { get; set; }

        /// <summary>
        /// The ID of the project this HCP Consul cluster is located in.
        /// </summary>
        [Input("projectId")]
        public Input<string>? ProjectId { get; set; }

        /// <summary>
        /// Denotes that the cluster has a public endpoint for the Consul UI. Defaults to false.
        /// </summary>
        [Input("publicEndpoint")]
        public Input<bool>? PublicEndpoint { get; set; }

        /// <summary>
        /// The region where the HCP Consul cluster is located.
        /// </summary>
        [Input("region")]
        public Input<string>? Region { get; set; }

        /// <summary>
        /// The number of Consul server nodes in the cluster.
        /// </summary>
        [Input("scale")]
        public Input<int>? Scale { get; set; }

        /// <summary>
        /// A unique URL identifying the HCP Consul cluster.
        /// </summary>
        [Input("selfLink")]
        public Input<string>? SelfLink { get; set; }

        /// <summary>
        /// The t-shirt size representation of each server VM that this Consul cluster is provisioned with. Valid option for development tier - `x_small`. Valid options for other tiers - `small`, `medium`, `large`. For more details - https://cloud.hashicorp.com/pricing/consul. Upgrading the size of a cluster after creation is allowed.
        /// </summary>
        [Input("size")]
        public Input<string>? Size { get; set; }

        /// <summary>
        /// The tier that the HCP Consul cluster will be provisioned as.  Only `development`, `standard` and `plus` are available at this time. See [pricing information](https://cloud.hashicorp.com/pricing/consul).
        /// </summary>
        [Input("tier")]
        public Input<string>? Tier { get; set; }

        public ConsulClusterState()
        {
        }
    }
}