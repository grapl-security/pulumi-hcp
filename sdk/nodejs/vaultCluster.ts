// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

/**
 * The Vault cluster resource allows you to manage an HCP Vault cluster.
 *
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as hcp from "@pulumi/hcp";
 *
 * const exampleHvn = new hcp.Hvn("exampleHvn", {
 *     hvnId: "hvn",
 *     cloudProvider: "aws",
 *     region: "us-west-2",
 *     cidrBlock: "172.25.16.0/20",
 * });
 * const exampleVaultCluster = new hcp.VaultCluster("exampleVaultCluster", {
 *     clusterId: "vault-cluster",
 *     hvnId: exampleHvn.hvnId,
 * });
 * ```
 *
 * ## Import
 *
 * # The import ID is {cluster_id}
 *
 * ```sh
 *  $ pulumi import hcp:index/vaultCluster:VaultCluster example vault-cluster
 * ```
 */
export class VaultCluster extends pulumi.CustomResource {
    /**
     * Get an existing VaultCluster resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: VaultClusterState, opts?: pulumi.CustomResourceOptions): VaultCluster {
        return new VaultCluster(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'hcp:index/vaultCluster:VaultCluster';

    /**
     * Returns true if the given object is an instance of VaultCluster.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is VaultCluster {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === VaultCluster.__pulumiType;
    }

    /**
     * The provider where the HCP Vault cluster is located.
     */
    public /*out*/ readonly cloudProvider!: pulumi.Output<string>;
    /**
     * The ID of the HCP Vault cluster.
     */
    public readonly clusterId!: pulumi.Output<string>;
    /**
     * The time that the Vault cluster was created.
     */
    public /*out*/ readonly createdAt!: pulumi.Output<string>;
    /**
     * The ID of the HVN this HCP Vault cluster is associated to.
     */
    public readonly hvnId!: pulumi.Output<string>;
    /**
     * The minimum Vault version to use when creating the cluster. If not specified, it is defaulted to the version that is currently recommended by HCP.
     */
    public readonly minVaultVersion!: pulumi.Output<string | undefined>;
    /**
     * The name of the customer namespace this HCP Vault cluster is located in.
     */
    public /*out*/ readonly namespace!: pulumi.Output<string>;
    /**
     * The ID of the organization this HCP Vault cluster is located in.
     */
    public /*out*/ readonly organizationId!: pulumi.Output<string>;
    /**
     * The ID of the project this HCP Vault cluster is located in.
     */
    public /*out*/ readonly projectId!: pulumi.Output<string>;
    /**
     * Denotes that the cluster has a public endpoint. Defaults to false.
     */
    public readonly publicEndpoint!: pulumi.Output<boolean | undefined>;
    /**
     * The region where the HCP Vault cluster is located.
     */
    public /*out*/ readonly region!: pulumi.Output<string>;
    /**
     * Tier of the HCP Vault cluster. Valid options for tiers - `dev`, `standardSmall`, `standardMedium`, `standardLarge`, `starterSmall`. See [pricing information](https://cloud.hashicorp.com/pricing/vault).
     */
    public readonly tier!: pulumi.Output<string>;
    /**
     * The private URL for the Vault cluster.
     */
    public /*out*/ readonly vaultPrivateEndpointUrl!: pulumi.Output<string>;
    /**
     * The public URL for the Vault cluster. This will be empty if `publicEndpoint` is `false`.
     */
    public /*out*/ readonly vaultPublicEndpointUrl!: pulumi.Output<string>;
    /**
     * The Vault version of the cluster.
     */
    public /*out*/ readonly vaultVersion!: pulumi.Output<string>;

