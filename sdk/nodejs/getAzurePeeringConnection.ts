// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

/**
 * > **Note:** This data source is currently in public beta.
 *
 * The Azure peering connection data source provides information about a peering connection between an HVN and a peer Azure VNet.
 *
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as hcp from "@pulumi/hcp";
 *
 * const test = hcp.getAzurePeeringConnection({
 *     hvnId: _var.hvn_id,
 *     peeringId: _var.peering_id,
 *     waitForActiveState: true,
 * });
 * ```
 */
export function getAzurePeeringConnection(args: GetAzurePeeringConnectionArgs, opts?: pulumi.InvokeOptions): Promise<GetAzurePeeringConnectionResult> {
    if (!opts) {
        opts = {}
    }

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
    return pulumi.runtime.invoke("hcp:index/getAzurePeeringConnection:getAzurePeeringConnection", {
        "hvnLink": args.hvnLink,
        "peeringId": args.peeringId,
        "waitForActiveState": args.waitForActiveState,
    }, opts);
}

/**
 * A collection of arguments for invoking getAzurePeeringConnection.
 */
export interface GetAzurePeeringConnectionArgs {
    hvnLink: string;
    peeringId: string;
    waitForActiveState?: boolean;
}

/**
 * A collection of values returned by getAzurePeeringConnection.
 */
export interface GetAzurePeeringConnectionResult {
    readonly applicationId: string;
    readonly azurePeeringId: string;
    readonly createdAt: string;
    readonly expiresAt: string;
    readonly hvnLink: string;
    /**
     * The provider-assigned unique ID for this managed resource.
     */
    readonly id: string;
    readonly organizationId: string;
    readonly peerResourceGroupName: string;
    readonly peerSubscriptionId: string;
    readonly peerTenantId: string;
    readonly peerVnetName: string;
    readonly peerVnetRegion: string;
    readonly peeringId: string;
    readonly projectId: string;
    readonly selfLink: string;
    readonly waitForActiveState?: boolean;
}

export function getAzurePeeringConnectionOutput(args: GetAzurePeeringConnectionOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetAzurePeeringConnectionResult> {
    return pulumi.output(args).apply(a => getAzurePeeringConnection(a, opts))
}

/**
 * A collection of arguments for invoking getAzurePeeringConnection.
 */
export interface GetAzurePeeringConnectionOutputArgs {
    hvnLink: pulumi.Input<string>;
    peeringId: pulumi.Input<string>;
    waitForActiveState?: pulumi.Input<boolean>;
}
