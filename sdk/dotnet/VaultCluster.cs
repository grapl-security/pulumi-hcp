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
    /// The Vault cluster resource allows you to manage an HCP Vault cluster.
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
    ///         var exampleVaultCluster = new Hcp.VaultCluster("exampleVaultCluster", new Hcp.VaultClusterArgs
    ///         {
    ///             ClusterId = "vault-cluster",
    ///             HvnId = exampleHvn.HvnId,
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
    ///  $ pulumi import hcp:index/vaultCluster:VaultCluster example vault-cluster
    /// ```
    /// </summary>
    [HcpResourceType("hcp:index/vaultCluster:VaultCluster")]
    public partial class VaultCluster : Pulumi.CustomResource
    {
        /// <summary>
        /// The provider where the HCP Vault cluster is located.
        /// </summary>
        [Output("cloudProvider")]
        public Output<string> CloudProvider { get; private set; } = null!;

        /// <summary>
        /// The ID of the HCP Vault cluster.
        /// </summary>
        [Output("clusterId")]
        public Output<string> ClusterId { get; private set; } = null!;

        /// <summary>
        /// The time that the Vault cluster was created.
        /// </summary>
        [Output("createdAt")]
        public Output<string> CreatedAt { get; private set; } = null!;

        /// <summary>
        /// The ID of the HVN this HCP Vault cluster is associated to.
        /// </summary>
        [Output("hvnId")]
        public Output<string> HvnId { get; private set; } = null!;

        /// <summary>
        /// The minimum Vault version to use when creating the cluster. If not specified, it is defaulted to the version that is currently recommended by HCP.
        /// </summary>
        [Output("minVaultVersion")]
        public Output<string?> MinVaultVersion { get; private set; } = null!;

        /// <summary>
        /// The name of the customer namespace this HCP Vault cluster is located in.
        /// </summary>
        [Output("namespace")]
        public Output<string> Namespace { get; private set; } = null!;

        /// <summary>
        /// The ID of the organization this HCP Vault cluster is located in.
        /// </summary>
        [Output("organizationId")]
        public Output<string> OrganizationId { get; private set; } = null!;

        /// <summary>
        /// The ID of the project this HCP Vault cluster is located in.
        /// </summary>
        [Output("projectId")]
        public Output<string> ProjectId { get; private set; } = null!;

        /// <summary>
        /// Denotes that the cluster has a public endpoint. Defaults to false.
        /// </summary>
        [Output("publicEndpoint")]
        public Output<bool?> PublicEndpoint { get; private set; } = null!;

        /// <summary>
        /// The region where the HCP Vault cluster is located.
        /// </summary>
        [Output("region")]
        public Output<string> Region { get; private set; } = null!;

        /// <summary>
        /// Tier of the HCP Vault cluster. Valid options for tiers - `dev`, `standard_small`, `standard_medium`, `standard_large`, `starter_small`. See [pricing information](https://cloud.hashicorp.com/pricing/vault).
        /// </summary>
        [Output("tier")]
        public Output<string> Tier { get; private set; } = null!;

        /// <summary>
        /// The private URL for the Vault cluster.
        /// </summary>
        [Output("vaultPrivateEndpointUrl")]
        public Output<string> VaultPrivateEndpointUrl { get; private set; } = null!;

        /// <summary>
        /// The public URL for the Vault cluster. This will be empty if `public_endpoint` is `false`.
        /// </summary>
        [Output("vaultPublicEndpointUrl")]
        public Output<string> VaultPublicEndpointUrl { get; private set; } = null!;

        /// <summary>
        /// The Vault version of the cluster.
        /// </summary>
        [Output("vaultVersion")]
        public Output<string> VaultVersion { get; private set; } = null!;


        /// <summary>
        /// Create a VaultCluster resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public VaultCluster(string name, VaultClusterArgs args, CustomResourceOptions? options = null)
            : base("hcp:index/vaultCluster:VaultCluster", name, args ?? new VaultClusterArgs(), MakeResourceOptions(options, ""))
        {
        }

        private VaultCluster(string name, Input<string> id, VaultClusterState? state = null, CustomResourceOptions? options = null)
            : base("hcp:index/vaultCluster:VaultCluster", name, state, MakeResourceOptions(options, id))
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
        /// Get an existing VaultCluster resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static VaultCluster Get(string name, Input<string> id, VaultClusterState? state = null, CustomResourceOptions? options = null)
        {
            return new VaultCluster(name, id, state, options);
        }
    }

    public sealed class VaultClusterArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The ID of the HCP Vault cluster.
        /// </summary>
        [Input("clusterId", required: true)]
        public Input<string> ClusterId { get; set; } = null!;

        /// <summary>
        /// The ID of the HVN this HCP Vault cluster is associated to.
        /// </summary>
        [Input("hvnId", required: true)]
        public Input<string> HvnId { get; set; } = null!;

        /// <summary>
        /// The minimum Vault version to use when creating the cluster. If not specified, it is defaulted to the version that is currently recommended by HCP.
        /// </summary>
        [Input("minVaultVersion")]
        public Input<string>? MinVaultVersion { get; set; }

        /// <summary>
        /// Denotes that the cluster has a public endpoint. Defaults to false.
        /// </summary>
        [Input("publicEndpoint")]
        public Input<bool>? PublicEndpoint { get; set; }

        /// <summary>
        /// Tier of the HCP Vault cluster. Valid options for tiers - `dev`, `standard_small`, `standard_medium`, `standard_large`, `starter_small`. See [pricing information](https://cloud.hashicorp.com/pricing/vault).
        /// </summary>
        [Input("tier")]
        public Input<string>? Tier { get; set; }

        public VaultClusterArgs()
        {
        }
    }

    public sealed class VaultClusterState : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The provider where the HCP Vault cluster is located.
        /// </summary>
        [Input("cloudProvider")]
        public Input<string>? CloudProvider { get; set; }

        /// <summary>
        /// The ID of the HCP Vault cluster.
        /// </summary>
        [Input("clusterId")]
        public Input<string>? ClusterId { get; set; }

        /// <summary>
        /// The time that the Vault cluster was created.
        /// </summary>
        [Input("createdAt")]
        public Input<string>? CreatedAt { get; set; }

        /// <summary>
        /// The ID of the HVN this HCP Vault cluster is associated to.
        /// </summary>
        [Input("hvnId")]
        public Input<string>? HvnId { get; set; }

        /// <summary>
        /// The minimum Vault version to use when creating the cluster. If not specified, it is defaulted to the version that is currently recommended by HCP.
        /// </summary>
        [Input("minVaultVersion")]
        public Input<string>? MinVaultVersion { get; set; }

        /// <summary>
        /// The name of the customer namespace this HCP Vault cluster is located in.
        /// </summary>
        [Input("namespace")]
        public Input<string>? Namespace { get; set; }

        /// <summary>
        /// The ID of the organization this HCP Vault cluster is located in.
        /// </summary>
        [Input("organizationId")]
        public Input<string>? OrganizationId { get; set; }

        /// <summary>
        /// The ID of the project this HCP Vault cluster is located in.
        /// </summary>
        [Input("projectId")]
        public Input<string>? ProjectId { get; set; }

        /// <summary>
        /// Denotes that the cluster has a public endpoint. Defaults to false.
        /// </summary>
        [Input("publicEndpoint")]
        public Input<bool>? PublicEndpoint { get; set; }

        /// <summary>
        /// The region where the HCP Vault cluster is located.
        /// </summary>
        [Input("region")]
        public Input<string>? Region { get; set; }

        /// <summary>
        /// Tier of the HCP Vault cluster. Valid options for tiers - `dev`, `standard_small`, `standard_medium`, `standard_large`, `starter_small`. See [pricing information](https://cloud.hashicorp.com/pricing/vault).
        /// </summary>
        [Input("tier")]
        public Input<string>? Tier { get; set; }

        /// <summary>
        /// The private URL for the Vault cluster.
        /// </summary>
        [Input("vaultPrivateEndpointUrl")]
        public Input<string>? VaultPrivateEndpointUrl { get; set; }

        /// <summary>
        /// The public URL for the Vault cluster. This will be empty if `public_endpoint` is `false`.
        /// </summary>
        [Input("vaultPublicEndpointUrl")]
        public Input<string>? VaultPublicEndpointUrl { get; set; }

        /// <summary>
        /// The Vault version of the cluster.
        /// </summary>
        [Input("vaultVersion")]
        public Input<string>? VaultVersion { get; set; }

        public VaultClusterState()
        {
        }
    }
}