    /**
     * Create a VaultCluster resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: VaultClusterArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: VaultClusterArgs | VaultClusterState, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (opts.id) {
            const state = argsOrState as VaultClusterState | undefined;
            resourceInputs["cloudProvider"] = state ? state.cloudProvider : undefined;
            resourceInputs["clusterId"] = state ? state.clusterId : undefined;
            resourceInputs["createdAt"] = state ? state.createdAt : undefined;
            resourceInputs["hvnId"] = state ? state.hvnId : undefined;
            resourceInputs["minVaultVersion"] = state ? state.minVaultVersion : undefined;
            resourceInputs["namespace"] = state ? state.namespace : undefined;
            resourceInputs["organizationId"] = state ? state.organizationId : undefined;
            resourceInputs["projectId"] = state ? state.projectId : undefined;
            resourceInputs["publicEndpoint"] = state ? state.publicEndpoint : undefined;
            resourceInputs["region"] = state ? state.region : undefined;
            resourceInputs["tier"] = state ? state.tier : undefined;
            resourceInputs["vaultPrivateEndpointUrl"] = state ? state.vaultPrivateEndpointUrl : undefined;
            resourceInputs["vaultPublicEndpointUrl"] = state ? state.vaultPublicEndpointUrl : undefined;
            resourceInputs["vaultVersion"] = state ? state.vaultVersion : undefined;
        } else {
            const args = argsOrState as VaultClusterArgs | undefined;
            if ((!args || args.clusterId === undefined) && !opts.urn) {
                throw new Error("Missing required property 'clusterId'");
            }
            if ((!args || args.hvnId === undefined) && !opts.urn) {
                throw new Error("Missing required property 'hvnId'");
            }
            resourceInputs["clusterId"] = args ? args.clusterId : undefined;
            resourceInputs["hvnId"] = args ? args.hvnId : undefined;
            resourceInputs["minVaultVersion"] = args ? args.minVaultVersion : undefined;
            resourceInputs["publicEndpoint"] = args ? args.publicEndpoint : undefined;
            resourceInputs["tier"] = args ? args.tier : undefined;
            resourceInputs["cloudProvider"] = undefined /*out*/;
            resourceInputs["createdAt"] = undefined /*out*/;
            resourceInputs["namespace"] = undefined /*out*/;
            resourceInputs["organizationId"] = undefined /*out*/;
            resourceInputs["projectId"] = undefined /*out*/;
            resourceInputs["region"] = undefined /*out*/;
            resourceInputs["vaultPrivateEndpointUrl"] = undefined /*out*/;
            resourceInputs["vaultPublicEndpointUrl"] = undefined /*out*/;
            resourceInputs["vaultVersion"] = undefined /*out*/;
        }
        if (!opts.version) {
            opts = pulumi.mergeOptions(opts, { version: utilities.getVersion()});
        }
        super(VaultCluster.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering VaultCluster resources.
 */
export interface VaultClusterState {
    /**
     * The provider where the HCP Vault cluster is located.
     */
    cloudProvider?: pulumi.Input<string>;
    /**
     * The ID of the HCP Vault cluster.
     */
    clusterId?: pulumi.Input<string>;
    /**
     * The time that the Vault cluster was created.
     */
    createdAt?: pulumi.Input<string>;
    /**
     * The ID of the HVN this HCP Vault cluster is associated to.
     */
    hvnId?: pulumi.Input<string>;
    /**
     * The minimum Vault version to use when creating the cluster. If not specified, it is defaulted to the version that is currently recommended by HCP.
     */
    minVaultVersion?: pulumi.Input<string>;
    /**
     * The name of the customer namespace this HCP Vault cluster is located in.
     */
    namespace?: pulumi.Input<string>;
    /**
     * The ID of the organization this HCP Vault cluster is located in.
     */
    organizationId?: pulumi.Input<string>;
    /**
     * The ID of the project this HCP Vault cluster is located in.
     */
    projectId?: pulumi.Input<string>;
    /**
     * Denotes that the cluster has a public endpoint. Defaults to false.
     */
    publicEndpoint?: pulumi.Input<boolean>;
    /**
     * The region where the HCP Vault cluster is located.
     */
    region?: pulumi.Input<string>;
    /**
     * Tier of the HCP Vault cluster. Valid options for tiers - `dev`, `standardSmall`, `standardMedium`, `standardLarge`, `starterSmall`. See [pricing information](https://cloud.hashicorp.com/pricing/vault).
     */
    tier?: pulumi.Input<string>;
    /**
     * The private URL for the Vault cluster.
     */
    vaultPrivateEndpointUrl?: pulumi.Input<string>;
    /**
     * The public URL for the Vault cluster. This will be empty if `publicEndpoint` is `false`.
     */
    vaultPublicEndpointUrl?: pulumi.Input<string>;
    /**
     * The Vault version of the cluster.
     */
    vaultVersion?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a VaultCluster resource.
 */
export interface VaultClusterArgs {
    /**
     * The ID of the HCP Vault cluster.
     */
    clusterId: pulumi.Input<string>;
    /**
     * The ID of the HVN this HCP Vault cluster is associated to.
     */
    hvnId: pulumi.Input<string>;
    /**
     * The minimum Vault version to use when creating the cluster. If not specified, it is defaulted to the version that is currently recommended by HCP.
     */
    minVaultVersion?: pulumi.Input<string>;
    /**
     * Denotes that the cluster has a public endpoint. Defaults to false.
     */
    publicEndpoint?: pulumi.Input<boolean>;
    /**
     * Tier of the HCP Vault cluster. Valid options for tiers - `dev`, `standardSmall`, `standardMedium`, `standardLarge`, `starterSmall`. See [pricing information](https://cloud.hashicorp.com/pricing/vault).
     */
    tier?: pulumi.Input<string>;
}
