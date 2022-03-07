// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

/**
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as hcp from "@pulumi/hcp";
 *
 * const example = new hcp.ConsulClusterRootToken("example", {
 *     clusterId: "consul-cluster",
 * });
 * ```
 */
export class ConsulClusterRootToken extends pulumi.CustomResource {
    /**
     * Get an existing ConsulClusterRootToken resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: ConsulClusterRootTokenState, opts?: pulumi.CustomResourceOptions): ConsulClusterRootToken {
        return new ConsulClusterRootToken(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'hcp:index/consulClusterRootToken:ConsulClusterRootToken';

    /**
     * Returns true if the given object is an instance of ConsulClusterRootToken.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is ConsulClusterRootToken {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === ConsulClusterRootToken.__pulumiType;
    }

    /**
     * The accessor ID of the root ACL token.
     */
    public /*out*/ readonly accessorId!: pulumi.Output<string>;
    /**
     * The ID of the HCP Consul cluster.
     */
    public readonly clusterId!: pulumi.Output<string>;
    /**
     * The root ACL token Base64 encoded in a Kubernetes secret.
     */
    public /*out*/ readonly kubernetesSecret!: pulumi.Output<string>;
    /**
     * The secret ID of the root ACL token.
     */
    public /*out*/ readonly secretId!: pulumi.Output<string>;

    /**
     * Create a ConsulClusterRootToken resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: ConsulClusterRootTokenArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: ConsulClusterRootTokenArgs | ConsulClusterRootTokenState, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (opts.id) {
            const state = argsOrState as ConsulClusterRootTokenState | undefined;
            resourceInputs["accessorId"] = state ? state.accessorId : undefined;
            resourceInputs["clusterId"] = state ? state.clusterId : undefined;
            resourceInputs["kubernetesSecret"] = state ? state.kubernetesSecret : undefined;
            resourceInputs["secretId"] = state ? state.secretId : undefined;
        } else {
            const args = argsOrState as ConsulClusterRootTokenArgs | undefined;
            if ((!args || args.clusterId === undefined) && !opts.urn) {
                throw new Error("Missing required property 'clusterId'");
            }
            resourceInputs["clusterId"] = args ? args.clusterId : undefined;
            resourceInputs["accessorId"] = undefined /*out*/;
            resourceInputs["kubernetesSecret"] = undefined /*out*/;
            resourceInputs["secretId"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(ConsulClusterRootToken.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering ConsulClusterRootToken resources.
 */
export interface ConsulClusterRootTokenState {
    /**
     * The accessor ID of the root ACL token.
     */
    accessorId?: pulumi.Input<string>;
    /**
     * The ID of the HCP Consul cluster.
     */
    clusterId?: pulumi.Input<string>;
    /**
     * The root ACL token Base64 encoded in a Kubernetes secret.
     */
    kubernetesSecret?: pulumi.Input<string>;
    /**
     * The secret ID of the root ACL token.
     */
    secretId?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a ConsulClusterRootToken resource.
 */
export interface ConsulClusterRootTokenArgs {
    /**
     * The ID of the HCP Consul cluster.
     */
    clusterId: pulumi.Input<string>;
}
